import bpy
import math
import random

d = 4
anz = 100
frameAnz = 21
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 200

a6 = bpy.data.objects['taijia']
l6 = a6.rotation_euler

for actFrame in range(0, frameAnz):
    if actFrame == 0:
        a6.location[0] == l6[0]
        a6.location[1] == l6[1]
        a6.location[2] == l6[2]
        a6.keyframe_insert(data_path='rotation_euler', index=0, frame=actFrame)
        a6.keyframe_insert(data_path='rotation_euler', index=1, frame=actFrame)
        a6.keyframe_insert(data_path='rotation_euler', index=2, frame=actFrame)
        
    elif actFrame % 2 != 0:
        actframe = actFrame * 10
        if actframe == 10:
            l6[0] -= 0.0071212053298950195
            l6[1] -= 0.030328532215207815
            l6[2] -= -0.0000569075345993
            a6.keyframe_insert(data_path='rotation_euler', index=0, frame=actframe)
            a6.keyframe_insert(data_path='rotation_euler', index=1, frame=actframe)
            a6.keyframe_insert(data_path='rotation_euler', index=2, frame=actframe)
    
        else:
            l6[0] -= 0.01319003477692604
            l6[1] -= 0.05616631731390953
            l6[2] -= 0.0000650361180306
            a6.keyframe_insert(data_path='rotation_euler', index=0, frame=actframe)
            a6.keyframe_insert(data_path='rotation_euler', index=1, frame=actframe)
            a6.keyframe_insert(data_path='rotation_euler', index=2, frame=actframe)
    
    else:
        actframe = actFrame * 10
        l6[0] += 0.01319003477692604
        l6[1] += 0.05616631731390953
        l6[2] += 0.0000650361180306
        a6.keyframe_insert(data_path='rotation_euler', index=0, frame=actframe)
        a6.keyframe_insert(data_path='rotation_euler', index=1, frame=actframe)
        a6.keyframe_insert(data_path='rotation_euler', index=2, frame=actframe)
        