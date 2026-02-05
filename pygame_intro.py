#Prva naloga:

#naredi pygame program, kjer so na ekranu 4je recti; vsi se premikajo, lahko levo-desno, ali pa gor-dol, 
#lahko tudi poševno

#naloga je, da vsakič, ko se dva recta dotakneta, si izmenjata malo barve 
#(če je rumen, drug zelen, bo rumen dal malo svoje barve zelenemu in obratno)


#dodatna naloga; ko se recta dotakneta, se odbijeta nazaj v smer iz katere sta prišla 



#dodatna naloga 2; recti se na začetku premikajo v naključne smeri. odbijajo se od drug drugega in od robov 

#------------------------------------------------------------------------------------------------------------------------


"""
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((2000, 1200))
pygame.display.set_caption("Pygame")
kvadrat1 = pygame.Rect(0, 0, 50, 50)
kvadrat2 = pygame.Rect(1950, 0, 50, 50)
kvadrat3 = pygame.Rect(0, 1150, 50, 50)
kvadrat4 = pygame.Rect(1950, 1150, 50, 50)

bg = (0,0,0)
igra = True

faktor1 = 3
faktor2 = -1
faktor3 = 1
faktor4 = -2
barva1 = [100, 230, 50]
barva2 = [0, 200, 80]
barva3 = [80, 0, 50]
barva4 = [170, 240, 0]
barvaNew1 = [0,0,0]
barvaNew2 = [0,0,0]
barvaNew3 = [0,0,0]
barvaNew4 = [0,0,0]



while igra:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			igra = False





	if kvadrat1.x > 1950 or kvadrat1.x < 0:
		faktor1 *= -1

	if kvadrat2.x > 1950 or kvadrat2.x < 0:
		faktor2 *= -1

	if kvadrat3.x > 1950 or kvadrat3.x < 0:
		faktor3 *= -1

	if kvadrat4.x > 1950 or kvadrat4.x < 0:
		faktor4 *= -1	

	



	if kvadrat1.colliderect(kvadrat2):
		faktor1 *= -1
		faktor2 *= -1
		barvaNew1[0] = random.choice(barva2)
		barvaNew1[1] = random.choice(barva2)
		barvaNew1[2] = random.choice(barva2)
		for i in barvaNew1:
			if i > 230:
				i -= 10
			elif i < 20:
				i += 10
			elif i < 230 and i > 20:
				i += 20

		barvaNew2[0] = random.choice(barva1)
		barvaNew2[1] = random.choice(barva1)
		barvaNew2[2] = random.choice(barva1)
		for i in barvaNew2:
			if i > 230:
				i -= 10
			elif i < 20:
				i += 10
			elif i < 230 and i > 20:
				i += 20




	if kvadrat3.colliderect(kvadrat4):
		faktor3 *= -1
		faktor4 *= -1
		barvaNew3[0] = random.choice(barva4)
		barvaNew3[1] = random.choice(barva4)
		barvaNew3[2] = random.choice(barva4)
		for i in barvaNew3:
			if i > 230:
				i -= 10
			elif i < 20:
				i += 10
			elif i < 230 and i > 20:
				i += 20

		barvaNew4[0] = random.choice(barva3)
		barvaNew4[1] = random.choice(barva3)
		barvaNew4[2] = random.choice(barva3)
		for i in barvaNew4:
			if i > 230:
				i -= 10
			elif i < 20:
				i += 10
			elif i < 230 and i > 20:
				i += 20




	kvadrat1.x += faktor1
	kvadrat2.x += faktor2
	kvadrat3.x += faktor3
	kvadrat4.x += faktor4

	print(tuple(barva1))
	screen.fill(bg)
	pygame.draw.rect(screen, tuple(barvaNew1), kvadrat1)
	pygame.draw.rect(screen, tuple(barvaNew2), kvadrat2)
	pygame.draw.rect(screen, tuple(barvaNew3), kvadrat3)
	pygame.draw.rect(screen, tuple(barvaNew4), kvadrat4)
	
	pygame.display.update()
"""

import pygame
import random
import numpy as np
import time


pygame.init()

screen = pygame.display.set_mode((2000, 1200))
pygame.display.set_caption("Pygame")
bg = (0,0,0)
igra = True


