# --------------------------------------------------
# IMPORTS
# --------------------------------------------------

# OpenCV for webcam and drawing
import cv2

# Used to calculate FPS
import time

# Used to monitor CPU and RAM usage
import psutil

# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

from config.settings import (
    CAMERA_ID,
    WINDOW_NAME
)

# --------------------------------------------------
# DETECTORS
# --------------------------------------------------

from detectors.hand_detector import (
    detect_hands
)

from detectors.emotion_detector import (
    detect_emotion
)

# --------------------------------------------------
# DRAWING UTILITIES
# --------------------------------------------------

from utils.draw_utils import (
    draw_hands,
    draw_emotion
)

# --------------------------------------------------
# OPEN WEBCAM
# --------------------------------------------------

cap = cv2.VideoCapture(
    CAMERA_ID
)

# --------------------------------------------------
# PERFORMANCE VARIABLES
# --------------------------------------------------

# Store previous frame time
# Used to calculate FPS
prev_time = time.time()

# Current FPS value
fps = 0

# --------------------------------------------------
# FRAME SKIPPING VARIABLES
# --------------------------------------------------

# Counts how many frames have passed
frame_count = 0

# Stores previous emotion result
# Used during skipped frames
emotion_data = None

# Run emotion detection every 5th frame
FRAME_SKIP = 5

# --------------------------------------------------
# MAIN LOOP
# --------------------------------------------------

while True:

    # ----------------------------------
    # CAPTURE FRAME
    # ----------------------------------

    success, frame = cap.read()

    # Stop if camera fails
    if not success:
        break

    # ----------------------------------
    # FPS CALCULATION
    # ----------------------------------

    # Current timestamp
    current_time = time.time()

    # FPS Formula
    # FPS = Frames Per Second
    fps = 1 / (current_time - prev_time)

    # Update previous timestamp
    prev_time = current_time

    # ----------------------------------
    # SYSTEM PERFORMANCE
    # ----------------------------------

    # CPU usage percentage
    cpu_usage = psutil.cpu_percent()

    # RAM usage percentage
    memory_usage = psutil.virtual_memory().percent

    # ----------------------------------
    # HAND DETECTION
    # ----------------------------------

    hand_results = detect_hands(
        frame
    )

    # ----------------------------------
    # FRAME COUNTER
    # ----------------------------------

    frame_count += 1

    # ----------------------------------
    # EMOTION DETECTION
    # ----------------------------------

    # Run DeepFace only every 5th frame
    if frame_count % FRAME_SKIP == 0:

        emotion_data = detect_emotion(
            frame
        )

    # ----------------------------------
    # DRAW DETECTION RESULTS
    # ----------------------------------

    draw_hands(
        frame,
        hand_results
    )

    # Draw latest emotion result
    # even on skipped frames
    if emotion_data is not None:

        draw_emotion(
            frame,
            emotion_data
        )

    # ----------------------------------
    # DRAW PERFORMANCE METRICS
    # ----------------------------------

    cv2.putText(
        frame,
        f"FPS: {fps:.1f}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"CPU: {cpu_usage:.1f}%",
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"RAM: {memory_usage:.1f}%",
        (10, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Skip: {FRAME_SKIP}",
        (10, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    # ----------------------------------
    # SHOW FINAL OUTPUT
    # ----------------------------------

    cv2.imshow(
        WINDOW_NAME,
        frame
    )

    # Exit when q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --------------------------------------------------
# CLEANUP
# --------------------------------------------------

cap.release()

cv2.destroyAllWindows()