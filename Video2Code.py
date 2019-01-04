# encoding=utf-8
import os
from PIL import Image
import cv2

WIDTH = 100
HEIGHT = 36

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#将256灰度映射到70个字符上
def get_char(r,g,b):
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 +1) /length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    cap = cv2.VideoCapture('3.mp4')
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        im=Image.fromarray(frame)
        im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

        txt=""

        for i in range(HEIGHT):
            for j in range(WIDTH):
                txt += get_char(*im.getpixel((j, i)))
            txt +='\n'
        os.system('cls')
        print(txt)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
