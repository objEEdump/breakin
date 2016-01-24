#!/usr/bin/env python

from PIL import Image

pic = Image.open("color.png")
data = pic.load()

red = (255, 0, 0)

# We create an array to hold all the lines and start to loop through 
# each pixel
binary_lines = []
width, height = pic.size
for y in xrange( height ):
	binary_line = []
	for x in xrange( width ):

		pixel = data[x, y]

		# We only have the two colors red and black, so I just test 
		#for one case and then use `else`.
		if pixel == red:
			binary_line.append( '1' )
		else:
			binary_line.append( '0' )

	binary_lines.append( binary_line )

# A little 'list comprehension' magic to get the good stuff out...
ascii_text = ''.join([ chr(int(''.join(separated),2)) 
					for separated in binary_lines ])
print ascii_text