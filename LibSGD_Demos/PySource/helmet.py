# File for libsgd Version 0.18.1 march 2025 
#
# Version 0.1, shows a nice helmet

from libsgd import sgd

import start

sgd.init()

Titel = "Helmet!"
Pfad = "../assets/envmaps/sunnysky-cube.png"

sgd.init()

sgd.createWindow(sgd.getDesktopWidth() // 2, sgd.getDesktopHeight() // 2, Titel,
				 sgd.WINDOW_FLAGS_CENTERED)

env = sgd.loadCubeTexture(Pfad, sgd.TEXTURE_FORMAT_ANY, sgd.TEXTURE_FLAGS_DEFAULT)
sgd.setEnvTexture(env)

skybox = sgd.createSkybox(env)
sgd.setSkyboxRoughness (skybox, 0.3)

light = sgd.createDirectionalLight()
sgd.turnEntity (light,-45,0,0) #; Tilt light down 45 degrees 

material = sgd.loadPBRMaterial("../assets/materials/Tiles019_1K-JPG")

mesh = sgd.createBoxMesh(-10,-3,-10,10,-2,10,material)
sgd.transformTexCoords (mesh,3,3,0,0)
ground = sgd.createModel(mesh)

mesh  = sgd.loadMesh("../assets/models/helmet.glb")
model = sgd.createModel(mesh)
sgd.moveEntity (model,0,0,3)

while not sgd.pollEvents():

    if sgd.isKeyDown(263):
        sgd.turnEntity (model,0,3,0)
    elif sgd.isKeyDown(262):
        sgd.turnEntity (model,0,-3,0)

    if sgd.isKeyDown(264):
        sgd.turnEntity (model,3,0,0)
    elif sgd.isKeyDown(265):
        sgd.turnEntity (model,-3,0,0)

    sgd.renderScene()
    sgd.present()

sgd.terminate()
###End###