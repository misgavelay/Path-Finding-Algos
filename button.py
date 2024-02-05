import pygame
import sys
import colors

# initialize pygame
pygame.init()


main_font = pygame.font.SysFont("poppins", 23)


# Surface - pygame object to represent images
# Rect - by game object to work with rectangle areas
# Transform - module to transform surfaces

class Button:

	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		# pygame uses rect to store and manipulate rectangle ares
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		# define the rect of the button to be the same rect as the image we loaded to it
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		# create a rect for the text
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	# Draw the button on the screen
	def update(self,screen):
		screen.blit(self.image,self.rect)  # blit draws an image (the image, position(can be a pair of coordinates or a rect))
		screen.blit(self.text, self.text_rect)

	# Check if button is pressed, this function is called only if event.MOUSEBUTTONDOWN happens
	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True

	# Change color while hovering over button, this function runs in a constant loop
	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom) :
			self.text = main_font.render(self.text_input, True, colors.LIGHT_GRAY)
		else:
			self.text = main_font.render(self.text_input, True, colors.WHITE)





