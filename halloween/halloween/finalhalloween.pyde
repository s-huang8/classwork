x = 0
y = 0
slide = 0

def setup():
    size(900, 600)
    global bush, pump1, star, pump, sunlight, hill, banner, witch, ghost, bat, pumpkin, mummy

    bush = loadImage ("bush.png")
    pump1 = loadImage("scarypump.png")
    star = loadImage ("star.png")
    pump = loadImage ("pump.png")
    sunlight = loadImage ("sunlight.png")
    hill = loadImage ("hill.png")
    banner = loadImage("halloween_banner.png")
    witch = loadImage("witch.png")
    ghost = loadImage("ghost.png")
    bat = loadImage("bat.png")
    pumpkin = loadImage("pumpkin.png")
    mummy = loadImage("mummy.png")
    
def draw(): 
    global x
    global y

    if slide == 0:
        if x >= 1650:
            x = 0
                
        else:
            x += 2
    
        background(0, 51, 102)
        noStroke()
        
        #hill
        image(hill, -100, 250, 1200, 300)
        
        #light
        image(sunlight, 150, 200, 600, 600)
            
        #pumpkin
        image(pump, 0, 450, 100, 85)
        image(pump, 170, 450, 100, 85)
        image(pump, 630, 450, 100, 85)
        image(pump, 800, 450, 100, 85)
        
        #bushes
        fill(51, 73, 20)
        rect(0, 560, width, height)
        tint(100)
        image(bush, -170, 460, 400, 200)
        image(bush, 60, 460, 400, 200)
        image(bush, 290, 460, 400, 200)
        image(bush, 510, 460, 400, 200)
    
        
        #cresent moon
        fill(245, 227, 135)
        ellipse(width/3, height/4, 225,225)
        fill(0, 51, 102)
        ellipse(width/2.5, height/3.9, 150, 150)
        
        #pumpkin
        tint(255)
        image(pump, 10, 515, 100, 85)
        image(pump, 110, 515, 100, 85)
        image(pump, 600, 515, 100, 85)
        image(pump, 850, 515, 100, 85)
        
        #jackolantern
        image(pump1, 250, 260, 400, 350)
        
        #enter button
        fill(23,113,32)
        rect(340, 260, 200, 40,17)
        fill(255)
        stroke(255,45,234)
        textSize(20)
        text("Click to enter", 370, 285)    
        
        #stars
        image(star, x-50, height/12, 50, 50)
        image(star, x-100, height/4, 50, 50)
        image(star, x-200, height/8, 50, 50)
        image(star, x-300 , height/3, 50, 50)
        image(star, x-400, height/12.5, 50, 50)
        image(star, x-500, height/4.3, 50, 50)
        image(star, x-600, height/8, 50, 50)
        image(star, x-700 , height/3.7, 50, 50)
        
    elif slide == 1:
        if y >= 700:
            y = 35
            
        else:
            y += 3.5
        image(pumpkin, 0, 0, width, height)
        
        #bats
        image(bat, 300, 0, 150, 50)
        image(bat, 50, 250, 150, 50)
        image(bat, 775, 200, 125, 50)


        #ghost
        image(ghost, 540, y+35, 100, 100)
        image(ghost, 600, y+35*3, 100, 100)
        image(ghost, 660, y+35, 100, 100)
        
        #mummy
        image(mummy, 300, 200, 300, 400)
    
        #banner
        image(banner, 50, 25, 800, 200)
        
        #witch
        image(witch, 25, 300, 270, 280)
            
        textSize(18)
        text("Click twice to go back", 0, 590)   
         
def mousePressed():
    global slide
    slide +=1
    if slide >= 3:
        slide = 0
