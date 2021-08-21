y_position = 0
color_is = False
def setup():
    size(600,610)
    
def draw():
    global y_position 
    background(255)
    if color_is == True:
       fill(230, 0, 38)
    else:
       fill(0, 47, 187)

    ellipse(width /1.15, y_position, 50, 50)
    if y_position > height:
       y_position = 0
    else:
       y_position = map(second(), 0, 59, 0, height)


    ellipse(width / 5, y_position, 50, 50)
    if y_position > height:
       y_position = 0
    else:
       y_position = map(minute(), 0, 59, 0, height)
       
    ellipse(width / 1.85, y_position, 50, 50)
    if y_position > height:
       y_position = 0
    else:
       y_position = map(hour(), 0, 23, 0, height)
    line(425, 0,425, 600)
    line(225,0,225,600)
    line(25,0,25,600)
    
    line(0,150,425,150)
    line(0, 300, 425, 300)
    line(0,450,425,450)
    line(0,600,425,600)
    line(0,35,600,30)
    line(425,50,600,50)
    line(425,75,600,75)
    line(425,100,600,100)
    line(425,125,600,125)
    line(425,150,600,150)
    line(425,175,600,175)
    line(425,200,600,200)
    line(425,225,600,225)
    line(425,250,600,250)
    line(425,275,600,275)
    line(425,300,600,300)
    line(425,325,600,325)
    line(425,350,600,350)
    line(425,375,600,375)
    line(425,400,600,400)
    line(425,425,600,425)
    line(425,450,600,450)
    line(425,475,600,475)
    line(425,500,600,500)
    line(425,525,600,525)
    line(425,550,600,550)
    line(425,575,600,575)
    line(425,600,600,600)
    textSize(25)
    text("Segundos",65,30)
    textSize(25)
    text("Minutos",280,30)
    textSize(25)
    text("Horas",480,30)
    textSize(20)
    text("15",0,149)
    textSize(20)
    text("30",0,299)
    textSize(20)
    text("45",0,449)
    textSize(20)
    text("59",0,599)
    textSize(20)
    text("1",425,49)
    textSize(20)
    text("2",425,74)
    textSize(20)
    text("3",425,99)
    textSize(20)
    text("4",425,124)
    textSize(20)
    text("5",425,149)
    textSize(20)
    text("6",425,174)
    textSize(20)
    text("7",425,199)
    textSize(20)
    text("8",425,224)
    textSize(20)
    text("9",425,249)
    textSize(20)
    text("10",425,274)
    textSize(20)
    text("11",425,299)
    textSize(20)
    text("12",425,324)
    textSize(20)
    text("13",425,349)
    textSize(20)
    text("14",425,374)
    textSize(20)
    text("15",425,399)
    textSize(20)
    text("16",425,424)
    textSize(20)
    text("17",425,449)
    textSize(20)
    text("18",425,474)
    textSize(20)
    text("19",425,499)
    textSize(20)
    text("20",425,524)
    textSize(20)
    text("21",425,549)
    textSize(20)
    text("22",425,574)
    textSize(20)
    text("23",425,599)
def mousePressed():
    global color_is
    color_is = not color_is
