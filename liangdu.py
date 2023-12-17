import cv2
import pandas as pd

def calculate_brightness(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightness = gray_image.mean()
    return brightness

if __name__ == '__main__':
    data = pd.read_csv('features.csv',encoding='GBK')
    for i in range(len(data)):
        sourcePath = data.iloc[i, 0]
        data.at[i,'lightness'] = calculate_brightness(sourcePath)
    data.to_csv('features.csv',encoding='GBK',index=False)