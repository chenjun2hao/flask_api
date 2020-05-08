'''
for api test
chenjun
2020-05-08
'''
import cv2
import json
import base64
import requests
from src.utils import MyEncoder

if __name__ == "__main__":
    # 路由
    url = 'http://0.0.0.0:8080/pig_count'

    # prepare image
    imgpath = './CenterNet/images/0001.png'
    img = cv2.imread(imgpath)
    imageData = base64.b64encode(cv2.imencode('.png', img)[1].tobytes())#读取图片并
    
    # prepare the post data and header
    data = {'img' : imageData}
    encode_json = json.dumps(data, cls=MyEncoder)
    headers = {'content-type': 'application/json'}
    # response = requests.get(url, )
    response = requests.post(url, data=encode_json, headers=headers)
    print(response.json())