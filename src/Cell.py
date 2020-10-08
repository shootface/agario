import random,pygame, copy

class Cell:
    colors_cells = [(80,252,54),(36,244,255),(243,31,46),(4,39,243),(254,6,178),(255,211,7),(216,6,254),(145,255,7),(7,255,182),(255,6,86),(147,7,255)]
    def __init__(self,surface):
        self.x = random.randint(20,1980)
        self.y = random.randint(20,1980)
        self.mass = 7
        self.surface = surface
        
    def draw(self,cam):
        self.color = Cell.colors_cells[random.randint(0,len(Cell.colors_cells)-1)]
        pygame.draw.circle(self.surface,self.color,(int((self.x*cam.zoom+cam.x)),int(self.y*cam.zoom+cam.y)),int(self.mass*cam.zoom))