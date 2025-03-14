# File for libsgd Version 0.18.1 march 2025 
#
# Version 0.1, shows some primitives and collision

from libsgd import sgd

import start

sgd.init()

sgd.createWindow(sgd.getDesktopWidth() // 2, sgd.getDesktopHeight() // 2, "Primitives",
				 sgd.WINDOW_FLAGS_CENTERED)

env = sgd.loadCubeTexture("../assets/envmaps/sunnysky-cube.png",sgd.TEXTURE_FORMAT_ANY,sgd.TEXTURE_FLAGS_DEFAULT)
sgd.setEnvTexture (env)

skybox = sgd.createSkybox(env)
sgd.setSkyboxRoughness (skybox, 0.3)

sgd.setConfigVar ("psm.textureSize", str(4096))
sgd.setConfigVar ("psm.maxLights", str(6))
sgd.updateShadowMappingConfig()

light0 = sgd.createPointLight()
sgd.setEntityPosition (light0,0,5,-2.5)
sgd.setLightRange (light0, 10)
sgd.setLightShadowsEnabled (light0,True)

groundMaterial = sgd.createPBRMaterial()
sgd.setMaterialColor (groundMaterial,"albedo",1,0.75,0,1)
#SGD.setMaterialColor (groundMaterial,"albedo",1,0.75,0,1)

groundMesh = sgd.createBoxMesh(-5,-0.1,-5,5,0,5,groundMaterial)
sgd.setMeshShadowsEnabled (groundMesh, True)

groundModel = sgd.createModel(groundMesh)

material = sgd.loadPBRMaterial("../assets/materials/Fabric050_1K-JPG")

r = 0.5
y = 1.5

start.createPlayer(0)
sgd.moveEntity (start.player,0,y,-5)

mesh0 = sgd.createSphereMesh(r, 96, 48, material)
sgd.setMeshShadowsEnabled (mesh0, True)
model0 = sgd.createModel(mesh0)
sgd.moveEntity (model0, -2.5, y, 0)

r2=r*0.7071
mesh1 = sgd.createBoxMesh(-r2, -r2, -r2, r2, r2, r2, material)
sgd.setMeshShadowsEnabled (mesh1, True)
model1 = sgd.createModel(mesh1)
sgd.moveEntity (model1, -1.25, y, 0)

mesh2 = sgd.createCylinderMesh(r * 2, r / 2, 96, material)
sgd.setMeshShadowsEnabled (mesh2, True)
model2 = sgd.createModel(mesh2)
sgd.moveEntity (model2, 0, y, 0)

mesh3 = sgd.createConeMesh(r * 2, r / 2, 96, material)
sgd.setMeshShadowsEnabled (mesh3, True)
model3 = sgd.createModel(mesh3)
sgd.moveEntity (model3, 1.25, y, 0)

mesh4 = sgd.createTorusMesh(r * 0.75, r * 0.25, 96, 48, material)
sgd.setMeshShadowsEnabled (mesh4, True)
model4 = sgd.createModel(mesh4)
sgd.moveEntity (model4, 2.5, y, 0)

collider0=sgd.createMeshCollider(model0,0,0)
collider1=sgd.createMeshCollider(model1,0,0)
collider2=sgd.createMeshCollider(model2,0,0)
collider3=sgd.createMeshCollider(model3,0,0)
collider4=sgd.createMeshCollider(model4,0,0)

sgd.set2DTextColor (0,0,0,1)

cursorMesh = sgd.createSphereMesh(0.01, 32,16,sgd.createPBRMaterial())
cursor= sgd.createModel(cursorMesh)
sgd.setModelColor (cursor, 0, 1, 0, 1)

while (sgd.pollEvents() & 1) == 0:

    sgd.turnEntity (model0, 0.3, 0.4, 0.5)
    sgd.turnEntity (model1, 0.3, 0.4, 0.5)
    sgd.turnEntity (model2, 0.3, 0.4, 0.5)
    sgd.turnEntity (model3, 0.3, 0.4, 0.5)
    sgd.turnEntity (model4, 0.3, 0.4, 0.5) 

    if sgd.isKeyHit(49) :
        sgd.setEntityVisible (model0, ~sgd.isEntityVisible(model0)+2)
    if sgd.isKeyHit(50) :
        sgd.setEntityVisible (model1, ~sgd.isEntityVisible(model1)+2)
    if sgd.isKeyHit(51) :
        sgd.setEntityVisible (model2, ~sgd.isEntityVisible(model2)+2)
    if sgd.isKeyHit(52) :
        sgd.setEntityVisible (model3, ~sgd.isEntityVisible(model3)+2) 
    if sgd.isKeyHit(53) :
        sgd.setEntityVisible (model4, ~sgd.isEntityVisible(model4)+2) 

    start.playerFly(0.05)

    collider = sgd.cameraPick(start.camera,sgd.getMouseX(),sgd.getMouseY(),1)
    
    sgd.clear2D()
    sgd.draw2DText ("Picked collider: " + str(collider),0,0)
    
    sgd.cameraUnproject (start.camera, sgd.getMouseX(), sgd.getMouseY(), 1)
    sgd.setEntityPosition (cursor, sgd.getUnprojectedX(), sgd.getUnprojectedY(), sgd.getUnprojectedZ())
    
    sgd.renderScene()
    sgd.present()

sgd.terminate()
###End###
