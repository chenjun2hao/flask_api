import cv2
from class_centernet import centernet_detector
import matplotlib.pyplot as plt

if __name__ == "__main__":
    img_path = './CenterNet/images/0001.png'
    img = cv2.imread(img_path)
    # img = img[:,:,(2,1,0)]
    model = centernet_detector()
    result = model.detect(img)
    # debug show
    for per_res in result:
        cv2.rectangle(img, (per_res[0], per_res[1]), (per_res[2], per_res[3]), (0, 0, 255), 3)
        # cv2.putText(img, f'{per_res[4]})
    plt.imshow(img)
    plt.show()
    print(result)