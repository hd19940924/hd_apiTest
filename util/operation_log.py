# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/7/13 13:35
# @filename :operation_log.py
# 开发工具 ：PyCharm
import logging
import colorama
from colorama import Fore, Style
class ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_str = super().format(record)
        if record.levelno == logging.INFO:
            log_str = f'{Fore.GREEN}{log_str}{Style.RESET_ALL}'
        elif record.levelno == logging.DEBUG:
            log_str = f'{Fore.WHITE}{log_str}{Style.RESET_ALL}'
        elif record.levelno == logging.WARNING:
            log_str = f'{Fore.YELLOW}{log_str}{Style.RESET_ALL}'
        elif record.levelno == logging.ERROR or record.levelno == logging.CRITICAL:
            log_str = f'{Fore.RED}{log_str}{Style.RESET_ALL}'
        return log_str
class ColoredLogger:
    def __init__(self, log_file='logfile.log', level=logging.DEBUG):
        self.log_file = log_file
        self.level = level
        self.logger = self._create_logger()
    def _create_logger(self):
        # 创建日志记录器
        logger = logging.getLogger('my_logger')
        logger.setLevel(self.level)
        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.level)
        console_formatter = ColoredFormatter('[%(asctime)s] %(module)s - %(funcName)s, line %(lineno)d: %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
        console_handler.setFormatter(console_formatter)
        # 创建文件处理器
        file_handler = logging.FileHandler(self.log_file, mode='a')
        file_handler.setLevel(self.level)
        file_formatter = logging.Formatter('[%(asctime)s] %(module)s - %(funcName)s, line %(lineno)d: %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(file_formatter)
        # 添加处理器到日志记录器
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        return logger
    def info(self, message):
        self.logger.info(message)
    def debug(self, message):
        self.logger.debug(message)
    def warning(self, message):
        self.logger.warning(message)
    def error(self, message):
        self.logger.error(message)
def test_logger():
        logger = ColoredLogger()
        logger.info('This is an information message')
        logger.debug('This is a debug message')
        logger.warning('This is a warning message')
        logger.error('This is an error message')
if __name__ == '__main__':
    colorama.init()
    test_logger()