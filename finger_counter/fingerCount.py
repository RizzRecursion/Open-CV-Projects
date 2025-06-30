import cv2
import mediapipe as mp

cap= cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils        
tip_ids = [4, 8, 12, 16, 20]
while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Mirror image for better UX
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks:
        handLms = result.multi_hand_landmarks[0]
        lm_list = []

        for id, lm in enumerate(handLms.landmark):
            h, w, _ = frame.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lm_list.append((cx, cy))

        fingers = []

        # Thumb: check x position
        # lm[id][1]=y
        if lm_list[tip_ids[0]][0] < lm_list[tip_ids[0] - 1][0]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other fingers: check y position
        for i in range(1, 5):
            if lm_list[tip_ids[i]][1] < lm_list[tip_ids[i] - 2][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        total_fingers = sum(fingers)

        # Draw landmarks & connections
        mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

        # Display finger count
        cv2.rectangle(frame, (0, 0), (150, 100), (0, 0, 0), -1)
        cv2.putText(frame, f'Fingers: {total_fingers}', (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("Finger Counter", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break