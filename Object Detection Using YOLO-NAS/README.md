# 🕵️‍♂️📷 Object Detection Using YOLO NAS

This project demonstrates how to build a computer vision interface using Streamlit in Python for real-time object detection. It utilizes the YOLO NAS (You Only Look Once - Neural Architecture Search) object detection model, which is known for its efficiency and accuracy in detecting objects in images and videos.

## 📚 Project Overview

YOLO NAS (You Only Look Once - Neural Architecture Search) is an advanced version of the YOLO object detection model. It leverages neural architecture search to automatically design a network architecture optimized for speed and accuracy. YOLO NAS combines the benefits of YOLO's real-time object detection capabilities with the optimization advantages of neural architecture search.

## 🚀 Features

- **Real-Time Object Detection**: Perform object detection on images and videos in real-time.
- **Streamlit Interface**: User-friendly web interface for uploading images and videos, and viewing detection results.
- **High Accuracy**: Utilizes YOLO NAS for precise object detection with optimized network architecture.
- **Adjustable Confidence Threshold**: Customize the confidence threshold to control detection sensitivity.

## 📁 Project Structure

```
📦Object Detection Using YOLO NAS
 ┣ 📜Project Demo.mp4                          # Demo video showcasing the app's functionality
 ┣ 📜object_detection_image_video_streamlit.py # Script for performing object detection on images and videos using Streamlit
 ┣ 📜packages.txt                              # Additional package information
 ┣ 📜requirements.txt                          # List of required dependencies
 ┗ 📜yolo_nas_app.py                           # Main script for running the Streamlit app
```

## 🛠️ Requirements

- Python 3.10
- OpenCV-python
- SuperGradients

## 📦 Installation

1. **Create a new Python project directory.**
2. **Create a file named `requirements.txt` and add the following lines:**

   ```plaintext
   super-gradients==3.1.0
   opencv-python
   streamlit
   ```

3. **Open a terminal in the project directory and run:**

   ```bash
   pip install -r requirements.txt
   ```

## 📂 Code Structure

- `object_detection_image_video_streamlit.py`: This script performs object detection on images and videos using YOLO NAS.
- `yolo_nas_app.py`: This script creates the Streamlit app with three pages: About Me, Run on Image, and Run on Video.

## 🚀 Running the App

1. **Ensure you have installed the required libraries.**
2. **Open a terminal in the project directory and run:**

  ```bash
   streamlit run yolo_nas_app.py
   ```

## 🎦 Project Demo
https://github.com/user-attachments/assets/901ae109-edea-443f-af1f-fdac761dcb2c

## 🖥️ App Functionality

- **About Me**: This page displays information about the app and its creator.
- **Run on Image**: This page allows users to upload an image and perform object detection on it. Detected objects will be displayed with bounding boxes and confidence scores.
- **Run on Video**: This page allows users to select a video file or use the live webcam feed for object detection. Detected objects will be displayed with bounding boxes and confidence scores in real-time.

## 📝 Technical Details about YOLO NAS

YOLO NAS combines the efficiency of YOLO with the optimization capabilities of Neural Architecture Search (NAS). Here's a breakdown of its technical aspects:

1. **Neural Architecture Search (NAS)**:
   - NAS automates the process of designing network architectures, leading to optimized structures that balance speed and accuracy.
   - NAS explores a vast search space of possible architectures and identifies the best-performing model configurations.

2. **YOLO NAS Model Architecture**:
   - **Backbone**: A feature extraction network that captures spatial information from input images.
   - **Neck**: Aggregates features from different levels of the backbone to enhance object detection.
   - **Head**: Outputs the final predictions, including bounding box coordinates, class probabilities, and confidence scores.

3. **Loss Functions**:
   - **Localization Loss**: Measures the error between predicted and ground-truth bounding boxes.
   - **Confidence Loss**: Measures the confidence score accuracy of the predicted bounding boxes.
   - **Class Loss**: Measures the accuracy of classifying the detected objects.

4. **Training and Inference**:
   - YOLO NAS models are trained using large datasets with annotated bounding boxes and class labels.
   - During inference, the model processes input images or video frames, performing real-time object detection with high accuracy.

## 🔍 Further Exploration

- **Experiment with different YOLO NAS models**: Evaluate the performance trade-offs between speed and accuracy.
- **Integrate additional functionalities**: Enhance the Streamlit app with features such as saving the output images or videos.
- **Optimize performance**: Fine-tune the confidence threshold and other hyperparameters for improved detection accuracy.

## 📧 Contact

For any questions or feedback, feel free to reach out to:

- **Name**: Aradhya Dhruv
- **Email**: aradhya.dhruv@gmail.com

---
