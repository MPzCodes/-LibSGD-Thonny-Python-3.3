# File for libsgd Version 0.18.1 march 2025 
#
# Version 0.1, 3d Spritegrass Demo

from libsgd import sgd

import random
import start

sgd.init()

sgd.createWindow(sgd.getDesktopWidth() // 2, sgd.getDesktopHeight() // 2, "Sprite Grass",
				 sgd.WINDOW_FLAGS_CENTERED)

env = sgd.loadCubeTexture("../assets/envmaps/sunnysky-cube.png",sgd.TEXTURE_FORMAT_ANY,sgd.TEXTURE_FLAGS_DEFAULT)
sgd.setEnvTexture (env)
skybox = sgd.createSkybox(env)

light = sgd.createDirectionalLight()
sgd.turnEntity (light,-45,0,0)	#; Tilt light down 45 degrees 

far=300.0

start.createPlayer(0)
sgd.setCameraFar (start.camera, far)
sgd.moveEntity (start.player,0,1.5,0)

grassImage = sgd.loadImage("../assets/misc/grass1.png")
sgd.setImageRect (grassImage,-0.5,0,0.5,0.5)

n=50000

for i in range (0, n+1):
    sprite = sgd.createSprite(grassImage)

    sgd.turnEntity(sprite,0,random.randint(0,360),0)
    sgd.moveEntity(sprite,0,0,random.randint(0,far))

    sc=random.uniform(0,1)
    sgd.scaleEntity (sprite,sc,sc,sc)

viewMode = 1 
sgd.setImageViewMode (grassImage,viewMode)

while not sgd.pollEvents():
  
    start.playerFly(0.1)

    sgd.clear2D()
    if sgd.isKeyHit(sgd.KEY_SPACE):
        viewMode = viewMode + 1
        if viewMode == 4 :
            viewMode=1 
        sgd.setImageViewMode (grassImage,viewMode)

    sgd.draw2DText ("Sprite View mode:"+str(viewMode)+" (space to toggle)",0,0)

    sgd.renderScene()
    sgd.present()

sgd.terminate()
##### bye #####