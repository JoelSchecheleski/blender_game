from bge import logic, events, types
from PlayerController import *

tc = logic.keyboard.inputs
mouseKeys = logic.mouse.inputs

keyTAP = logic.KX_INPUT_JUST_ACTIVATED


def start(controller):
    owner = controller.owner  # Ao iniciar pega o owner
    player = Character(owner)


# A cada (F)ps frame atualiza
def update(controller):
    owner = controller.owner
    owner.update(controller)
    owner.damage(10)
