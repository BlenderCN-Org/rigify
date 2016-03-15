import bpy
from mathutils import Vector
import importlib

from ...utils import copy_bone, new_bone, put_bone
from ...utils import make_mechanism_name, make_deformer_name, strip_org
from ...utils import create_bone_widget, create_widget, create_cube_widget
from ...utils import connected_children_names, has_connected_children
from ...utils import align_bone_x_axis

from . import pantin_utils

importlib.reload(pantin_utils)

class IKLimb:
    def __init__(self, obj, org_bones, stretch_joint_name, layers, side_suffix='', follow_org=False):
        self.obj = obj

        # Get the chain of 3 connected bones
        self.org_bones = org_bones #[bone1, bone2, bone3]

        # Get (optional) parent
        if self.obj.data.bones[org_bones[0]].parent is None:
            self.org_parent = None
        else:
            self.org_parent = self.obj.data.bones[org_bones[0]].parent.name

        self.stretch_joint_name = stretch_joint_name
        self.side_suffix = side_suffix

        self.layers = layers

    def generate(self):
        bpy.ops.object.mode_set(mode='EDIT')

        eb = self.obj.data.edit_bones

        # Create the control bones
        ulimb_ik = copy_bone(self.obj, self.org_bones[0], strip_org(self.org_bones[0]) + ".ik" + self.side_suffix)
        flimb_ik = copy_bone(self.obj, self.org_bones[1], make_mechanism_name(strip_org(self.org_bones[1]) + ".ik" + self.side_suffix))
        elimb_ik = copy_bone(self.obj, self.org_bones[2], strip_org(self.org_bones[2]) + ".ik" + self.side_suffix)

        # elimb_mch = copy_bone(self.obj, self.org_bones[2], make_mechanism_name(strip_org(self.org_bones[2])))

        ulimb_str = copy_bone(self.obj, self.org_bones[0], make_mechanism_name(strip_org(self.org_bones[0]) + ".stretch.ik" + self.side_suffix))
        flimb_str = copy_bone(self.obj, self.org_bones[1], make_mechanism_name(strip_org(self.org_bones[1]) + ".stretch.ik" + self.side_suffix))
        elimb_str = copy_bone(self.obj, self.org_bones[2], make_mechanism_name(strip_org(self.org_bones[2]) + ".stretch.ik" + self.side_suffix))

        joint_str = new_bone(self.obj, self.stretch_joint_name + self.side_suffix)
        eb[joint_str].head = eb[flimb_str].head
        eb[joint_str].tail = eb[flimb_str].head + Vector((0,0,1)) * eb[flimb_str].length/2
        align_bone_x_axis(self.obj, joint_str, Vector((-1, 0, 0)))
        #put_bone(self.obj, joint_str, Vector(eb[flimb_str].head))
        print('POS', eb[joint_str].head)

        # Get edit bones
        ulimb_ik_e = eb[ulimb_ik]
        flimb_ik_e = eb[flimb_ik]
        elimb_ik_e = eb[elimb_ik]

        ulimb_str_e = eb[ulimb_str]
        flimb_str_e = eb[flimb_str]
        elimb_str_e = eb[elimb_str]

        joint_str_e = eb[joint_str]

        # Parenting
        ulimb_ik_e.use_connect = False
        ulimb_ik_e.parent = eb[self.org_parent]

        flimb_ik_e.use_connect = False
        flimb_ik_e.parent = ulimb_ik_e

        elimb_ik_e.use_connect = False
        elimb_ik_e.parent = None

        ulimb_str_e.use_connect = False
        ulimb_str_e.parent = eb[self.org_parent]

        flimb_str_e.use_connect = False
        flimb_str_e.parent = joint_str_e

        elimb_str_e.use_connect = True
        elimb_str_e.parent = flimb_ik_e

        joint_str_e.use_connect = False
        joint_str_e.parent = ulimb_ik_e

        # Object mode, get pose bones
        bpy.ops.object.mode_set(mode='OBJECT')
        pb = self.obj.pose.bones

        ulimb_ik_p = pb[ulimb_ik]
        flimb_ik_p = pb[flimb_ik]
        elimb_ik_p = pb[elimb_ik]

        ulimb_str_p = pb[ulimb_str]
        flimb_str_p = pb[flimb_str]
        elimb_str_p = pb[elimb_str]

        joint_str_p = pb[joint_str]

        # Constraints

        con = flimb_ik_p.constraints.new('IK')
        con.name = "ik"
        con.target = self.obj
        con.subtarget = elimb_ik
        con.chain_count = 2

        con = ulimb_str_p.constraints.new('COPY_LOCATION')
        con.name = "anchor"
        con.target = self.obj
        con.subtarget = ulimb_ik
        con.target_space = 'LOCAL'
        con.owner_space = 'LOCAL'

        con = elimb_str_p.constraints.new('COPY_ROTATION')
        con.name = "copy rotation"
        con.target = self.obj
        con.subtarget = elimb_ik
        con.target_space = 'POSE'
        con.owner_space = 'POSE'

        con = ulimb_str_p.constraints.new('STRETCH_TO')
        con.name = "stretch to"
        con.target = self.obj
        con.subtarget = joint_str
        con.volume = 'NO_VOLUME'
        con.rest_length = ulimb_str_p.length

        con = flimb_str_p.constraints.new('STRETCH_TO')
        con.name = "stretch to"
        con.target = self.obj
        con.subtarget = elimb_str
        con.volume = 'NO_VOLUME'
        con.rest_length = flimb_str_p.length

        # Set layers if specified
        if self.layers:
            ulimb_ik_p.bone.layers = self.layers
            joint_str_p.bone.layers = self.layers
            elimb_ik_p.bone.layers = self.layers
        return [ulimb_ik, ulimb_str, flimb_str, joint_str, elimb_ik, elimb_str]