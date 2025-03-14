# File for libsgd Version 0.18.1 march 2025 
#
# Version 0.1, Canyon! fly baby fly

from libsgd import sgd
import start

sgd.init()

sgd.createWindow(sgd.getDesktopWidth() // 2, sgd.getDesktopHeight() // 2, "Canyon!",
				 sgd.WINDOW_FLAGS_CENTERED)

sgd.setEnvTexture (sgd.loadCubeTexture("../assets/envmaps/sunnysky-cube.png",sgd.TEXTURE_FORMAT_ANY,sgd.TEXTURE_FLAGS_DEFAULT))

sgd.setAmbientLightColor (1,0.9,0.8,0.1)

light = sgd.createDirectionalLight()
sgd.setEntityRotation (light,-45,-45,0)

fog = sgd.createFogEffect()
sgd.setClearColor (0.5,0.8,1,1)
sgd.setFogEffectColor (fog,0.5,0.8,1,1)
sgd.setFogEffectRange (fog,0.2,2000)
sgd.setFogEffectPower (fog,2.5)

heightTexture = sgd.load2DTexture("../assets/terrains/canyon/height.exr", sgd.TEXTURE_FORMAT_ANY, sgd.TEXTURE_FLAGS_DEFAULT)
normalTexture = sgd.load2DTexture("../assets/terrains/canyon/normal.png", sgd.TEXTURE_FORMAT_RGBA8, sgd.TEXTURE_FLAGS_DEFAULT)
albedoTexture = sgd.load2DTexture("../assets/terrains/canyon/albedo.png", sgd.TEXTURE_FORMAT_ANY, sgd.TEXTURE_FLAGS_DEFAULT)

# heightTexture = sgd.load2DTexture("~/Desktop/rocky/height.exr", sgd.TEXTURE_FORMAT_ANY, sgd.TEXTURE_FLAGS_IMAGE)
# normalTexture = sgd.load2DTexture("~/Desktop/rocky/normal.png", sgd.TEXTURE_FORMAT_RGBA8, sgd.TEXTURE_FLAGS_IMAGE)
# albedoTexture = sgd.load2DTexture("~/Desktop/rocky/albedo.png", sgd.TEXTURE_FORMAT_ANY, sgd.TEXTURE_FLAGS_IMAGE)

material=sgd.createPBRMaterial()
sgd.setMaterialTexture (material,"albedo",albedoTexture)

terrain = sgd.createTerrain()
sgd.setEntityScale (terrain,1,512,1)
sgd.setTerrainSize (terrain,4096)
sgd.setTerrainLODs (terrain,5)
sgd.setTerrainMaterialSize (terrain,4096)
sgd.setTerrainHeightTexture (terrain,heightTexture)
sgd.setTerrainNormalTexture (terrain,normalTexture)
sgd.setTerrainMaterial (terrain,material)

start.createPlayer(0)
sgd.moveEntity (start.player,0,512,-1024)

sgd.setCameraNear (start.camera,0.2)
sgd.setCameraFar (start.camera,2000)

sgd.createTerrainCollider (terrain,0) #; new terrain collision
sgd.createSphereCollider (start.player,1,1)

sgd.enableCollisions (1,0,sgd.COLLISION_RESPONSE_SLIDE)

De_bug=0

while (sgd.pollEvents() and 1) != 1:

    start.playerFly2(.75,1.25,.25)
#    start.playerFly2(0.25,0.5,0.125)
#    start.playerFly(2)

    sgd.updateColliders()


    if sgd.isKeyHit(sgd.KEY_SPACE):
        De_bug=1-De_bug
        sgd.setTerrainDebugMode (terrain,De_bug)

    sgd.clear2D()
    sgd.draw2DText ("Camera: "+str(sgd.getEntityX(start.camera))+","+str(sgd.getEntityY(start.camera))+","+str(sgd.getEntityZ(start.camera)),0,0)
    sgd.draw2DText ("Debug (space to toggle): "+str(De_bug),0,16)
    sgd.draw2DText ("FPS:"+str(sgd.getFPS()),0,32)

    sgd.renderScene()

    sgd.present()
    
sgd.terminate()
##### bye #####