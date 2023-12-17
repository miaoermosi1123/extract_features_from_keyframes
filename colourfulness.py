import cv2
import numpy as np
import pandas as pd
def calculate_saturation(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)
    saturation_std = np.std(s)
    return saturation_std

if __name__ == '__main__':
    data = pd.read_csv('features.csv',encoding='GBK')
    for i in range(len(data)):
        sourcePath = data.iloc[i, 0]
        data.at[i,'contrast'] = calculate_saturation(sourcePath)
    data.to_csv('features.csv',encoding='GBK',index=False)