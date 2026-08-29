
def Frame():
    import cv2
    cam = cv2.VideoCapture("https://192.168.88.112:8080/video")
    print("Camera Connected!")
    imagecount=1
    while True:
        frame = cam.read()[1]
        # faceframe=frame[100:380 , 200:460]
        # scalepercent=20
        # shrunkheight=int(faceframe.shape[0]*(scalepercent/100))
        # shrunkwidth=int(faceframe.shape[1]*(scalepercent/100))
        # print(shrunkheight,shrunkwidth)
        # shrunkframe=cv2.resize(faceframe,(shrunkwidth,shrunkheight))
        # # print(shrunkframe.shape)
        # finalframe=frame
        # finalframe[0:shrunkheight,0:shrunkwidth] = shrunkframe
        cv2.imshow("Image",frame)
        if cv2.waitKey(1) == 13:
            break
        elif cv2.waitKey(1) == ord("q"):
            cv2.imwrite("Image{}.png".format(imagecount),frame)
            imagecount+=1
    cv2.destroyAllWindows()
    cam.release()




def NewFrame(name):
    import cv2
    cam = cv2.VideoCapture(0)
    imagecount=1
    while True:
        frame = cam.read()[1]
        faceframe=frame[100:380 , 200:460]
        grayFaceFrame = cv2.cvtColor(faceframe, cv2.COLOR_BGR2GRAY)
        textGrayFaceFrame = cv2.putText(grayFaceFrame, name, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255) , 2)
        # scalepercent=20
        # shrunkheight=int(faceframe.shape[0]*(scalepercent/100))
        # shrunkwidth=int(faceframe.shape[1]*(scalepercent/100))
        # print(shrunkheight,shrunkwidth)
        # shrunkframe=cv2.resize(faceframe,(shrunkwidth,shrunkheight))
        # print(shrunkframe.shape)
        # finalframe=frame
        # finalframe[0:shrunkheight,0:shrunkwidth] = shrunkframe
        cv2.imshow("Image",textGrayFaceFrame)
        if cv2.waitKey(1) == 13:
            break
        elif cv2.waitKey(1) == ord("q"):
            cv2.imwrite("Image{}.png".format(imagecount),textGrayFaceFrame)
            imagecount+=1
    cv2.destroyAllWindows()
    cam.release()
