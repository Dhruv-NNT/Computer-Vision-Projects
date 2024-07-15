# 🖼️ Panoramic Image Stitching

Welcome to the **Panoramic Image Stitching** project. This project explores the process of combining multiple photographic images with overlapping fields of view to produce a segmented panorama or high-resolution image using homography. The work is part of the Computer Vision Projects repository.

## 📝 Project Overview

In the field of computer vision, image stitching is a fundamental technique used to create a larger, more comprehensive image or panorama by combining multiple overlapping images. This project implements the Scaled-Invariant Feature Transform (SIFT) algorithm for feature detection and matching, and employs homography for aligning and blending the images seamlessly.

## 🌟 Features

- **Feature Detection using SIFT**: Identifies distinctive points or regions in the images.
- **Feature Matching**: Matches features between images using brute force and K-Nearest Neighbors (KNN).
- **Homography**: Estimates the transformation between images to align them.
- **Image Blending**: Seamlessly merges overlapping images using techniques like weighted averaging and feathering.

## 📂 Project Structure

```
📦Image Stitching Assignment
 ┣ 📂image pairs
 ┃ ┣ 📜image pairs_01_01.jpg
 ┃ ┣ 📜image pairs_01_02.jpg
 ┃ ┣ 📜image pairs_02_01.png
 ┃ ┣ 📜image pairs_02_02.png
 ┃ ┣ 📜image pairs_03_01.jpg
 ┃ ┣ 📜image pairs_03_02.jpg
 ┃ ┣ 📜image pairs_04_01.jpg
 ┃ ┗ 📜image pairs_04_02.jpg
 ┣ 📜Assignment Code (pdf).pdf
 ┣ 📜Assignment Code.ipynb
 ┣ 📜Image stitching.ipynb
 ┗ 📜Report - Aradhya Dhruv.pdf
```

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/computer-vision-projects.git
cd computer-vision-projects/image-stitching
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

2. **Run the `Image stitching.ipynb` notebook to execute the image stitching process and view the results.**

## 📝 Project Details

### 1. Introduction

Image stitching combines multiple overlapping images to create a single panoramic image. This technique is widely used in applications such as autonomous robotics, medical imaging, virtual reality, and photography.

### 2. Feature Detection

**SIFT Algorithm**: Detects distinctive points or regions in images.

- **Scale Space Representation**: Uses a Laplacian function to create an image pyramid.
- **Difference of Gaussians (DoG)**: Identifies stable keypoint locations.
- **Extrema Detection**: Compares pixel values to find keypoints.

### 3. Feature Description and Matching

**Best Match using Brute Force**: Compares each keypoint in one image with every keypoint in another image.

**K-Nearest Neighbors (KNN)**: Finds the top k matches for each keypoint based on descriptor distances.

### 4. Homography and Image Stitching

**Homography Matrix**: Estimates the transformation between images.

**Image Stitching**: Aligns and blends multiple images to create a seamless panorama.

**Blending Techniques and Perspective Warping**:

- **Weighted Averaging**: Assigns weights to pixels in overlapping regions.
- **Feathering**: Smoothly transitions pixel values from one image to another.

## 📊 Results

### Stitched Images

Below are the results of the image stitching process. You can replace these placeholders with the actual images once they are generated.

1. **Stitched Image 1**
   
   ![image](https://github.com/user-attachments/assets/52453f09-e7d9-4754-a423-8d7272a4dad3)

2. **Stitched Image 2**
   
   ![image](https://github.com/user-attachments/assets/5790cb06-4ee3-4233-937f-85cfaae56721)

3. **Stitched Image 3**
   
   ![image](https://github.com/user-attachments/assets/38189b22-73a8-45dd-a581-43dec14eabae)

5. **Stitched Image 4**
   
   ![image](https://github.com/user-attachments/assets/f6d733db-d923-46e0-a1f2-522c14f345e2)


## 🔍 Future Work

- Explore real-time image stitching with enhanced computational efficiency.
- Investigate alternative feature detection and matching algorithms for improved accuracy.
- Enhance blending techniques to minimize artifacts and improve seamlessness.

## 📧 Contact

For any questions or feedback, feel free to reach out to:

- **Name**: Aradhya Dhruv
- **Email**: aradhya.dhruv@example.com

## 📝 Acknowledgements

This project was conducted as part of the coursework for the Masters in Artificial Intelligence program at Nanyang Technological University, School of Computer Science and Engineering, Singapore.

---
