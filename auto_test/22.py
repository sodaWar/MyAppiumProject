# -*- coding: utf-8 -*-
import cv2
#该文件作用是读取一个本地视频文件的码率、尺寸,然后指定视频的格式，将本地视频的每一帧提取并保存在另一个视频文件中

# 获得视频的格式
videoCapture = cv2.VideoCapture('cider.mp4')

# 获得码率及尺寸
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print fps
print size

# 指定写视频的格式, I420-avi, MJPG-mp4
videoWriter = cv2.VideoWriter('cider_one.mp4', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)

# 读帧
success, frame = videoCapture.read()

while success:
    cv2.imshow("Oto Video", frame)  # 显示
    cv2.waitKey(1000 / int(fps))  # 延迟
    videoWriter.write(frame)  # 写视频帧
    success, frame = videoCapture.read()  # 获取下一帧