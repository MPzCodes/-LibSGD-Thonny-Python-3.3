# File for libsgd Version 0.18.1 march 2025 
#
# Version 0.1, shows a 2d screen over a 3d world

from libsgd import sgd
import random

sgd.init()


sgd.createWindow(sgd.getDesktopWidth() // 2, sgd.getDesktopHeight() // 2, "Overlay",
				 sgd.WINDOW_FLAGS_CENTERED)

env = sgd.loadCubeTexture("../assets/envmaps/sunnysky-cube.png",sgd.TEXTURE_FORMAT_ANY,sgd.TEXTURE_FLAGS_DEFAULT)

sgd.setEnvTexture (env)

skybox = sgd.createSkybox(env)
sgd.setSkyboxRoughness (skybox, 0.3)

sgd.clear2D()

sgd.draw2DText ("Hello World!",0,0)

#; Draw some lines
#;Set2DLineWidth 5


for i in range (1, 101):
    sgd.set2DFillColor (random.randint(0, 1),random.randint(0, 1),random.randint(0, 1),1)
    sgd.draw2DLine (random.randint(0, 1920), random.randint(0, 1080), random.randint(0, 1920), random.randint(0, 1080))

sgd.set2DOutlineEnabled (True)

#; Draw some outlined rects
for i in range (1,101):
    w=random.randint(32,64)
    h=random.randint(32,64)
    x=random.randint(0,1920-w)
    y=random.randint(0,1080-h)
    sgd.set2DFillColor (random.randint(0,1),random.randint(0,1),random.randint(0,1),1)
    sgd.draw2DRect (x, y, x+w, y+h)

sgd.set2DOutlineColor (0,255,0,1)

#; Draw some ovals
for i in range (1,101):
    w=random.randint(32,64)
    h=random.randint(32,62)
    x=random.randint(0,1920-w)
    y=random.randint(0,1080-h)
    sgd.set2DFillColor (random.randint(0,1),random.randint(0,1),random.randint(0,1),1)
    sgd.draw2DOval (x, y, x+w, y+h)

while (sgd.pollEvents() & 1) == 0:

    sgd.renderScene()
    
    sgd.present()

sgd.terminate()
###End###