import pygame
 
class App:
    x = 0
    y = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.clock = pygame.time.Clock()
 
    def on_init(self):
        pygame.init()
        self._running = True
        self._image_surf = pygame.image.load("cat.jpg")
        self._display_surf = pygame.display.set_mode(self._image_surf.get_rect().size, pygame.HWSURFACE)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    
    def on_loop(self):
        pass
        

    def on_render(self):
        self._display_surf.blit(self._image_surf,(0,0))
        pygame.display.update()
        self.clock.tick(30)
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()



