# 猪只点数

说明：整个项目做猪只点数，前端采用android，后台采用flask+pytorch实现。算法上采用centernet进行猪只检测

## 特点
- flask和pytorch model分开模块化整理，便于维护
- 包含api serve和client 文件，便于测试

## 依赖
1. 这里给出了一个pip的文件列表
```bash
pip install -r requirements.txt
```

2. 编译centernet的拓展
```bash
cd $CenterNet/src/lib/external
make
```

3. 编译centernet的dcn拓展
~~~bash
cd $CenterNet_ROOT/src/lib/models/networks/DCNv2
./make.sh
~~~

## 起服务
安装好以上依赖之后
```bash
cd $project/
python app.py
```

## 测试
起好服务之后
```bash
cd $project
python app_test.py
```

## 请求api
- post,get都行
- 参数：img:base64编码

返回结果：
返回json字符串，参数及类型如下：  
flag        bool    标志位，0：错误；1：正确  
nums        int     猪只数量  
coordinates list    每只猪的位置  