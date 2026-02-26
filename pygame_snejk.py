#Napiši snake-game v pygamu
#koda od prej ti lahko sliži za inspiracijo (npr dolzina kace s kvadratki -> to pride prav)

#za projekt naredite github repo, in spremembe sproti comitatje addajte in pushajte
#na koncu morajo biti v repozitoriju vsaj 3 vecji commiti

#1. dodatna naloga:
#naredi branch "izgled"
#v tem brancu naredi logiko, da ko igra tece, lahko pritisnes gumb "space" kar celotni kaci nastavi nakljucno barvo

#2. dodatna naloga:
#naredi branch "multiplayer"
#v tem branchu naredi logiko, da sta na zacetku igre 2 kaci, ena se upravlja z wasd, druga z gumbi s puscicami
#ce se aca zabije vase, v drugo kaco ali v steno, izgubi

#3. dodatna naloga
#naredi megre obeh branchov 



import pygame
import copy
import time
import random

class Kaca:
	def __init__(self):
		self.smer = "gor"
		self.zivljenje = True
		self.pozicije=[[914, 804], [912, 804], [910, 804], [908, 804], [906, 804], [904, 804], [902, 804], [900, 804], [898, 804], [896, 804], [894, 804]]
	def sprememba_smeri(self, pritisk):
		smeri = ["gor", "levo", "dol", "desno"]
		if pritisk == "a":
			self.smer = "levo"
		elif pritisk == "d":
			self.smer = "desno"
		elif pritisk == "w":
			self.smer = "gor"
		elif pritisk == "s":
			self.smer = "dol"



		

	def premik(self, podaljsevanje=False):
		potem = copy.deepcopy(self.pozicije)

		if self.smer == "levo":
				potem[0][0] -= 2

		elif self.smer == "desno":
				potem[0][0] += 2


		elif self.smer == "gor":
				potem[0][1] -= 2

		elif self.smer == "dol":
				potem[0][1] += 2

		for i in range(1, len(potem)):
			potem[i] = self.pozicije[i-1]


		self.pozicije = potem



	def podaljsevanje(self):
		for x in range(5):
			potem = copy.deepcopy(self.pozicije)
			if self.smer == "levo":
					potem[0][0] -= 2

			elif self.smer == "desno":
					potem[0][0] += 2


			elif self.smer == "gor":
					potem[0][1] -= 2

			elif self.smer == "dol":
					potem[0][1] += 2

			for i in range(1, len(potem)):
				potem[i] = self.pozicije[i-1]
				
			potem.append(self.pozicije[-1])


			if self.smer == "levo":
				potem.append([self.pozicije[-1][0]+2, self.pozicije[-1][1]])

			elif self.smer == "desno":
				potem.append([self.pozicije[-1][0]-2, self.pozicije[-1][1]])


			elif self.smer == "gor":
				potem.append([self.pozicije[-1][0], self.pozicije[-1][1]+2])


			elif self.smer == "dol":
				potem.append([self.pozicije[-1][0], self.pozicije[-1][1]-2])

			self.pozicije = potem


class Polje(Kaca):
	def __init__(self):
		super().__init__()
		self.rezultat = 0
		self.hrana = [350, 450]
		self.znotraj = True
		self.igra = True





	def znotraj_check(self):
		if self.pozicije[0][0] < 10 or self.pozicije[0][1] < 10 or self.pozicije[0][0] > 1990 or self.pozicije[0][1] > 1190:  #PAZI SIRINE RECTOV!!!
			self.znotraj = False
			print("Šu si vn")
		for x in self.pozicije:
			if self.pozicije.count(x) > 1:  # pazi 10
				self.znotraj = False
				print("Pojedu si se")
				break



	def nova_hrana(self):
		snake = self.pozicije

		possible = [
			[x, y]
			for x in range(100, 1900)
			for y in range(100, 1000)
			if [x, y] not in snake
		]

		self.hrana = random.choice(possible)



	def igranje(self):
		while self.znotraj and self.igra:
			clock.tick(120)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.igra = False


				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_w:
						self.sprememba_smeri("w")

					if event.key == pygame.K_s:
						self.sprememba_smeri("s")

					if event.key == pygame.K_a:
						self.sprememba_smeri("a")

					if event.key == pygame.K_d:
						self.sprememba_smeri("d")


					if event.key == pygame.K_UP:
						self.sprememba_smeri("w")

					if event.key == pygame.K_DOWN:
						self.sprememba_smeri("s")

					if event.key == pygame.K_LEFT:
						self.sprememba_smeri("a")

					if event.key == pygame.K_RIGHT:
						self.sprememba_smeri("d")

			screen.fill(bg)

			pygame.draw.circle(screen, (0, 255, 0), (self.hrana[0], self.hrana[1]), 5)
			# rectangle size

			x = self.pozicije[0][0]
			y = self.pozicije[0][1]

			if self.smer == "levo":
			    head_center = (x, y+10)
			elif self.smer == "desno":
			    head_center = (x+20, y+10)
			elif self.smer == "gor":
			    head_center = (x+10, y)
			elif self.smer == "dol":
			    head_center = (x+10, y+20)

			if abs(head_center[0]-self.hrana[0]) <= 12 and abs(head_center[1]-self.hrana[1]) <= 12 :
				self.podaljsevanje()
				self.nova_hrana()
			else:
				self.premik()
			for i in self.pozicije:
				x = i[0]
				y = i[1]
				try: 
					if self.pozicije.index(i) == 0:
						if self.smer == "levo":
							pygame.draw.circle(screen, (0,225,255), (x,y+10), 10)  #SMER POMEMBNA
						elif self.smer == "desno":
							pygame.draw.circle(screen, (0,225,255), (x+20,y+10), 10)  #SMER POMEMBNA
						elif self.smer == "gor":
							pygame.draw.circle(screen, (0,225,255), (x+10,y), 10)  #SMER POMEMBNA

						elif self.smer == "dol":
							pygame.draw.circle(screen, (0,225,255), (x+10,y+20), 10)  #SMER POMEMBNA

					else:
						pygame.draw.rect(screen, (0,225,255), (x,y,20,20))
				except Exception as e:
					self.znotraj = False

			dolzina = str(len(self.pozicije)//10)

			screen.blit(font.render(f"score: {dolzina}",True,(255,0,0)),(1810,40))

			self.znotraj_check()

			
			pygame.display.flip()











pygame.init()

screen = pygame.display.set_mode((2000, 1200))
pygame.display.set_caption("Pygame")
bg = (0,0,0)
igra = True
font=pygame.font.Font(None,50)


clock = pygame.time.Clock()



igralna_plosca = Polje()
kaca = Kaca()


igralna_plosca.igranje()






