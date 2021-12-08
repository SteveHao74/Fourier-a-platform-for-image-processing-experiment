

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import  skimage




#
#
def getGrayDiff(img,currentPoint,targetPoint):
    # print(abs(img[currentPoint[0]][currentPoint[1]]-img[targetPoint[0]][targetPoint[1]]))
    return abs(img[currentPoint[0]][currentPoint[1]]-img[targetPoint[0]][targetPoint[1]])

#区生长
def regional_growth(gray,seeds,threshold=15):
    connects = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]#[(-1,-1),(-1,0),(-1,1),(1,-1),(0,-1),(1,1),(1,0),(0,1)]
    height,weight = gray.shape
    seedMark = np.zeros(gray.shape,np.uint8)
    seedList=list(seeds)
    print(seedList)
    while(len(seedList)>0):
        currentPoint = seedList.pop(0)
        seedMark[currentPoint[0],currentPoint[1]]=255
        for i in range(4):
            tmpx = currentPoint[0]+connects[i][0]
            tmpy = currentPoint[1]+connects[i][1]
            if tmpx<0 or tmpy<0 or tmpx >= height or tmpy >= weight:
                continue
            grayDiff = getGrayDiff(gray,currentPoint,(tmpx,tmpy))
            if grayDiff < threshold and seedMark[tmpx,tmpy]==0:
                seedMark[tmpx,tmpy] = 255
                seedList.append((tmpx,tmpy))
    print(seedMark)
    return seedMark

img = cv2.imread("pic/hanfeng.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img = cv2.GaussianBlur(img,(3,3),0)
imghilght=img.copy()
imghilght[imghilght < 240] = 0
imgline=np.zeros_like(img)
seed=edge = cv2.Canny(img,10,100)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3 ))
edge = cv2.morphologyEx(edge, cv2.MORPH_CLOSE, kernel,iterations=3)
edge1 = edge+imghilght
marker = np.min((edge1, img), axis=0)
# edge = cv2.morphologyEx(edge, cv2.MORPH_CLOSE, kernel,iterations=3)
# lines=cv2.HoughLinesP(edge,1,np.pi/180,5,20,5)

x,y = np.where(marker > 180)
seedlist = list(zip(x, y))
print(seedlist)
# seedlist=[(103,192),(222,191),(331,183)]
result=regional_growth(marker,seedlist,22)

plt.rcParams['font.sans-serif']=['SimHei']
# 图像显示
plt.figure(figsize=(16, 5))  # width * height
plt.subplot(2, 3, 1), plt.imshow(img, cmap='gray'), plt.title('原始图像'), plt.axis("off")
plt.subplot(2, 3, 2), plt.imshow(seed, cmap='gray'), plt.title('canny提取边缘'), plt.axis("off")
plt.subplot(2, 3, 3), plt.imshow(edge1, cmap='gray'), plt.title('边缘做闭运算填充\n从而标记出大致分割区域'), plt.axis("off")
plt.subplot(2, 3,4), plt.imshow(marker, cmap='gray'), plt.title('按照带分割区域标记\n从原图中分割出来粗略结果'), plt.axis("off")
plt.subplot(2, 3,5), plt.imshow(result, cmap='gray'), plt.title("使用生长算法在粗略分割的基础上得出精细结果"), plt.axis("off")
plt.show()

def pic_sobel_edge(img):
    x= cv2.Sobel(img,cv2.CV_16S,1,0)
    y= cv2.Sobel(img,cv2.CV_16S,0,1)
    absx = cv2.convertScaleAbs(x)
    absy = cv2.convertScaleAbs(y)
    result_sobel = cv2.addWeighted(absx,0.5,absy,0.5,0)
    return result_sobel

def pic_Prewitt_edge(img):
    kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
    kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
    x = cv2.filter2D(img, cv2.CV_16S, kernelx)
    y = cv2.filter2D(img, cv2.CV_16S, kernely)
    # 转uint8
    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    result_Prewitt = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
    return result_Prewitt

