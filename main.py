import pygame
import math
import rotate_app

def translate_image(image,x,y,x_speed,y_speed,distance):
    
    current_distance = 0
    while current_distance <= distance:
        x += x_speed
        y += y_speed
        current_distance += math.sqrt(x_speed**2 + y_speed**2)
        #print(current_distance)

        screen.blit(image,(x,y))
        time.sleep(0.1)
        pygame.display.update()

if __name__ == "__main__":
    rot_app = rotate_app.App()
    rot_app.on_execute()