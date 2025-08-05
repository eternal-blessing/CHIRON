import cv2
import mediapipe as mp
import time
import psutil
import logging
from typing import Optional


class HandTracker:
    """
    Real-time hand landmark tracker using MediaPipe.
    Supports:
    - landmark overlay visualization
    - latency measurement
    - CPU usage monitoring
    """

    def __init__(
        self,
        max_num_hands: int = 1,
        detection_confidence: float = 0.5,
        tracking_confidence: float = 0.5,
        show_perf_overlay: bool = True,
    ):
        self.max_num_hands = max_num_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence
        self.show_perf_overlay = show_perf_overlay

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=self.max_num_hands,
            min_detection_confidence=self.detection_confidence,
            min_tracking_confidence=self.tracking_confidence,
        )
        self.drawing_utils = mp.solutions.drawing_utils

        self.cap = cv2.VideoCapture(0)
        self.running = False
        self._init_logging()

    def _init_logging(self):
        logging.basicConfig(
            filename="hand_tracker.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    def process_frame(self, image) -> Optional[any]:
        """
        Process a BGR frame, return annotated frame
        """
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_image)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.drawing_utils.draw_landmarks(
                    image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                )
                # highlight index fingertip
                index_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
                h, w, _ = image.shape
                cx, cy = int(index_tip.x * w), int(index_tip.y * h)
                cv2.circle(image, (cx, cy), 5, (255, 0, 255), -1)
                cv2.putText(
                    image,
                    "Index Tip",
                    (cx, cy - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 0, 255),
                    1,
                )

        return image

    def run(self):
        """
        Start real-time hand tracking loop.
        """
        self.running = True
        if not self.cap.isOpened():
            logging.error("Camera not available for HandTracker")
            return

        logging.info("HandTracker started successfully.")
        print("Press ESC to quit...")

        while self.running:
            success, frame = self.cap.read()
            if not success:
                logging.warning("Frame read failed in HandTracker")
                continue

            frame = cv2.flip(frame, 1)

            start_time = time.perf_counter()
            frame = self.process_frame(frame)
            latency_ms = (time.perf_counter() - start_time) * 1000

            cpu_percent = psutil.cpu_percent(interval=None)

            if self.show_perf_overlay:
                cv2.putText(
                    frame,
                    f"Latency: {latency_ms:.2f} ms",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2,
                )
                cv2.putText(
                    frame,
                    f"CPU: {cpu_percent:.2f}%",
                    (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 255),
                    2,
                )

            cv2.imshow("HandTracker", frame)

            if latency_ms > 50:
                logging.warning(f"High latency: {latency_ms:.2f} ms")

            if cpu_percent > 25:
                logging.warning(f"High CPU usage: {cpu_percent:.2f}%")

            if cv2.waitKey(5) & 0xFF == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()
        logging.info("HandTracker stopped")

    def stop(self):
        self.running = False
        logging.info("HandTracker manually stopped.")

    def __del__(self):
        self.stop()
        if self.cap and self.cap.isOpened():
            self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    tracker = HandTracker()
    tracker.run()
    print("Test completed successfully!")