import cv2
import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv('features.csv',encoding='GBK')
    for i in range(len(data)):
        sourcePath = data.iloc[i, 0]
        img = cv2.imread(sourcePath)
        sp = img.shape
        data.at[i,'size'] = '('+str(sp[0]) + ', '+ (sp[1]) + ')'
    data.to_csv('features.csv',encoding='GBK',index=False)