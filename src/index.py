import pygame,random,math, importlib

from . import Player


game = Game()

#Cell.spawn_cells(2000)

def draw_HUD():
    w,h = font.size("Score: "+str(int(blob.mass*2))+" ")
    surface.blit(pygame.transform.scale(t_surface,(w,h)),(8,screen_height-30))
    surface.blit(t_lb_surface,(screen_width-160,15))
    game.drawText("Score: " + str(int(blob.mass*2)),(10,screen_height-30))
    surface.blit(big_font.render("Leaderboard",0,(255,255,255)),(screen_width-157,20))
    game.drawText("1. G #1",(screen_width-157,20+25))
    game.drawText("2. G #2",(screen_width-157,20+25*2))
    game.drawText("3. ISIS",(screen_width-157,20+25*3))
    game.drawText("4. ur mom",(screen_width-157,20+25*4))
    game.drawText("5. w = pro team",(screen_width-157,20+25*5))
    game.drawText("6. jumbo",(screen_width-157,20+25*6))
    game.drawText("7. [voz]plz team",(screen_width-157,20+25*7))
    game.drawText("8. G #3",(screen_width-157,20+25*8))
    game.drawText("9. doge",(screen_width-157,20+25*9))
    if(blob.mass <= 500):
        game.drawText("10. G #4",(screen_width-157,20+25*10))
    else:
        game.drawText("10. Viliami",(screen_width-157,20+25*10),(210,0,0))

while(True):
    clock.tick(70)
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
    blob.update()
    camera.zoom = 100/(blob.mass)+0.3
    camera.centre(blob)
    surface.fill((242,251,255))
    #surface.fill((0,0,0))
    draw_grid()
    for c in cell_list:
        c.draw(camera)
    blob.draw(camera)
    draw_HUD()
    pygame.display.flip()