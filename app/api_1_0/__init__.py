# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 11:33
# @Author  : TIANPO
# @Email   : mailtp@foxmail.com
from flask import Blueprint

api = Blueprint('api', __name__)
from . import authentication, posts, users, comments, errors
