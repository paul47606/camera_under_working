import cv2
#import VideoCapture

video_cap = cv2.VideoCapture(0)
while True:
    ret, video_data  = video_cap.read()
    cv2.imshow("Video_Live", video_data)
    if cv2.waitKey(10) == ord("a"):
        break
video_cap.release()
