import logging
fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') #将格式化格式化为可传入参数
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger("vllbc")
handle = logging.FileHandler("log.txt",encoding='utf-8')


handle.setLevel(level=logging.INFO)

handle.setFormatter(fmt=fmt)

logger.addHandler(handle)

logger.info("hello world")
logger.info("你好")
logger.debug("我不hao")
logger.warning("出错了")
