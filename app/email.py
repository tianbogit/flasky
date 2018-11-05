# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 11:33
# @Author  : TIANPO
# @Email   : mailtp@foxmail.com
import os
from threading import Thread
from flask_mail import Message
from flask import current_app, render_template

from . import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

# https://github.com/mikelkl/flasky/tree/master/app
def send_mail(to, subject, template, **kwargs):
    msg = Message(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=current_app.config['FLASKY_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    # current_app只是一个代理获取而已,传递给其它子线程获取到的依然是子线程的上下文
    # 必须_get_current_object线获取到原始对象再传递过去
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
