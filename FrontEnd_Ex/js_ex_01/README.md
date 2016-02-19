
## 浏览器需求

- 最新版Chrome, Firefox, Safari测试通过；
- 需要网络连接，不需要翻墙（使用了bootstrap cn的cdn）。

## 后端支持需求

- Python 2.7.9 / 3.4.3
- Django 1.8.2

## 外部库引用

- jQuery
- jQuery-UI（js与css）
- Bootstrap 3（js与css）
- d3.js
- Django

## 运行测试方法

- 在Terminal中进入`js_ex_01`目录，运行`python manage.py runserver`启动Django的测试服务器，默认端口号为8000；
- 如果显示端口被占用，则在上述命令后再加上一个参数指定新端口，如`python manage.py runserver 9000`即在9000端口开服务器；
- 在浏览器地址栏输入`http://127.0.0.1:8000/`或任何在启动服务器时定义的端口号，访问实现效果。

## 功能实现

- 实现了要求的全部三项功能与附加题；
- 使用简单的Django后端来处理AJAX请求；
- 应用Django Model层连接了Sqlite3数据库，跑一次脚本向其中插入几万条之前采集的Weibo传播数据样本；
- 每次点击第三层导航Tab，即将该Tab的信息传给后端，用示例算法计算出对应的一组数据id并从数据库取出，返回给前端重新绘制d3图表。