#! /usr/bin/python3

import cv2
import numpy as np
from networktables import NetworkTables
from cscore import CameraServer, UsbCamera
from time import sleep
import logging

RIO = 'roborio-1289-frc.local'
FIELD_OF_VIEW = 58.0 # degrees per logitech C170 tech specs

def main(table):
    cs = CameraServer.getInstance()
    cs.enableLogging()
    
    cam = cs.startAutomaticCapture()
    
    cam.setResolution(640, 480)
    
    # Get a CvSink. This will capture images from the camera
    cvSink = cs.getVideo(camera=cam)
    
    # (optional) Setup a CvSource. This will send images back to the Dashboard
    #outputStream = cs.putVideo("Rectangle", 640, 480)
    
    # Allocating new images is very expensive, always try to preallocate
    img = np.zeros(shape=(480, 640, 3), dtype=np.uint8)    

    while True:
        # Tell the CvSink to grab a frame from the camera and put it
        # in the source image.  If there is an error notify the output.
        print('grab a frame...')
        time, img = cvSink.grabFrame(img,0.5)
        if time == 0:
            # Send the output the error.
            print(cvSink.getError())
            #outputStream.notifyError(cvSink.getError())
            # skip the rest of the current iteration
            continue
        
        # Put a rectangle on the image
        #cv2.rectangle(img, (100, 100), (400, 400), (255, 255, 255), 5)
        #print('raw img', img)
        # Convert RGB to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        print('hsv img', hsv)
        # define range of blue color in HSV
        lower_blue = np.array([80, 50, 50])
        upper_blue = np.array([100,255,255])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        print('mask', mask)

        contours, hierarchy, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        print('contours ', contours)
        target = contours[0]
        for c in contours:
            if cv2.contourArea(c) > cv2.contourArea(target):
                target = c

        m = cv2.moments(target)
        cx = int(m['m10'] / m['m00'])
        cy = int(m['m01'] / m['m00'])

        angle = (cx / 320.0) * (FIELD_OF_VIEW / 2)
        print(angle)

        
        # Give the output stream a new image to display
        #print('put frame')
        #outputStream.putFrame(img)    


# def main(table):
    # while True:
        # cam = cv2.VideoCapture(0)
        # cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        # cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        # cam.set(cv2.CAP_PROP_MODE, cv2.CAP_MODE_YUYV)

        # ret, frame = cam.read()    # frame is the image
        # if ret is False:
            # continue

        # # Convert RGB to HSV
        # hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)


        # # define range of blue color in HSV
        # lower_blue = np.array([110,50,50])
        # upper_blue = np.array([130,255,255])

        # # Threshold the HSV image to get only blue colors
        # mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # contours, hierarchy, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # target = contours[0]
        # # print(target)
        # # for c in contours:
            # # print(c)
            # # if cv2.contourArea(c) > cv2.contourArea(target):
                # # target = c

        # m = cv2.moments(target)
        # cx = int(m['m10'] / m['m00'])
        # cy = int(m['m01'] / m['m00'])

        # angle = (cx / 320.0) * (FIELD_OF_VIEW / 2)
        # print(angle)

        # # add center? area?
       # # PutValue(table, 'angle', angle)
        
        # sleep(0.1)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    NetworkTables.initialize(server=RIO)
    sleep(5)
    main(NetworkTables.getTable('SmartDashboard'))
