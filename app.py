'''
use for python api, Package into a separate package
chenjun
2020-05-08
'''

import json
from flask import Flask, request
from src.utils import Base64ToImage

from CenterNet.class_centernet import centernet_detector


app = Flask(__name__)
# 0. 模型初始化 // 在model类的初始化中设置相关参数
model = centernet_detector()


@app.route('/pig_count', methods=['POST', 'GET'])
def process_fun():
    '''
    api服务主函数
    输入：
        参用字典的方式传入参数，用json封装
        img         base64          需要测试的图片

    输出：
        用json封装字典
        flag        bool            标志位
        nums        int             猪只只数
        coordinate  string          每只猪的具体位置
    '''
    try:
        # 1. 解析图片
        base64img = request.json['img']
        img = Base64ToImage(base64img)

        # 2. 调用模型
        detect_result = model.detect(img)
        
        # 3. 返回结果
        coordinates = [per_result.tolist() for per_result in detect_result]
        result = {}
        result['flag'] = '1'
        result['nums'] = len(detect_result)
        result['coordinates'] = coordinates
        
    except:
        result = {}
        result['flag'] = '0'
        result['nums'] = 0
        result['coordinates'] = '0,0,0,0,0'

    return json.dumps(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
