x = 0

def setup():
    size (1000, 400)

def draw():
     #sun
    fill(225,122,0)
    ellipse(width/2, height/3, 100,100)
       
    global x
    if x >= 700:
        x = -320
    else:
       x += 1.5
       background(253,94,83)
       noStroke()
       fill(249,146,190)
       ellipse(x, height/2, 75, 75)
       ellipse(x+60,height/2.1, 100,100)
       ellipse(x+120, height/2, 75, 75)
       
      


    
