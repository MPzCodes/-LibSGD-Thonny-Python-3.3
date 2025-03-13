from libsgd import sgd

import start

sgd.init()

sgd.createWindow(sgd.getDesktopWidth() // 2, sgd.getDesktopHeight() // 2, "Caesiumman",
				 sgd.WINDOW_FLAGS_CENTERED)


def LoadScene():
    
    global model
    global camera

    env = sgd.loadCubeTexture("../assets/envmaps/sunnysky-cube.png", sgd.TEXTURE_FORMAT_ANY, sgd.TEXTURE_FLAGS_DEFAULT)
    sgd.setEnvTexture(env)

    skybox = sgd.createSkybox(env)
    sgd.setSkyboxRoughness (skybox,0.3)

    light = sgd.createDirectionalLight()
    sgd.setLightShadowsEnabled (light, True)
    sgd.turnEntity (light,-30,0,0) #; Tilt light down 30 degrees 

    camera = sgd.createPerspectiveCamera()
    sgd.moveEntity (camera,0,1,-5)

    material = sgd.loadPBRMaterial("../assets/materials/PavingStones065_1K-JPG") #; Loaderror... search error
    mesh = sgd.createBoxMesh(-10, -1, -10, 10, 0, 10, material)
    sgd.transformTexCoords (mesh, 4,4,0,0)
    ground = sgd.createModel(mesh)
 
    model = sgd.loadBonedModel("../assets/models/cesiumman.glb", True)
    sgd.setMeshShadowsEnabled (sgd.getModelMesh(model),True)

LoadScene()

#;Cheesy sepia-tone render effect!
monocolor = sgd.createMonocolorEffect()
sgd.setMonocolorEffectColor (monocolor, 1,1,0.75,1)

atime=0.0
while not (sgd.pollEvents() & sgd.EVENT_MASK_CLOSE_CLICKED):
    
    if sgd.isKeyDown(263):
        sgd.turnEntity (model,0,3,0)
    elif sgd.isKeyDown(262):
        sgd.turnEntity (model,0,-3,0)

    if sgd.isKeyDown(264):
        sgd.moveEntity (model,0,0,0.03)
    elif sgd.isKeyDown(265):
       sgd.moveEntity (model,0,0,-0.03)

    atime = atime + 0.03
    sgd.animateModel (model,0,atime,2,1)
    
    sgd.renderScene()
    sgd.present()

sgd.terminate()

