import cv2
import numpy as np
from enum import Enum
from time import sleep

  
squaresize = 41

class square:
  
  def __init__(self,letter,number):
    self.size = squaresize
    self.piece = '.'
    self.x = (ord(letter)-64)*(squaresize+2) 
    self.y = (number+1)*(squaresize+2)      
        



def take_picture(mirror=False):
  cam = cv2.VideoCapture(0)
  while True:
		ret_val, img = cam.read()
		img = rotate_image(img, 0)

		img = img[:,0:(squaresize+2)*11] 
		
		if mirror: 
			img = cv2.flip(img, 1)
		
		output = img.copy()


		img = cv2.medianBlur(img,9)
		
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		cv2.imshow('img', img)
		
		circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1, 20, param1=20, param2=25, minRadius=15, maxRadius=(squaresize+6)/2)
		
		text = "Circles: 0"
		
		######### DEFINE GRID
		grid = [[0 for i in range(10)] for i in range(10)]
				
		for letter in ('ABCDEFGHIJ'):
		  for num in range(10):
		    grid[ord(letter)-65][num]=square(letter,num)		
	
		if circles is not None:
		        
			# convert the (x, y) coordinates and radius of the circles to integers
			circles = np.round(circles[0, :]).astype("int")	
			text = "Circles: %d" % (len(circles))
			
			for (x, y, r) in circles:
					# draw the circle in the output image, then draw a rectangle
					# corresponding to the center of the circle
					cv2.circle(output, (x, y), r, (0, 255, 0), 4)	
					cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
					for x in range(15):
					  for letter in ('ABCDEFGHIJ'):
					    for num in range(10):
					      for i in range(len(circles)):					
							if(grid[ord(letter)-65][num].x  - squaresize/2 <= circles[i,0] <= grid[ord(letter)-65][num].x + squaresize/2):
							  if(grid[ord(letter)-65][num].y  - squaresize/2 <= circles[i,1] <= grid[ord(letter)-65][num].y + squaresize/2):
							    grid[ord(letter)-65][num].piece = 'x'
							    #print(grid[ord(letter)-65][num].x, grid[ord(letter)-65][num].y)
							    #print(circles[i])
							    c = output[circles[i,0],circles[i,1]]
							    print " --- color ---"
							    print(c)
					  
		font = cv2.FONT_HERSHEY_SIMPLEX	
		cv2.putText(img, text, (100,100), font, 2, 255)
		cv2.putText(output, text, (100,100), font, 2, 255)
	      
		
		board = np.chararray([10,10])
		
		
		for num in range(10):
		  for letter in ('ABCDEFGHIJ'):
		    board[num,ord(letter)-65] = grid[ord(letter)-65][num].piece
		    print grid[ord(letter)-65][num].piece,
		  print
		  
		    
		#print(board)
		
		#board.tofile('board.txt')
		np.savetxt('board.txt', board, delimiter=" ", fmt ="%s")

		# boardfile = open('board.txt', 'w')
		# boardfile.write(board)

		     
		#if circles is not None:
		 # print(circles)
		 
		print('-------------------')
		
		  
		drawgrid(grid, output)
		
		#gridlines(output)
		
		
		#cv2.imshow('my webcam', img)
		cv2.imshow('output', output)
		cv2.imwrite( "output.jpg", output );
		
		if cv2.waitKey(1) == 27: 
			break  # esc to quit
		
		
		cv2.destroyAllWindows()
		return board
  cv2.destroyAllWindows()
  
def rotate_image(img, angle):
	if angle == 0:
		return img
	image_center = tuple(np.array(img.shape)/2)
	rot_mat = cv2.getRotationMatrix2D((image_center[0], image_center[1]),angle, 1.0)
	result = cv2.warpAffine(img, rot_mat, (img.shape[0], img.shape[1]),flags=cv2.INTER_LINEAR)
	return result

def drawgrid(grid,image):
  
  for letter in ('ABCDEFGHIJ'):
    for num in range(10):
      pt1 = (grid[ord(letter)-65][num].x - squaresize/2, grid[ord(letter)-65][num].y - squaresize/2)
      pt2 = (grid[ord(letter)-65][num].x + squaresize/2, grid[ord(letter)-65][num].y + squaresize/2)
      color = (255,255,255)
      if(grid[ord(letter)-65][num].piece == 'x'):
	color = (255,0,0)
      myRectangle(image,pt1,pt2,color)
  

def gridlines(image):
  height, width = image.shape[:2]
  offset = 100
  cols = 8
  rows = 8
 
  for i in range(1,cols+2):
    x = (i-1)*(width/2)/cols + offset
    pt1 = (x,offset)
    pt2 = (x,height/2+offset)
    myline(image, pt1, pt2)
    
  for j in range(1,rows+2):
      y = (j-1)*height/2/rows + offset
      pt1 = (0+offset,y)
      pt2 = (width/2+offset,y)
      myline(image, pt1, pt2)  

def myline(image, start, end):
  thickness = 2
  lineType = 8
  cv2.line(image, start, end, (255,255,255) , thickness, lineType)

def myRectangle(image,pt1,pt2,color):
  thickness = 2
  lineType = 8
  cv2.rectangle(image,pt1,pt2, color, thickness, lineType)


def main():
	board = take_picture(mirror=False)
	return board

if __name__ == '__main__':
	main()