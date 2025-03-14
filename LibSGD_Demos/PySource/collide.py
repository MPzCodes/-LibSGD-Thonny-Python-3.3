# File for libsgd Version 0.18.1 march 2025 
#
# Version 0.1, 3d collision test

from libsgd import sgd

import start

sgd.init()

COLLIDER_TYPE_LEVEL=0
COLLIDER_TYPE_SPHERE=1
COLLIDER_TYPE_PLAYER=2

sgd.createWindow(sgd.getDesktopWidth() // 2, sgd.getDesktopHeight() // 2, "Collide Demo",
				 sgd.WINDOW_FLAGS_CENTERED)

sgd.enableCollisions (COLLIDER_TYPE_PLAYER,COLLIDER_TYPE_LEVEL,sgd.COLLISION_RESPONSE_SLIDEXZ)
sgd.enableCollisions (COLLIDER_TYPE_PLAYER,COLLIDER_TYPE_SPHERE,sgd.COLLISION_RESPONSE_SLIDE)

sgd.setAmbientLightColor (1,0.9,0.8,0.2)

env =  sgd.loadCubeTexture("../assets/envmaps/sunnysky-cube.png",sgd.TEXTURE_FORMAT_ANY,sgd.TEXTURE_FLAGS_DEFAULT)
sgd.setEnvTexture (env)

skybox = sgd.createSkybox(env)

light = sgd.createDirectionalLight()
sgd.turnEntity (light,-45,-45,0)

levelMesh = sgd.loadMesh("../assets/models/ManurewaDuplex.glb")

sz=50.0
sgd.fitMesh (levelMesh,-sz,-sz,-sz,sz,sz,sz,True)

levelModel = sgd.createModel(levelMesh)
levelCollider = sgd.createMeshCollider(levelModel, COLLIDER_TYPE_LEVEL, 0)

sphereMesh = sgd.createSphereMesh(2.5,48,23,sgd.createPBRMaterial());
sgd.setMaterialColor(sgd.getMaterial(sgd.getSurface(sphereMesh,0)),"albedo",1,0.75,0,1)

sphereModel = sgd.createModel(sphereMesh)
sgd.moveEntity (sphereModel,0,-6,36)
sphereCollider = sgd.createMeshCollider(sphereModel, COLLIDER_TYPE_SPHERE, 0)

start.createPlayer(0)
sgd.setEntityPosition (start.player,-8,0,36)
sgd.setEntityRotation (start.player,0,-145.5,0)
sgd.moveEntity(start.camera,0,0.8,0)

#;Skinny dude!
playerCollider = sgd.createEllipsoidCollider(start.player, COLLIDER_TYPE_PLAYER, 0.2, 1.8)

gravity=-9.81/60.0/60.0
vel=0.0
jumping=False

while sgd.pollEvents() != 1:

    sp=3.2
    if sgd.isKeyDown(sgd.KEY_LEFT_SHIFT) :
        sp=5.6 

    if sgd.isKeyHit(sgd.KEY_F11):
        if not sgd.getWindowState()==4:
            sgd.setWindowState (4)
        else:
            sgd_SetWindowState (2)

    start.playerFly(sp/60.0)
    #start.playerWalk(sp/60.0)

    py = sgd.getEntityY(start.player)

    if sgd.isKeyHit(sgd.KEY_SPACE):
        vel = vel + 0.1
        jumping=True

    vel = vel + gravity
    sgd.moveEntity(start.player, 0, vel, 0)

    sgd.updateColliders()

    vel = sgd.getEntityY(start.player) - py

    if jumping:
        if vel<=0 :
            jumping = False
    else:
        if vel>0 :
            vel=0 

    sgd.clear2D()
    sgd.set2DTextColor (0,0,0,1)

    sgd.draw2DText ("Player position: "+str(sgd.getEntityX(start.player))+", "+str(sgd.getEntityY(start.player))+", "+str(sgd.getEntityZ(start.player)),0,0)
    sgd.draw2DText ("Player rotation: "+str(sgd.getEntityRX(start.player))+", "+str(sgd.getEntityRY(start.player))+", "+str(sgd.getEntityRZ(start.player)),0,16)

    for i in range (0, sgd.getCollisionCount(playerCollider)):
        sgd.draw2DText ("Collision "+str(i)+" Type:"+str(sgd.getColliderType(sgd.getCollisionCollider(playerCollider,i))),0,i*48+32)
        sgd.draw2DText ("Collision "+str(i)+" Point : "+str(sgd.getCollisionX(playerCollider,i))+", "+str(sgd.getCollisionY(playerCollider,i))+", "+str(sgd.getCollisionZ(playerCollider,i)),0,i*48+48)
        sgd.draw2DText ("Collision "+str(i)+" Normal: "+str(sgd.getCollisionNX(playerCollider,i))+", "+str(sgd.getCollisionNY(playerCollider,i))+", "+str(sgd.getCollisionNZ(playerCollider,i)),0,i*48+64)

    sgd.renderScene()
    sgd.present()

sgd.terminate()
##### bye #####