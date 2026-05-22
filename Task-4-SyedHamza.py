import cv2
import pytesseract
import numpy as np
from datetime import datetime
import os

# =========================================================
# AI OCR PROJECT
# ADVANCED VERSION
# =========================================================

print("\n====================================")
print("   AI OCR TEXT RECOGNITION SYSTEM")
print("====================================\n")

# =========================================================
# TESSERACT OCR PATH
# =========================================================

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# =========================================================
# CREATE OUTPUT FOLDER
# =========================================================

if not os.path.exists("output"):
    os.makedirs("output")

# =========================================================
# LOAD IMAGE
# =========================================================

# CHANGE THIS PATH IF YOUR IMAGE NAME IS DIFFERENT
image_path = r"E:\project cod\decodelab projects\Task-4-SyedHamza.jpg"

print("Trying to load image...")
print(image_path)

image = cv2.imread(image_path)

# =========================================================
# CHECK IMAGE
# =========================================================

if image is None:
    print("\nERROR: Image not found!")
    print("\nFix:")
    print("1. Check image name")
    print("2. Check image extension")
    print("3. Make sure image exists")
    exit()

print("\nImage loaded successfully!")

# =========================================================
# IMAGE RESIZE
# =========================================================

image = cv2.resize(image, (1000, 700))

# Copy image for drawing boxes
original = image.copy()

# =========================================================
# IMAGE PREPROCESSING
# =========================================================

print("\nProcessing image...")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Remove noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Sharpen image
kernel = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
])

sharpen = cv2.filter2D(blur, -1, kernel)

# Adaptive thresholding
thresh = cv2.adaptiveThreshold(
    sharpen,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

# =========================================================
# MORPHOLOGICAL OPERATIONS
# EXTRA FEATURE
# =========================================================

kernel2 = np.ones((1, 1), np.uint8)

thresh = cv2.morphologyEx(
    thresh,
    cv2.MORPH_CLOSE,
    kernel2
)

# =========================================================
# OCR CONFIGURATION
# =========================================================

custom_config = r'--oem 3 --psm 6'

# =========================================================
# OCR DETECTION
# =========================================================

print("\nRunning OCR Detection...")

data = pytesseract.image_to_data(
    thresh,
    config=custom_config,
    output_type=pytesseract.Output.DICT
)

# =========================================================
# TEXT STORAGE
# =========================================================

detected_text = []

# =========================================================
# DRAW BOUNDING BOXES
# =========================================================

n_boxes = len(data['text'])

for i in range(n_boxes):

    text = data['text'][i].strip()

    if text != "":

        try:
            confidence = float(data['conf'][i])

        except:
            confidence = 0

        # Confidence Filter
        if confidence > 60:

            x = data['left'][i]
            y = data['top'][i]
            w = data['width'][i]
            h = data['height'][i]

            # Draw rectangle
            cv2.rectangle(
                original,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Create label
            label = f"{text} ({int(confidence)}%)"

            # Put text on image
            cv2.putText(
                original,
                label,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

            detected_text.append(label)

# =========================================================
# FULL TEXT EXTRACTION
# =========================================================

full_text = pytesseract.image_to_string(
    thresh,
    config=custom_config
)

# =========================================================
# PRINT RESULTS
# =========================================================

print("\n====================================")
print("       DETECTED TEXT OUTPUT")
print("====================================\n")

print(full_text)

# =========================================================
# SAVE TEXT FILE
# =========================================================

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

text_file = (
    f"output/extracted_text_{timestamp}.txt"
)

with open(text_file, "w", encoding="utf-8") as file:
    file.write(full_text)

print("\nText file saved:")
print(text_file)

# =========================================================
# SAVE OUTPUT IMAGE
# =========================================================

output_image = (
    f"output/output_image_{timestamp}.jpg"
)

cv2.imwrite(output_image, original)

print("\nOutput image saved:")
print(output_image)

# =========================================================
# SAVE PROCESSED IMAGE
# EXTRA FEATURE
# =========================================================

processed_image = (
    f"output/processed_image_{timestamp}.jpg"
)

cv2.imwrite(processed_image, thresh)

print("\nProcessed image saved:")
print(processed_image)

# =========================================================
# WORD COUNT FEATURE
# EXTRA FEATURE
# =========================================================

words = full_text.split()

print("\n====================================")
print("           STATISTICS")
print("====================================")

print(f"\nTotal Words Detected: {len(words)}")
print(f"Total Characters: {len(full_text)}")

# =========================================================
# SHOW IMAGES
# =========================================================

cv2.imshow("Original Image", image)

cv2.imshow("Processed Image", thresh)

cv2.imshow("AI OCR Detection", original)

# =========================================================
# KEYBOARD SHORTCUTS
# =========================================================

print("\n====================================")
print("KEYBOARD SHORTCUTS")
print("====================================")

print("\nPress 'S' to save screenshots")
print("Press any key to exit")

key = cv2.waitKey(0)

# =========================================================
# MANUAL SCREENSHOT SAVE
# =========================================================

if key == ord('s') or key == ord('S'):

    cv2.imwrite(
        "output/manual_original.jpg",
        image
    )

    cv2.imwrite(
        "output/manual_processed.jpg",
        thresh
    )

    cv2.imwrite(
        "output/manual_detection.jpg",
        original
    )

    print("\nManual screenshots saved!")

# =========================================================
# CLOSE WINDOWS
# =========================================================

cv2.destroyAllWindows()

# =========================================================
# END MESSAGE
# =========================================================

print("\n====================================")
print(" PROJECT FINISHED SUCCESSFULLY!")
print("====================================\n")