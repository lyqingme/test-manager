# vue+django开发的前后端分离的web项目

目录结构

| Location             |  Content                                   |
|----------------------|--------------------------------------------|
| `/backend`           | django后端项目                             |
| `/backend/api`       | django，api应用                            |
| `/src`               | Vue前端项目                                |
| `/src/main.js`       | VUE mainjs文件                             |
| `/public/index.html` | VUE indexhtml文件                          |
| `/public/static`     | 前端静态文件目录                           |
| `/dist/`             | 前端构建后的dist目录                       |

本地安装部署
$ yarn install
$ python manage.py migrate

本地开发启动后端服务
$ python manage.py runserver
启动前端服务
$ yarn serve

项目发布及服务器部署
$ yarn build
$ python manage.py runserver

