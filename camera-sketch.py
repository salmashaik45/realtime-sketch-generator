import cv2

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("Press SPACE to capture image")
print("Press ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)

    # Press SPACE to capture
    if key % 256 == 32:
        img = frame
        break

    # Press ESC to exit
    elif key % 256 == 27:
        cap.release()
        cv2.destroyAllWindows()
        exit()

cap.release()
cv2.destroyAllWindows()

# Convert to sketch (drawing effect)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted = cv2.bitwise_not(gray)
blur = cv2.GaussianBlur(inverted, (21, 21), 0)
inverted_blur = cv2.bitwise_not(blur)
sketch = cv2.divide(gray, inverted_blur, scale=256.0)

# Save sketch image
cv2.imwrite("sketch_image.jpg", sketch)
print("Sketch saved as sketch_image.jpg")

# Show sketch
cv2.imshow("Sketch Drawing", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()