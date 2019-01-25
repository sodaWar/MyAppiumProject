# -* encoding:utf-8 *-
import cv2
import time
#该文件实时计算每秒的帧数

cap = cv2.VideoCapture("cider.mp4")
# cap = cv2.VideoCapture(0)                                                     #默认参数0为计算机摄像头

# Define the codec and create VideoWriter object
# fourcc = cv2.cv.FOURCC(*'XVID')                                               #该方式的创建是OpenCV版本号为3以上的创建方式
fourcc = cv2.VideoWriter_fourcc(*'XVID')                                        #该函数的参数是用来确定视频的编码格式
out = cv2.VideoWriter('test.avi', fourcc, 20, (640, 480))

num = 0

while cap.isOpened():
    # get a frame
    rval, frame = cap.read()                      #cap.read()函数会返回两个参数,第一个参数rval的值为True或False,代表有没有读到图片,第二个参数是frame,是当前截取一帧的图片,该函数返回值是一个元组
    # save a frame
    if rval == True:
        #  frame = cv2.flip(frame,0)
        # Start time
        start = time.time()
        # rclasses, rscores, rbboxes = process_image(frame)                                 # 换成自己调用的函数,该处函数有疑问
        # End time
        end = time.time()
        # Time elapsed
        seconds = end - start
        print("Time taken : {0} seconds".format(seconds))
        # Calculate frames per second
        fps = 1 / seconds
        print("Estimated frames per second : {0}".format(fps))
        # bboxes_draw_on_img(frame,rclasses,rscores,rbboxes)
        # print(rclasses)
        out.write(frame)
        num = num + 1
        print(num)
        # fps = cap.get(cv2.CAP_PROP_FPS)
        # print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    else:
        break
        # show a frame显示帧
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# 释放VideoCapture对象和内存
cap.release()
out.release()
cv2.destroyAllWindows()