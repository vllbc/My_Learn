from socket import socket
import asyncio

sk = socket()
sk.connect(('127.0.0.1', 9090))


async def loops():
    while 1:
        msg_s = input('>>>')
        sk.send(msg_s.encode('utf-8'))
        if msg_s == 'q':
            break
        msg_r = sk.recv(1024).decode('utf-8')
        print(f"收到来自服务端的消息：{msg_r}")
        if msg_r == 'q':
            break
    sk.close()


loop = asyncio.get_event_loop()

loop.run_until_complete(loops())
