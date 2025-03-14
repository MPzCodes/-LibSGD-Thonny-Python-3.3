# File for libsgd Version 0.18.1 march 2025 
#
# Version 0.1, Open only a libsgd windows and write a log.txt file in the folder

from libsgd import sgd

sgd.setConfigVar("log.logfilePath","log.txt")
sgd.setConfigVar("log.logfileEnabled","1")
sgd.log("This is my lofile of the helloworld_DEBUG_file")

sgd.init()
sgd.createWindow(640, 480, "Hallo Welt!" , 0)
sgd.setClearColor (1, 0.5, 0, 1)

while (sgd.pollEvents() & 1) == 0:
    if sgd.isKeyHit(sgd.KEY_ESCAPE):
       break
    sgd.renderScene()
    sgd.present()
    
sgd.terminate()