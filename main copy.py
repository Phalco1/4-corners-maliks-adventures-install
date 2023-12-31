import pygame, sys
from settings import *
from level import Level
import asyncio


class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption("4 Corners: Malik's Adventures")
		self.clock = pygame.time.Clock()

		self.level = Level()
	
		#sound
		main_sound = pygame.mixer.Sound('/Users/learnacademy/Desktop/4-Cornerz-4/audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)

	async	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)
			await asyncio.sleep(0)

if __name__ == '__main__':
	game = Game()
	asyncio.run(game.run())