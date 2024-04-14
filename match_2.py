import pygame 

pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill((0,0,128))

pygame.display.update()

salt = pygame.image.load("salt.png")
peanutbutter = pygame.image.load("peanut_butter.png")
macaroni = pygame.image.load("macaroni.png")
cat = pygame.image.load("cat.png")

screen.blit(salt, (150,100))
screen.blit(peanutbutter, (150,200))
screen.blit(macaroni, (150,300))
screen.blit(cat, (150,400))

pygame.display.update()


jam = pygame.image.load("jam.png")
pepper = pygame.image.load("pepper.png")
dog = pygame.image.load("dog.png")
cheese = pygame.image.load("cheese.png")

screen.blit(jam, (350,100))
screen.blit(pepper, (350,200))
screen.blit(cheese, (350,300))
screen.blit(dog, (350,400))

pygame.display.update()