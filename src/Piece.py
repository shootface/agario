class Piece:
    def __init__(self,surface,pos,color,mass,name,transition=False):
        self.x,self.y = pos
        self.mass = mass
        self.splitting = transition
        self.surface = surface
        self.name = name

    def draw(self):
        pass

    def update(self):
        if(self.splitting):
            pass

class Cell:
    def __init__(self,surface):
        self.x = random.randint(20,1980)
        self.y = random.randint(20,1980)
        self.mass = 7
        self.surface = surface
        self.color = colors_cells[random.randint(0,len(colors_cells)-1)]

    def draw(self,cam):
        pygame.draw.circle(self.surface,self.color,(int((self.x*cam.zoom+cam.x)),int(self.y*cam.zoom+cam.y)),int(self.mass*cam.zoom))

def spawn_cells(numOfCells):
    for i in range(numOfCells):
        cell = Cell(surface)
        cell_list.append(cell)

def draw_grid():
    for i in range(0,2001,25):
        pygame.draw.line(surface,(230,240,240),(0+camera.x,i*camera.zoom+camera.y),(2001*camera.zoom+camera.x,i*camera.zoom+camera.y),3)
        pygame.draw.line(surface,(230,240,240),(i*camera.zoom+camera.x,0+camera.y),(i*camera.zoom+camera.x,2001*camera.zoom+camera.y),3)
