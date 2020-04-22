import bpy

#import many files



list(bpy.data.objects)

#name objects
TOR = bpy.data.objects[2]

#get object location
Cube.delta_location

#move the object
TOR.location = (4,0,0)

#move object
import mathutils
Cube.delta_location += mathutils.Vector((1, 1, 1))

# Rotate object in X Y or Z.Note that you need to use radians rather than angles here
bpy.data.objects[0].rotation_euler = (1.57,0,0) # 


#get the files in the order that you want first, then 
objs = list(bpy.data.objects)

#space them by 1 unit apart on the x axis
for i in range(11):
	objs[i].location = (i,0,0)

# Iterate over all the selected objects
for o in bpy.context.selected_objects:
    # Set the active materials diffuse color to the specified RGB
    o.active_material.diffuse_color = (r,g,b)

for i in objs:
	i.active_material.diffuse_color = (0.1,0.5,0.7)


#new material
bpy.data.materials.new("MyMaterial")

#transform selected object. select the object then run the operator
bpy.ops.transform.translate(value = (0.5, 0, 10))
