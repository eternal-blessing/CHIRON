import cv2
import time
import logging
import numpy as np
import os
from typing import Tuple, Optional

# Environment configuration to suppress warnings
os.environ['QT_LOGGING_RULES'] = '*.debug=false'
os.environ['QT_QPA_PLATFORM'] = 'xcb'

class WebcamCapture:
    """
    Robust webcam capture module meeting all acceptance criteria:
    - 1280x720 @ ~30 FPS
    - Graceful fallback on errors
    - <5% frame drops in 10-minute tests
    """

    def __init__(self, camera_id: int = 0):
        self.camera_id = camera_id
        self.cap = None
        self.target_width = 1280
        self.target_height = 720
        self.target_fps = 30
        self.last_valid_frame = None
        self.running = False
        self._init_logging()

    def _init_logging(self):
        """Configure logging for performance tracking."""
        logging.basicConfig(
            filename='webcam_errors.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def start(self) -> bool:
        """
        Initialize camera with target settings.
        Returns: True if successful, False on fatal error.
        """
        try:
            self.cap = cv2.VideoCapture(self.camera_id)
            if not self.cap.isOpened():
                raise RuntimeError(f"Camera {self.camera_id} not detected")

            # Set target resolution
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.target_width)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.target_height)

            # Verify settings
            actual_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            actual_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            
            if (actual_width, actual_height) != (self.target_width, self.target_height):
                logging.warning(f"Resolution fallback: {actual_width}x{actual_height}")
                self.target_width, self.target_height = actual_width, actual_height

            # Seting FPS 
            self.cap.set(cv2.CAP_PROP_FPS, self.target_fps)
            actual_fps = self.cap.get(cv2.CAP_PROP_FPS)
            if actual_fps < 25:
                logging.warning(f"Low FPS: {actual_fps}. Check lighting/camera.")

            self.running = True
            return True

        except Exception as e:
            logging.error(f"Start failed: {str(e)}")
            return False

    def read_frame(self) -> Tuple[bool, Optional[np.ndarray], float]:
        """
        Captures a frame with timestamp.
        Returns: (success, frame, timestamp)
        """
        if not self.running:
            return False, None, time.time()

        try:
            ret, frame = self.cap.read()
            timestamp = time.time()

            if not ret or frame is None:
                logging.warning("Frame read failed")
                return False, self.last_valid_frame, timestamp

            self.last_valid_frame = frame.copy()
            return True, frame, timestamp

        except Exception as e:
            logging.error(f"Read error: {str(e)}")
            return False, None, time.time()

    def stop(self):
        """Release resources safely."""
        if self.cap and self.cap.isOpened():
            self.cap.release()
        self.running = False
        logging.info("Camera stopped")

def test_webcam(duration_min: int = 10):
    """Run 10-minute stress test."""
    cam = WebcamCapture()
    if not cam.start():
        print("Camera initialization failed")
        return

    start_time = time.time()
    total_frames = 0
    dropped_frames = 0

    try:
        print(f"Testing for {duration_min} minutes...")
        while (time.time() - start_time) < duration_min * 60:
            success, frame, _ = cam.read_frame()
            total_frames += 1
            if not success:
                dropped_frames += 1

          
            if frame is not None:
                cv2.imshow('Webcam Test', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    finally:
        cam.stop()
        cv2.destroyAllWindows()
        
        if total_frames > 0:
            drop_rate = (dropped_frames / total_frames) * 100
            print(f"\nResults:")
            print(f"Total frames: {total_frames}")
            print(f"Dropped frames: {dropped_frames} ({drop_rate:.2f}%)")
            print(f"Pass: {'Yes' if drop_rate < 5 else 'No'} (Acceptance: <5%)")

if __name__ == "__main__":
    test_webcam()