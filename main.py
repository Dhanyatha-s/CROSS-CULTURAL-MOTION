import cv2
import mediapipe as mp

#initialize mediapipe
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils


# input vedio frame
cap = cv2.VideoCapture("test.mp4")