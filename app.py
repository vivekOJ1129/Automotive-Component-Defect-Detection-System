import streamlit as st
from ultralytics import YOLO
from PIL import Image

# 1. Page Configuration
st.set_page_config(page_title="Industrial Defect Detection", layout="wide")
st.title("Automotive Component Defect Detection System")
st.write("Upload an image of a surface to identify and localize defects (Scratches, Crazing, Inclusions, etc.).")

# 2. Load the Model (We cache it so it only loads once)
@st.cache_resource
def load_model():
    # Make sure this path matches where your best.pt is saved!
    return YOLO('runs/detect/neu_defect_model2/weights/best.pt')

model = load_model()

# 3. Create the File Uploader
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Read the uploaded image
    image = Image.open(uploaded_file)
    
    # Create two columns for a side-by-side view
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Surface")
        # FIX: Changed to use_column_width for older Streamlit compatibility
        st.image(image, use_column_width=True) 
    
    with st.spinner("Analyzing surface for defects..."):
        # 4. Run Inference
        results = model.predict(image)
        
        # YOLO's .plot() automatically draws the bounding boxes and labels
        # Note: It returns a numpy array in BGR color format
        res_plotted = results[0].plot()
        
    with col2:
        st.subheader("Inspection Results")
        # FIX: Added channels="BGR" so the colors display correctly, and use_column_width
        st.image(res_plotted, channels="BGR", use_column_width=True)
        
    # 5. Display a textual summary below the images
    st.write("---")
    st.write("Defect Summary")
    
    boxes = results[0].boxes
    if len(boxes) == 0:
        st.success("No defects detected. Component passes inspection.")
    else:
        st.error(f"{len(boxes)} defect(s) detected!")
        for box in boxes:
            class_id = int(box.cls[0])
            conf = float(box.conf[0])
            class_name = model.names[class_id]
            st.write(f"- **{class_name.capitalize()}** detected with **{conf*100:.1f}%** confidence.")
        