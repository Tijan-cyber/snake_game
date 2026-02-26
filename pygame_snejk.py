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
		self.smer1 = "gor"
		self.smer2 = "gor"
		self.zivljenje1 = True
		self.zivljenje2 = True
		self.pozicije1=[[914, 804], [912, 804], [910, 804], [908, 804], [906, 804], [904, 804], [902, 804], [900, 804], [898, 804], [896, 804], [894, 804]]
		self.pozicije2=[[614, 504], [612, 504], [610, 504], [608, 504], [606, 504], [604, 504], [602, 504], [600, 504], [598, 504], [596, 504], [594, 504]]
		
	def sprememba_smeri_wasd(self, pritisk):
		smeri = ["gor", "levo", "dol", "desno"]
		if pritisk == "a":
			self.smer1 = "levo"
		elif pritisk == "d":
			self.smer1 = "desno"
		elif pritisk == "w":
			self.smer1 = "gor"
		elif pritisk == "s":
			self.smer1 = "dol"



	def sprememba_smeri_puscice(self, pritisk):
		smeri = ["gor", "levo", "dol", "desno"]
		if pritisk == "a":
			self.smer2 = "levo"
		elif pritisk == "d":
			self.smer2 = "desno"
		elif pritisk == "w":
			self.smer2 = "gor"
		elif pritisk == "s":
			self.smer2 = "dol"


	def premik(self, igralec, podaljsevanje=False):
		if igralec == 1:
			potem = copy.deepcopy(self.pozicije1)
			if self.smer1 == "levo":
					potem[0][0] -= 2

			elif self.smer1 == "desno":
					potem[0][0] += 2


			elif self.smer1 == "gor":
					potem[0][1] -= 2

			elif self.smer1 == "dol":
					potem[0][1] += 2

			for i in range(1, len(potem)):
				potem[i] = self.pozicije1[i-1]


			self.pozicije1 = potem


		else:
			potem = copy.deepcopy(self.pozicije2)
			if self.smer2 == "levo":
					potem[0][0] -= 2

			elif self.smer2 == "desno":
					potem[0][0] += 2


			elif self.smer2 == "gor":
					potem[0][1] -= 2

			elif self.smer2 == "dol":
					potem[0][1] += 2

			for i in range(1, len(potem)):
				potem[i] = self.pozicije2[i-1]


			self.pozicije2 = potem


	def podaljsevanje(self, igralec):
		if igralec == 1:
			for x in range(5):
				potem = copy.deepcopy(self.pozicije1)
				if self.smer1 == "levo":
						potem[0][0] -= 2

				elif self.smer1 == "desno":
						potem[0][0] += 2


				elif self.smer1 == "gor":
						potem[0][1] -= 2

				elif self.smer1 == "dol":
						potem[0][1] += 2

				for i in range(1, len(potem)):
					potem[i] = self.pozicije1[i-1]
					
				potem.append(self.pozicije1[-1])


				if self.smer1 == "levo":
					potem.append([self.pozicije1[-1][0]+2, self.pozicije1[-1][1]])

				elif self.smer1 == "desno":
					potem.append([self.pozicije1[-1][0]-2, self.pozicije1[-1][1]])


				elif self.smer1 == "gor":
					potem.append([self.pozicije1[-1][0], self.pozicije1[-1][1]+2])


				elif self.smer1 == "dol":
					potem.append([self.pozicije1[-1][0], self.pozicije1[-1][1]-2])

				self.pozicije1 = potem


		else: 
			for x in range(5):
				potem = copy.deepcopy(self.pozicije2)
				if self.smer2 == "levo":
						potem[0][0] -= 2

				elif self.smer2 == "desno":
						potem[0][0] += 2


				elif self.smer2 == "gor":
						potem[0][1] -= 2

				elif self.smer2 == "dol":
						potem[0][1] += 2

				for i in range(1, len(potem)):
					potem[i] = self.pozicije2[i-1]
					
				potem.append(self.pozicije2[-1])


				if self.smer2 == "levo":
					potem.append([self.pozicije2[-1][0]+2, self.pozicije2[-1][1]])

				elif self.smer2 == "desno":
					potem.append([self.pozicije2[-1][0]-2, self.pozicije2[-1][1]])


				elif self.smer2 == "gor":
					potem.append([self.pozicije2[-1][0], self.pozicije2[-1][1]+2])


				elif self.smer2 == "dol":
					potem.append([self.pozicije2[-1][0], self.pozicije2[-1][1]-2])

				self.pozicije2 = potem



