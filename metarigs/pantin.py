# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy


def create(obj):
    # generated by rigify.utils.write_metarig
    bpy.ops.object.mode_set(mode='EDIT')
    arm = obj.data

    for i in range(28):
        arm.rigify_layers.add()

    arm.rigify_layers[0].name = "Head"
    arm.rigify_layers[0].row = 1
    arm.rigify_layers[1].name = " "
    arm.rigify_layers[1].row = 1
    arm.rigify_layers[2].name = "Torso"
    arm.rigify_layers[2].row = 2
    arm.rigify_layers[3].name = " "
    arm.rigify_layers[3].row = 1
    arm.rigify_layers[4].name = "Left Arm"
    arm.rigify_layers[4].row = 3
    arm.rigify_layers[5].name = ""
    arm.rigify_layers[5].row = 1
    arm.rigify_layers[6].name = "Right Leg"
    arm.rigify_layers[6].row = 4
    arm.rigify_layers[7].name = " "
    arm.rigify_layers[7].row = 1
    arm.rigify_layers[8].name = "Torso"
    arm.rigify_layers[8].row = 5
    arm.rigify_layers[9].name = " "
    arm.rigify_layers[9].row = 1
    arm.rigify_layers[10].name = " "
    arm.rigify_layers[10].row = 1
    arm.rigify_layers[11].name = " "
    arm.rigify_layers[11].row = 1
    arm.rigify_layers[12].name = " "
    arm.rigify_layers[12].row = 1
    arm.rigify_layers[13].name = " "
    arm.rigify_layers[13].row = 1
    arm.rigify_layers[14].name = " "
    arm.rigify_layers[14].row = 1
    arm.rigify_layers[15].name = " "
    arm.rigify_layers[15].row = 1
    arm.rigify_layers[16].name = "Face"
    arm.rigify_layers[16].row = 1
    arm.rigify_layers[17].name = " "
    arm.rigify_layers[17].row = 1
    arm.rigify_layers[18].name = " "
    arm.rigify_layers[18].row = 1
    arm.rigify_layers[19].name = " "
    arm.rigify_layers[19].row = 1
    arm.rigify_layers[20].name = "Right Arm"
    arm.rigify_layers[20].row = 3
    arm.rigify_layers[21].name = " "
    arm.rigify_layers[21].row = 1
    arm.rigify_layers[22].name = "Right Leg"
    arm.rigify_layers[22].row = 4
    arm.rigify_layers[23].name = " "
    arm.rigify_layers[23].row = 1
    arm.rigify_layers[24].name = " "
    arm.rigify_layers[24].row = 1
    arm.rigify_layers[25].name = " "
    arm.rigify_layers[25].row = 1
    arm.rigify_layers[26].name = " "
    arm.rigify_layers[26].row = 1
    arm.rigify_layers[27].name = " "
    arm.rigify_layers[27].row = 1

    bones = {}

    bone = arm.edit_bones.new('Pelvis')
    bone.head[:] = -0.0029, 0.0000, 0.8893
    bone.tail[:] = 0.0294, -0.0000, 1.0480
    bone.roll = -2.9408
    bone.use_connect = False
    bones['Pelvis'] = bone.name
    bone = arm.edit_bones.new('Thigh')
    bone.head[:] = -0.0029, 0.0000, 0.8893
    bone.tail[:] = -0.0283, 0.0000, 0.4894
    bone.roll = 0.0634
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Pelvis']]
    bones['Thigh'] = bone.name
    bone = arm.edit_bones.new('Spine')
    bone.head[:] = 0.0294, -0.0000, 1.0480
    bone.tail[:] = -0.0027, 0.0000, 1.1745
    bone.roll = 2.8931
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Pelvis']]
    bones['Spine'] = bone.name
    bone = arm.edit_bones.new('Shin')
    bone.head[:] = -0.0283, 0.0000, 0.4894
    bone.tail[:] = -0.0587, 0.0000, 0.0736
    bone.roll = 0.0730
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Thigh']]
    bones['Shin'] = bone.name
    bone = arm.edit_bones.new('Thorax')
    bone.head[:] = -0.0027, 0.0000, 1.1745
    bone.tail[:] = -0.0135, 0.0000, 1.3005
    bone.roll = 3.0561
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Spine']]
    bones['Thorax'] = bone.name
    bone = arm.edit_bones.new('Foot')
    bone.head[:] = -0.0587, 0.0000, 0.0736
    bone.tail[:] = -0.0030, 0.0000, 0.0227
    bone.roll = -0.8304
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Shin']]
    bones['Foot'] = bone.name
    bone = arm.edit_bones.new('Heel')
    bone.head[:] = -0.0587, 0.0000, 0.0736
    bone.tail[:] = -0.0954, 0.0000, 0.0000
    bone.roll = 0.4626
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Shin']]
    bones['Heel'] = bone.name
    bone = arm.edit_bones.new('Chest')
    bone.head[:] = -0.0135, 0.0000, 1.3005
    bone.tail[:] = 0.0005, 0.0000, 1.4038
    bone.roll = -3.0069
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Thorax']]
    bones['Chest'] = bone.name
    bone = arm.edit_bones.new('Toe')
    bone.head[:] = -0.0030, 0.0000, 0.0227
    bone.tail[:] = 0.0558, 0.0000, 0.0000
    bone.roll = -1.2024
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Foot']]
    bones['Toe'] = bone.name
    bone = arm.edit_bones.new('Neck')
    bone.head[:] = 0.0005, 0.0000, 1.4038
    bone.tail[:] = 0.0271, 0.0000, 1.4720
    bone.roll = -2.7697
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Chest']]
    bones['Neck'] = bone.name
    bone = arm.edit_bones.new('Arm')
    bone.head[:] = -0.0488, 0.0000, 1.3385
    bone.tail[:] = -0.0929, 0.0000, 1.1169
    bone.roll = 0.1964
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Chest']]
    bones['Arm'] = bone.name
    bone = arm.edit_bones.new('Head')
    bone.head[:] = 0.0271, 0.0000, 1.4720
    bone.tail[:] = 0.0592, 0.0000, 1.6173
    bone.roll = -2.9242
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Neck']]
    bones['Head'] = bone.name
    bone = arm.edit_bones.new('Forearm')
    bone.head[:] = -0.0929, 0.0000, 1.1169
    bone.tail[:] = -0.0646, 0.0000, 0.8523
    bone.roll = -0.1065
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Arm']]
    bones['Forearm'] = bone.name
    bone = arm.edit_bones.new('Jaw')
    bone.head[:] = 0.0223, 0.0000, 1.4938
    bone.tail[:] = 0.0964, 0.0000, 1.4450
    bone.roll = -0.9884
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Head']]
    bones['Jaw'] = bone.name
    bone = arm.edit_bones.new('Eyelid')
    bone.head[:] = 0.0713, -0.0000, 1.5667
    bone.tail[:] = 0.1014, 0.0000, 1.5618
    bone.roll = -1.4094
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Head']]
    bones['Eyelid'] = bone.name
    bone = arm.edit_bones.new('Hat')
    bone.head[:] = 0.0432, -0.0000, 1.6260
    bone.tail[:] = 0.0432, -0.0000, 1.7549
    bone.roll = 3.1416
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Head']]
    bones['Hat'] = bone.name
    bone = arm.edit_bones.new('Mouth')
    bone.head[:] = 0.0629, 0.0000, 1.4873
    bone.tail[:] = 0.0629, 0.0000, 1.5074
    bone.roll = 3.1416
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Head']]
    bones['Mouth'] = bone.name
    bone = arm.edit_bones.new('Eyes')
    bone.head[:] = -0.0045, -0.0000, 1.5476
    bone.tail[:] = 0.0964, -0.0000, 1.5476
    bone.roll = -1.5708
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Head']]
    bones['Eyes'] = bone.name
    bone = arm.edit_bones.new('Eyebrow.parent.L')
    bone.head[:] = 0.1103, -0.0000, 1.6279
    bone.tail[:] = 0.0695, -0.0000, 1.5915
    bone.roll = 0.8423
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Head']]
    bones['Eyebrow.parent.L'] = bone.name
    bone = arm.edit_bones.new('Eyebrow.parent.R')
    bone.head[:] = -0.0203, -0.0000, 1.6243
    bone.tail[:] = 0.0178, -0.0000, 1.5915
    bone.roll = -0.8600
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Head']]
    bones['Eyebrow.parent.R'] = bone.name
    bone = arm.edit_bones.new('Hand')
    bone.head[:] = -0.0646, 0.0000, 0.8523
    bone.tail[:] = -0.0646, 0.0000, 0.7518
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Forearm']]
    bones['Hand'] = bone.name
    bone = arm.edit_bones.new('Mouth_upper.R')
    bone.head[:] = 0.0417, 0.0000, 1.4935
    bone.tail[:] = 0.0539, 0.0000, 1.4973
    bone.roll = -1.8728
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Mouth']]
    bones['Mouth_upper.R'] = bone.name
    bone = arm.edit_bones.new('Eyebrow.L')
    bone.head[:] = 0.0695, -0.0000, 1.5915
    bone.tail[:] = 0.0984, 0.0000, 1.6019
    bone.roll = -1.9162
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Eyebrow.parent.L']]
    bones['Eyebrow.L'] = bone.name
    bone = arm.edit_bones.new('Eyebrow.R')
    bone.head[:] = 0.0178, -0.0000, 1.5915
    bone.tail[:] = -0.0110, 0.0000, 1.6019
    bone.roll = 1.9173
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Eyebrow.parent.R']]
    bones['Eyebrow.R'] = bone.name
    bone = arm.edit_bones.new('Prop')
    bone.head[:] = -0.1701, 0.0000, 0.7032
    bone.tail[:] = -0.3672, 0.0000, 0.0000
    bone.roll = 0.2733
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Hand']]
    bones['Prop'] = bone.name
    bone = arm.edit_bones.new('Mouth_upper')
    bone.head[:] = 0.0539, 0.0000, 1.4973
    bone.tail[:] = 0.0718, 0.0000, 1.4973
    bone.roll = -1.5708
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Mouth_upper.R']]
    bones['Mouth_upper'] = bone.name
    bone = arm.edit_bones.new('Eyebrow_center.L')
    bone.head[:] = 0.0984, 0.0000, 1.6019
    bone.tail[:] = 0.1256, 0.0000, 1.6019
    bone.roll = -1.5708
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Eyebrow.L']]
    bones['Eyebrow_center.L'] = bone.name
    bone = arm.edit_bones.new('Eyebrow_center.R')
    bone.head[:] = -0.0110, 0.0000, 1.6019
    bone.tail[:] = -0.0383, 0.0000, 1.6019
    bone.roll = 1.5708
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Eyebrow.R']]
    bones['Eyebrow_center.R'] = bone.name
    bone = arm.edit_bones.new('Mouth_upper.L')
    bone.head[:] = 0.0718, 0.0000, 1.4973
    bone.tail[:] = 0.0841, 0.0000, 1.4935
    bone.roll = -1.2712
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Mouth_upper']]
    bones['Mouth_upper.L'] = bone.name
    bone = arm.edit_bones.new('Eyebrow_side.L')
    bone.head[:] = 0.1256, 0.0000, 1.6019
    bone.tail[:] = 0.1529, 0.0000, 1.5840
    bone.roll = -0.9904
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Eyebrow_center.L']]
    bones['Eyebrow_side.L'] = bone.name
    bone = arm.edit_bones.new('Eyebrow_side.R')
    bone.head[:] = -0.0383, 0.0000, 1.6019
    bone.tail[:] = -0.0656, 0.0000, 1.5840
    bone.roll = 0.9904
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Eyebrow_center.R']]
    bones['Eyebrow_side.R'] = bone.name
    bone = arm.edit_bones.new('Mouth_lower.R')
    bone.head[:] = 0.0417, 0.0000, 1.4935
    bone.tail[:] = 0.0539, 0.0000, 1.4898
    bone.roll = -1.2763
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Mouth_upper.L']]
    bones['Mouth_lower.R'] = bone.name
    bone = arm.edit_bones.new('Mouth_lower')
    bone.head[:] = 0.0539, 0.0000, 1.4898
    bone.tail[:] = 0.0718, 0.0000, 1.4898
    bone.roll = -1.5708
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Mouth_lower.R']]
    bones['Mouth_lower'] = bone.name
    bone = arm.edit_bones.new('Mouth_lower.L')
    bone.head[:] = 0.0718, 0.0000, 1.4898
    bone.tail[:] = 0.0841, 0.0000, 1.4935
    bone.roll = -1.8630
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Mouth_lower']]
    bones['Mouth_lower.L'] = bone.name

    bpy.ops.object.mode_set(mode='OBJECT')
    pbone = obj.pose.bones[bones['Pelvis']]
    pbone.rigify_type = 'pantin.torso'
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (True, True, True)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.Z_index = 1.0
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.flip_switch = False
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.root_name = "Root"
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Thigh']]
    pbone.rigify_type = 'pantin.leg'
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.Z_index = 2.0
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.joint_name = "Knee"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.right_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.pelvis_name = "Pelvis"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.duplicate_lr = True
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Spine']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (True, True, True)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Shin']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Thorax']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Foot']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Heel']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Chest']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Toe']]
    pbone.rigify_type = ''
    pbone.lock_location = (True, True, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Neck']]
    pbone.rigify_type = 'pantin.head'
    pbone.lock_location = (True, True, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (True, True, True)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.Z_index = 0.0
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.flip_switch = False
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.detach = True
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Arm']]
    pbone.rigify_type = 'pantin.arm'
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.right_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.joint_name = "Elbow"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.pelvis_name = "Pelvis"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.duplicate_lr = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.Z_index = 3.0
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Head']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (True, True, True)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Forearm']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Jaw']]
    pbone.rigify_type = 'pantin.simple'
    pbone.lock_location = (True, True, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (True, True, True)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.pelvis_name = "Pelvis"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.chain_type = "Curve"
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Eyelid']]
    pbone.rigify_type = 'pantin.simple'
    pbone.lock_location = (True, True, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.pelvis_name = "Pelvis"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.do_flip = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.use_parent_Z_index = True
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Hat']]
    pbone.rigify_type = 'pantin.simple'
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.pelvis_name = "Pelvis"
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Mouth']]
    pbone.rigify_type = 'pantin.mouth'
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Eyes']]
    pbone.rigify_type = 'pantin.eyes'
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.eye_name = "Eye"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.pelvis_name = "Pelvis"
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Eyebrow.parent.L']]
    pbone.rigify_type = 'pantin.simple'
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.pelvis_name = "Pelvis"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.chain_type = "Curve"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.curve_parent_to_first = True
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Eyebrow.parent.R']]
    pbone.rigify_type = 'pantin.simple'
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.pelvis_name = "Pelvis"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.chain_type = "Curve"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.curve_parent_to_first = True
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Hand']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Mouth_upper.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, True)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Eyebrow.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.pelvis_name = "Pelvis"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.do_flip = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.chain_type = "Curve"
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Eyebrow.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.pelvis_name = "Pelvis"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.do_flip = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.chain_type = "Curve"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.curve_parent_to_first = True
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Prop']]
    pbone.rigify_type = 'pantin.simple'
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.object_side = ".R"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.use_parent_Z_index = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.flip_switch = False
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.pelvis_name = "Pelvis"
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Mouth_upper']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, True)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Eyebrow_center.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Eyebrow_center.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Mouth_upper.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, True)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Eyebrow_side.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Eyebrow_side.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Mouth_lower.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, True)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Mouth_lower']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, True)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Mouth_lower.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, True)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

    bpy.ops.object.mode_set(mode='EDIT')
    for bone in arm.edit_bones:
        bone.select = False
        bone.select_head = False
        bone.select_tail = False
    for b in bones:
        bone = arm.edit_bones[bones[b]]
        bone.select = True
        bone.select_head = True
        bone.select_tail = True
        arm.edit_bones.active = bone

    arm.layers = [(x in [0, 2, 4, 6, 16]) for x in range(32)]

    # Select proper UI template
    template_name = 'pantin_template'
    arm_templates = arm.rigify_templates.items()
    template_index = None
    for i, template in enumerate(arm_templates):
        if template[0] == template_name:
            template_index = i
            break
    if template_index is None:
        template_index = 0 # Default to something...
    else:
        arm.rigify_active_template = template_index

if __name__ == "__main__":
    create(bpy.context.active_object)
