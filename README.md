[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)


# EasyUse_FastApi
#### 快速使用FastAPI部署机器学习模型,使用全局定义和全局加载模型，提升inference速度。在初始化的时候（第一次推理的时候速度较慢，在第二次使用则恢复正常，在10ms左右）
#### 利用FastApi自带的异步的方式进行数据的推理，比Flask更加方便和快一些

#####  启动服务 uvicorn Text-CNN-server:app --reload ，开启热启动模式
#####  启动服务 uvicorn Text-CNN-server:app --port=5000 --workers=4，开启生产模式


> backend 

<div align=center><img  src="https://github.com/CarryChang/EasyUse_FastApi/blob/master/pic/backend.png"></div>

> frontend 

<div align=center><img  src="https://github.com/CarryChang/EasyUse_FastApi/blob/master/pic/api.png"></div>


> inference 

<div align=center><img  src="https://github.com/CarryChang/EasyUse_FastApi/blob/master/pic/inference.png"></div>