kvadrat1 = pygame.Rect(0, 0, 50, 50)
kvadrat2 = pygame.Rect(1950, 0, 50, 50)
kvadrat3 = pygame.Rect(0, 1150, 50, 50)
kvadrat4 = pygame.Rect(1950, 1150, 50, 50)

hitrost1 = np.array([random.randint(2,19), random.randint(5,19)])
hitrost2 = np.array([random.randint(-20,9), random.randint(4,15)])
hitrost3 = np.array([random.randint(2,20), random.randint(-13,5)])
hitrost4 = np.array([random.randint(-20,6), random.randint(-17,6)])

hitrosti = {
"kvadrat1" : hitrost1,
"kvadrat2" : hitrost2,
"kvadrat3" : hitrost3,
"kvadrat4" : hitrost4
}

RectNames = ["kvadrat1", "kvadrat2", "kvadrat3", "kvadrat4"]

# vektor hitrosti v numpy + kok je hitrost ves iz framov -> kok se je premaknu (pot)

barva1 = [100, 230, 50]
barva2 = [0, 200, 80]
barva3 = [80, 0, 50]
barva4 = [170, 240, 0]
barvaNew1 = [0,0,0]
barvaNew2 = [0,0,0]
barvaNew3 = [0,0,0]
barvaNew4 = [0,0,0]
barve = np.array([barva1, barva2, barva3, barva4])
barveNew = np.array([barvaNew1, barvaNew2, barvaNew3, barvaNew4])
clock = pygame.time.Clock()

