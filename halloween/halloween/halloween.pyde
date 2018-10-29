x = 0
y = 600

def setup():
    size(900, 600)
    global bush
    global pump1
    global enter
    global pump

    bush = loadImage ("bush.png")
    pump1 = loadImage("scarypump.png")
    enter = loadImage ("enter.gif")
    pump = loadImage ("pump.png")
    
def draw(): 
    global x
    global y
     
    if x >= 1000:
        x = -100
          
    else:
        x +=1.5
          
    background(0, 51, 102)
    noStroke()
    #bushes
    fill(101, 146, 41)
    rect(0, 560, width, height)
    image(bush, -170, 460, 400, 200)
    image(bush, 60, 460, 400, 200)
    image(bush, 290, 460, 400, 200)
    image(bush, 510, 460, 400, 200)

    
    #cresent moon
    fill(245, 227, 135)
    ellipse(width/3, height/4, 225,225)
    fill(0, 51, 102)
    ellipse(width/2.5, height/3.7, 200, 200)
    

    image(pump, 50, 350, 100, 85)
    image(pump1, 250, 260, 400, 350)
    
    stroke(255,45,234)
    textSize(20)
    text("Click to enter", 400, 550)    
