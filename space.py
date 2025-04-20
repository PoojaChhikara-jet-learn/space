import pgzrun,time,random
WIDTH=750
HEIGHT=600
TITLE="connecting the satellite"
satellite=[]
line=[]
nextsatellite=0
number=random.randint(6,9)
for i in range(number):
    s=Actor("satellite.png")
    s.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
    satellite.append(s)


def draw():
    screen.blit("space.png",(0,0))

    #for i in range(number):
        #satellite[i].draw()
        #screen.draw.text(str(i+1),(satellite[i].pos[0],satellite[i].pos[1]+20))
    for i,v in enumerate (satellite):
        v.draw()
        screen.draw.text(str(i+1),(v.pos[0],v.pos[1]-40))




















pgzrun.go()