import cv2
import numpy as np
img = cv2.imread("examples/00196_surgical.jpg")
def makemask():
    mask = np.zeros(img.shape,np.uint8)
    cv2.rectangle(mask, (68, 141), (195, 240), (255,255,255), -1)
    cv2.imwrite('examples/mask.jpg', mask)


makemask()
#python test.py --image examples/00000_surgical.jpg --mask examples/mask.jpg --output examples/output.jpg --checkpoint_dir model_logs/

#python test.py --image examples/00196_surgical.jpg --mask examples/mask.jpg --output examples/output.jpg --checkpoint_dir model_logs/