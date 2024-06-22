<br>

<br>

<p align="center" width="100%">
  <img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/557f80b9-eee0-4d4d-be7e-9517f228a540" style="width: 50%; display: block; margin: auto;"></a><br>
  Fine-tune a YOLOv8 model to detect Pikachu without worrying about the training data.
</p>

<br>

<br>

<p align="center">
  <img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/bcad884c-8bf1-4ba8-842e-0d828449c5df" width="49.5%"/> 
  <img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/d6be350e-6db9-4bf2-b1a8-01a163912318" width="49.5%"/> 
</p>

<br>

<br>

# About

The main problem when training a detection model, or generally when dealing with machine learning models, is the data. The goal of this project is to train an object detection model (YOLOv8) without manually creating every training image and annotation. Instead, we create a 3D model of the object and we exploit Unity Perception package to automatically generate several images and annotations.

The overall pipeline looks as follows.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/4a8b6a39-3ff6-4c6b-8037-76d78f5fee8a" style="width: 100%">
</p>

- Use MagiScan 3D to make the 3D model of Pikachu. This model is in a raw format and needs some cleaning.
- The raw 3D Pikachu model is post-processed in Blender, where the support and other small noises are deleted.
- Export the 3D model and its texture, and move it to Unity, where a Perception project needs to be set up.
- Generate the detection data. Afterwards, modify the generated coordinates to match the YOLOv8 format.
- Finally, train the YOLOv8 model solely with synthetic data.

<br>

<br>

<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/87953e10-a612-4071-9d68-ea2d6b348bd9" style="width: 100%">
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

<br>

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
- Now, pressing the play button, the data generation will begin.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/78856b5d-8e81-42e6-b195-664e5bd7b220" style="width: 80%">
</p>

- To find where the images are being saved: `Edit` > `Project Settings` > `Perception` > `Solo Endpoint` > `Base Path` is the folder where the outputs are collected. (`Show Folder`) to check.








