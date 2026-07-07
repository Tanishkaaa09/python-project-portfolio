import cv2
import os

# Get the folder where this Python file is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Full path of the Haar Cascade XML file
xml_path = os.path.join(base_dir, "haarcascade_frontalface_default.xml")

# Load Haar Cascade
face_capture = cv2.CascadeClassifier(xml_path)

# Check if XML loaded successfully
if face_capture.empty():
    print("Error: Could not load Haar Cascade XML file.")
    print("Expected location:", xml_path)
    exit()

# Open webcam
video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Check webcam
if not video_capture.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = video_capture.read()

    if not ret:
        print("Failed to capture frame.")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_capture.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show number of faces
    cv2.putText(
        frame,
        f"Faces: {len(faces)}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    # Display webcam
    cv2.imshow("Face Detection", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()