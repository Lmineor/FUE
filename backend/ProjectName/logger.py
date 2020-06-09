#!/usr/bin/env python3
# -*- coding:utf-8 -*-


r"""python log with color
log.py
    log module
Usage:
    from log import logger
    logger.debug("Hello World")
"""
import os
import time
import logging
import logging.handlers

from .config.default import DefaultConfig

__all__ = ["logger"]


# 用户配置部分 ↓
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
    'DEBUG':        'cyan',
    'INFO':         'green',
    'WARNING':      'yellow',
    'ERROR':        'red',
    'CRITICAL':     'red,bg_white',
}

STDOUT_LOG_FMT = "%(log_color)s[%(asctime)s] [%(levelname)s] [%(threadName)s] [%(filename)s:%(lineno)d] %(message)s"
STDOUT_DATE_FMT = "%Y-%m-%d %H:%M:%S"
FILE_LOG_FMT = "[%(asctime)s] [%(levelname)s] [%(threadName)s] [%(filename)s:%(lineno)d] %(message)s"
FILE_DATE_FMT = "%Y-%m-%d %H:%M:%S"
# 用户配置部分 ↑


class ColoredFormatter(logging.Formatter):

    COLOR_MAP = {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magenta": "35",
        "cyan": "36",
        "white": "37",
        "bg_black": "40",
        "bg_red": "41",
        "bg_green": "42",
        "bg_yellow": "43",
        "bg_blue": "44",
        "bg_magenta": "45",
        "bg_cyan": "46",
        "bg_white": "47",
        "light_black": "1;30",
        "light_red": "1;31",
        "light_green": "1;32",
        "light_yellow": "1;33",
        "light_blue": "1;34",
        "light_magenta": "1;35",
        "light_cyan": "1;36",
        "light_white": "1;37",
        "light_bg_black": "100",
        "light_bg_red": "101",
        "light_bg_green": "102",
        "light_bg_yellow": "103",
        "light_bg_blue": "104",
        "light_bg_magenta": "105",
        "light_bg_cyan": "106",
        "light_bg_white": "107",
    }

    def __init__(self, fmt, datefmt):
        super(ColoredFormatter, self).__init__(fmt, datefmt)

    def parse_color(self, level_name):
        color_name = LEVEL_COLOR.get(level_name, "")
        if not color_name:
            return ""

        color_value = []
        color_name = color_name.split(",")
        for _cn in color_name:
            color_code = self.COLOR_MAP.get(_cn, "")
            if color_code:
                color_value.append(color_code)

        return "\033[" + ";".join(color_value) + "m"

    def format(self, record):
        record.log_color = self.parse_color(record.levelname)
        message = super(ColoredFormatter, self).format(record) + "\033[0m"

        return message


def _get_logger(log_to_file=False, log_filename="", log_level="DEBUG"):

    _logger = logging.getLogger(__name__)

    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(
        ColoredFormatter(
            fmt=STDOUT_LOG_FMT,
            datefmt=STDOUT_DATE_FMT,
        )
    )
    _logger.addHandler(stdout_handler)

    if log_to_file or log_filename:
        _tmp_path = DefaultConfig.LOGPATH
        try:
            os.makedirs(os.path.join(_tmp_path, "logs"))
        except Exception as e:
            pass
        if log_filename:
            log_filename = log_filename.split('.')[0] + time.strftime('%Y%m%d', time.localtime(time.time())) + '.log'
            _tmp_path = os.path.join(_tmp_path, "logs/{}".format(log_filename))
        else:
            log_filename = 'default'+ time.strftime('%Y%m%d', time.localtime(time.time())) + '.log'
            _tmp_path = os.path.join(_tmp_path, "logs/{}".format(log_filename))
        file_handler = logging.handlers.TimedRotatingFileHandler(_tmp_path, when="midnight", backupCount=30)
        file_formatter = logging.Formatter(
            fmt=FILE_LOG_FMT,
            datefmt=FILE_DATE_FMT,
        )
        file_handler.setFormatter(file_formatter)
        _logger.addHandler(file_handler)

    _logger.setLevel(log_level)
    return _logger


logger = _get_logger(log_filename="app.log")