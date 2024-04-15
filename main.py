import pygame
pygame.init()

SCREEN_WIDTH=800
SCREEN_HEIGHT=int(SCREEN_WIDTH*0.8)
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')

#set frame
clock=pygame.time.Clock()
FPS=60

#define colors
BG=(144,201,120)

#Drawing black background
def draw_bg():
    screen.fill(BG)

run=True
moving_left = False
moving_right = False

class Soldier(pygame.sprite.Sprite):
    def __init__(self,x,y,scale,speed):
        pygame.sprite.Sprite.__init__(self)
        image=pygame.image.load('img/player/Idle/0.png')
        self.image=pygame.transform.scale(image,(image.get_width()*scale,image.get_height()*scale))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.speed=speed
        self.direction=1
        self.flip=False


    def draw(self):
        screen.blit(self.image,self.rect)

    def move(self,moving_left,moving_right):
        #reset movement variables
        dx=0
        dy=0
        #
        if moving_left:
            dx=-self.speed
        if moving_right:
            dx=+self.speed

        #Updating position of rect
        self.rect.x+=dx
        self.rect.y+=dy
        


player=Soldier(200,200,1,5)


while run:
    clock.tick(FPS)
    draw_bg()
    player.draw()
    player.move(moving_left,moving_right)

    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            run=False
        
        #Keyboard press down
        if event.type==pygame.KEYDOWN:
            if event.type==pygame.K_ESCAPE:
                run=False
            if event.key==pygame.K_a:
                moving_left=True
            if event.key==pygame.K_d:
                moving_right=True

        #keybarod button up
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_a:
                moving_left=False
            if event.key==pygame.K_d:
                moving_right=False
        

        
    pygame.display.update()

pygame.quit()