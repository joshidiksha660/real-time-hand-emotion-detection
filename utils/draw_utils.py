# OpenCV is used for drawing rectangles and text
import cv2

# MediaPipe is used for drawing hand landmarks
import mediapipe as mp

# Import settings from config file
from config.settings import (
    BOX_COLOR,
    TEXT_COLOR,
    LINE_THICKNESS,
    FONT_SCALE
)

# Used to draw hand landmarks
mpDraw = mp.solutions.drawing_utils

# Used to access MediaPipe hand connections
mpHands = mp.solutions.hands


# --------------------------------------------------
# Draw Hand Landmarks
# --------------------------------------------------
#
# Input:
#   frame
#   hand detection results
#
# Output:
#   Modified frame
#
def draw_hands(frame, hand_results):

    # Check if any hand was detected
    if hand_results.multi_hand_landmarks:

        # Loop through every detected hand
        for handLms in hand_results.multi_hand_landmarks:

            # Draw 21 landmarks and connections
            mpDraw.draw_landmarks(
                frame,
                handLms,
                mpHands.HAND_CONNECTIONS
            )


# --------------------------------------------------
# Draw Face Box and Emotion
# --------------------------------------------------
#
# Input:
#   frame
#   emotion data dictionary
#
# Output:
#   Modified frame
#
def draw_emotion(frame, emotion_data):

    # If no face/emotion detected
    if emotion_data is None:
        return

    # Get face coordinates
    x = emotion_data["x"]
    y = emotion_data["y"]
    w = emotion_data["w"]
    h = emotion_data["h"]

    # Get emotion name
    emotion = emotion_data["emotion"]

    # Get confidence score
    confidence = emotion_data["confidence"]

    # Draw rectangle around face
    cv2.rectangle(
        frame,
        (x, y),
        (x + w, y + h),
        BOX_COLOR,
        LINE_THICKNESS
    )

    # Create text
    text = f"{emotion}: {confidence:.2f}"

    # Draw text above face
    cv2.putText(
        frame,
        text,
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        FONT_SCALE,
        TEXT_COLOR,
        LINE_THICKNESS
    )