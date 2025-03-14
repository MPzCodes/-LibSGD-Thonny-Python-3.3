# File for libsgd Version 0.18.1 march 2025 
#
# Version 0.1, program load a scene

# -Please start the serialize.pb file before you  start thi sprogram. You need the "~/Desktop/test-scene.json" file

from libsgd import sgd

import start

sgd.init()

sgd.createWindow(sgd.getDesktopWidth() // 2, sgd.getDesktopHeight() // 2, "Load Serialize!",
				 sgd.WINDOW_FLAGS_CENTERED)

# Load scene from desktop!
sgd.loadScene("~/Desktop/test-scene.json")
#- end of here

start.createPlayer(0)
sgd.moveEntity(start.player, 0.0, 10.0, 0)

start.player = sgd.findEntityChild(0,"Player")
start.camera = sgd.findEntityChild(0,"Camera")

while not (sgd.pollEvents() & sgd.EVENT_MASK_CLOSE_CLICKED):
    start.playerFly(.25)

    sgd.renderScene()
    sgd.clear2D()
    sgd.draw2DText ("FPS:"+str(round(sgd.getFPS(),2)),0,0)
    sgd.present()

sgd.terminate()
##### bye #####