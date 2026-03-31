from ultralytics import YOLO

# 1. Load the pre-trained YOLOv8 Nano model
# This downloads a small foundational model that already understands basic shapes and edges.
model = YOLO('yolov8n.pt') 

if __name__ == '__main__':
    print("Starting YOLOv8 training on NEU-DET dataset...")
    
    # 2. Train the model on our specific dataset
    results = model.train(
        data='data.yaml',       # Points to the map we made in Step 2
        epochs=50,              # How many times the AI will look through the entire dataset
        imgsz=200,              # NEU-DET images are naturally 200x200 pixels
        batch=16,               # How many images it processes at once before updating its weights
        name='neu_defect_model' # The folder name where our results will be saved
    )
    
    print("Training complete! Check the 'runs/detect/neu_defect_model' folder for your results.")