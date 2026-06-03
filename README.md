# Vision AI - Hand & Emotion Detection

## Overview

Vision AI is a real-time Computer Vision project built using Python.

The application uses a webcam to:

- Detect hands in real time
- Track 21 hand landmarks
- Detect facial emotions
- Display emotion confidence scores
- Draw face bounding boxes
- Display hand landmark connections

---

## Features

### Hand Detection

Uses MediaPipe Hands to:

- Detect hands
- Track 21 hand landmarks
- Draw landmark connections

### Emotion Detection

Uses DeepFace to:

- Detect faces
- Analyze facial expressions
- Predict emotions
- Display confidence scores

---

## Technologies Used

- Python
- OpenCV
- MediaPipe
- DeepFace
- TensorFlow

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
│   └── draw_utils.py

├── requirements.txt

├── README.md

└── .gitignore
```

---

## Architecture

### main.py

Acts as the controller of the application.

Responsibilities:

- Capture webcam frames
- Call hand detector
- Call emotion detector
- Display final output

---

### detectors/hand_detector.py

Responsible for:

- Loading MediaPipe Hands
- Detecting hands
- Returning hand landmark data

---

### detectors/emotion_detector.py

Responsible for:

- Running DeepFace emotion analysis
- Returning emotion predictions
- Returning face coordinates

---

### utils/draw_utils.py

Responsible for:

- Drawing hand landmarks
- Drawing face bounding boxes
- Displaying emotion labels

---

### config/settings.py

Stores application settings such as:

- Camera ID
- Window name
- Font size
- Colors
- Drawing thickness

---

## Installation

### Create Virtual Environment

```bash
uv venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

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

## Example Workflow

```text
Webcam Frame
      ↓
Hand Detector
      ↓
Emotion Detector
      ↓
Drawing Utilities
      ↓
Display Output
```

---

## Future Improvements

- Hand Gesture Recognition
- Face Recognition
- Emotion Analytics Dashboard
- FPS Counter
- Emotion History Tracking
- CSV Logging
- Streamlit Dashboard

---

## Author

Diksha Joshi

MCA Student | Python Developer | Computer Vision Enthusiast