x = 0

def setup():
    size (1000, 600)

def draw():
           
    global x

    if x >= 2000:
        x = -320
    else:
       x += 1.5
       background(253,94,83)
       noStroke()
          
    fill(0)  
    triangle(40, 580, 60, 475, 80, 580)
    rect(50, 580, 20, 75)
    
    #tower
    quad(800, 181, 800, 181, 760, 750, 840, 850)
    rect(750, 300, 100, 80, 17)
    rect(740, 325, 120, 20, 17)

    #dome
    arc(620, 620, 280, 280, PI, TWO_PI);

    
        #sun
    fill(255,215,0)
    ellipse(width/2, height/3, 150,150)
       
       #clouds
    fill(249,146,190)
    ellipse(x, height/2, 75, 75)   
    ellipse(x+60,height/2.1, 100,100)

       
       ellipse(x-120, height/1.5, 75, 75)
       ellipse(x-180,height/1.55, 100,100)
       ellipse(x-240, height/1.5, 75, 75)
       
       ellipse(x-350, height/2, 75, 75)
       ellipse(x-410,height/2.1, 100,100)
       ellipse(x-470, height/2, 75, 75)
 
