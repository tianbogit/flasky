# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 11:33
# @Author  : TIANPO
# @Email   : mailtp@foxmail.com
from flask import render_template, request, jsonify
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    # 只为接受 JSON 格式而不接受 HTML 格式的客户端生成 JSON 格式响应
    # 针对api中404处理
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'Internal server error'})
        response.status_code = 500
        return response
    return render_template('500.html'), 500
