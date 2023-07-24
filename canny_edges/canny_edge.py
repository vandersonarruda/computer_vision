import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True, help="Video path to input")
args = vars(parser.parse_args())

cap = cv2.VideoCapture(args["file"])

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = cap.get(cv2.CAP_PROP_FPS)

# Codec for VideoWrite
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # codec 'mp4v'
out = cv2.VideoWriter('output.mp4', fourcc, fps,
                      (frame_width, frame_height)) # to save in .mp4

while (cap.isOpened()):
    result, frame = cap.read()
    if result == True:

        # convert to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect edges
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)
        edges_bgr  =cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        out.write(edges_bgr)

        cv2.imshow('edges', edges)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
