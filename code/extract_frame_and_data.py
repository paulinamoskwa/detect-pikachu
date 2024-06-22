import os
import shutil
import json

INPUT_DATA_PATH = "__<PATH_TO_UNITY_OUTPUT>__"
OUTPUT_DATA_PATH = "__<PATH_TO_WHERE_TO_SAVE_PROCESSED_OUTPUT>__"
OUTPUT_IMAGES_PATH = OUTPUT_DATA_PATH + "images/"
OUTPUT_LABELS_PATH = OUTPUT_DATA_PATH + "labels/"


if __name__ == "__main__":

    os.makedirs(OUTPUT_DATA_PATH, exist_ok=True)
    os.makedirs(OUTPUT_IMAGES_PATH, exist_ok=True)
    os.makedirs(OUTPUT_LABELS_PATH, exist_ok=True)

    # There are 4 folders of generated data 
    for index in range(1, 5):
        full_input_data_path = INPUT_DATA_PATH + str(index)
        list_of_sequences = [seq for seq in os.listdir(full_input_data_path) if "sequence" in seq]
        list_of_sequences.sort()
        
        for sequence in list_of_sequences:
            # Let's consider only from the 11th to 110th sequence
            sequence_number = int(sequence.split(".")[-1])
            
            if sequence_number > 10:
                # For every considered sequence
                # extract only the 5th frame (more stable)
                sequence_path = os.path.join(full_input_data_path, sequence)
                elem_path = os.path.join(sequence_path, "step4.camera.png")
                shutil.copy(elem_path, os.path.join(OUTPUT_IMAGES_PATH, f"v{index}__{sequence_number - 10}.png"))

                # YOLOv8 (from ultralytics) needs the following annotations
                #   image0.png -> image0.txt -> <class_id> <x_center> <y_center> <width> <height>
                elem_data_path = os.path.join(sequence_path, "step4.frame_data.json")
                with open(elem_data_path, 'r') as file:
                    data = json.load(file)

                image_width, image_height = data['captures'][0]['dimension']

                annotations = data['captures'][0]['annotations']
                for annotation in annotations:
                    if 'box' in annotation['id'] :
                        box_coord = annotation['values'][0]
                        width, height = box_coord['dimension']
                        x, y = box_coord['origin']
                        x_center = (x+(width/2))/image_width
                        y_center = (y+(height/2))/image_height
                        width = width/image_width
                        height = height/image_height
                        with open(os.path.join(OUTPUT_LABELS_PATH, f"v{index}__{sequence_number-10}.txt"), 'w') as f:
                            f.write(f"0 {x_center} {y_center} {width} {height}")

