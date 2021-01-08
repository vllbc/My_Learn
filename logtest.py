import logging  # 引入logging模块
import time
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Log等级总开关
# 第二步，创建一个handler，用于写入日志文件
fh = logging.FileHandler('logs.log', mode='w')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
# 第三步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
# 第四步，将logger添加到handler里面
logger.addHandler(fh)
# 日志
logger.debug("hello")
logger.debug("hi")
logger.debug("yes")
logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')
