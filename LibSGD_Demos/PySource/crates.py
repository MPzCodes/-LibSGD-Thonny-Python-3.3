# File for libsgd Version 0.18.1 march 2025 
#
# Version 0.1, show some blocks in a 3d Space, with moving

from libsgd import sgd

import start
import math

sgd.init()

sgd.createWindow(sgd.getDesktopWidth() // 2, sgd.getDesktopHeight() // 2, "Crates",
				 sgd.WINDOW_FLAGS_CENTERED)

env = sgd.loadCubeTexture("../assets/envmaps/sunnysky-cube.png", sgd.TEXTURE_FORMAT_ANY, sgd.TEXTURE_FLAGS_DEFAULT)
sgd.setEnvTexture(env)

skybox = sgd.createSkybox(env)

#sgd.setSkyboxRoughness (skybox, 0.3)

start.createPlayer(0)
sgd.moveEntity(start.player, 0.0, 15.0, -25)

light = sgd.createDirectionalLight()
sgd.setLightShadowsEnabled (light,True)
sgd.turnEntity(light, -90, 0, 0)

sz=32.0

groundMaterial = sgd.loadPBRMaterial("../assets/misc/brownish-grass.jpg")
groundMesh = sgd.createBoxMesh(-sz, -1, -sz, sz, 0, sz, groundMaterial)
sgd.transformTexCoords (groundMesh, sz, sz, 0,0)
groundModel = sgd.createModel(groundMesh)

crateMesh = sgd.loadMesh("../assets/models/sci-fi_crate.glb")
sgd.setMeshShadowsEnabled (crateMesh,True)
sgd.fitMesh (crateMesh,-0.4,-0.4,-0.4,0.4,0.4,0.4,True)

for x in range(-20,21):
    for z in range(-20,21):
        crateModel = sgd.createModel(crateMesh)
        sgd.moveEntity (crateModel,x*1.25,30-math.sqrt(x*x+z*z),z*1.25)

while not (sgd.pollEvents() & sgd.EVENT_MASK_CLOSE_CLICKED):
    start.playerFly(.1)
    sgd.renderScene()
    sgd.present()

sgd.terminate()
###Bye###
