import pygame,random,math, random
from src.element import GameElement
#from src.Piece import Piece

class Enemy(GameElement):
    
    def __init__(self,surface,screen_w,screen_h,name = ""):
        colors_players = [(37,7,255),(35,183,253),(48,254,241),(19,79,251),(255,7,230),(255,7,23),(6,254,13)]
        print("PLAYER")
        self.startX = self.x = self.cell_f_x =  random.randint(100,400)
        self.startY = self.y = self.cell_f_y = random.randint(100,400)
        self.mass = 20
        self.surface = surface
        self.color = colors_players[random.randint(0,len(colors_players)-1)]
        self.na = name
        #self.pieces = list()
        #piece = Piece(self.surface,(self.x,self.y),self.color,self.mass,self.na)
        self.screen_width = screen_w
        self.screen_height = screen_h
        self.font = pygame.font.SysFont('Ubuntu',20,True)
        

    def update(self,cell_list,enemy_list):
        self.move(cell_list,enemy_list)
        self.collisionDetection(cell_list)
        self.enemyDetection(enemy_list)

    def collisionDetection(self,cell_list):
        for cell in cell_list:
            if(self.getDistance((cell.x,cell.y),(self.x,self.y)) <= self.mass/2):
                self.mass+=0.5
                cell_list.remove(cell)

    def move(self,cell_list,enemy_list):
        r_cell = random.choice(cell_list)
        self.cell_f_x = random.randint(-800,800)
        self.cell_f_y =random.randint(-500,500)
        dX,dY = (self.cell_f_x,self.cell_f_y)
        print(dX,dY)
        rotation = math.atan2(dY-(float(self.screen_height)/2),dX-(float(self.screen_width)/2))*180/math.pi
        speed = 5-1
        vx = speed * (90-math.fabs(rotation))/90
        vy = 0
        if(rotation < 0):
            vy = -speed + math.fabs(vx)
        else:
            vy = speed - math.fabs(vx)
        self.x += vx
        self.y += vy

    def feed(self):
        pass

    def split(self):
        pass

    def draw(self,cam):
        col = self.color
        zoom = cam.zoom
        x = cam.x
        y = cam.y
        pygame.draw.circle(self.surface,(col[0]-int(col[0]/3),int(col[1]-col[1]/3),int(col[2]-col[2]/3)),(int(self.x*zoom+x),int(self.y*zoom+y)),int((self.mass/2+3)*zoom))
        pygame.draw.circle(self.surface,col,(int(self.x*cam.zoom+cam.x),int(self.y*cam.zoom+cam.y)),int(self.mass/2*zoom))
        if(len(self.na) > 0):
            fw, fh = self.font.size(self.na)
            self.drawText(self.na, (self.x*cam.zoom+cam.x-int(fw/2),self.y*cam.zoom+cam.y-int(fh/2)),(50,50,50))

    def getDistance(self,pos1,pos2):
        px,py = pos1
        p2x,p2y = pos2
        diffX = math.fabs(px-p2x)
        diffY = math.fabs(py-p2y)
        return ((diffX**2)+(diffY**2))**(0.5)
    
    def drawText(self,message,pos,color=(255,255,255)):
        self.surface.blit(self.font.render(message,1,color),pos)

    def enemyDetection(self,player_list):
        for enemy in player_list:
            if(enemy.x!=self.x and enemy.y != self.y):
                if(self.getDistance((enemy.x,enemy.y),(self.x,self.y)) <= self.mass/2) :
                    if(self.mass > enemy.mass):
                        self.mass+=enemy.mass
                        player_list.remove(enemy)
                        print("Comido")
