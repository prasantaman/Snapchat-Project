import cv2
import cvzone

# Webcam capture
cap = cv2.VideoCapture(0)
# Haar Cascade Classifier for face detection
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# List of overlay images
overlay_images = [
    cv2.imread('beard.png', cv2.IMREAD_UNCHANGED),
    cv2.imread('native.png', cv2.IMREAD_UNCHANGED),
    cv2.imread('sunglass.png', cv2.IMREAD_UNCHANGED),
    cv2.imread('Snapchatlogo.png', cv2.IMREAD_UNCHANGED),
    cv2.imread('bhoot.png', cv2.IMREAD_UNCHANGED)
]

# Initialize the index for overlay images
overlay_index = 0

while True:
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        overlay_resize = cv2.resize(overlay_images[overlay_index], (int(w * 1.5), int(h * 1.5)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x - 45, y - 75])

    cv2.imshow('Snap Dude', frame)

    key = cv2.waitKey(10)
    if key == ord('m'):
        break
    elif key == ord('n'):  # Press 'n' to switch to the next overlay
        overlay_index = (overlay_index + 1) % len(overlay_images)  # Cycle through overlay images

cap.release()
cv2.destroyAllWindows()


