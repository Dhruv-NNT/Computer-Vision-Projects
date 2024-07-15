# 🌉➡️🌆 Image-to-Image Translation using CycleGAN

Welcome to the **Image-to-Image Translation using CycleGAN** project. This project explores the use of Cycle-Consistent Generative Adversarial Networks (CycleGANs) for unpaired image-to-image translation. The focus is on translating images from one domain to another without the need for paired training examples. This work is part of the Computer Vision Projects repository.

## 📝 Project Overview

Image-to-image translation aims to learn the mapping between an input image and an output image using a training set of aligned image pairs. CycleGAN, however, tackles this problem in the unpaired setting by introducing cycle consistency to ensure that an image translated to the target domain can be mapped back to the original domain. This project applies CycleGAN to translate images between the Cityscapes and GTA V datasets, focusing on enhancing the realism and fidelity of the translated images.

## 🌟 Features

- **Unpaired Image Translation**: Translate images between different domains without paired training data.
- **Cycle Consistency Loss**: Ensures that translated images can be mapped back to the original domain.
- **Adversarial Training**: Uses GANs to generate realistic images in the target domain.
- **Residual Blocks**: Utilized in the generator for effective feature extraction and propagation.
- **Patch-based Discriminator**: Discriminates between real and synthetic images in localized regions.

## 📂 Project Structure

```
📦Image Stitching Assignment
 ┣ 📜image-translation-using-cyclegans.ipynb       # Jupyter notebook with code and experiments
 ┣ 📜Image Translation Project Report.pdf          # Detailed project report
 ┣ 📜README.md                                     # Project overview and instructions
 ┗ 📜requirements.txt                              # Dependencies for the project
```

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/computer-vision-projects.git
cd computer-vision-projects/image-to-image-translation
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

2. **Run the `image-translation-using-cyclegans.ipynb` notebook to execute the image translation process and view the results.**

## 📝 Project Details

### 1. Introduction

Recent advancements in computer vision have highlighted the potential of CycleGAN for unpaired image-to-image translation, which does not require paired training data. This project implements CycleGAN to translate images between the Cityscapes and GTA V datasets, focusing on maintaining visual fidelity and realism in the translated images.

### 2. Datasets Used

**Cityscapes**: Urban street scenes dataset with 30 distinct classes, diverse conditions, and 25,000 annotated images.

**GTA V**: Synthetic images from the GTA V game, annotated at the pixel level for 19 semantic classes, providing 24,966 images.

Provided below, is a snapshot the images from both the datasets:
![image](https://github.com/user-attachments/assets/8091a326-0a99-41c8-b20f-c9b6785c1270)


### 3. CycleGAN Overview

CycleGAN consists of two generator-discriminator pairs, \(G\) and \(F\), where \(G\) translates images from domain \(X\) to domain \(Y\), and \(F\) translates images from domain \(Y\) to domain \(X\). The key components include:

- **Adversarial Loss**: Encourages generators to produce realistic images.
- **Cycle Consistency Loss**: Ensures \(x \rightarrow G(x) \rightarrow F(G(x)) \approx x\) and \(y \rightarrow F(y) \rightarrow G(F(y)) \approx y\).
- **Identity Loss**: Ensures that \(G(y) \approx y\) and \(F(x) \approx x\) for stability.

### 4. Architecture Description

**Generators**: Utilize ResNet-style residual blocks for feature extraction and propagation. Incorporate downsample and upsample blocks to manage spatial dimensions.

**Discriminators**: Patch-based strategy with convolutional layers and Leaky ReLU activation to distinguish real from synthetic images in localized regions.

### 5. Insights Acquired during CycleGAN Implementation

- Optimal learning rate and loss function selection were critical.
- Implemented dropout layers and gradient penalty to stabilize training.
- Emphasized normalization and residual block adjustments for better performance.

## 📊 Results

### Translated Images

Below are the results of the image translation process. You can replace these placeholders with the actual images once they are generated.

![image](https://github.com/user-attachments/assets/d57e31fb-b4b2-458a-b4a7-520a9df750a9)

## 🔍 Future Work

- Explore advanced loss functions such as Wasserstein GAN (WGAN) for improved stability.
- Implement learning rate scheduling for more stable convergence.
- Incorporate data augmentation techniques for better generalization.

## 📧 Contact

For any questions or feedback, feel free to reach out to:

- **Name**: Aradhya Dhruv
- **Email**: aradhya.dhruv@gmail.com

## 📝 Acknowledgements

This project was conducted as part of the coursework for the Masters in Artificial Intelligence program at Nanyang Technological University, School of Computer Science and Engineering, Singapore.

---
