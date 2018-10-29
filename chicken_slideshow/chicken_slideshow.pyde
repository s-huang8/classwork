slide = 0

def setup():
    global chicken_img
    size(600,400)
    chicken_img = loadImage("data/chicken.jpg")
    
def draw():
    global slide
    
    if frameCount % (60*0.5) == 0:
        slide += 1
        if slide >= 4:
            slide = 0
        
    if slide == 0:
        background(135, 234, 60)
        image(chicken_img, 50, 0, 500, 400)
    elif slide == 1:
        background(145,135,12)
    elif slide == 2:
        background(43, 123, 234)
        ellipse(height/2, width/2, 500, 500)
    else:
        background(255)


    '''    
def mousePressed():
    global slide
    slide += 1
    if slide >= 4:
        slide = 0 
    '''
