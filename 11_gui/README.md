simple_pygtk_app.py
#跳过,没有linux gui环境

pygtk_log_viewer.py
link ../../3text/code/apache_log_parser_regex.py
#引用?

#curses_log_viewer.py 可以使用,部分功能报错
#TypeError: unorderable types: NoneType() < NoneType()


urls.py
#映射/到域名,映射所有URL到视图

views.py
#list_files函数列出所有文件,传递给模板
#view_log 打开日志,参数有排序和日志名

base.html
#模板 标题和内容

list_files.html
#对于在file_list中的每一个元素,创建一个连接

view_logfile.html
#创建表格,排序
完成 还是要看代码


django-admin startproject sysmanage
cd sysmanage
django-admin startapp inventory

settings.py
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(os.path.dirname(__file__), 'dev.db')
#数据库引擎,数据库位置,使用的相对位置,注意技巧

INSTALLED_APPS
#增加django.contrib.admin 和 sysmanage.inventory

urls.py
    (r'^admin/', include('django.contrib.admin.urls')),

models.py
#数据库设计 ORM将类转为表格
#创建了5个类OperatingSystem, Service, HardwareComponent,
Server, and IPAddress

python manage.py syncdb
python manage.py runserver 0.0.0.0:8080

urls.py
#映射非管理URL到函数

views.py
#填加3个函数,包括os,硬件,服务,传给模板

main.html
#三个部分,三个类别加链接,点链接的时候,会转到另一个视图categorized()

categorized.html
#server_detail()

server_detail.html
#各类信息
#三级页面, 分类,厂商,详情

