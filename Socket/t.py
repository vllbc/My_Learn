from socket import *
import numpy as np
import cv2
import base64

def main():
    HOST = '127.0.0.1'
    PORT = 9999
    BUFSIZ = 1024*20
    ADDR = (HOST, PORT)
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)
    while True:
        rec_d = bytes([])
        print('waiting for connection...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('...connected from:', addr)
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data or len(data) == 0:
                break
            else:
                rec_d = rec_d + data
        rec_d = base64.b64decode(rec_d)
        np_arr = np.fromstring(rec_d, np.uint8)
        image = cv2.imdecode(np_arr, 1)
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('image', image)
        cv2.imwrite("res.jpg",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        tcpCliSock.send("0001".encode())
        # tcpCliSock.send("返回值")
        tcpCliSock.close()
    tcpSerSock.close()

if __name__ == "__main__":
    main()