class Polje(Kaca):
	def __init__(self):
		super().__init__()
		self.hrana = [350, 450]
		self.znotraj1 = True
		self.znotraj2 = True
		self.igra = True





	def znotraj_check(self, head_center1, head_center2):
		if self.pozicije1[0][0] < 10 or self.pozicije1[0][1] < 10 or self.pozicije1[0][0] > 1990 or self.pozicije1[0][1] > 1190:  #PAZI SIRINE RECTOV!!!
			self.znotraj1 = False
		for x in self.pozicije1:
			if self.pozicije1.count(x) > 1:  # pazi 10
				self.znotraj1 = False
			

		if self.pozicije2[0][0] < 10 or self.pozicije2[0][1] < 10 or self.pozicije2[0][0] > 1990 or self.pozicije2[0][1] > 1190:  #PAZI SIRINE RECTOV!!!
			self.znotraj2 = False
		for x in self.pozicije2:
			if self.pozicije2.count(x) > 1:  # pazi 10
				self.znotraj2 = False
				

		for i in self.pozicije1:
			for y in self.pozicije2:
				if abs(i[0]-y[0]) <= 10 and abs(i[1]-y[1]) <= 10:
					print("trk")
					self.igra = False



	def nova_hrana(self):
		snake1 = self.pozicije1
		snake2 = self.pozicije2

		possible = [
			[x, y]
			for x in range(100, 1900)
			for y in range(100, 1000)
			if [x, y] not in snake1 or snake2
		]

		self.hrana = random.choice(possible)



	def igranje(self):
		while (self.znotraj1 or self.znotraj2) and self.igra:
			clock.tick(120)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.igra = False


				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_w:
						self.sprememba_smeri_wasd("w")

					if event.key == pygame.K_s:
						self.sprememba_smeri_wasd("s")

					if event.key == pygame.K_a:
						self.sprememba_smeri_wasd("a")

					if event.key == pygame.K_d:
						self.sprememba_smeri_wasd("d")


					if event.key == pygame.K_UP:
						self.sprememba_smeri_puscice("w")

					if event.key == pygame.K_DOWN:
						self.sprememba_smeri_puscice("s")

					if event.key == pygame.K_LEFT:
						self.sprememba_smeri_puscice("a")

					if event.key == pygame.K_RIGHT:
						self.sprememba_smeri_puscice("d")

			screen.fill(bg)

			pygame.draw.circle(screen, (0, 255, 0), (self.hrana[0], self.hrana[1]), 5)

			xp = self.pozicije1[0][0]
			yp = self.pozicije1[0][1]
			xd = self.pozicije2[0][0]
			yd = self.pozicije2[0][1]

			if self.smer1 == "levo":
			    head_center1 = (xp, yp+10)
			elif self.smer1 == "desno":
			    head_center1 = (xp+20, yp+10)
			elif self.smer1 == "gor":
			    head_center1 = (xp+10, yp)
			elif self.smer1 == "dol":
			    head_center1 = (xp+10, yp+20)

			if self.smer2 == "levo":
			    head_center2 = (xd, yd+10)
			elif self.smer2 == "desno":
			    head_center2 = (xd+20, yd+10)
			elif self.smer2 == "gor":
			    head_center2 = (xd+10, yd)
			elif self.smer2 == "dol":
			    head_center2 = (xd+10, yd+20)



			if abs(head_center1[0]-self.hrana[0]) <= 12 and abs(head_center1[1]-self.hrana[1]) <= 12 :
				self.podaljsevanje(1)
				self.nova_hrana()



			if abs(head_center2[0]-self.hrana[0]) <= 12 and abs(head_center2[1]-self.hrana[1]) <= 12 :
				self.podaljsevanje(2)
				self.nova_hrana()



			self.premik(1)
			self.premik(2) #!!!!!!!!!!!!!!!!!!!


			for i in self.pozicije1:
				x = i[0]
				y = i[1]
				try: 
					if self.pozicije1.index(i) == 0:
						if self.smer1 == "levo":
							pygame.draw.circle(screen, (0,225,255), (x,y+10), 10)  #SMER POMEMBNA
						elif self.smer1 == "desno":
							pygame.draw.circle(screen, (0,225,255), (x+20,y+10), 10)  #SMER POMEMBNA
						elif self.smer1 == "gor":
							pygame.draw.circle(screen, (0,225,255), (x+10,y), 10)  #SMER POMEMBNA

						elif self.smer1 == "dol":
							pygame.draw.circle(screen, (0,225,255), (x+10,y+20), 10)  #SMER POMEMBNA

					else:
						pygame.draw.rect(screen, (0,225,255), (x,y,20,20))
				except Exception as e:
					self.znotraj1 = False

			for i in self.pozicije2:
				x = i[0]
				y = i[1]
				try: 
					if self.pozicije2.index(i) == 0:
						if self.smer2 == "levo":
							pygame.draw.circle(screen, (0,225,255), (x,y+10), 10)  #SMER POMEMBNA
						elif self.smer2 == "desno":
							pygame.draw.circle(screen, (0,225,255), (x+20,y+10), 10)  #SMER POMEMBNA
						elif self.smer2 == "gor":
							pygame.draw.circle(screen, (0,225,255), (x+10,y), 10)  #SMER POMEMBNA

						elif self.smer2 == "dol":
							pygame.draw.circle(screen, (0,225,255), (x+10,y+20), 10)  #SMER POMEMBNA

					else:
						pygame.draw.rect(screen, (0,225,255), (x,y,20,20))
				except Exception as e:
					self.znotraj2 = False


			dolzina1 = str(len(self.pozicije1)//10)
			dolzina2 = str(len(self.pozicije2)//10)

			screen.blit(font.render(f"score1: {dolzina1}",True,(255,0,0)),(1810,40))
			screen.blit(font.render(f"score2: {dolzina2}",True,(255,0,0)),(1810,80))


			self.znotraj_check(head_center1, head_center2)


			
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






