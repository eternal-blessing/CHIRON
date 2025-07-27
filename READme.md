# Chiron: AI-Powered Hand Gesture Game Controller

## Project Overview

**Chiron**  standalone desktop application designed to empower users with intuitive control over simple computer games and interactive applications via real-time hand gesture recognition. Utilizing standard USB webcams and advanced computer vision techniques, Chiron transforms natural hand movements into simulated keyboard inputs, facilitating a seamless, contactless gaming experience.

This project integrates state-of-the-art AI models including MediaPipe for hand landmark detection and custom-trained machine learning architectures for gesture classification, all operating locally to ensure privacy and responsiveness.

## Key Features

**Real-Time Webcam Video Capture**: Displays live video feed from the user's default USB webcam within an interactive GUI.
**Robust Single-Hand Detection and Tracking**: Employs MediaPipe framework to accurately identify 21 three-dimensional hand landmarks.
**Comprehensive Gesture Recognition**: Supports recognition of at least five static gestures and two dynamic gestures with high accuracy and low latency.
**Gesture-to-Keyboard Mapping**: Translates recognized gestures into configurable standard keyboard inputs compatible with a broad range of PC games.
**Customizable Control Scheme**: Provides an accessible GUI and configuration file for users to assign or remap gestures to preferred key actions without requiring application restarts.
**Immediate Visual and Auditory Feedback**: Enhances user experience with overlays displaying recognized gestures and confidence levels, complemented by distinct sound cues.
**Built-in Demonstration Game**: Includes a simple, gesture-controlled interactive game, demonstrating core functionality and user interaction.
**Error Handling and User Guidance**: Implements clear, user-friendly notifications for common operational issues such as webcam absence or performance bottlenecks.
**Privacy-Centric Local Processing**: All data processing is performed locally with no external data transmission, ensuring user privacy.

## System Requirements

### Hardware Specifications

 Operating System: Windows 10 or 11 (64-bit), macOS (latest two stable versions), or Ubuntu 20.04+ (64-bit).
 Processor: Intel Core i5 8th Generation or equivalent.
 Memory: Minimum 8 GB RAM.
 Webcam: USB-connected webcam supporting at least 720p resolution.

### Software Environment

 Python Interpreter: Versions 3.8 through 3.11 supported.
 Required Python Packages:
   `opencv-python`
   `mediapipe`
   `pygame`
   `pynput` or `pyautogui` (for simulating keyboard inputs)

### Permissions

 The application requires access to the webcam device and permission to simulate keyboard events at the operating system level.

## Installation Instructions

Follow these steps to install and prepare Chiron for use:

1. **Clone the repository:**

    
    git clone <https://github.com/eternal-blessing/CHIRON.git>
    cd chiron
    

2. **Create and activate a Python virtual environment to isolate dependencies:**

    
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    

3. **Install necessary dependencies from the requirements file:**

    
    pip install -r requirements.txt
    

4. **Ensure your USB webcam is properly connected before launching the application.**

## Usage Guide

Launch the application by executing:



Upon startup, Chiron will attempt to access the system’s default webcam and open the main graphical interface, displaying a live video feed with hand landmark overlays.

### How to Control Games Using Gestures

 Place your hand within the webcam’s field of view under adequate lighting conditions.
 Perform any of the supported gestures listed below to trigger the corresponding keyboard inputs.
 Compatible with PC games and applications that accept standard keyboard controls.

### Supported Gestures and Default Mappings

| Gesture           | Default Keyboard Action | Description                                  |
|-------------------|------------------------|----------------------------------------------|
| Open Palm         | Move Right             | Hand fully open, palm facing the camera.     |
| Closed Fist       | Move Left              | Hand tightly clenched into a fist.            |
| Pointing Index    | Jump                   | Index finger extended, others curled.        |
| "V" Sign          | Pause                  | Index and middle fingers extended forming V.|
| Thumbs Up         | Confirm                | Thumb extended upward, other fingers folded. |
| Swipe Left        | Previous Item          | Dynamic leftward hand movement across frame. |
| Swipe Right       | Next Item              | Dynamic rightward hand movement across frame.|

*Visual overlays display the detected gesture name and confidence score in real time.*

## Configuration

Users may customize gesture-to-key mappings using an intuitive configuration interface or by directly editing the `config.json` file located in the project directory. Changes take effect immediately without requiring application restarts.

## Included Demo Game

Chiron features a simple, built-in gesture-controlled game (such as a maze navigator or Pong-style game) to demonstrate the integration of hand detection, gesture recognition, and keyboard input simulation in a practical context.



For detailed troubleshooting, advanced configuration, and development guidelines, please refer to the documentation in the `doc/README.md` file.



**Chiron is a privacy-conscious, locally operating application that enhances user interaction with computer games through natural hand gestures, providing a novel and immersive gaming interface.**


