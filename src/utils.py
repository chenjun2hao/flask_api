import cv2
import json
import base64
import numpy as np

def Base64ToImage_list(bslist: list) -> np.ndarray:
    '''将base64编码的列表转换成n×h×w×c的numpy矩阵
    balist：
        base64编码的图像列表
    '''
    imglist = []
    for base in bslist:
        imgData = base64.b64decode(base) 
        nparr = np.frombuffer(imgData,np.uint8)    
        img = cv2.imdecode(nparr,cv2.IMREAD_COLOR)
        img = cv2.resize(img, image_size)               # 进行resize，统一图像尺寸
        img = img[:,:,::-1]                             # 转换成RGB顺序
        imglist.append(np.expand_dims(img, axis=0))
    imgs = np.concatenate(imglist, axis=0)
    return imgs


def Base64ToImage(base)-> np.ndarray:
    '''
        将base64的图片转成cv2 image
        输入：
            base    base64      测试图像

        输出：
            img     cv2         转换后图像
    '''
    imgdata = base64.b64decode(base)
    nparr = np.frombuffer(imgdata, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    return img


class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        """
            json封装base64时的问题，只要检查到了是bytes类型的数据就把它转为str类型
        :param obj:
        :return:
        """
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)