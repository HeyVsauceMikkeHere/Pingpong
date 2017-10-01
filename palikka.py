import pygame
import random
# initialize game engine
pygame.init()
pygame.font.init()
# set screen width/height and caption
HEIGHT = 480
WIDTH = 640
size = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space Invaders')
# initialize clock. used later in the loop.
clock = pygame.time.Clock()
font = pygame.font.SysFont('Helvetica', 30)

#COLORS
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)

#Global variables
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 70
MARGIN = 20
START_X = WIDTH - PLAYER_WIDTH / 2
START_Y = HEIGHT - PLAYER_HEIGHT - MARGIN
PLAYER_SPEED = 0.5

BALL_WIDTH = 10
BALL_HEIGHT = 10
BALL_SPEED = 2

game_over = False
playerShip = None
playerShip2 = None
Ball = None
hit = False



class Ball():
	def __init__(self, x, y, screen, width, height, speed):
		self.x = x
		self.y = y
		self.screen = screen
		self.width = width
		self.height = height
		self.speed = speed

	def update(self, dt):
		global playerShip, playerShip2
		if self.x + self.width >= playerShip.x and self.y < playerShip.y + playerShip.height and self.y > playerShip.y:
			self.speed = -self.speed

		if self.y < 0:
			self.y = 0
		if self.y > 410:
			self.y = 410
		elif self.y > WIDTH - self.width:
			self.y = WIDTH - self.width

		self.x = self.x + self.speed


	def draw(self, x, y):
		rect = (self.x - 20, self.y, self.width, self.height)
		pygame.draw.rect(screen, RED, rect, 0)


class Ship():
	def __init__(self, x, y, screen, width, height):
		self.x = x
		self.y = y
		self.screen = screen
		self.width = width
		self.height = height

		self.goingUp = False
		self.goingDown = False


	def update(self, dt):
		v = PLAYER_SPEED
		if self.goingUp:
			self.y = self.y - v * dt
		elif self.goingDown:
			self.y = self.y + v * dt

		if self.y < 0:
			self.y = 0
		if self.y > 410:
			self.y = 410
		elif self.y > WIDTH - self.width:
			self.y = WIDTH - self.width
			

	def draw(self):
		rect = (self.x - 15, self.y, self.width, self.height)
		pygame.draw.rect(screen, WHITE, rect, 0)


def restartGame():
	global level, score, game_over
	level = 1
	score = 0
	game_over = False
	startLevel()

def startLevel():
	global playerShip, playerShip2, ball, enemies, level, defences
	playerShip = Ship(START_X, START_Y, screen, PLAYER_WIDTH, PLAYER_HEIGHT)
	playerShip2 = Ship(20, 20, screen, PLAYER_WIDTH, PLAYER_HEIGHT)
	ball = Ball(320, 240, screen, BALL_WIDTH, BALL_HEIGHT, 1)
	i = 0
	j = 0


# Loop until the user clicks close button
done = False
# Start the game for the first time
restartGame()

while done == False:
	dt = clock.tick(60)
	restart = False

	# write event handlers here
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				playerShip.goingUp = True
			if event.key == pygame.K_DOWN:
				playerShip.goingDown = True
			if event.key == pygame.K_RETURN:
				restart = True
			if event.key == pygame.K_w:
				playerShip2.goingUp = True
			if event.key == pygame.K_s:
				playerShip2.goingDown = True
			if event.key == pygame.K_RETURN:
				restart = True


		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				playerShip.goingUp = False
			if event.key == pygame.K_DOWN:
				playerShip.goingDown = False
			if event.key == pygame.K_w:
				playerShip2.goingUp = False
			if event.key == pygame.K_s:
				playerShip2.goingDown = False


	# write game logic here
	playerShip.update(dt)
	playerShip2.update(dt)
	ball.update(dt)
	
	if game_over:
		if restart:
			restartGame()
		else:
			gameOverString = 'Game over! Score: ' + str(score)
			textsurface = font.render(gameOverString, True, (255, 255, 255))
			screen.blit(textsurface,(WIDTH / 2 - 100, HEIGHT / 2))

			gameOverString2 = 'Press Enter to continue'
			textsurface2 = font.render(gameOverString2, True, (255, 255, 255))
			screen.blit(textsurface2,(WIDTH / 2 - 100, HEIGHT / 2 + 50))

			pygame.display.update()
			continue

	# write draw code here
	# clear the screen before drawing
	screen.fill((0, 0, 0)) 


	playerShip.draw()

	playerShip2.draw()

	ball.draw(ball.x, ball.y)

	# display what’s drawn. this might change.
	pygame.display.update()
	# run at 20 fps

# close the window and quit
pygame.quit()
exit()
