#coding:utf-8
import logging

logger_info = logging.getLogger('log_info')
logger_error = logging.getLogger('log_error')

def log_info(*args):
    logger_info.info(args)

def log_error(*args):
    logger_error.error(args)