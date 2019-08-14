# ToggleNormalMaps
Blender Add-On to Mute and Unmute Normal Maps in Blender's Node Tree to improve Eevee Viewport Performance

Since Eevee re-evaluates the normals each frame, viewport performance goes down once a Normal Map is added to the Shader Node Tree.
This script iterates through the Normal Nodes and mutes them, which restores performace. The muting can be reversed for render time.

Original Bug Report with explanation of the problem and a sample file.
https://developer.blender.org/T64458
