import cv2
import numpy as np


def cal_acutance(image):
    return np.sum(np.abs(cv2.Laplacian(image, cv2.CV_64F))) / image.shape[0] / image.shape[1]
