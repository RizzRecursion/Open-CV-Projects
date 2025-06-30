import cv2
import mediapipe as mp

# Webcam input
cap = cv2.VideoCapture(0)

# Mediapipe initialization
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

tip_ids = [4, 8, 12, 16, 20]

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks and result.multi_handedness:
        handLms = result.multi_hand_landmarks[0]
        handType = result.multi_handedness[0].classification[0].label  # 'Left' or 'Right'
        lm_list = []

        for id, lm in enumerate(handLms.landmark):
            h, w, _ = frame.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lm_list.append((cx, cy))

        fingers = []

        # Thumb logic depending on hand type
        if handType == "Right":
            if lm_list[4][0] > lm_list[3][0]:
                fingers.append(1)
            else:
                fingers.append(0)
        else:  # Left hand
            if lm_list[4][0] < lm_list[3][0]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Other 4 fingers
        for i in range(1, 5):
            if lm_list[tip_ids[i]][1] < lm_list[tip_ids[i] - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        total_fingers = sum(fingers)

        # Draw landmarks
        mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

        # Show count
        cv2.rectangle(frame, (0, 0), (160, 100), (0, 0, 0), -1)
        cv2.putText(frame, f'{handType} Hand', (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
        cv2.putText(frame, f'Fingers: {total_fingers}', (10, 85),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.imshow("Finger Counter", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
