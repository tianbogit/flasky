# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 11:33
# @Author  : TIANPO
# @Email   : mailtp@foxmail.com
import os
from app import create_app, db
from app.models import User, Role, Post, Follow, Comment
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
    return dict(app=app, db=db, User=User, Role=Role, Post=Post, Follow=Follow, Comment=Comment)


# 注册shell命令：通过这种方式调用（python manager.py shell）
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

COV = None
if os.environ.get('FLASK_COVERAGE') or False:
    import coverage

    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()


# 单元测试命令
@manager.command
def test(coverage=False):
    """Run the unit tests."""
    if coverage and not (os.environ.get('FLASK_COVERAGE') or False):
        import sys
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)

    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version：file://%s/index.html' % covdir)
        COV.erase()


# 监视资源消耗命令
@manager.command
def profile(length=25, profile_dir=None):
    """Start the application under the code profiler."""
    from werkzeug.contrib.profiler import ProfilerMiddleware

    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length],
                                      profile_dir=profile_dir)
    app.run()


# 自动迁移数据库命令
@manager.command
def deploy():
    """Run deployment tasks."""
    from flask.ext.migrate import upgrade
    from app.models import Role, User
    # 把数据库迁移到最新修订版本
    upgrade()
    # 创建用户角色
    Role.insert_roles()
    # 让所有用户都关注此用户
    User.add_self_follows()


if __name__ == '__main__':
    manager.run()
