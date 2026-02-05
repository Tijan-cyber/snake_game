import pygame



pygame.init()

screen = pygame.display.set_mode((2000, 1200))
pygame.display.set_caption("Pygame")
bg = (0,0,0)
igra = True

clock = pygame.time.Clock()

while igra:
	clock.tick(1000)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			igra = False


	screen.fill(bg)
	pygame.display.update()