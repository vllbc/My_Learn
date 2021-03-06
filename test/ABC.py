from abc import ABC,abstractmethod
import logging


class AbsLogger(ABC):
    @abstractmethod
    def info(self, msg):
        pass

    @abstractmethod
    def debug(self, msg):
        pass

    @abstractmethod
    def error(self, msg):
        pass

    @abstractmethod
    def warn(self, msg):
        pass

    @abstractmethod
    def exception(self, msg):
        pass

class LogingLogger(AbsLogger):
    def __init__(self) -> None:
        logging.basicConfig(
            format="[%(asctime)s][%(levelname)s]: %(message)s", level=logging.DEBUG
        )
    
    def info(self, msg):
        return logging.info(msg)
    
    def debug(self, msg):
        return logging.debug(msg)
    
    def error(self, msg):
        return logging.error(msg)
    
    def warn(self, msg):
        return logging.warn(msg)
    
    def exception(self, msg):
        return logging.exception(msg)

class Test(LogingLogger):
    def info(self, msg):
        super().info(msg)
        print("info")
    
    def debug(self, msg):
        super().info(msg)
        print("debug")
    
    def error(self, msg):
        super().info(msg)
        print("error")
    
    def warn(self, msg):
        super().info(msg)
        print("warn")
    
    def exception(self, msg):
        super().info(msg)
        print("exception")
    
T = Test()
T.info("1")