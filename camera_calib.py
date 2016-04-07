import numpy as np
import cv2
import glob

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = cv2.VideoCapture(0)

for i in range(1):
    ret_val, img = images.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (7,7),None)
    

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        cv2.drawChessboardCorners(img, (7,7), corners2,ret)
        cv2.imshow('img',img)
        
        angle = 35
        image_center = tuple(np.array(img.shape)/2)
        rot_mat = cv2.getRotationMatrix2D((image_center[0], image_center[1]),angle, 1.0)
        result = cv2.warpAffine(img, rot_mat, (img.shape[0], img.shape[1]),flags=cv2.INTER_LINEAR)
        cv2.imshow('result', result)


        cv2.waitKey(1000)

cv2.destroyAllWindows()