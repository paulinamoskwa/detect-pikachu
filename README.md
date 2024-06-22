<br>

<p align="center" width="100%">
  <img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/920a3889-83a9-456b-9865-f116cf44d986" style="width: 60%; display: block; margin: auto;"></a><br>
  3D Pikachu modeling, synthetic data generation with Unity Perception.<br>YOLOv8 fine-tuning exclusively on synthetic data.<br>
</p>


.

.

.

.

.


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
<img src="https://github.com/paulinamoskwa/detect-pikachu/assets/104844027/4d96d068-bd16-4c19-8211-a5ff48781424" style="width: 20%">
</p>












