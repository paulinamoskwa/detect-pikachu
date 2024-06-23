<br>

<br>

<p align="center" width="100%">
  <img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/7aa24fc2-3598-474f-bfae-fe6a3452d193" style="width: 50%; display: block; margin: auto;"></a><br>
  <h1 align="center">Detect Pikachu</h1>
  <p align="center">
    Fine-tune a YOLOv8 model to detect Pikachu without worrying about the training data.
  </p>
</p>

<br>

<br>

<p align="center">
  <img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/c8b49e72-9afb-4c51-8c86-573c3547fc3a" width="49.5%"/> 
  <img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/dc0eb7fd-3af1-411e-920c-72f4c6573c14" width="49.5%"/><br>
  <i>3D Pikachu modeling, synthetic data generation with Unity Perception.</i><br><br>
  <img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/bcad884c-8bf1-4ba8-842e-0d828449c5df" width="49.5%"/> 
  <img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/d6be350e-6db9-4bf2-b1a8-01a163912318" width="49.5%"/><br>
  <i>YOLOv8 fine-tuning exclusively on synthetic data.</i>
</p>

<br>

# About

The main problem when training a detection model, or generally when dealing with machine learning models, is the data. The goal of this project is to train an object detection model (YOLOv8) without manually creating every training image and annotation. Instead, we create a 3D model of the object and we exploit the Unity Perception package to automatically generate several images and annotations.

The overall pipeline looks as follows.
<p align="center" width="100%">
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/8f67802a-7dca-43ff-ace3-fa7102aa9658" style="width: 100%">
</p>

- Use MagiScan 3D to make the 3D model of Pikachu. This model is in a raw format and needs some cleaning.
- The raw 3D Pikachu model is post-processed in Blender, where small noises are deleted.
- Export the 3D model and its texture, and move it to Unity, where a Perception project needs to be set up.
- Generate the detection data. Afterwards, modify the generated coordinates to match the YOLOv8 format.
- Finally, train the YOLOv8 model solely with synthetic data.

<br>

<br>

<p align="center" width="100%">
  <a href="https://github.com/paulinamoskwa/detect-pikachu/tree/main/tutorial.md">
    <img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/732f7213-04fc-4ac6-bbe9-4da3db9a73fd" style="width: 100%">
  </a>
</p>


