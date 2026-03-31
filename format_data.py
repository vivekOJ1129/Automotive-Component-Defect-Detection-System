import os
import glob
import shutil
import xml.etree.ElementTree as ET

# The 6 defect classes in exact order (do not change this)
classes = ["crazing", "inclusion", "patches", "pitted_surface", "rolled-in_scale", "scratches"]

def convert_box(size, box):
    # Converts exact pixel coordinates to normalized YOLO format (0.0 to 1.0)
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    return (x * dw, y * dh, w * dw, h * dh)

def prep_yolo_data(base_src, base_dst, split_name):
    print(f"Processing {split_name} data...")
    # YOLO prefers the name 'val' instead of 'validation'
    yolo_split = 'val' if split_name == 'validation' else 'train'
    
    # Create the new YOLO directory structure
    img_dst_dir = os.path.join(base_dst, 'images', yolo_split)
    lbl_dst_dir = os.path.join(base_dst, 'labels', yolo_split)
    os.makedirs(img_dst_dir, exist_ok=True)
    os.makedirs(lbl_dst_dir, exist_ok=True)

    src_ann_dir = os.path.join(base_src, split_name, 'annotations')
    src_img_dir = os.path.join(base_src, split_name, 'images')

    # Step A: Find all images, even if they are hidden in subfolders
    img_paths = {}
    for root, _, files in os.walk(src_img_dir):
        for f in files:
            if f.endswith('.jpg'):
                img_paths[f] = os.path.join(root, f)

    # Step B: Parse XMLs, create TXTs, and copy corresponding images
    xml_files = glob.glob(os.path.join(src_ann_dir, '*.xml'))
    
    for xml_file in xml_files:
        base_name = os.path.splitext(os.path.basename(xml_file))[0]
        img_name = base_name + '.jpg'
        
        if img_name not in img_paths:
            print(f"Warning: Could not find image {img_name} for annotation {xml_file}")
            continue
            
        # 1. Copy the image over to the new flat folder
        shutil.copy(img_paths[img_name], os.path.join(img_dst_dir, img_name))
        
        # 2. Parse the XML and create the .txt file
        tree = ET.parse(xml_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)
        
        txt_path = os.path.join(lbl_dst_dir, base_name + '.txt')
        with open(txt_path, 'w') as out_file:
            for obj in root.iter('object'):
                cls = obj.find('name').text
                if cls not in classes:
                    continue
                cls_id = classes.index(cls)
                xmlbox = obj.find('bndbox')
                b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
                     float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
                bb = convert_box((w, h), b)
                # Write to file
                out_file.write(f"{cls_id} {' '.join([str(a) for a in bb])}\n")

# Run the formatting for both train and validation folders
prep_yolo_data('NEU-DET', 'yolo_dataset', 'train')
prep_yolo_data('NEU-DET', 'yolo_dataset', 'validation')

print("\nSuccess! Your data is now perfectly formatted for YOLO.")