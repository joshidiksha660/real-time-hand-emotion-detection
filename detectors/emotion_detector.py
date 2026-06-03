# Import DeepFace library
# This library contains a pre-trained AI model
# that can detect emotions from a face.
from deepface import DeepFace


# Function responsible for emotion detection
# Input  -> Webcam frame (image)
# Output -> Emotion data dictionary
def detect_emotion(frame):

    try:

        # ----------------------------------
        # STEP 1: Analyze the current frame
        # ----------------------------------
        #
        # DeepFace will:
        # 1. Find a face
        # 2. Crop the face
        # 3. Send it to the emotion model
        # 4. Return emotion scores
        #
        results = DeepFace.analyze(
            frame,
            actions=['emotion'],
            enforce_detection=False
        )

        # ----------------------------------
        # STEP 2: Get emotion scores
        # ----------------------------------
        #
        # Example:
        #
        # {
        #   "happy": 92.5,
        #   "sad": 1.2,
        #   "neutral": 5.0
        # }
        #
        emotions = results[0]["emotion"]

        # ----------------------------------
        # STEP 3: Find highest emotion
        # ----------------------------------
        #
        # max() checks all emotions
        # and returns the one with
        # the highest confidence score
        #
        top_emotion = max(
            emotions,
            key=emotions.get
        )

        # ----------------------------------
        # STEP 4: Get confidence score
        # ----------------------------------
        #
        # Example:
        #
        # happy -> 92.5
        #
        confidence = emotions[top_emotion]

        # ----------------------------------
        # STEP 5: Get face location
        # ----------------------------------
        #
        # DeepFace returns:
        #
        # {
        #   "x":100,
        #   "y":50,
        #   "w":200,
        #   "h":250
        # }
        #
        face = results[0]["region"]

        # ----------------------------------
        # STEP 6: Return clean data
        # ----------------------------------
        #
        # Instead of returning the huge
        # DeepFace response, we return only
        # the data needed by our application.
        #
        return {

            # Predicted emotion
            "emotion": top_emotion,

            # Confidence score
            "confidence": confidence,

            # Face coordinates
            "x": face["x"],
            "y": face["y"],
            "w": face["w"],
            "h": face["h"]
        }

    except Exception:

        # If DeepFace fails to detect a face
        # or throws an error, return None
        return None