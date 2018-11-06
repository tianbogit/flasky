# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 11:33
# @Author  : TIANPO
# @Email   : mailtp@foxmail.com
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
