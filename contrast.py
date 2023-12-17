import cv2
import numpy as np
import pandas as pd

def calculate_contrast(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    contrast_value = np.std(gray_image)

    return contrast_value

if __name__ == '__main__':
    data = pd.read_csv('features.csv',encoding='GBK')
    for i in range(len(data)):
        sourcePath = data.iloc[i, 0]
        data.at[i,'contrast'] = calculate_contrast(sourcePath)
    data.to_csv('features.csv',encoding='GBK',index=False)