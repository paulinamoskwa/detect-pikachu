<br>

<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/3d75596b-c157-4e46-92c9-aa5dd919f376" style="width: 100%">
</p>

## Part 1 - MagiScan 3D and Blender to Create the Pikachu Model

- Download the free app MagiScan3D and follow the instruction to create the 3D model.
- Once the model is ready, export it as `glb` format. At this stage the 3D scan is raw, and needs a cleanup.
- Download Blender `3.6.3` and open it.
- `File` > `Import` > `glTF 2.0` > Load the model from MagiScan3D.
- First, on the top right, change the view of the object. Then, change `Object Mode` to `Edit Mode`.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/439e29af-4432-4554-9286-0b388dc0b12d" style="width: 60%">
</p>

- Select all the vertices to be deleted > Right click > `Delete Vertices`.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/4682cfb9-4b94-4716-9773-fd88c21241a9" style="width: 60%">
</p>

- The final model should be clean and should look as follow.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/4256cab5-416f-4483-8b77-7c7f0416f9c3" style="width: 60%">
</p>

- `File` > `Export` > `.fbx` > On the right column, `Path Mode` > `Copy` > Select the box near `Copy` and save.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/fc091643-4c51-499a-bca6-9fbba7af8352" style="width: 20%">
</p>

- `UV Editing` > `Image` > `Save As...` > Save the image texture of the object (as `RGBA`).
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/4d96d068-bd16-4c19-8211-a5ff48781424" style="width: 60%">
</p>

## Part 2 - Unity Perception for Synthetic Data Generation

- Download Unity Hub and Unity `2022.3.21f1 Silicon`.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/1510a8b3-d388-4b59-8ac7-07e5b885c13c" style="width: 60%">
</p>

- Start a new `High Definition 3D project`.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/2253c3fe-6cec-4b14-9d00-4a576e8991e7" style="width: 60%">
</p>

- `Window` > `Package Manager` > `Add package from git URL` > Insert `com.unity.perception`.
- `Window` > `Package Manager` > `Perception` > `Samples` > `Tutorial Files` > `Import`.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/258998d5-cea6-4ed0-8773-e96fa0e90bb5" style="width: 60%">
</p>

- `Project` tab > `Assets` > Create a new folder called `Scene`.
- Inside the `Scene` folder > `Create` > `Scene`, and call it `TutorialScene`, then double click on it.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/9479a39e-4639-4911-ad82-c0bb302f6b0d" style="width: 60%">
</p>

- In the `Hierarchy` panel, double click the `Main Camera`.
- In the `Inspector` panel of the `Main Camera` modify the values according to the image.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/df49a150-5da3-401d-a161-e4af8aa70cbd" style="width: 60%">
</p>

- Always in the `Inspector` panel of the `Main Camera` click on `Add Component` and add `Perception Camera`.  
- `Edit` > `Project Settings` > `Editor` > disable `Asynchronous Shader Compilation`.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/a4f26eda-869f-4491-9d16-dd3c2066bab6" style="width: 60%">
</p>

- `Project` tab > Look for `"HDRP High Fidelity"` in the search tab > `Lit Shader Mode` > `Both`.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/d16aadf2-3c3c-452a-b4e3-d1f7a94196f0" style="width: 60%">
</p>

- `Main Camera` > `Inspector` > `Perception Camera (Script)` > `Camera Labelers` > `+`, and add first `BoundingBox2DLabeler`, and then `SemanticSegmentationLabeler`.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/f60581ac-03fc-414b-9282-a873ae4c3e96" style="width: 60%">
</p>

- `Project` > `Assets` folder > `Create` > `Perception` > `ID Label Config`, renamed `TutorialIdLabelConfig`.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/5fd5bbb5-cafc-41ec-8e22-1ab2d8269126" style="width: 60%">
</p>

- `Project` > `Assets` folder > `Create` > `Perception` > `Semantic Segmentation Label Config`, renamed `TutorialSemanticSegmentationLabelConfig`.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/98609e03-1fad-413c-809c-17d74a92257b" style="width: 60%">
</p>

- `Main Camera` > `Perception Camera (Script)` > Drag and drop the newly created files to the corresponding `Camera Labelers Label Config` (see image).
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/4a44b8bd-d2da-4078-b9be-ffb179fbb113" style="width: 60%">
</p>

- `Project` > `Scene` > Drag and drop the Pikachu model (`.fbx`), the model texture (`.png`), and the background image (`png`).
- `Project` > `Scene` > `Create` > `Material` > Drag and drop the model texture (`.png`) to the new material's `Surface Inputs` > `Base Map`.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/6ba8310b-db15-4ada-9eae-d921dd8bc5e1" style="width: 60%">
</p>

