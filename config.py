#用户配置部分
# 
"""可选颜色
black,              red,                green,              yellow,             blue,
magenta,            cyan,               white,              bg_black,           bg_red,
bg_green,           bg_yellow,          bg_blue,            bg_magenta,         bg_cyan,
bg_white,           light_black,        light_red,          light_green,        light_yellow,
light_blue,         light_magenta,      light_cyan,         light_white,        light_bg_black,
light_bg_red,       light_bg_green,     light_bg_yellow,    light_bg_blue,      light_bg_magenta,
light_bg_cyan,      light_bg_white
"""
LEVEL_COLOR = {
    'DEBUG': 'white',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red,bg_white',
}

STDOUT_LOG_FMT = "%(log_color)s[%(asctime)s] [%(levelname)s] [%(threadName)s] [%(filename)s:%(lineno)d] %(message)s"
STDOUT_DATE_FMT = "%Y-%m-%d %H:%M:%S"
FILE_LOG_FMT = "[%(asctime)s] [%(levelname)s] [%(threadName)s] [%(filename)s:%(lineno)d] %(message)s"
FILE_DATE_FMT = "%Y-%m-%d %H:%M:%S"
