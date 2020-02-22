[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)


# EasyUse_FastApi
#### 快速使用FastAPI部署机器学习模型,使用全局定义和全局加载模型，提升inference速度。在初始化的时候（第一次推理的时候速度较慢，在第二次使用则恢复正常，在10ms左右）
#### 利用FastApi搭配uvicorn自带的异步的方式进行数据的推理，比Flask+gunicorn更加方便和快一些
 
#####  启动服务 uvicorn Text-CNN-server:app --reload ，开启热启动模式
#####  启动服务 uvicorn Text-CNN-server:app --port=5000 --workers=4，开启生产模式， 注意: Sanic(FastAPI) 的性能的确很棒，当时技术验证时，测试的时候，不同业务逻辑下，基本都能保证其性能在 Flask 的 1.5 倍以上。但是就目前的使用经验来说 Sanic（(FastAPI)）距离真正生产可用，还有相当长一段路要走。无论是内部的架构，还是周边的生态，亦或者是其他。大家可以没事拿来玩玩，但是如果要上生产线，请做好被坑的准备

> backend 

<div align=center><img  src="https://github.com/CarryChang/EasyUse_FastApi/blob/master/pic/backend.png"></div>

> frontend 

<div align=center><img  src="https://github.com/CarryChang/EasyUse_FastApi/blob/master/pic/api.png"></div>


> inference 

<div align=center><img  src="https://github.com/CarryChang/EasyUse_FastApi/blob/master/pic/inference.png"></div>
