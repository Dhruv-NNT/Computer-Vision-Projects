Here is a detailed README file for the first project in your "Computer Vision Projects" repository, crafted based on the provided assignment report and other files:

---

# 📸 Histogram Equalization for Image Enhancement

Welcome to the **Histogram Equalization for Image Enhancement** project. This project explores various Histogram Equalization (HE) techniques to enhance the contrast and improve the visual quality of digital images. The work is part of the Computer Vision Projects repository.

## 📝 Project Overview

Histogram Equalization (HE) is a fundamental image processing technique used to enhance the contrast of images. This project evaluates several HE methods, including Global HE, Adaptive HE, and Contrast-Limited Adaptive Histogram Equalization (CLAHE). It also investigates enhancements using Gaussian Smoothing and Non-Local Means (NLM) Denoising to optimize image quality.

## 🌟 Features

- **Global Histogram Equalization**: Enhances the global contrast of an image.
- **Luminance Histogram Equalization**: Operates on the luminance component to improve brightness distribution.
- **Adaptive Histogram Equalization**: Enhances local contrast by dividing the image into smaller regions.
- **Contrast-Limited Adaptive Histogram Equalization (CLAHE)**: Limits the contrast enhancement to avoid noise amplification.
- **Wavelet Denoising**: Reduces noise while preserving image details.
- **Gaussian Smoothing**: Applies Gaussian blur to reduce noise.

## 📂 Project Structure

```
📦Histogram Equalization for Image Enhancement
 ┣ 📜Assignment Report - Aradhya Dhruv.pdf         # Detailed assignment report
 ┣ 📜Assignment 1 Code - Aradhya Dhruv.pdf         # Code for the assignment
 ┣ 📜Assignment 1 Objective.pdf                    # Objectives and guidelines for the assignment
 ┣ 📜README.md                                     # Project overview and instructions
 ┗ 📜requirements.txt                              # Dependencies for the project
```

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/computer-vision-projects.git
cd computer-vision-projects/histogram-equalization
```

2. **Create a virtual environment and activate it:**

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

3. **Install the required dependencies:**

```bash
pip install -r requirements.txt
```

## 🚀 Running the Code

1. **Open the Jupyter Notebook:**

```bash
jupyter notebook
```

2. **Run the cells in the notebook to execute the experiments and view the results.**

## 📊 Detailed Results

### Metrics Used

- **Peak Signal-to-Noise Ratio (PSNR)**: Measures image quality by comparing the original image to the processed image.
- **Structural Similarity Index (SSIM)**: Evaluates the structural similarity between the original and processed images.

### Key Findings

- **Global Histogram Equalization**: Provides basic contrast enhancement but is less effective for images with varied exposure.
- **Luminance Histogram Equalization**: Improves luminance distribution but has limitations with overexposed images.
- **Adaptive Histogram Equalization**: Achieves the highest PSNR and SSIM scores, making it the most effective method for diverse exposure conditions.
- **CLAHE**: Effectively enhances contrast while avoiding noise amplification, but may introduce visual artifacts.
- **Wavelet Denoising**: Reduces high-frequency noise but can affect color saturation.

### Results:
- The 1st row represents the raw image data given for equalization, whereas the 2nd row shows the equalized images
![image](https://github.com/user-attachments/assets/f18ca2f3-baba-4d9a-8c6a-eb4e6f98a158)

### Enhancements

- **Gaussian Smoothing**: Minor improvements in noise reduction but limited impact on overall image quality.
- **NLM Denoising**: Successfully reduces noise but requires further optimization to avoid altering high-frequency details.

## 🔍 Future Work

- Further research on alternative enhancement methods or parameter optimization for better image quality.
- Exploration of real-time applications with computational efficiency improvements.

## 📧 Contact

For any questions or feedback, feel free to reach out to:

- **Name**: Aradhya Dhruv
- **Email**: aradhya.dhruv@example.com

## 📝 Acknowledgements

This project was conducted as part of the coursework for the Masters in Artificial Intelligence program at Nanyang Technological University, School of Computer Science and Engineering, Singapore.

---

Feel free to further customize this README file based on any additional specific details or preferences you have!
