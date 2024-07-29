import sys,pygame
from pygame.locals import*
pygame.init()
size=width,height=500,500
speed=[5,5]
black=0,0,0
white=255,255,255
screen=pygame.display.set_mode(size)
pygame.display.set_caption('BOUNCING BALL')

ball=pygame.image.load("ball.jpeg")
ballrect=ball.get_rect()

Clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    ballrect=ballrect.move(speed)
    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]=-speed[1]
    screen.fill(white)
    screen.blit(ball,ballrect)
    pygame.display.flip()
    Clock.tick(60)