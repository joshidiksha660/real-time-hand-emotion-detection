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
# LOGGER
# --------------------------------------------------

from utils.logger import logger

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
# APPLICATION START
# --------------------------------------------------

logger.info(
    "Application Started"
)

# --------------------------------------------------
# OPEN WEBCAM
# --------------------------------------------------

cap = cv2.VideoCapture(
    CAMERA_ID
)

logger.info(
    "Webcam Initialized"
)

# --------------------------------------------------
# PERFORMANCE VARIABLES
# --------------------------------------------------

# Used for FPS calculation
prev_time = time.time()

# Current FPS value
fps = 0

# --------------------------------------------------
# FRAME SKIPPING VARIABLES
# --------------------------------------------------

# Counts processed frames
frame_count = 0

# Stores previous emotion result
emotion_data = None

# Run DeepFace every Nth frame
FRAME_SKIP = 10

logger.info(
    f"Frame Skipping Enabled: {FRAME_SKIP}"
)

# --------------------------------------------------
# MAIN LOOP
# --------------------------------------------------

while True:

    # ----------------------------------
    # CAPTURE FRAME
    # ----------------------------------

    success, frame = cap.read()

    # Stop if webcam fails
    if not success:

        logger.error(
            "Failed To Read Webcam Frame"
        )

        break

    # ----------------------------------
    # FPS CALCULATION
    # ----------------------------------

    current_time = time.time()

    fps = 1 / (current_time - prev_time)

    prev_time = current_time

    # ----------------------------------
    # SYSTEM PERFORMANCE
    # ----------------------------------

    cpu_usage = psutil.cpu_percent()

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

    # Run emotion detection only
    # every FRAME_SKIP frames

    if frame_count % FRAME_SKIP == 0:

        emotion_data = detect_emotion(
            frame
        )

    # ----------------------------------
    # DRAW RESULTS
    # ----------------------------------

    draw_hands(
        frame,
        hand_results
    )

    if emotion_data is not None:

        draw_emotion(
            frame,
            emotion_data
        )

    # ----------------------------------
    # PERFORMANCE DISPLAY
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
    # SHOW OUTPUT
    # ----------------------------------

    cv2.imshow(
        WINDOW_NAME,
        frame
    )

    # ----------------------------------
    # EXIT
    # ----------------------------------

    if cv2.waitKey(1) & 0xFF == ord('q'):

        logger.info(
            "Application Closed By User"
        )

        break

# --------------------------------------------------
# CLEANUP
# --------------------------------------------------

cap.release()

cv2.destroyAllWindows()

logger.info(
    "Application Shutdown Complete"
)