while igra:
	clock.tick(1000)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			igra = False




	kvadrat1.x += hitrosti["kvadrat1"][0] * 0.1
	kvadrat2.x += hitrosti["kvadrat2"][0] * 0.1
	kvadrat3.x += hitrosti["kvadrat3"][0] * 0.1
	kvadrat4.x += hitrosti["kvadrat4"][0] * 0.1

	kvadrat1.y += hitrosti["kvadrat1"][1] * 0.1
	kvadrat2.y += hitrosti["kvadrat2"][1] * 0.1
	kvadrat3.y += hitrosti["kvadrat3"][1] * 0.1
	kvadrat4.y += hitrosti["kvadrat4"][1] * 0.1

	seznamRect = [kvadrat1, kvadrat2, kvadrat3, kvadrat4]

	for x in seznamRect:
		print(type(x))
		if x.y < 0:
			hitrosti[RectNames[seznamRect.index(x)]][1] = -hitrosti[RectNames[seznamRect.index(x)]][1]
		if x.y > 1150:
			hitrosti[RectNames[seznamRect.index(x)]][1] = -hitrosti[RectNames[seznamRect.index(x)]][1]

		if x.x < 0:
			hitrosti[RectNames[seznamRect.index(x)]][0] = -hitrosti[RectNames[seznamRect.index(x)]][0]
		if x.x > 1950:
			hitrosti[RectNames[seznamRect.index(x)]][0] = -hitrosti[RectNames[seznamRect.index(x)]][0]



	for i, rect in enumerate(seznamRect):
		if i != 0:
			if kvadrat1.colliderect(rect):
				barveNew[0,0] = random.choice(barve[i])
				barveNew[0,1] = random.choice(barve[i])
				barveNew[0,2] = random.choice(barve[i])
				for x in barveNew[0]:
					if x > 230:
						x -= 10
					elif x < 20:
						x += 10
					elif x < 230 and x > 20:
						x += 20

				if abs(rect.x - seznamRect[i].x) > abs(rect.y - seznamRect[i].y):
					hitrosti[RectNames[seznamRect.index(rect)]][0] -= hitrosti[RectNames[seznamRect.index(rect)]][0]
					hitrosti[RectNames[i]][0] -= hitrosti[RectNames[i]][0]
				else:
					hitrosti[RectNames[seznamRect.index(rect)]][1] -= hitrosti[RectNames[seznamRect.index(rect)]][1]
					hitrosti[RectNames[i]][1] -= hitrosti[RectNames[i]][1]

	for i, rect in enumerate(seznamRect):
		if i != 1:
			if kvadrat2.colliderect(rect):
				barveNew[1,0] = random.choice(barve[i])
				barveNew[1,1] = random.choice(barve[i])
				barveNew[1,2] = random.choice(barve[i])
				for x in barveNew[1]:
					if x > 230:
						x -= 10
					elif x < 20:
						x += 10
					elif x < 230 and x > 20:
						x += 20

				if abs(rect.x - seznamRect[i].x) > abs(rect.y - seznamRect[i].y):
					hitrosti[RectNames[seznamRect.index(rect)]][0] -= hitrosti[RectNames[seznamRect.index(rect)]][0]
					hitrosti[RectNames[i]][0] -= hitrosti[RectNames[i]][0]
				else:
					hitrosti[RectNames[seznamRect.index(rect)]][1] -= hitrosti[RectNames[seznamRect.index(rect)]][1]
					hitrosti[RectNames[i]][1] -= hitrosti[RectNames[i]][1]

	for i, rect in enumerate(seznamRect):
		if i != 2:
			if kvadrat3.colliderect(rect):
				barveNew[2,0] = random.choice(barve[i])
				barveNew[2,1] = random.choice(barve[i])
				barveNew[2,2] = random.choice(barve[i])
				for x in barveNew[2]:
					if x > 230:
						x -= 10
					elif x < 20:
						x += 10
					elif x < 230 and x > 20:
						x += 20

				if abs(rect.x - seznamRect[i].x) > abs(rect.y - seznamRect[i].y):
					hitrosti[RectNames[seznamRect.index(rect)]][0] -= hitrosti[RectNames[seznamRect.index(rect)]][0]
					hitrosti[RectNames[i]][0] *= -1
				else:
					hitrosti[RectNames[seznamRect.index(rect)]][1] -= hitrosti[RectNames[seznamRect.index(rect)]][1]
					hitrosti[RectNames[i]][1] -= hitrosti[RectNames[i]][1]


	for i, rect in enumerate(seznamRect):
		if i != 3:
			if kvadrat4.colliderect(rect):
				barveNew[3,0] = random.choice(barve[i])
				barveNew[3,1] = random.choice(barve[i])
				barveNew[3,2] = random.choice(barve[i])
				for x in barveNew[3]:
					if x > 230:
						x -= 10
					elif x < 20:
						x += 10
					elif x < 230 and x > 20:
						x += 20


				if abs(rect.x - seznamRect[i].x) > abs(rect.y - seznamRect[i].y):
					hitrosti[RectNames[seznamRect.index(rect)]][0] -= hitrosti[RectNames[seznamRect.index(rect)]][0]
					hitrosti[RectNames[i]][0] -= hitrosti[RectNames[i]][0]
				else:
					hitrosti[RectNames[seznamRect.index(rect)]][1] -= hitrosti[RectNames[seznamRect.index(rect)]][1]
					hitrosti[RectNames[i]][1] -= hitrosti[RectNames[i]][1]
	"""
	if kvadrat1.colliderect(kvadrat2):
		faktor1 *= -1
		faktor2 *= -1
		barvaNew1[0] = random.choice(barva2)
		barvaNew1[1] = random.choice(barva2)
		barvaNew1[2] = random.choice(barva2)
		for i in barvaNew1:
			if i > 230:
				i -= 10
			elif i < 20:
				i += 10
			elif i < 230 and i > 20:
				i += 20

		barvaNew2[0] = random.choice(barva1)
		barvaNew2[1] = random.choice(barva1)
		barvaNew2[2] = random.choice(barva1)
		for i in barvaNew2:
			if i > 230:
				i -= 10
			elif i < 20:
				i += 10
			elif i < 230 and i > 20:
				i += 20




	"""


	screen.fill(bg)
	#pygame.draw.rect(screen, tuple(barvaNew1), kvadrat1)

	pygame.draw.rect(screen, tuple(barveNew[0]), kvadrat1)
	pygame.draw.rect(screen, tuple(barveNew[1]), kvadrat2)
	pygame.draw.rect(screen, tuple(barveNew[2]), kvadrat3)
	pygame.draw.rect(screen, tuple(barveNew[3]), kvadrat4)
	
	pygame.display.flip()
