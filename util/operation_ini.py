# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/7/12 15:59
# @filename :operation_ini.py
# 开发工具 ：PyCharm
import configparser
import configparser
class ConfigHandler:
    def __init__(self, filename):
        self.filename = filename
        self.config = configparser.ConfigParser()
        self.config.read(self.filename, encoding='utf-8')
    #def read_config(self):

    def get_value(self, section, key):
        return self.config.get(section, key)
    def set_value(self, section, key, value):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, value)
        self.write_config()
    def write_config(self):
        with open(self.filename, 'w') as configfile:
            self.config.write(configfile)
if __name__=="__main__":
    co=ConfigHandler("..\config\config.ini")
    #co.read_config()
    port= co.get_value("DATABASE","port")
    print(port)