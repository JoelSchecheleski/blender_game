from bge import logic, events

tc = logic.keyboard.inputs
mouseKeys = logic.mouse.inputs

keyTAP = logic.KX_INPUT_JUST_ACTIVATED


def start(controller):
    owner = controller.owner  # Ao iniciar pega o owner
    owner["vida"] = 100
    owner["inventário"] = []


# A cada (F)ps frame atualiza
def update(controller):
    owner = controller.owner

    owner["inventário"].append(1)

    if tc[events.WKEY].values[-1]:
        owner.applyMovement([0, 0.1, 0], True)
    elif tc[events.SKEY].values[-1]:
        owner.applyMovement([0, -0.1, 0], True)
    elif tc[events.AKEY].values[-1]:
        owner.applyRotation([0, 0, 0.05], True)
    elif tc[events.DKEY].values[-1]:
        owner.applyRotation([0, 0, -0.05], True)
