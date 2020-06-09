#!/bin/bash
# author:lex<luohai2233@163.com>

# config variables
# Path
CONDA_ENV=EnvName
PROJECT_F_BASE_PATH=/Project/Backend/Base/Path/    # frontend
PROJECT_B_BASE_PATH=/Project/frontend/Base/Path/     # backend
PROJECT_PORT=5000                                   # backend port
GIT=git@github.com:xx/xx.git

# Frontend Name
PROJECT_NAME_F=xx                              # frontend name


# stop backend
lsof -i:${PROJECT_PORT}|awk '{print$2}' |grep -v PID|xargs kill -9 # 暂停

# stop frontend
pm2 stop $PROJECT_NAME_F

#pull
git pull

# install dependence & build
# backend
source activate $CONDA_ENV
cd $PROJECT_B_BASE_PATH
pip install -r requirements.txt
# start
nohup python run.py >> server.log 2>&1 &
echo "Complete Backend"

# frontend
cd $PROJECT_F_BASE_PATH$PROJECT_NAME_F
npm install
npm run build

# start
pm2 restart $PROJECT_NAME_F
echo "Complete Fronteend"