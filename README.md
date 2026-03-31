# 🏭 Automotive Component Defect Detection System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![YOLOv8](https://img.shields.io/badge/YOLO-v8-yellow)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Industry 4.0](https://img.shields.io/badge/Domain-Industry%204.0-lightgrey)

An Industrial Computer Vision Pipeline using Deep Learning to detect and localize surface defects on automotive steel components in real-time. 

Developed as a **Minor-2 Project** for the Minor Degree in Electronics and Communication Engineering at the **National Institute of Technology, Andhra Pradesh**.

---

## 📖 About the Project

Automated visual inspection is a critical component of modern manufacturing, significantly reducing human error and minimizing scrap costs in high-throughput environments. This project bridges the gap between mechanical material science and electronic computer vision (Industry 4.0) by transitioning from manual feature-extraction methods to a deep Convolutional Neural Network (CNN) architecture.

The system utilizes the **YOLOv8** (You Only Look Once) architecture for single-pass regression, achieving high accuracy and an exceptional inference speed of **~6.5 milliseconds per image**. The model is deployed via a **Streamlit** web dashboard, empowering factory operators with a real-time, user-friendly interface for immediate quality control decisions.

### 🔍 Detectable Defect Classes:
The model is trained on the NEU Surface Defect Database (NEU-DET) to simultaneously localize and classify six distinct types of surface defects:
1. Crazing
2. Inclusions
3. Patches
4. Pitted Surface
5. Rolled-in Scale
6. Scratches

---

## 🛠️ Tech Stack

*   **Computer Vision Framework:** Ultralytics YOLOv8
*   **Web Application Interface:** Streamlit
*   **Programming Language:** Python
*   **Image Processing:** OpenCV, PIL
*   **Data Manipulation:** NumPy, Pandas

---

## 🚀 Installation and Setup

To run this project locally on your machine, follow these steps:

### 1. Clone the repository
```bash
git clone [https://github.com/vivekOJ1129/Automotive-Component-Defect-Detection-System.git](https://github.com/vivekOJ1129/Automotive-Component-Defect-Detection-System.git)
cd Automotive-Component-Defect-Detection-System
