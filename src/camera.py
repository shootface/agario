class Camera:
    
    def __init__(self,screen_width,screen_height,player):
        self.x = 0
        self.y = 0
        self.width = screen_width
        self.height = screen_height
        self.zoom = 0.5
        self.p = player

    def centre(self,blobOrPos):
        #if(isinstance(blobOrPos,self.p)):
            p = blobOrPos
            self.x = (p.startX-(p.x*self.zoom))-p.startX+((self.width/2))
            self.y = (p.startY-(p.y*self.zoom))-p.startY+((self.height/2))
        #elif(type(blobOrPos) == tuple):
            #self.x,self.y = blobOrPos