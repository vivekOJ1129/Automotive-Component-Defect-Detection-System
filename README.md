Markdown

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

2. Create a Virtual Environment (Recommended)
Bash

python -m venv venv
# On Windows use: venv\Scripts\activate
# On Mac/Linux use: source venv/bin/activate

3. Install the dependencies
Bash

pip install ultralytics streamlit opencv-python pillow

4. Run the Streamlit Application

Ensure your YOLOv8 weights file (e.g., best.pt) is placed in the correct directory as referenced in your code, then run:
Bash

streamlit run app.py

🖥️ Usage

    Open the local web address provided by Streamlit in your terminal (usually http://localhost:8501).

    Upload an image of a steel or automotive component (JPG, JPEG, PNG).

    The application will instantly process the image using the YOLOv8 model.

    View the resulting image with color-coded bounding boxes drawn directly over the localized defects.

    Check the dynamic summary report for a breakdown of detected classes and confidence scores.

📸 Screenshots

(Note: Replace these placeholder links with actual screenshots of your running Streamlit app once you upload the images to your repository!)

Home Page & Upload Interface:

<!-- <img src="images/home_screen.png" width="600"> -->

Real-Time Defect Detection Results:

<!-- <img src="images/prediction_result.png" width="600"> -->
👨‍💻 Author

Vivekanand Ojha

    Roll No. 723159

    3rd Year, B.Tech Mechanical Engineering

    Minor in Electronics and Communication Engineering

    National Institute of Technology, Andhra Pradesh

Under the Guidance of:

    Dr. P Usha, Assistant Professor (ECE)

If you find this project helpful, please consider giving it a ⭐!
