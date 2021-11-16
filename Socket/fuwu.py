import socket
import asyncio
import sys
sk = socket.socket(type=socket.SOCK_STREAM)
sk.bind(('127.0.0.1', 9090))
sk.listen()


def loops():
    while 1:
        print("等待链接中------------")
        conn, addr = sk.accept()  # 等待连接 -- 阻塞
        print(f"链接成功！{addr}")
        
        # msg_r = conn.recv(1024).decode('utf-8')
        for msg_r in iter(lambda:conn.recv(1024).decode('utf-8'),"q"):
            print(f'接收到来自{addr}的一个消息:{msg_r}')
            msg_s = input('>>>')
            conn.send(msg_s.encode('utf-8'))
            if msg_s == "q":
                sys.exit()
                break
        conn.close()  # 服务器和当前客户端断开连接,程序回到上一层死循环,重新等待客户端的连接
    sk.close()

if __name__ == '__main__':
    loops()
