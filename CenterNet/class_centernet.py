import os
import sys 

# add the centernet path
path = os.path.dirname(os.path.realpath(__file__))

centernet_path = os.path.join(path, 'src/lib')
sys.path.insert(0, centernet_path)

from detectors.detector_factory import detector_factory
from opts import opts

class centernet_detector(object):
    def __init__(self,):
        model_path = os.path.join(path, 'models/model_90_2.pth')
        arch = 'dla_34'
        task = 'ctdet'
        confidence = 0.5
        detect_id = 1

        opt = opts().init('{} --load_model {} --arch {}'.format(task, model_path, arch).split(' '))
        self.detector = detector_factory[opt.task](opt)
        self.confidence = confidence
        self.detect_id = detect_id

    def detect(self, img):
        '''
            centernet推理检测
            img     cv2     测试图片
        '''
        bbox = self.detector.run(img)['results'][self.detect_id]
        bbox = bbox[bbox[:, 4] > self.confidence, :]

        return bbox