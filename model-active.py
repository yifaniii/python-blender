import bpy
import math
import random
d = 4
anz = 100
frameAnz = 21 # 动画帧到20结束
scene = bpy.context.scene
scene.frame_start = 1 # 从第一帧开始
scene.frame_end = 100 # 第100帧结束

# 不同物体进行大致动画生成，变化坐标进行移动
a = bpy.data.objects['1010']
l = a.location

a1 = bpy.data.objects['1011']
l1 = a1.location

a2 = bpy.data.objects['1012']
l2 = a2.location

a3 = bpy.data.objects['1013']
l3 = a3.location

a4 = bpy.data.objects['1014']
l4 = a4.location

a5 = bpy.data.objects['1015']
l5 = a5.location

for actFrame in range(0, frameAnz):
    if actFrame == 0:
        a.location[0] == l[0]
        a.location[1] == l[1]
        a.location[2] == l[2]
        a.keyframe_insert(data_path='location', index=0, frame=actFrame)
        a.keyframe_insert(data_path='location', index=1, frame=actFrame)
        a.keyframe_insert(data_path='location', index=2, frame=actFrame)
        
        a1.location[0] == l1[0]
        a1.location[1] == l1[1]
        a1.location[2] == l1[2]
        a1.keyframe_insert(data_path='location', index=0, frame=actFrame)
        a1.keyframe_insert(data_path='location', index=1, frame=actFrame)
        a1.keyframe_insert(data_path='location', index=2, frame=actFrame)
        
        a2.location[0] == l2[0]
        a2.location[1] == l2[1]
        a2.location[2] == l2[2]
        a2.keyframe_insert(data_path='location', index=0, frame=actFrame)
        a2.keyframe_insert(data_path='location', index=1, frame=actFrame)
        a2.keyframe_insert(data_path='location', index=2, frame=actFrame)
        
        a3.location[0] == l3[0]
        a3.location[1] == l3[1]
        a3.location[2] == l3[2]
        a3.keyframe_insert(data_path='location', index=0, frame=actFrame)
        a3.keyframe_insert(data_path='location', index=1, frame=actFrame)
        a3.keyframe_insert(data_path='location', index=2, frame=actFrame)
        
        a4.location[0] == l4[0]
        a4.location[1] == l4[1]
        a4.location[2] == l4[2]
        a4.keyframe_insert(data_path='location', index=0, frame=actFrame)
        a4.keyframe_insert(data_path='location', index=1, frame=actFrame)
        a4.keyframe_insert(data_path='location', index=2, frame=actFrame)
        
        a5.location[0] == l5[0]
        a5.location[1] == l5[1]
        a5.location[2] == l5[2]
        a5.keyframe_insert(data_path='location', index=0, frame=actFrame)
        a5.keyframe_insert(data_path='location', index=1, frame=actFrame)
        a5.keyframe_insert(data_path='location', index=2, frame=actFrame)

    elif actFrame % 2 != 0:
        actframe = actFrame * 10
        l[0] -= 0.026955358684062958
        l[1] += 0.01596839353442192
        l[2] += 0.018691837787628174
        a.keyframe_insert(data_path='location', index=0, frame=actframe)
        a.keyframe_insert(data_path='location', index=1, frame=actframe)
        a.keyframe_insert(data_path='location', index=2, frame=actframe)
        
        a1.location[0] -= 0.031150944530963898
        a1.location[1] += 0.015446566045284271
        a1.location[2] -= 0.01989150047302246
        a1.keyframe_insert(data_path='location', index=0, frame=actframe)
        a1.keyframe_insert(data_path='location', index=1, frame=actframe)
        a1.keyframe_insert(data_path='location', index=2, frame=actframe)
        
        l2[0] += 0.00044395774602890015
        l2[1] -= 0.03267942741513252
        l2[2] -= 0.020321309566497803
        a2.keyframe_insert(data_path='location', index=0, frame=actframe)
        a2.keyframe_insert(data_path='location', index=1, frame=actframe)
        a2.keyframe_insert(data_path='location', index=2, frame=actframe)
        
        l3[0] -= 0.0017795190215110779
        l3[1] -= 0.037521377205848694
        l3[2] += 0.027913987636566162
        a3.keyframe_insert(data_path='location', index=0, frame=actframe)
        a3.keyframe_insert(data_path='location', index=1, frame=actframe)
        a3.keyframe_insert(data_path='location', index=2, frame=actframe)
        
        l4[0] += 0.025655612349510193
        l4[1] += 0.023852061480283737
        l4[2] -= 0.020132601261138916
        a4.keyframe_insert(data_path='location', index=0, frame=actframe)
        a4.keyframe_insert(data_path='location', index=1, frame=actframe)
        a4.keyframe_insert(data_path='location', index=2, frame=actframe)
        
        l5[0] += 0.02605719119310379
        l5[1] += 0.014940187335014343
        l5[2] += 0.017255127429962158
        a5.keyframe_insert(data_path='location', index=0, frame=actframe)
        a5.keyframe_insert(data_path='location', index=1, frame=actframe)
        a5.keyframe_insert(data_path='location', index=2, frame=actframe)
    else:
        actframe = actFrame * 10
        l[0] += 0.026955358684062958
        l[1] -= 0.01596839353442192
        l[2] -= 0.018691837787628174
        a.keyframe_insert(data_path='location', index=0, frame=actframe)
        a.keyframe_insert(data_path='location', index=1, frame=actframe)
        a.keyframe_insert(data_path='location', index=2, frame=actframe)
        
        a1.location[0] += 0.031150944530963898
        a1.location[1] -= 0.015446566045284271
        a1.location[2] += 0.01989150047302246
        a1.keyframe_insert(data_path='location', index=0, frame=actframe)
        a1.keyframe_insert(data_path='location', index=1, frame=actframe)
        a1.keyframe_insert(data_path='location', index=2, frame=actframe)
        
        l2[0] -= 0.00044395774602890015
        l2[1] += 0.03267942741513252
        l2[2] += 0.020321309566497803
        a2.keyframe_insert(data_path='location', index=0, frame=actframe)
        a2.keyframe_insert(data_path='location', index=1, frame=actframe)
        a2.keyframe_insert(data_path='location', index=2, frame=actframe)
        
        l3[0] += 0.0017795190215110779
        l3[1] += 0.037521377205848694
        l3[2] -= 0.027913987636566162
        a3.keyframe_insert(data_path='location', index=0, frame=actframe)
        a3.keyframe_insert(data_path='location', index=1, frame=actframe)
        a3.keyframe_insert(data_path='location', index=2, frame=actframe)
        
        l4[0] -= 0.025655612349510193
        l4[1] -= 0.023852061480283737
        l4[2] += 0.020132601261138916
        a4.keyframe_insert(data_path='location', index=0, frame=actframe)
        a4.keyframe_insert(data_path='location', index=1, frame=actframe)
        a4.keyframe_insert(data_path='location', index=2, frame=actframe)
        
        l5[0] -= 0.02605719119310379
        l5[1] -= 0.014940187335014343
        l5[2] -= 0.017255127429962158
        a5.keyframe_insert(data_path='location', index=0, frame=actframe)
        a5.keyframe_insert(data_path='location', index=1, frame=actframe)
        a5.keyframe_insert(data_path='location', index=2, frame=actframe)
