# diva-camtool
Simple tool for converting an MMD VMD CSV to a Project Diva Auth 3D Camera

# Usage (Preparing the VMD):

To begin, open blender, then delete everything in the current scene and add a single camera object
Next load your MMD camera VMD onto the camera you just added with a margin of 0 and scale of 1
Then add an armature with the bones "view_point", "interest" and "fov", make sure these are all located at 0,0,0
For view_point, add a copy location and copy rotation constraint and set both to target the camera object (NOT MMD_Camera)
For interest, add a copy location constraint and set it to target the MMD_Camera object
For FOV, set a dummy keyframe in Euler mode just to set up the dope sheet view, then open the dope sheet view, right click one of the angle() key frames, then with the mouse still
on it use L to select Linked
Use Ctrl + C to copy the angle() key frames, then select the fov bone's Euler X rotation line and paste with Ctrl + V
go back to the 3d view and select the view_point and interest bones, then use bake action with only selected, clear constraints, visual keying and overwrite current action
wait for that to finish, then delete the MMD_Camera and Camera objects
then export a VMD from the armature you just created
finally use VMDConverterGraphical to convert the VMD to a CSV for use with the tool

# Usage (Converting the VMD):

simply run the command: python diva-camtool.py infile outfile
where infile is the VMD name, and outfile is the JSON name (for use with KorenKonder's PD_Tool.exe)

# Usage (Converting to A3DA from JSON):

Run PD_Tool.exe and use 6, 1, select your A3DA file, and choose 1 for A3DA AFT/DT/F
