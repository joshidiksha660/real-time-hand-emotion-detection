# OpenCV for webcam
import cv2

# Settings
from config.settings import (
    CAMERA_ID,
    WINDOW_NAME
)

# Hand Detection Module
from detectors.hand_detector import (
    detect_hands
)

# Emotion Detection Module
from detectors.emotion_detector import (
    detect_emotion
)

# Drawing Utilities
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
# MAIN LOOP
# --------------------------------------------------

while True:

    # Capture one frame
    success, frame = cap.read()

    # Stop if camera fails
    if not success:
        break

    # ----------------------------------
    # HAND DETECTION
    # ----------------------------------

    hand_results = detect_hands(
        frame
    )

    # ----------------------------------
    # EMOTION DETECTION
    # ----------------------------------

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

    draw_emotion(
        frame,
        emotion_data
    )

    # ----------------------------------
    # SHOW OUTPUT
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