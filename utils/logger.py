# --------------------------------------------------
# LOGGER CONFIGURATION
# --------------------------------------------------

# Built-in Python logging module
import logging

# Used for file and folder paths
import os

# --------------------------------------------------
# PROJECT ROOT DIRECTORY
# --------------------------------------------------

# Current file:
# vision_ai_final/utils/logger.py
#
# Go one level up:
# vision_ai_final/
#

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# --------------------------------------------------
# LOG DIRECTORY
# --------------------------------------------------

# Final path:
# vision_ai_final/logs

LOG_FOLDER = os.path.join(
    BASE_DIR,
    "logs"
)

# Create logs folder if missing
os.makedirs(
    LOG_FOLDER,
    exist_ok=True
)

# --------------------------------------------------
# LOG FILE PATH
# --------------------------------------------------

# Final file:
# vision_ai_final/logs/vision_ai.log

LOG_FILE = os.path.join(
    LOG_FOLDER,
    "vision_ai.log"
)

# --------------------------------------------------
# CREATE LOGGER
# --------------------------------------------------

logger = logging.getLogger(
    "VisionAI"
)

# Log INFO and above
logger.setLevel(
    logging.INFO
)

# --------------------------------------------------
# FILE HANDLER
# --------------------------------------------------

file_handler = logging.FileHandler(
    LOG_FILE
)

# --------------------------------------------------
# LOG FORMAT
# --------------------------------------------------

# Example:
#
# 2026-06-03 16:10:22,123 | INFO | Application Started
#

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(
    formatter
)

# --------------------------------------------------
# PREVENT DUPLICATE HANDLERS
# --------------------------------------------------

if not logger.handlers:

    logger.addHandler(
        file_handler
    )