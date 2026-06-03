import cv2
import mediapipe as mp

# Load MediaPipe hand model
mpHands = mp.solutions.hands

# Create hand detector object
hands = mpHands.Hands()


def detect_hands(frame):

    # Convert image from BGR to RGB
    imgRGB = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    # Detect hands
    results = hands.process(imgRGB)

    # Return detection results
    return results