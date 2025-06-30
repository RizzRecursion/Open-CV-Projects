import cv2
from deepface import DeepFace

# Open webcam
cap = cv2.VideoCapture(0)
print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)  # Flip the frame horizontally for a mirror effect
    if not ret:
        break

    try:
        # Analyze for emotions
        results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        for result in results:
            # Get face region
            region = result['region']
            x, y, w, h = region['x'], region['y'], region['w'], region['h']

            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Get dominant emotion
            emotion = result['dominant_emotion']

            # Put emotion text above rectangle
            cv2.putText(frame,
                        emotion,
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,
                        (0, 255, 0),
                        2)

    except Exception as e:
        print("Error:", e)

    cv2.imshow("Facial Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
