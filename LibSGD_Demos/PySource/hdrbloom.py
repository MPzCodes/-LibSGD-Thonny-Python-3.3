# File for libsgd Version 0.18.1 march 2025 
#
# Version 0.1, shows render effects on a picture

from libsgd import sgd

# Visit https://openexr.com/en/latest/ for more exr info and samples.

sgd.init()

sgd.createWindow(sgd.getDesktopWidth() // 2, sgd.getDesktopHeight() // 2, "Bloomeffect",
				 sgd.WINDOW_FLAGS_CENTERED)

mat = sgd.loadEmissiveMaterial("../assets/misc/StillLife.exr")
sgd.setMaterialBlendMode (mat, sgd.BLEND_MODE_ALPHA_BLEND)

sgd.set2DFillMaterial (mat)

bloom = sgd.createBloomEffect()


#while not (sgd.pollEvents() & sgd.EVENT_MASK_CLOSE_CLICKED):

while ((sgd.pollEvents() & 1) == 0):

    if sgd.isKeyHit(sgd.KEY_SPACE):
        sgd.setRenderEffectEnabled (bloom, ~sgd.isRenderEffectEnabled(bloom)+2)

    if sgd.isKeyHit(sgd.KEY_UP): 
        if sgd.getBloomEffectRadius(bloom) < 31:
            sgd.setBloomEffectRadius(bloom, sgd.getBloomEffectRadius(bloom)+1)

    elif sgd.isKeyHit(sgd.KEY_DOWN):
        if sgd.getBloomEffectRadius(bloom) > 2:
            sgd.setBloomEffectRadius(bloom, sgd.getBloomEffectRadius(bloom)-1)

    sgd.clear2D()

    sgd.draw2DRect (0,0,sgd.getWindowWidth(),sgd.getWindowHeight())
    sgd.draw2DText ("Bloom enabled (space): " + str(sgd.isRenderEffectEnabled(bloom)),0,0)
    sgd.draw2DText ("Bloom Radius (up/down): " + str(sgd.getBloomEffectRadius(bloom)),0,16)

    sgd.renderScene()
    
    sgd.present()

sgd.terminate()
###End###

