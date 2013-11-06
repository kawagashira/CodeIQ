#!/usr/bin/python
#
#								dragon.py
#

from PIL import Image, ImageDraw
from math import cos, sin, pi, sqrt

class Turtle:

	def __init__(self, width=1200, height=800):

		#mode = "1"		# Black and White
		mode = "RGB"		# Black and White
		#width, height = 1200, 800
		bg = "#ffffff"
		self.window = Image.new(mode, (width,height), bg)
		self.dr = ImageDraw.Draw(self.window)
	
	def set_initial_point(self, x, y):

		self.x0, self.y0 = x, y

	def plot_line(self, length, theta):

		x1, y1 = self.x0 + length*cos(theta), self.y0 + length*sin(theta)
		#print self.x0, self.y0, x1, y1, theta
		self.dr.line((self.x0, self.y0, x1, y1), (0,0,255))
		self.x0, self.y0 = x1, y1

	def save(self, o_file, form="PNG"):

		self.window.show()
		self.window.save(o_file, form)

	def ccurve(self, length, theta):

		if length <= 4:
			self.plot_line(length, theta)
		else:
			self.ccurve(length/sqrt(2), theta + pi/4)
			self.ccurve(length/sqrt(2), theta - pi/4)

	def dragon(self, length, theta, flip):

		if length <= 5:
			print length, theta, flip
			self.plot_line(length, theta)
		else:
			self.dragon(length/sqrt(2), theta + flip*pi/4, 1)
			self.dragon(length/sqrt(2), theta - flip*pi/4, -1)

if __name__ == '__main__':

	d = Turtle(1200, 800)
	d.set_initial_point(400, 300)	# C-CURVE
	#d.set_initial_point(300, 300)	# C-CURVE
	d.ccurve(400, 0)
	d.save("ccurve.png")	

	'''
	d = Turtle(1200, 800)
	d.set_initial_point(300, 300)	# DRAGON CURVE
	d.dragon(600, 0, +1)
	d.save("dragon.png")	
	'''
