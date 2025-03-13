
from libsgd import sgd

import math
sgd.init()

def sgd_createSphere(radius, xSegs, ySegs, material):
    
    mesh = sgd.createMesh(0,1)

    fxSegs = 1/xSegs
    fySegs = 1/ySegs
    
    for i in range (0, xSegs):
        sgd.addVertex (mesh, 0, radius, 0, 0, 1, 0, (i + 0.5) * 2 * fxSegs, 0)

    for j in range (1, ySegs):
        pitch = math.radians(90 - j * fySegs * 180) 
        for i in range (0, xSegs+1):
            yaw = math.radians(i * fxSegs * 360)
            r = math.cos(pitch)
            y = math.sin(pitch)
            x = math.cos(yaw) * r
            z = math.sin(yaw) * r
            sgd.addVertex (mesh, x * radius, y * radius, z * radius, x, y, z, i * 2 * fxSegs, j * fySegs)

    for i in range (0, xSegs):
        sgd.addVertex (mesh, 0, -radius, 0, 0, -1, 0, (i + 0.5) * 2 * fxSegs, 1)

    surf = sgd.createSurface(mesh, material,0)

    for i in range (0, xSegs):
        sgd.addTriangle (surf, i, i + xSegs, i + xSegs + 1)

    for j in range (1,  ySegs-1):
        for i in range (0, xSegs):
            v0 = j * (xSegs + 1) + i - 1
            v2 = v0 + xSegs + 2
            sgd.addTriangle (surf, v0, v2, v0 + 1)
            sgd.addTriangle (surf, v0, v2 - 1, v2)

    for i in range (0, xSegs):
        v0 = (xSegs + 1) * (ySegs - 1) + i - 1
        sgd.addTriangle (surf, v0, v0 + xSegs + 1, v0 + 1)

    sgd.updateMeshTangents(mesh)

    return mesh

sgd.createWindow(sgd.getDesktopWidth() // 2, sgd.getDesktopHeight() // 2, "Custom mesh demo",
				 sgd.WINDOW_FLAGS_CENTERED)

env = sgd.loadCubeTexture("../assets/envmaps/sunnysky-cube.png", sgd.TEXTURE_FORMAT_ANY, sgd.TEXTURE_FLAGS_DEFAULT)
sgd.setEnvTexture(env)

skybox = sgd.createSkybox(env)
sgd.setSkyboxRoughness (skybox, 0.3)

light = sgd.createDirectionalLight()
sgd.turnEntity (light,-45,0,0) #; Tilt light down 45 degrees 

material = sgd.loadPBRMaterial("../assets/misc/test-texture.png")
sgd.setMaterialFloat (material, "roughness", 0.5)

mesh = sgd_createSphere(1,96,48,material)
#mesh = sgd.createSphereMesh(1,96,48,material)

model=sgd.createModel(mesh)
sgd.moveEntity (model,0,0,3)

while not sgd.pollEvents():

    if sgd.isKeyDown(263):
        sgd.turnEntity (model,0,3,0)
    elif sgd.isKeyDown(262):
        sgd.turnEntity (model,0,-3,0)

    if sgd.isKeyDown(264):
        sgd.TurnEntity (model,3,0,0)
    elif sgd.isKeyDown(265):
        sgd.turnEntity (model,-3,0,0)

    sgd.renderScene()
  
    sgd.present()
    
sgd.terminate()   
 