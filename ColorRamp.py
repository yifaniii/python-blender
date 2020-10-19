import bpy
import random

# obj.color_ramp.elements[0].position = 0.5
# obj.color_ramp.elements[0].keyframe_insert(data_path='position', frame=20, index=-1)

def b_color(key):
    obj = bpy.data.materials["Material"].node_tree.nodes["颜色渐变"]  # 用代码定位blender中颜色渐变节点
    
    for actFrame in range(key):
        if actFrame == 0:
            # 改变颜色渐变节点中指针的位置（0~1），blender中可改变该指针的颜色
            obj.color_ramp.elements[0].position = 0.1
            # 把指针设置好的位置以及颜色添加到关键帧里，形成动画
            obj.color_ramp.elements[0].keyframe_insert(data_path='position', frame=actFrame, index=-1)

        elif actFrame % 2 == 0:
            act = actFrame * 10
            obj.color_ramp.elements[0].position = random.uniform(0,0.6)    
            obj.color_ramp.elements[0].keyframe_insert(data_path='position', frame=act, index=-1)
            
            a = obj.color_ramp.elements[0].position
            if a < 0.15:
                a += 0.1 
                obj.color_ramp.elements[1].position = random.uniform(a,0.5)
                obj.color_ramp.elements[1].keyframe_insert(data_path='position', frame=act, index=-1)
                
            elif a > 0.3 and a < 0.5:
                obj.color_ramp.elements[1].position = random.uniform(a,0.8)
                obj.color_ramp.elements[1].keyframe_insert(data_path='position', frame=act, index=-1)
                
            elif a > 0.5:
                a += 0.15
                obj.color_ramp.elements[1].position = random.uniform(a,0.8)
                obj.color_ramp.elements[1].keyframe_insert(data_path='position', frame=act, index=-1)

b_color(21)