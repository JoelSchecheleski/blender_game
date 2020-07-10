from bge import logic, events, types

tc = logic.keyboard.inputs
mouseKeys = logic.mouse.inputs

keyTAP = logic.KX_INPUT_JUST_ACTIVATED

"""
Imlementação do comportamento do personagem e sua física 
"""


class Character(types.KX_GameObject):
    def __init__(self, owner):
        self.vida = 100

    def damage(self, dano):
        self.vida -= dano
        print(self.vida)

    def update(self, controller):
        if tc[events.WKEY].values[-1]:
            self.applyMovement([0, 0.1, 0], True)
        elif tc[events.SKEY].values[-1]:
            self.applyMovement([0, -0.1, 0], True)
        elif tc[events.AKEY].values[-1]:
            self.applyRotation([0, 0, 0.05], True)
        elif tc[events.DKEY].values[-1]:
            self.applyRotation([0, 0, -0.05], True)
