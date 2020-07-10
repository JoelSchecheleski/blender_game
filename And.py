# Módulo principal
from bge import logic, events

controller = logic.getCurrentController()

# Instancia um actuator do tipo Motion
# motion = controller.actuators["Motion"]

# Ativa o controller motion
# controller.activate(motion)

# Sensores do Objeto
tc = logic.keyboard.inputs
mouseKey = logic.mouse.inputs
keyTAP = logic.KX_INPUT_JUST_ACTIVATED

# Pega o Objeto proprietário do controlador
owner = controller.owner

# Rotação do objeto conforme uso do teclado WASD
if tc[events.WKEY].values[-1]:
    owner.applyMovement([0, 0.1, 0], True)
elif tc[events.SKEY].values[-1]:
    owner.applyMovement([0, -0.1, 0], True)
elif tc[events.AKEY].values[-1]:
    owner.applyRotation([0, 0, 0.05], True)
elif tc[events.DKEY].values[-1]:
    owner.applyRotation([0, 0, -0.05], True)