- `Project` > `Scene` > Drag and drop the Pikachu model into the `Hierarchy`. For the moment, this Pikachu will appear without colors nor texture.
- Drag and drop the material ball on the white Pikachu in `Scene`. Now the Pikachu should appear colored. 
- `Hierarchy` > Pikachu object > `Inspector` > `Add Component` > `Labeling` > `Use Automatic Labeling` > `Labeling Scheme` > `Use asset name` > `Add to Label Config...` > Select both `TutorialIdLabelConfig` and `TutorialSemanticSegmentationLabelConfig` (`Add Label` for both).
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/9e088041-bc21-4939-bcf4-ee6771c5f5ff" style="width: 60%">
</p>

- `Hierarchy` > Right click > `3D Object` > `Cube` > Drag the background image and drop it on the `Cube` object (which should now have the texture of the background image).
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/62aed873-5f68-45ca-8459-9239b4798d69" style="width: 60%">
</p>

- `Hierarchy` > `Cube` > `Inspector` > Adjust the values of `Transform` according to the image.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/48f42183-8e49-40a8-a607-d9244068a45c" style="width: 60%">
</p>

- Before proceeding, it might be necessary to modify the `Directional Light` to match some better values.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/df435e9c-7446-4dcb-90e1-5355144d5b2f" style="width: 60%">
</p>

- `Hierarchy` > Pikachu object > `Inspector` > `Add Component` > `Fixed Lenght Scenario` > `Add Randomizer` > `RotationRandomizer` > Set the values of the image.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/0663baaa-b3bd-4333-9755-e8813f48685f" style="width: 60%">
</p>

- Lastly, always in the Pikachu object `Inspector` > `Add Component` > `Rotation Randomizer Tag` (which is already present in the above image).
- Now, by pressing the play button the data generation will begin.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/78856b5d-8e81-42e6-b195-664e5bd7b220" style="width: 80%">
</p>

- To find where the images are being saved: `Edit` > `Project Settings` > `Perception` > `Solo Endpoint` > `Base Path` is the folder where the outputs are collected. (`Show Folder`) to check.

## Part 3 - Train YOLO Model and use it in Real Time
- It is convenient to repeat the synthetic data generation process with multiple position of the object in the frame. In this case, repeat the generation with 4 different position-size combination. 
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/bd6e1cbf-13ee-49b1-a1ec-c05d78e7c819" style="width: 60%">
</p>

- For each data generation (4) we have now a folder of sequences. The decision of generating sequences rather than single frames is because the first shot is blurry; the Perception package is so fast in making screenshots that the object movement cannot follow. The structure of the Unity outputs is as follows. 
```
data
 |
 └── pika1
 |    |
 |    └── annotation_definitions.json
 |    └── metadata.json
 |    └── metric_definition.json
 |    └── sensor_definitions.json
 |    └── sequence.0
 |    └── sequence.1
 |    └── ..
 |    └── sequence.2
 |    |    |
 |    |    └── step0.camera.png
 |    |    └── step0.camera.semantic.segmentation.png
 |    |    └── step0.frame_data.json
 |    |    └── ..
 |    |    └── step4.camera.png
 |    |    └── step4.camera.semantic.segmentation.png
 |    |    └── step4.frame_data.json
 |    |
 |    └── ..
 |    └── sequence.110
 |
 └── pika2
 └── pika3
 └── pika4
```

- From each sequence extract the last frame, the 5-th. Together with the frame, we collect the data from the corresponding `.json` annotation and we save it in the YOLOv8 format, namely `<class_id> <x_center> <y_center> <width> <height>`. The script that does that is `code/extract_frame_and_data.py`.
- Navigate to the output of the script and create a new file, `data.yaml`, with the following content. This is needed during the training of the YOLOv8 model.
```
train: ../images
val: ../images

nc: 1
names: ['Pikachu']
```

- The folder has to have the following format.
```
dataset
 |
 └── data.yaml
 |
 └── images
 |    |
 |    └── v1__1.png
 |    └── ..
 |    └── v1__100.png
 |    └── v2__1.png
 |    └── ..
 |    └── v2__100.png
 |    └── v3__1.png
 |    └── ..
 |    └── v3__100.png
 |    └── v4__1.png
 |    └── ..
 |    └── v4__100.png
 |
 └── labels
      |
      └── v1__1.txt
      └── ..
      └── v1__100.txt
      └── v2__1.txt
      └── ..
      └── v2__100.txt
      └── v3__1.txt
      └── ..
      └── v3__100.txt
      └── v4__1.txt
      └── ..
      └── v4__100.txt
```

- Zip the folder and load it on Colab.
- Move to Colab > Use the notebook `code/train_yolov8_model.ipynb` to train a YOLOv8 model.
- Save `/content/runs/detect/train/weights/best.pt` locally.
- To run the model, connect a webcam and run `code/run_realtime_pikachu_detection.py`.




