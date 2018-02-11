# Django-With-Vue
使用Django与Vue实现前后端分离，暂时没有想好做什么

参考文章：[友情链接](https://cloud.tencent.com/developer/article/1005607)

之前在项目中使用的是Django模板系统，虽然对后端程序员很友好，但是如果需要做移动端服务，则需要另起炉灶，重新设计系统。所以想实现前后端分离，采用restful API来设计数据交互接口，提高程序的可扩展性。

## Quick Start

- 1 安装Django，创建project和app
- 2 安装node.js，然后配置路径
- 3 在terminal中用npm安装vue-cli脚手架

```
npm install -g vue-cli
```
- 4 在project目录下创建前端工程
    
```
vue-init webpack appfront  //安装中把vue-router选上，我们须要它来做前端路由
```
- 5 添加工程依赖

```
npm install //安装vue所须要的node依赖
```
- 6 测试前端

```
npm run dev
```
用浏览器打开 [http://localhost:8080/](http://localhost:8080/) ，就可以看到前端页面了

- 7 webpack自动打开

```
npm run build   // webpack会将所有资源文件打包到前端工程的dist目录下
```

- 8 整合

在setting.py中配置静态文件路径和模板路径

```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "appfront/dist/static"),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['appfront/dist'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- 9 创建index.html，添加url，运行Django

```
python manage.py runserver
```
这时，你可以通过 [http://localhost:8000/](http://localhost:8000/) 访问你的project了
