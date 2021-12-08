# #第二章 数字图像基础
#
# #更改图像空间分辨率 像素区域关系重采样
#
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import transform,data
import matplotlib.pyplot as plt

# 读取原始图像
img = cv2.imread('C:/Users/74/Desktop/Steve/myself.jpg')#('2.1.jpg') #1024*1024图像
b,g,r = cv2.split(img)
img = cv2.merge([r,g,b])
#获取图像的高度和宽度
height = img.shape[0]
width = img.shape[1]
#缩小, 象素关系重采样
# 将1024*1024图像，逐渐减少采样数到 512*512 256*256 128*128 64*64 32*32
img1=cv2.resize(img,(width//2,height//2),interpolation=cv2.INTER_AREA) #1024*1024 to 512*512
img2=cv2.resize(img,(width//4,height//4),interpolation=cv2.INTER_AREA) #1024*1024 to 256*256
img3=cv2.resize(img,(width//8,height//8),interpolation=cv2.INTER_AREA) #1024*1024 to 128*128
img4=cv2.resize(img,(width//16,height//16),interpolation=cv2.INTER_AREA) #1024*1024 to 64*64
img5=cv2.resize(img,(width//32,height//32),interpolation=cv2.INTER_AREA) #1024*1024 to 32*32
#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
#显示图像
plt.figure(figsize=(12, 7))  # width * height
plt.subplot(231), plt.imshow(img, cmap = 'gray'),plt.title('原始图像 1024*1024')
plt.subplot(232), plt.imshow(img1, cmap = 'gray'),plt.title('重采样 1024*1024 to 512*512')
plt.subplot(233), plt.imshow(img2, cmap = 'gray'),plt.title('重采样 1024*1024 to 256*256')
plt.subplot(234), plt.imshow(img3, cmap = 'gray'),plt.title('重采样 1024*1024 to 128*128')
plt.subplot(235), plt.imshow(img4, cmap = 'gray'),plt.title('重采样 1024*1024 to 64*64')
plt.subplot(236), plt.imshow(img5, cmap = 'gray'),plt.title('重采样 1024*1024 to 32*32')
plt.show()

#获取图像的高度和宽度
height1 = img1.shape[0]
width1 = img1.shape[1]
height2 = img2.shape[0]
width2 = img2.shape[1]
height3 = img3.shape[0]
width3 = img3.shape[1]
height4 = img4.shape[0]
width4 = img4.shape[1]
height5 = img5.shape[0]
width5 = img5.shape[1]

#放大, 象素关系重采样
# 分别将512*512 256*256 128*128 64*64 32*32图像复原为1024*1024像素的图像
newimg1=cv2.resize(img1,(width1*2,height1*2),interpolation=cv2.INTER_AREA)
newimg2=cv2.resize(img2,(width2*4,height2*4),interpolation=cv2.INTER_AREA)
newimg3=cv2.resize(img3,(width3*8,height3*8),interpolation=cv2.INTER_AREA)
newimg4=cv2.resize(img4,(width4*16,height4*16),interpolation=cv2.INTER_AREA)
newimg5=cv2.resize(img5,(width5*32,height5*32),interpolation=cv2.INTER_AREA)
con_3=img3
con_4=img4
con_5=img5
#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
#显示图像
plt.figure(figsize=(12, 7))  # width * height
plt.subplot(231), plt.imshow(img, cmap = 'gray'),plt.title('原始图像1024*1024')
plt.subplot(232), plt.imshow(newimg1, cmap = 'gray'),plt.title('512*512 复原 1024*1024')
plt.subplot(233), plt.imshow(newimg2, cmap = 'gray'),plt.title('256*256 复原 1024*1024')
plt.subplot(234), plt.imshow(newimg3, cmap = 'gray'),plt.title('128*128 复原 1024*1024')
plt.subplot(235), plt.imshow(newimg4, cmap = 'gray'),plt.title('64*64 复原 1024*1024')
plt.subplot(236), plt.imshow(newimg5, cmap = 'gray'),plt.title('32*32 复原 1024*1024')
plt.show()


# 更改图像的灰度级
#保持空间分辨率为常数，对灰度级为256的原图像分别以灰度级8、4、2显示

import cv2
import numpy as np
import matplotlib.pyplot as plt

#读取原始图像
img = cv2.imread('2.2.jpg')#('C:\\Users\\74\\Desktop\\Steve\\sample.jpg')

# b,g,r = cv2.split(img)
# img = cv2.merge([r,g,b])
#获取图像高度和宽度
height = img.shape[0]
width = img.shape[1]
print(img.shape[2])
#创建一幅图像
new_img1 = np.zeros((height, width, 3), np.uint8)
new_img2 = np.zeros((height, width, 3), np.uint8)

#以灰度级4显示图像
for i in range(height):
    for j in range(width):
        for k in range(3): #对应BGR三分量
            if img[i, j][k] < 42:
                gray = 0
            elif img[i, j][k] < 128:
                gray = 84
            elif img[i, j][k] < 213:
                gray = 170
            else:
                gray = 255
            new_img1[i, j][k] = np.uint8(gray)

#以灰度级2显示图像
for i in range(height):
     for j in range(width):
        for k in range(3): #对应BGR三分量
            if img[i, j][k] < 128:
                gray = 0
            else:
                gray = 255
            new_img2[i, j][k] = np.uint8(gray)


#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
#显示图像
plt.figure(figsize=(10, 5))  # width * height
titles = [u'原始图像256灰度级', u'以4灰度级显示 ', u'以2灰度级显示']
images = [img, new_img1, new_img2]
for i in range(3):
   plt.subplot(1,3,i+1), plt.imshow(images[i], 'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()


#最近领域内插法扩大分辨率

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import transform,data
import matplotlib.pyplot as plt


# 读取原始图像
img1 = con_3#cv2.imread('2.3.jpg')  #128*128像素
img2 = con_4#cv2.imread('2.4.jpg')  #64*64像素
img3 = con_5#cv2.imread('2.5.jpg')  #32*32像素

#获取图像的高度和宽度
height1 = img1.shape[0]
width1 = img1.shape[1]
height2 = img2.shape[0]
width2 = img2.shape[1]
height3 = img3.shape[0]
width3 = img3.shape[1]

# 最近邻内插法分别将其放大到1024×1024像素
newimg1=cv2.resize(img1,(width1*8,height1*8),interpolation=cv2.INTER_NEAREST)  #128*128 to 1024*1024
newimg2=cv2.resize(img2,(width2*16,height2*16),interpolation=cv2.INTER_NEAREST) #64*64 to 1024*1024
newimg3=cv2.resize(img3,(width3*32,height3*32),interpolation=cv2.INTER_NEAREST) #32*32 to 1024*1024

#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize=(12, 6))  # width * height
plt.subplot(131), plt.imshow(newimg1, cmap = 'gray')
plt.title('最近领域内插法 128*128 to 1024*1024')
plt.subplot(132), plt.imshow(newimg2, cmap = 'gray')
plt.title('最近领域内插法 64*64 to 1024*1024')
plt.subplot(133), plt.imshow(newimg3, cmap = 'gray')
plt.title('最近领域内插法 32*32 to 1024*1024')
plt.show()


#双线性内插法扩大分辨率

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import transform,data
import matplotlib.pyplot as plt


# 读取原始图像
img1 = con_3#cv2.imread('2.3.jpg')  #128*128像素
img2 = con_4#cv2.imread('2.4.jpg')  #64*64像素
img3 = con_5#cv2.imread('2.5.jpg')  #32*32像素

#获取图像的高度和宽度
height1 = img1.shape[0]
width1 = img1.shape[1]
height2 = img2.shape[0]
width2 = img2.shape[1]
height3 = img3.shape[0]
width3 = img3.shape[1]

# 双线性内插法分别将其放大到1024×1024像素
newimg1=cv2.resize(img1,(width1*8,height1*8),interpolation=cv2.INTER_LINEAR)  #128*128 to 1024*1024
newimg2=cv2.resize(img2,(width2*16,height2*16),interpolation=cv2.INTER_LINEAR)  #64*64 to 1024*1024
newimg3=cv2.resize(img3,(width3*32,height3*32),interpolation=cv2.INTER_LINEAR)  #32*32 to 1024*1024

#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize=(12, 6))  # width * height
plt.subplot(131), plt.imshow(newimg1, cmap = 'gray')
plt.title('双线性内插法 128*128 to 1024*1024')
plt.subplot(132), plt.imshow(newimg2, cmap = 'gray')
plt.title('双线性内插法 64*64 to 1024*1024')
plt.subplot(133), plt.imshow(newimg3, cmap = 'gray')
plt.title('双线性内插法 32*32 to 1024*1024')
plt.show()


