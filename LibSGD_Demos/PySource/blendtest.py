# File for libsgd Version 0.18.1 march 2025 
#
# Version 0.1, sprite animation as overlay in 3D room

from libsgd import sgd

import random
import start

sgd.init()

sgd.createWindow(sgd.getDesktopWidth() // 2, sgd.getDesktopHeight() // 2, "Blendtest",
				 sgd.WINDOW_FLAGS_CENTERED)


sgd.setAmbientLightColor (1,1,1,0.2)

env =  sgd.loadCubeTexture("../assets/envmaps/stormy-cube.jpg", sgd.TEXTURE_FORMAT_ANY, sgd.TEXTURE_FLAGS_DEFAULT)
sgd.setEnvTexture (env)
sgd.createSkybox (env)

light = sgd.createDirectionalLight()
sgd.setEntityRotation (light,-45,-45,0)

mesh = sgd.loadMesh("../assets/models/blendtest.glb")
sgd.fitMesh (mesh,-0.5,-0.5,-0.5,0.5,0.5,0.5,True)

cells = 5
spc= 2.0
halfsz = cells*spc/2


# Initialize an empty list
entity = []

#Structure Model
#    entity.i
#EndStructure 

#NewList ModelList.Model()

for x in range (0,cells):
    for y in range (0,cells):
        for z in range (0,cells):
            entity.append(sgd.createModel(mesh))
            sgd.moveEntity (entity[-1],x*spc-halfsz, y*spc-halfsz,z*spc-halfsz)

start.createPlayer(0)
sgd.moveEntity (start.player,0,0,-halfsz)

while not (sgd.pollEvents() & sgd.EVENT_MASK_CLOSE_CLICKED):
    
    random.seed (1234)
    
    # Iterating over the list
    for item in entity:
        sgd.turnEntity (item,(random.randint(0, 14)-7)/10,(random.randint(0, 6)-3)/10,0)

    start.playerFly(0.125)

    sgd.renderScene()
    sgd.present()

sgd.terminate()
##### bye #####