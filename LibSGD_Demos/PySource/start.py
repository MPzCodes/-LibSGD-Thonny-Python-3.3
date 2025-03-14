# File for libsgd Version 0.18.1 march 2025 
#
# Version 0.1, is only a loaded program part to use a player/camera in other programs

from libsgd import sgd

player = None
player_rvx = 0.0
player_rvy = 0.0
player_vx = 0.0
player_vy = 0.0
player_vz = 0.0

camera = None
camera_rx = 0.0
camera_ry = 0.0

def createPlayer(mesh):

    global player
    global camera
    
    player = sgd.createModel(mesh)
    camera = sgd.createPerspectiveCamera()
    sgd.setEntityParent(camera, player)
    

def playerFly(speed):
    
    global player
    global player_rvx
    global player_rvy
    global player_vx
    global player_vy
    global player_vz
    global camera

    if sgd.isKeyDown(sgd.KEY_LEFT):
        player_rvy = player_rvy + (1.5 - player_rvy) * .3
    elif sgd.isKeyDown(sgd.KEY_RIGHT):
        player_rvy = player_rvy + (-1.5 - player_rvy) * .3
    else:
        player_rvy = player_rvy * .9
    sgd.rotateEntity(player, 0, player_rvy, 0)
    sgd.setEntityRotation(camera, 0, 0, player_rvy * -15)
    
    if sgd.isKeyDown(sgd.KEY_UP):
        player_rvx = player_rvx + (-1.5 - player_rvx) * .3
    elif sgd.isKeyDown(sgd.KEY_DOWN):
        player_rvx = player_rvx + (1.5 - player_rvx) * .3
    else:
        player_rvx = player_rvx * .9
    
    sgd.turnEntity(player,player_rvx, 0, 0)

    if sgd.isKeyDown(sgd.KEY_W):
        player_vz = player_vz + (speed - player_vz) * .3
    elif sgd.isKeyDown(sgd.KEY_S):
        player_vz = player_vz + (-speed - player_vz) * .3
    else:
        player_vz = player_vz * .9
        
    sgd.moveEntity(player, 0, 0, player_vz)

    if sgd.isKeyDown(sgd.KEY_A):
        player_vx = player_vx + (-speed - player_vx) * .3
    elif sgd.isKeyDown(sgd.KEY_D):
        player_vx = player_vx + (speed - player_vx) * .3
    else:
        player_vx = player_vx * .9

    sgd.moveEntity(player, player_vx, 0, 0)


def playerFly2(speed, maxSpeed, minSpeed):
    
    global player
    global player_rvx
    global player_rvy
    global player_vx
    global player_vy
    global player_vz
    global camera

    if sgd.isKeyDown(sgd.KEY_LEFT):
        player_rvy = player_rvy + (1.5 - player_rvy) * 0.3
    elif sgd.isKeyDown(sgd.KEY_RIGHT):
        player_rvy = player_rvy + (-1.5 - player_rvy) * 0.3
    else:
        player_rvy = player_rvy * 0.9
    sgd.rotateEntity(player, 0, player_rvy, 0)
    sgd.setEntityRotation(camera, 0, 0, player_rvy * -15)
    
    if sgd.isKeyDown(sgd.KEY_UP):
        player_rvx = player_rvx + (-1.5 - player_rvx) * 0.3
    elif sgd.isKeyDown(sgd.KEY_DOWN):
        player_rvx = player_rvx + (1.5 - player_rvx) * 0.3
    else:
        player_rvx = player_rvx * 0.9
    
    sgd.turnEntity(player,player_rvx, 0, 0)

    if sgd.isKeyDown(sgd.KEY_W):
        player_vz = player_vz + (maxSpeed - player_vz) * 0.3
    elif sgd.isKeyDown(sgd.KEY_S):
        player_vz = player_vz + (minSpeed - player_vz) * 0.3
    else:
        player_vz = player_vz * .9
        
    sgd.moveEntity(player, 0, 0, player_vz)

    if sgd.isKeyDown(sgd.KEY_A):
        player_vx = player_vx + (-speed - player_vx) * 0.3
    elif sgd.isKeyDown(sgd.KEY_D):
        player_vx = player_vx + (speed - player_vx) * 0.3
    else:
        player_vx = player_vx * 0.9

    sgd.moveEntity(player, player_vx, 0, 0)







