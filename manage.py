# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 11:33
# @Author  : TIANPO
# @Email   : mailtp@foxmail.com
import os
from app import create_app, db
from app.models import User, Role, Post
from flask_script import Manager, Shell
from flask_moment import Moment

'''
数据库版本管理，会根据模型与数据库表自动生成差异版本，根据模板自动实现如下函数：
upgrade
downgrade
'''
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
moment = Moment(app)


# shell界面回传参数，可以直接使用
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post)


# 注册shell命令：通过这种方式调用（python manager.py shell）
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


# 单元测试
@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
