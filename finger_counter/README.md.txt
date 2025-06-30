# ✋ Finger Counter using OpenCV + Mediapipe

A real-time hand tracking project that counts how many fingers you're holding up using your webcam.

## 📹 Demo
![Finger Counter Demo](../assets/finger_counter.gif)

## 🧰 Technologies Used
- Python
- OpenCV
- Mediapipe

## 🧠 How It Works
- Uses Mediapipe to detect 21 landmarks on your hand
- Compares fingertip positions to their lower joints
- Counts how many fingers are raised

## ▶️ How to Run
```bash
pip install opencv-python mediapipe
python main.py