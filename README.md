# Pikachu-Housing
CS411 Project Pikachu-housing 开发流程和注意事项

## 项目介绍

本项目是一个完整的LAMP（本意：Linux+Apache+MySQL+PHP) Web应用，是一个提供给UIUC新生的租房信息网站，包括基本的房价查询、推荐系统、Web爬虫、地图支持（optional)。与通常的LAMP项目相比，我们的project的对应的技术栈有所不同：整个服务器搭建在AWS上的EC2镜像（虚拟机），系统是基于CentOS的Amazon Linux AMI、服务器是Nginx、数据库是PostgreSQL、编程语言是Python。


（为什么不用课程推荐的cPanel：1. 不给root权限，啥都安装不了；2. 虽然支持python，但是搞不懂怎么用；3. 没想好怎么黑，先黑了再说...）

## 进入开发流程（开发准备）
* 提前安装软件和库：python(2.7)、pip、virtualenv、git、postgreSQL、nodejs（前端）；
* 保证自己github有权限访问repository；
* 下载私钥 pikachu.pem （已发到群里，或者私戳组长。非常重要：没这个私钥，无法登录AWS服务器）；
* 更改私钥权限 
`chmod 0400 pikachu.pem`
* 打开终端，进入pikachu.pem所在的文件夹，通过ssh连接服务器: 
` ssh -i "pikachu.pem" ec2-user@ec2-52-14-154-253.us-east-2.compute.amazonaws.com` 

### (线上启动后端）
* 检查gunicron（连接nginx服务器和django后端的工具）是否打开：`lsof -i :8000`；
* 如果存在进程，`sudo kill xxx(对应的pid)`；
* 进入Pikachu-Housing文件夹 cd /home/Pikachu-Housing，并开启gunicorn连接wsgi： `gunicorn settings.wsgi:application --bind 0.0.0.0:8000` 
* 打开http://www.pikachu-housing.art/ ，如果页面炫酷，则说明project已经生效。如果显示nginx相关的错误，则说明gunicorn启动失败；

## 开发流程（后端）
* 完成“进入开发流程”，并且阅读django官网的教程 https://www.djangoproject.com/ ，了解django程序的基础；
在自己的机器上找一个合适的位置，clone项目（需要输入账户密码），
`git clone https://github.com/DeepinSC/Pikachu-Housing.git` 
* 终端进入project目录（包含了manage.py)，激活virtualenv：
`virtualenv venv, source venv/bin/activate`
* 安装requirements，输入 `pip install -r requirements.txt`；（注意，如果你使用的是pycharm等IDE，上面的操作只能更改terminal的环境，但不能更改IDE的venv）
* 输入`python manage.py migrate`，然后输入`python manage.py runserver 8000`，即可启动本地django服务器，连接的是线上数据库；
* 写程序前，`git pull`;
* 愉快地写bug；
* 通过git或者github desktop提交代码，有两种提交方式：
* 暴力push master（嫌麻烦，赶时间或者对代码很自信）；
写代码之前开一个分支 `git branch -D your_name/your_branch_name` （比如 rick/add_parser_code)，publish branch。然后自由地在branch上更改，等确认可以提交后，到项目主页https://github.com/DeepinSC/Pikachu-Housing 会提示新建pull request，写好描述后，等待其他人或者组长review代码，通过后merge branch到master，并删除branch。（具体google github pr提交流程）
1. 进入服务器的Pikachu-Housing文件夹，输入git pull
2. 发现严重bug（网页挂了），不要慌立即revert到上一个节点（可以不用开branch），记得服务器git pull 以保持一致。

## 开发流程（前端）
* 完成“进入开发流程”，并且Vue的基础教程 https://vuejs.org/index.html ；
* 完成上述后端的配置后，进入frontend文件夹，运行`npm install`；
* 愉快的写button；
* 可以通过`npm run dev`，进入127.0.0.1:8080查看效果（推荐Chrome开发者模式查看bug）；
* 提交之前，进入frontend文件夹，运行`npm run build` 将网页打包；
* 同上述的提交方式，提交代码；
* 记得服务器git pull保持一致。


## 其他：
* 数据库名称：pikachu 用户：postgres，密码: 123 （线上数据库默认不需要密码访问）；
* 秉承本地随便搞，别服务器上debug的思想；
* 由于还没有配置本地数据库，所有数据库的操作都会影响线上，所以更改时千万小心；
* 在进行线上数据库操作时，需要通知其他人，防止冲突；
* django superuser username: pikachu, email: tinghui_liao@outlook.com password: pikachu.

## stage4 （10.31）前任务：
* 数据库：将服务器的数据库按照ER图建好（使用sql的ddl指令，可以保存一些测试数据），并将最终建好的数据库导出到本地备用；在建立好house表后，通知所有人；（徐艺嘉）
* 爬虫：实现爬虫的基本功能，能从一个指定网站，获取10条左右的数据，并且通过python程序导入到线上数据库；（杨过）
* 后端：通过django的框架，实现对house表的增删改查（CURD）功能以及一个高级SQL操作（比如group by）。最终能够在python控制台，输入一个http request，能够进行对应的数据库操作，返回对应的http response；（沈钟奕）
* 前端：实现前端的UI和jquery Ajax，向后端发送请求数据。协同组员完成功能，最终能在网页上完成CURD请求（类比一个todo list），整合所有人的代码，交付；（廖庭辉）

