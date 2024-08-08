@echo off
REM 设置Conda环境的名称
set ENV_NAME=THU

REM 激活Conda环境
call activate %ENV_NAME%

cd E:\Work\THU\code\THU_Project_project\

D:\\soft\\Anaconda\\envs\\py37\\Scripts\\pyside2-uic -o ./QTui/module/ui_main.py ./QTui/main.ui

cd E:\Work\THU\code\THU_Project_project\Scripts