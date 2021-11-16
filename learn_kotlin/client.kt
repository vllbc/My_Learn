import java.net.Socket


fun initConnect():Socket{
        val sc:Socket = Socket("127.0.0.1", 9090) //通过socket连接服务器,参数ip为服务端ip地址，port为服务端监听端口
        sc.setSoTimeout(10000)  //设置连接超时限制
        if (sc != null) {    //判断一下是否连上，避免NullPointException
            System.out.println("connect server successful")
        } else {
            System.out.println("connect server failed,now retry...")
            initConnect()   //没连上就重试一次
        }
        return sc
    }
