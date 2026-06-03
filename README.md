# Vision AI - Real-Time Hand & Emotion Detection

## Overview

Vision AI is a real-time Computer Vision application built using Python, OpenCV, MediaPipe, DeepFace, and TensorFlow.

The system captures live webcam video and performs:

* Real-time hand detection
* Hand landmark tracking
* Facial emotion recognition
* Emotion confidence scoring
* Face localization
* Performance monitoring and optimization

The project follows a modular architecture by separating configuration, detection logic, utility functions, and application control.

---

## Features

### Hand Detection

Uses MediaPipe Hands to:

* Detect hands in real time
* Track 21 hand landmarks
* Draw landmark connections
* Support multiple hand detection

---

### Emotion Detection

Uses DeepFace to:

* Detect faces
* Analyze facial expressions
* Predict emotions
* Display confidence scores
* Draw face bounding boxes

Supported emotions include:

* Happy
* Sad
* Angry
* Fear
* Surprise
* Disgust
* Neutral

---

### Performance Monitoring

The application displays real-time performance metrics:

* FPS (Frames Per Second)
* CPU Usage
* RAM Usage
* Frame Skip Value

---

### Logging System

A centralized logging system was implemented using Python's built-in `logging` module.

The logger records important application events such as:

* Application startup
* Application shutdown
* Runtime events
* Errors and warnings
* Performance testing events

Logs are stored inside:

```text
logs/vision_ai.log
```

Benefits:

* Easier debugging
* Better error tracking
* Runtime monitoring
* Production-style application logging
* Improved maintainability

---

### Performance Optimization

A frame-skipping strategy was implemented to improve application performance.

Since emotion detection is computationally expensive, DeepFace is not executed on every frame.

Instead:

* Hand detection runs continuously
* Emotion detection runs periodically
* Previous emotion predictions are reused between skipped frames

Benefits:

* Higher FPS
* Lower CPU usage
* Improved responsiveness
* Better real-time performance

---

## Performance Benchmarking

The application was benchmarked using multiple frame-skipping configurations.

### Benchmark Results

| Frame Skip | FPS  | CPU Usage |
| ---------- | ---- | --------- |
| 1          | 4.9  | 74.8%     |
| 5          | 13.5 | 75.0%     |
| 10         | 23.4 | 50.0%     |
| 13         | 25.4 | 25.9%     |

### Analysis

Increasing the frame skip value reduced the number of DeepFace emotion inference calls.

This resulted in:

* Higher FPS
* Lower CPU utilization
* Improved application responsiveness
* Reduced computational overhead

### Recommended Configuration

After benchmarking multiple configurations, the following value was selected:

```python
FRAME_SKIP = 10
```

Reasons:

* High FPS (~23 FPS)
* Moderate CPU usage (~50%)
* Smooth user experience
* Emotion predictions remain responsive
* Better balance between speed and accuracy

### Conclusion

Frame skipping improved performance by approximately:

* 377% FPS increase (4.9 → 23.4 FPS)
* Significant reduction in CPU utilization
* Smoother real-time interaction

This demonstrates how selective model execution can improve real-time computer vision systems without sacrificing usability.

---

## Technologies Used

* Python
* OpenCV
* MediaPipe
* DeepFace
* TensorFlow
* psutil

---

## Project Structure

```text
vision_ai_final/

├── main.py

├── config/
│   └── settings.py

├── detectors/
│   ├── hand_detector.py
│   └── emotion_detector.py

├── utils/
│   ├── draw_utils.py
│   └── logger.py

├── logs/
│   └── vision_ai.log

├── requirements.txt

├── README.md

└── .gitignore
```

---

## Architecture

### main.py

Main controller of the application.

Responsibilities:

* Open webcam
* Capture frames
* Calculate FPS
* Monitor CPU and RAM
* Manage frame skipping
* Call detectors
* Display output

---

### detectors/hand_detector.py

Responsible for:

* Loading MediaPipe Hands
* Processing webcam frames
* Detecting hand landmarks
* Returning landmark data

---

### detectors/emotion_detector.py

Responsible for:

* Running DeepFace emotion analysis
* Detecting faces
* Returning emotion predictions
* Returning confidence scores
* Returning face coordinates

---

### utils/draw_utils.py

Responsible for:

* Drawing hand landmarks
* Drawing hand connections
* Drawing face bounding boxes
* Displaying emotion labels
* Displaying confidence scores

---

### utils/logger.py

Responsible for:

* Creating application logs
* Recording runtime events
* Recording errors and warnings
* Supporting debugging and monitoring

---

### config/settings.py

Stores configurable settings such as:

* Camera ID
* Window Name
* Colors
* Drawing Thickness
* Font Size
* Frame Skip Value

---

## System Workflow

```text
Webcam Frame
      ↓
Frame Counter
      ↓
Hand Detector
      ↓
Emotion Detector
      ↓
Drawing Utilities
      ↓
Performance Metrics
      ↓
Logger
      ↓
Display Output
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/joshidiksha660/real-time-hand-emotion-detection.git

cd real-time-hand-emotion-detection
```

---

### Create Virtual Environment

```bash
uv venv
```

---

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

---

### Install Dependencies

```bash
uv pip install -r requirements.txt
```

---

## Run Application

```bash
python main.py
```

---

## Example Output

The application displays:

* Hand landmarks
* Face bounding box
* Emotion prediction
* Confidence score
* FPS
* CPU usage
* RAM usage
* Frame skip value

in real time through the webcam feed.

---

## Future Improvements

* GPU Utilization Monitoring
* Adaptive Frame Skipping
* Multi-Person Emotion Detection
* Hand Gesture Recognition
* Face Recognition
* Emotion Analytics Dashboard
* Emotion History Tracking
* Structured CSV Logging
* Log Rotation
* Streamlit Dashboard
* Model Performance Benchmarking

---

## Author

### Diksha Joshi

MCA Student
AI/ML Developer
Computer Vision Enthusiast

GitHub:
https://github.com/joshidiksha660
