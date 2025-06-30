`gesture_volume_control/README.md`

```markdown
# 🔊 Gesture-Based Volume Control

Control your system volume using just your fingers and webcam!

## 🎥 Demo
![Volume Control Demo](../assets/volume_control.gif)

## ⚙️ Technologies Used
- Python
- OpenCV
- Mediapipe
- Pycaw (Windows Audio Control)

## 💡 How It Works
- Detects your hand using Mediapipe
- Measures distance between thumb and index finger
- Maps that distance to a volume level using Pycaw

## ▶️ How to Run (Windows only)
```bash
pip install opencv-python mediapipe pycaw comtypes
python main.py