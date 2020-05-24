import os
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from PIL import Image


def process(img):
    # w = img.size[0]
    # h = img.size[1]
    # print(' From image file {}'.format(img))
    img = np.asarray(img)
    w = np.size(img, 1)
    h = np.size(img, 0)
    # print(img.shape, w, h)
    if h == w:
        pass
    elif h > w:
        gap = (h - w)//2
        Flag = True
        img = pad(img, gap, Flag)
    else:
        gap = (w - h)//2
        # the '/' in python means float!!! remember to use '//'
        # img = np.resize()
        Flag = False
        img = pad(img, gap, Flag)
    return img


def pad(img, gap, Flag):
    if Flag:
        img = np.pad(img, ((0, 0), (gap, gap), (0, 0)), 'constant', constant_values= 0)
        # print(img.shape)
        # 使用pad，np中矩阵式表示为行， 列， 维度。
        # 图片的size顺序为宽， 高， channel
    else:
        img = np.pad(img, ((gap, gap), (0, 0), (0, 0)), 'constant', constant_values= 0)
        # print(img.shape)
    return img


if __name__ == '__main__':
    path = 'imgpath'
    output_path = 'outputpath'
    q = 0
    if os.path.exists(output_path):
        pass
    else:
        os.makedirs(output_path)

    for root, dirs, files in os.walk(path):
        for i in tqdm(range(len(files))):
            file = files[i]
            file_path = os.path.join(root, file)
            if file.endswith('jpg') or file.endswith('png'):
                # print(file)
                with open(file_path, 'rb') as f:
                    img = Image.open(f)
                    if img.mode == 'RGBA':
                        img = img.convert('RGB')
                        # r, g, b, a = img.split()
                        # img = img.merge("RGB", (r, g, b))
                        # process the 1 channel image
                        img = process(img)
                    elif img.mode != 'RGB':
                        # print('this picture is NOT supported')
                        q += 1
                        continue
                    else:
                        img = process(img)
                    # print(type(img))
                    # print(img)
                    image = Image.fromarray(img)
                    # img = img.resize((width, height), Image.ANTIALIAS)
                    Output_path = os.path.join(output_path, file[:-4])
                    Output_path = Output_path + '.png'
                    image.save(Output_path, 'png')


    # print('Down! Processed %s images' %i)
    print("there exists %s images can not be read, please check the format" %q)







                
                
                
