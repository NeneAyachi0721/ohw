import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

L = len(frame)
W = len(frame[0])
print(frame.shape)
print(L, W)

SIZE = 100

X0 = int(W / 2 - 1.5 * SIZE)
Y0 = int(L / 2 - 1.5 * SIZE)

chessboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print(chessboard)


def mouse_dclick(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("get double click", x, y)
        if x > X0 and y > Y0 and x < (X0 + SIZE * 3) and y < (Y0 + SIZE * 3):
            i = int((x - X0) / SIZE)
            j = int((y - Y0) / SIZE)
            print(i, j)
            chessboard[i][j] = 1
            print(chessboard)


# 创建图像与窗口并将窗口与回调函数绑定
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', mouse_dclick)

while True:
    ret, frame = cap.read()
    for i in range(3):
        for j in range(3):
            cv2.rectangle(frame, (i * SIZE + X0, j * SIZE + Y0), (i * SIZE + SIZE + X0, j * SIZE + SIZE + Y0),
                          (255, 128, 255), 2)
            if chessboard[i][j] == 1:
                R = int(SIZE / 2)
                cv2.circle(frame, (i * SIZE + X0 + R, j * SIZE + Y0 + R), R, (255, 0, 0), -1)

    cv2.imshow('frame', frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()