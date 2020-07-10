from bge import logic, events

keys = logic.keyboard.inputs
mouseKeys = logic.mouse.inputs

keyTAP = logic.KX_INPUT_JUST_ACTIVATED


# Ao iniciar pega o owner
def start(controller):
    owner = controller.owner
    owner["vida"] = 100
    owner["inventário"] = []


# A cada (F)ps frame atualiza
def update(controller):
    owner = controller.owner

    owner["inventário"].append(1)

    if keys[events.WKEY].values[-1]:
        owner.applyMovement([0, 0.1, 0], True)
