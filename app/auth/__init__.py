# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 10:35
# @Author  : TIANPO
# @Email   : mailtp@foxmail.com
# @File    : __init__.py.py
from flask import Blueprint

auth = Blueprint('auth', __name__)
from . import views
