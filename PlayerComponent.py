from bge import *
from mathutils import *

# tc = logic.keyboard.inputs
# mouseKeys = logic.mouse.inputs
#
# keyTAP = logic.KX_INPUT_JUST_ACTIVATED

"""
    Component para uso no blender UPBGE
"""


# PlayerComponent.Component
class Component(types.KX_PythonComponent):
    args = {
        "speed": 0.1,
        "name": "",
        "enemy type": {"Ogre", "Human", "Elf", "Alien"},
        "position": Vector([0, 0, 0])
    }

    def start(self, args):
        self.speed = args["speed"]
        self.name = args["name"]
        self.enemyType = args["enemy type"]

        self.object.worldPosition = args["position"]
        pass

    def update(self):
        print("Name: {}, speed {}, type: {}".format(self.name, self.speed, self.enemyType))
        self.object.applyMovement([0, self.speed, 0], True)

    # if tc[events.WKEY].values[-1]:
    #     self.applyMovement([0, 0.1, 0], True)
    # elif tc[events.SKEY].values[-1]:
    #     self.applyMovement([0, -0.1, 0], True)
    # elif tc[events.AKEY].values[-1]:
    #     self.applyRotation([0, 0, 0.05], True)
    # elif tc[events.DKEY].values[-1]:
    #     self.applyRotation([0, 0, -0.05], True)
