from ultralytics import YOLO

# 1. Load YOUR newly trained brain
# Notice we are pointing it to the model2 folder exactly as your terminal output specified
model = YOLO('runs/detect/neu_defect_model2/weights/best.pt')

# 2. Pick a random validation image to test it on
# We are grabbing one image from your YOLO dataset
test_image_path = 'yolo_dataset/images/val/crazing_278.jpg' # Change the filename if this one doesn't exist

# 3. Run the prediction
print("Inspecting surface...")
results = model(test_image_path)

# 4. Show the image with the predicted boxes drawn on it!
for r in results:
    r.show()