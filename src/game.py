import pygame
import random
import math
import copy
from src.Player import Player
from src.Enemy import Enemy
from src.camera import Camera
from src.Cell import Cell
from src.Iterator import iteradorGE


class Game:

    screen_width, screen_height = (800, 500)
    instance = None

    #Singleton
    @staticmethod
    def getGame():
        if Game.instance is None:
            Game.instance = Game()
        return Game.instance

    def __init__(self):
        self.initScreen()
        self.initPlayer()
        self.initEnemys()
        self.initFood()
        self.run()

    def initScreen(self):
        pygame.init()
        screen_width, screen_height = (800, 500)
        self.surface = pygame.display.set_mode((screen_width, screen_height))
        self.t_surface = pygame.Surface(
            (95, 25), pygame.SRCALPHA)  # transparent rect for score
        # transparent rect for leaderboard
        self.t_lb_surface = pygame.Surface((155, 278), pygame.SRCALPHA)
        self.t_surface.fill((50, 50, 50, 80))
        self.t_lb_surface.fill((50, 50, 50, 80))
        pygame.display.set_caption("Agar.io")
        self.cell_list = list()
        self.player_list = list()
        self.player_colec = iter
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Ubuntu', 20, True)
        self.big_font = pygame.font.SysFont('Ubuntu', 24, True)

    def initPlayer(self):
        self.blob = Player(self.surface, Game.screen_width,
                           Game.screen_height, "Viliami")
        self.player_list.append(self.blob)
        self.camera = Camera(Game.screen_width, Game.screen_height, self.blob)

    def initEnemys(self):
        blob1 = Enemy(self.surface, Game.screen_width,
                           Game.screen_height, "test")
        blob2 = Enemy(self.surface, Game.screen_width,
                           Game.screen_height, "test")
        self.player_list.append(blob1)
        self.player_list.append(blob2)
    def initFood(self):
        cell = Cell()
        self.spawn_cells(cell,2000)

    def drawText(self, message, pos, color=(255, 255, 255)):
        self.surface.blit(self.font.render(message, 1, color), pos)

    def spawn_cells(self, cell,numOfCells):
        localCell = cell
        localCell.inicializar()
        for i in range(numOfCells):
            self.cell_list.append(localCell)
            localCell = copy.deepcopy(localCell)
            localCell.inicializar()

    def draw_grid(self):
        for i in range(0, 2001, 25):
            pygame.draw.line(self.surface,
                             (230, 240, 240),
                             (0+self.camera.x, i*self.camera.zoom + self.camera.y),
                             (2001*self.camera.zoom+self.camera.x, i*self.camera.zoom+self.camera.y), 3)
            pygame.draw.line(self.surface,
                             (230, 240, 240),
                             (i*self.camera.zoom+self.camera.x, 0 + self.camera.y),
                             (i*self.camera.zoom+self.camera.x,2001*self.camera.zoom+self.camera.y),
                             3)

    def draw_HUD(self):
        w, h = self.font.size("Score: "+str(int(self.blob.mass*2))+" ")
        self.surface.blit(pygame.transform.scale(
            self.t_surface, (w, h)), (8, Game.screen_height-30))
        self.surface.blit(self.t_lb_surface, (Game.screen_width-160, 15))
        self.drawText("Score: " + str(int(self.blob.mass*2)),
                      (10, Game.screen_height-30))
        self.surface.blit(self.big_font.render(
            "Leaderboard", 0, (255, 255, 255)), (Game.screen_width-157, 20))
        self.drawText("1. G #1", (Game.screen_width-157, 20+25))
        self.drawText("2. G #2", (Game.screen_width-157, 20+25*2))
        self.drawText("3. ISIS", (Game.screen_width-157, 20+25*3))
        self.drawText("4. ur mom", (Game.screen_width-157, 20+25*4))
        self.drawText("5. w = pro team", (Game.screen_width-157, 20+25*5))
        self.drawText("6. jumbo", (Game.screen_width-157, 20+25*6))
        self.drawText("7. [voz]plz team", (Game.screen_width-157, 20+25*7))
        self.drawText("8. G #3", (Game.screen_width-157, 20+25*8))
        self.drawText("9. doge", (Game.screen_width-157, 20+25*9))
        if(self.blob.mass <= 500):
            self.drawText("10. G #4", (Game.screen_width-157, 20+25*10))
        else:
            self.drawText("10. Viliami", (Game.screen_width -
                                          157, 20+25*10), (210, 0, 0))

    def run(self):
        while(True):
            self.clock.tick(70)
            for e in pygame.event.get():
                if(e.type == pygame.KEYDOWN):
                    if(e.key == pygame.K_ESCAPE):
                        pygame.quit()
                        quit()
                    if(e.key == pygame.K_SPACE):
                        blob.split()
                    if(e.key == pygame.K_w):
                        blob.feed()
                if(e.type == pygame.QUIT):
                    pygame.quit()
                    quit()
            #self.blob.update(self.cell_list)
            self.camera.zoom = 10/(self.blob.mass)+0.3
            self.camera.centre(self.blob)
            self.surface.fill((242, 251, 255))
            # surface.fill((0,0,0))
            self.draw_grid()
            for c in self.cell_list:
                c.draw(self.camera,self.surface)
            for player in self.player_list:
                player.draw(self.camera)
                player.update(self.cell_list,self.player_list)
            #self.draw_HUD()
            pygame.display.flip()