img = cv2.imread("pic/6.8.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img = cv2.GaussianBlur(img,(3,3),0)

result_Prewitt=pic_Prewitt_edge(img)
result_sobel = pic_sobel_edge(img)
result_canny = cv2.Canny(img,10,100)


plt.rcParams['font.sans-serif']=['SimHei']
# 图像显示
plt.figure(figsize=(16, 10))  # width * height
plt.subplot(2, 2, 1), plt.imshow(img), plt.title('原始图像'), plt.axis("off")
plt.subplot(2, 2, 2), plt.imshow(result_Prewitt), plt.title('Prewitt提取边缘'), plt.axis("off")
plt.subplot(2, 2, 3), plt.imshow(result_sobel), plt.title('sobel提取边缘'), plt.axis("off")
plt.subplot(2, 2, 4), plt.imshow(result_canny), plt.title('canny提取边缘'), plt.axis("off")
plt.show()






# class CH9_API:
#     def __init__(self):
#
#
#     #【9.1基础操作】 腐蚀，膨胀，开，闭操作:
#     # #传参：核，锚点，图像
#     def basic_operation(self,kernel,anchor,img=[]):
#         if img ==[]:#使用以上默认像素图
#             img =self.img_pre
#         # 腐蚀图像
#         img_eroded = cv2.erode(img, kernel,iterations = 1,anchor=(anchor[1],anchor[0]))
#         #膨胀图像
#         img_dilated= cv2.dilate(img, kernel,iterations = 1,anchor=(anchor[1],anchor[0]))
#         #将两幅图像相减获得边；cv2.absdiff参数：(膨胀后的图像，腐蚀后的图像)
#         absdiff_img = cv2.absdiff(img_dilated, img_eroded);
#         #上面得到的结果是灰度图，将其二值化以便观察结果
#         retval, threshold_img = cv2.threshold(absdiff_img, 40, 255, cv2.THRESH_BINARY);
#         img_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)#开或关操作内部抵消不需要标记锚点
#         img_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)  # 图像闭运算，
#         #用来正常显示中文标签
#         plt.rcParams['font.sans-serif']=['SimHei']
#         kernel[anchor[0]][anchor[1]]=127#把锚点标出来
#         plt.figure(figsize=(10, 5))  # width * height
#         plt.subplot(241), plt.imshow(img, cmap = 'gray'),plt.title('原始图像'),plt.axis("off")
#         plt.subplot(242), plt.imshow(kernel, cmap='gray'), plt.title('核，灰色为锚点'), plt.axis("off")
#         plt.subplot(243), plt.imshow(img_eroded, cmap = 'gray'),plt.title('图像腐蚀'),plt.axis("off")
#         plt.subplot(244), plt.imshow(img_dilated, cmap='gray'), plt.title('图像膨胀'), plt.axis("off")
#         plt.subplot(245), plt.imshow(threshold_img, cmap='gray'), plt.title('内外边界：膨胀-腐蚀'), plt.axis("off")
#         plt.subplot(246), plt.imshow(img_open, cmap = 'gray'),plt.title('图像开操作'),plt.axis("off")
#         plt.subplot(247), plt.imshow(img_close, cmap='gray'), plt.title('图像闭操作'), plt.axis("off")
#         plt.show()
#
#     #【9.2】形态学处理进行区域填充（孔洞填充）
#     def hole_filling(self,kernel,anchor,iteration,img =[]):#pic/9.4.jpg
#         #读取图像
#         print(kernel)
#         if img ==[]:#使用以上默认像素图
#             img =cv2.imread("pic/9.4.jpg")
#         # 二值化
#         # imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         imgray=img
#         imgray[imgray < 100] = 0
#         imgray[imgray >= 100] = 255
#         # 对原图取补得到MASK图像
#         mask = 255 - imgray
#         # 构造Marker图像
#         marker = np.zeros_like(imgray)
#         marker[0, :] = 255
#         marker[-1, :] = 255
#         marker[:, 0] = 255
#         marker[:, -1] = 255
#         marker_0 = marker.copy()
#         # 形态学重建
#         #设置卷积核
#
#         # 矩形：MORPH_RECT;
#         #
#         # 交叉形：MORPH_CROSS;
#         #
#         # 椭圆形：MORPH_ELLIPSE;
#         # kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
#         i=0
#         while True:
#             marker_pre = marker
#             dilation = cv2.dilate(marker, kernel,(anchor[1],anchor[0]))#通过传参的方式共享第二部分的核
#             marker = np.min((dilation, mask), axis=0)
#             if (marker_pre == marker).all():
#                 break
#             i = i + 1
#             if i%iteration==0:
#                 plt.rcParams['font.sans-serif'] = ['SimHei']
#                 plt.figure(figsize=(16, 5))
#                 plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title('原始图像'), plt.axis("off")
#                 plt.subplot(1, 3, 2), plt.imshow(kernel, cmap='gray'), plt.title('核'), plt.axis("off")
#                 plt.subplot(1, 3, 3), plt.imshow(marker, cmap='gray'), plt.title('区域填充第'+str(i)+'次迭代的marker图\n未完待续'), plt.axis("off")
#                 plt.show()
#
#         result = 255 - marker
#         #用来正常显示中文标签
#         plt.rcParams['font.sans-serif']=['SimHei']
#         # 图像显示
#         plt.figure(figsize=(16, 5))  # width * height
#         plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('原始图像'), plt.axis("off")
#         plt.subplot(1, 2, 2), plt.imshow(result, cmap='gray'), plt.title('填充完成,共'+str(i)+"次迭代\n最终图像通过对marker取反得到"), plt.axis("off")
#         plt.show()

