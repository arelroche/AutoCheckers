import cv2
import numpy as np




def show_webcam(mirror=False):
  cam = cv2.VideoCapture(0)
  while True:
		ret_val, img = cam.read()
		
		if mirror: 
			img = cv2.flip(img, 1)
		
		output = img.copy()
		
		img = cv2.medianBlur(img,5)
		
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		
		circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1, 20, param1=75, param2=65, minRadius=0, maxRadius=0)
		
		text = "Circles: 0"
	
		if circles is not None:
		        
			# convert the (x, y) coordinates and radius of the circles to integers
			circles = np.round(circles[0, :]).astype("int")	
			text = "Circles: %d" % (len(circles))
			
			for (x, y, r) in circles:
					# draw the circle in the output image, then draw a rectangle
					# corresponding to the center of the circle
					cv2.circle(output, (x, y), r, (0, 255, 0), 4)	
					cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
					
			
		
		
		font = cv2.FONT_HERSHEY_SIMPLEX	
		cv2.putText(img, text, (100,100), font, 2, 255)
		cv2.putText(output, text, (100,100), font, 2, 255)
		
		grid(output)
		
		
		#cv2.imshow('my webcam', img)
		cv2.imshow('output', output)
		
		if cv2.waitKey(1) == 27: 
			break  # esc to quit
  cv2.destroyAllWindows()

def grid(image):
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


def main():
	show_webcam(mirror=True)

if __name__ == '__main__':
	main()