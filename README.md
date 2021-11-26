<img src="frontend\lextool\static\tools.png" />
<h1 align="left">FUE</h1>
<p align="left">flask和vue(nuxt)的项目框架</p>

#### 说明
FUE = Flask+Vue(nuxt)
#### 技术栈
- 前端：vue全家桶 + nuxt
- 后端：Flask
- 数据库：MySQL

### 无耻的要个Star
老板，来都来了，给个star吧~

## 部署
### 后端
1、准备工作
 - conda虚拟环境
 - 安装依赖包
 ```py
 pip install -r requirements.txt
 ```

 2、 启动
 ```py
 python run.py
 ```

### 前端
1、准备工作
安装装[PM2](http://menvscode.com/detail/5ce21943e8c50a0870f41983)

2、项目clone到服务器
```bash
git clone git@github.com:xx/xx.git
```

3、运行
cd进入改目录下，安装依赖：
```bash
npm install
npm run build
```
运行项目命令(若用pm则可省)
```bash
npm start
```
此时运行的是 http://localhost:3000

4、pm2开启进程守护
```bash
pm2 start npm --name ProjectName -- start
# ProjectName 是项目名称 在package.json中
```

5、修改项目，重新打包，然后重新部署，则需要重新启动 pm2
```bash
pm2 stop ProjectName   // 先停止

pm2 restart ProjectName  // 再重启
```


