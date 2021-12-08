#第三章 空域图像增强


import cv2 as cv
import numpy as np
import math
from matplotlib import pyplot as plt

# x = np.random.normal(size=1000)
# y = np.random.normal(size=1000)
# pg.plot(x, y, pen=None, symbol='o')

pi=3.14159265
##########
class CH3_API:
    # def __init__(self):

##########################1. 图像反转
    def p2_Opposite_Tranform(self,img):
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        height = img.shape[0]
        width = img.shape[1]
        img_opposite = img.copy()  #将原图像赋给一个新的变量，便于后续处理
        for i in range(height):
            for j in range(width):
                img_opposite[i, j] = 255-img_opposite[i, j]
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("图像反转",figsize=(12, 7))
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title("原图"), plt.axis('off')
        plt.subplot(122), plt.imshow(img_opposite, cmap='gray')
        plt.title("图像反转"), plt.axis('off')
        plt.show()

    ##########################2. 对数变换
    def p2_log_Tranform(self,img, c_input):
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            def Tranform_log(img, c):
                if np.ndim(img) == 3:
                    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                height = img.shape[0]
                width = img.shape[1]
                img_new = np.zeros_like(img, dtype=np.float32)  # 创建同尺寸的二维 0-矩阵
                for i in range(height):  # 遍历全图
                    for j in range(width):
                        img_new[i, j] = c * math.log(1 + img[i, j])  # 像素值对数变换
                cv.normalize(img_new, img_new, 0, 255, cv.NORM_MINMAX)  # 图像归一化到0到255
                img_new = cv.convertScaleAbs(img_new)  # 图像取绝对
                return img_new
        image_log_input = Tranform_log(img, c=c_input)
        image_log_1 = Tranform_log(img, c=0.5)
        image_log_10 = Tranform_log(img, c=10)
        image_log_50 = Tranform_log(img, c=50)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("对数变换",figsize=(12, 7))
        plt.subplot(231), plt.imshow(img, cmap='gray')
        plt.title("原图"), plt.axis('off')
        plt.subplot(232), plt.imshow(image_log_1, cmap='gray')
        plt.title("对数变换(c=0.5)"), plt.axis('off')
        plt.subplot(233), plt.imshow(image_log_10, cmap='gray')
        plt.title("对数变换(c=10)"), plt.axis('off')
        plt.subplot(235), plt.imshow(image_log_50, cmap='gray')
        plt.title("对数变换(c=50)"), plt.axis('off')
        plt.subplot(236), plt.imshow(image_log_input, cmap='gray')
        plt.title("对数变换自定义\n(c="+str(c_input)+")"), plt.axis('off')
        plt.show()


    ##########################3. 幂次变换
    def p2_Power_Transform(self,img, L_input):
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        def Transform_MI(img, c, l):
            if np.ndim(img) == 3:
                img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            height = img.shape[0]
            width = img.shape[1]
            img_new = np.zeros((height, width), dtype= np.float32)  #创建同尺寸的二维 0-矩阵
            for i in range(height):     #遍历全图
                for j in range(width):
                    value = img[i, j]
                    img_new[i, j] = c * value ** l       #像素值幂次变换

            cv.normalize(img_new, img_new, 0, 255, cv.NORM_MINMAX)
            img_new = cv.convertScaleAbs(img_new)
            return img_new

        image_MI_input = Transform_MI(img, c=1, l=L_input)
        image_MI_1 = Transform_MI(img, c=1, l=0.5)
        image_MI_2 = Transform_MI(img, c=1, l=2.0)
        image_MI_6 = Transform_MI(img, c=1, l=6.0)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("直方图匹配", figsize=(12, 7))
        plt.subplot(231), plt.imshow(img, cmap='gray')
        plt.title("原图"), plt.axis('off')
        plt.subplot(232), plt.imshow(image_MI_1, cmap='gray')
        plt.title("幂次变换(幂次=0.5)"), plt.axis('off')
        plt.subplot(233), plt.imshow(image_MI_2, cmap='gray')
        plt.title("幂次变换(幂次=2)"), plt.axis('off')
        plt.subplot(235), plt.imshow(image_MI_6, cmap='gray')
        plt.title("幂次变换(幂次=5)"), plt.axis('off')
        plt.subplot(236), plt.imshow(image_MI_input, cmap='gray')
        plt.title("幂次变换自定义\n(幂次="+str(L_input)+")"), plt.axis('off')
        plt.show()

    ##########################4. 分段图像变换
    def p2_FenDuan_Transform(self,img, point_x, point_y):
        # point_x = np.array([90, 150])
        # point_y = np.array([50, 200])
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        height = img.shape[0]
        width = img.shape[1]
        point_all = img.flatten()
        point_max = np.max(point_all)
        y = [[] for _ in range(4)]

    #1  画出分段函数图像
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("分段图像变换",figsize=(12, 7))
        plt.subplot(222)
        x0 = np.linspace(0, point_x[0], point_x[0])     #给出分段函数图中该段中 X的范围，并规定点的数量
        for v in x0:
            y[0].append(point_y[0] / point_x[0] * v)    #计算出对应 Y的范围
        plt.plot(x0, y[0], 'b')                         #画出该段函数图像
    #2
        x1 = np.linspace(point_x[0], point_x[1], point_x[1]-point_x[0])
        for v in x1:
            y[1].append((point_y[0]-point_y[1])/(point_x[0]-point_x[1])*(v-point_x[0])+point_y[0])
        plt.plot(x1, y[1], 'b')
    #3
        x2 = np.linspace(point_x[1], point_max, point_max-point_x[1])
        for v in x2:
            y[2].append((point_y[1]-point_max)/(point_x[1]-point_max)*(v-point_x[1])+point_y[1])
        plt.plot(x2, y[2], 'b')
    #4
        plt.subplot(221)
        x3 = np.linspace(0, point_max, point_max)       #画出原函数图像
        for v in x3:
            y[3].append(v)
        plt.plot(x3, y[3], 'r')

        img_new = np.zeros((height, width), dtype= np.float32)
        for i in range(height):
            for j in range(width):
                v = img[i,j]
                if v < point_x[0]:
                    img_new[i,j] = point_y[0] / point_x[0] * v
                elif v > point_x[1]:
                    img_new[i,j] = (point_y[1]-point_max)/(point_x[1]-point_max)*(v-point_x[1])+point_y[1]
                else:
                    img_new[i,j] = (point_y[0]-point_y[1])/(point_x[0]-point_x[1])*(v-point_x[0])+point_y[0]

        img_new = cv.convertScaleAbs(img_new)
        plt.subplot(223), plt.imshow(img, cmap='gray')
        plt.title("原图"), plt.axis('off')
        plt.subplot(224), plt.imshow(img_new, cmap='gray')
        plt.title("分段图像变换"), plt.axis('off')
        plt.show()

    ##########################5. 直方图均衡化
    def p3_Hist_Equalize(self,img):
        # img = cv.imread("boat.jpg")
        if np.ndim(img)==3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img_new = cv.equalizeHist(img)                             #图像灰度直方图均衡化
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("直方图匹配", figsize=(12, 7))
        plt.subplot(221), plt.hist(img.flatten(), 256, [0, 256])
        plt.subplot(222), plt.hist(img_new.flatten(), 256, [0, 256], color='r')
        plt.subplot(223), plt.imshow(img, cmap='gray'),plt.title("原图"), plt.axis('off')
        plt.subplot(224), plt.imshow(img_new, cmap='gray'),plt.title("直方图均衡化"), plt.axis('off')
        plt.show()

    ##########################5. 直方图匹配
    def p3_Hist_Match(self,img,img_ref):
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        height = int(img.shape[0]/2 )
        width = int(img.shape[1]/2)

        img = cv.resize(img, (width, height))
        # img_ref = cv.imread("room.jpg")                             #读取图像
        img_ref_gray = cv.cvtColor(img_ref, cv.COLOR_BGR2GRAY)      #图像转化为灰度图
        height_ref, width_ref = img_ref_gray.shape                  #获取图像尺寸
        img_ref_gray = cv.resize(img_ref_gray, (int(width_ref/2), int(height_ref/2)))
        img_new = np.zeros((height, width), dtype= np.uint8)

        hist_img, _ = np.histogram(img, 256)       #获取图像直方图
        hist_ref, _ = np.histogram(img_ref_gray, 256)

        cdf_img = np.cumsum(hist_img)       #依次行叠加
        cdf_ref = np.cumsum(hist_ref)
        cdf_img=cdf_img/max(cdf_img)
        cdf_ref=cdf_ref/max(cdf_ref)

        for j in range(256):
            tmp = abs(cdf_img[j] - cdf_ref)     #找到和参考图像当前灰度像素数量累加值最接近的与原图像灰度像素数量累加值
            tmp = tmp.tolist()
            # print(tmp)
            idx = tmp.index(min(tmp))
            print(idx)
            img_new[img == j] = idx             #将参考图像中确定的灰度值赋值给原图，完成匹配

        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("直方图匹配",figsize=(12, 7))  # width * height
        plt.subplot(231), plt.hist(img.flatten(), 256, [0, 256])
        plt.title("Image")
        plt.subplot(232), plt.hist(img_ref_gray.flatten(), 256, [0, 256], color='g')
        plt.title("Reference")
        plt.subplot(233), plt.hist(img_new.flatten(), 256, [0, 256], color='r')
        plt.title("Match_result")
        plt.subplot(234), plt.imshow(img, cmap='gray')
        plt.title("原图"), plt.axis('off')
        plt.subplot(235), plt.imshow(img_ref_gray, cmap='gray')
        plt.title("匹配参考图像"), plt.axis('off')
        plt.subplot(236), plt.imshow(img_new, cmap='gray')
        plt.title("图像直方图匹配结果"), plt.axis('off')
        plt.show()




    def p4_convolutional_filter(self,img,kernel_list):
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        kernel = np.array(kernel_list, dtype="float32")
        img_res1 = cv.filter2D(img, -1, kernel)
        img_res2 = self.self_defined_convolution(img, kernel)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("卷积线性滤波", figsize=(12, 7))
        plt.subplot(131), plt.imshow(img, cmap='gray'),plt.title("原图"), plt.axis('off')
        plt.subplot(132), plt.imshow(img_res1, cmap='gray'),plt.title("opencv库函数"), plt.axis('off')
        plt.subplot(133), plt.imshow(img_res2, cmap='gray'),plt.title("手写卷积"), plt.axis('off')
        plt.show()

    def self_defined_convolution(self,img,kernel,str="smooth"):
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        edge = int((kernel.shape[0]-1)/2)
        img_res = np.zeros_like(img,np.uint16)
        img_normal=np.zeros_like(img,np.uint8)
        print(img.shape[0],img.shape[1]  )
        for i in range(edge, img.shape[0] - edge):  # 遍历全图
            for j in range(edge, img.shape[1] - edge):
                sum = 0
                for m in range(-edge, edge + 1):
                    for n in range(-edge, edge + 1):
                        sum = sum + kernel[m][n]*img[i+m][j+n]
                img_res[i][j]=abs(sum)
        if str == "smooth":
            cv.normalize(img_res,img_res, 0, 255, cv.NORM_MINMAX)#输入输出的数据类型一定要匹配，如果16位输入而8位接输出则会导致前八位截断
        elif str == "sharp":
            img_res[img_res > 255] = 255  # 上限限幅
        img_normal = img_res.copy()
        return img_normal

    def p4_smooth_boxfilter(self,img):
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        kernel= np.array([[1,1,1],[1,1,1],[1,1,1]])
        img_result=self.self_defined_convolution(img,kernel,"smooth")
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("线性盒状平滑滤波", figsize=(12, 7))
        plt.subplot(121), plt.imshow(img, cmap='gray'),plt.title("原图"), plt.axis('off')
        plt.subplot(122), plt.imshow(img_result, cmap='gray'),plt.title("盒装平滑滤波\n[1, 1, 1]\n[1, 1, 1],\n[1, 1, 1]"), plt.axis('off')
        plt.show()

    def p4_smooth_weightfilter(self, img):
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
        img_result = self.self_defined_convolution(img, kernel,"smooth")
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("线性加权平滑滤波（欧式距离）", figsize=(12, 7))
        plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title("原图"), plt.axis('off')
        plt.subplot(122), plt.imshow(img_result, cmap='gray'), plt.title("线性加权平滑滤波（欧式距离）\n[1, 2, 1]\n[2, 4, 2],\n[1, 2, 1]"), plt.axis('off')
        plt.show()

    def p4_smooth_middlefilter(self,img):#中值（中位数）平滑滤波器
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img_res = np.zeros_like(img,np.uint8)
        edge = 1
        for i in range(edge, img.shape[0] - edge):  # 遍历全图
            for j in range(edge, img.shape[1] - edge):
                sum =[]
                for m in range(-edge, edge + 1):
                    for n in range(-edge, edge + 1):
                        sum.append(img[i+m][j+n])
                sum.sort()
                img_res[i][j]=sum[5]
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("统计中值平滑滤波", figsize=(12, 7))
        plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title("原图"), plt.axis('off')
        plt.subplot(122), plt.imshow(img_res, cmap='gray'), plt.title("统计中值平滑滤波"), plt.axis('off')
        plt.show()



    def p4_sharpen_Roberts(self, img):  # 用拉普拉斯算子锐化，提边缘后叠加在原图，则可以直接在模板阶段合并成一个
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        def pic_Roberts_edge(img):
            kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
            kernely = np.array([[0, -1], [1, 0]], dtype=int)
            x = cv.filter2D(img, cv.CV_16S, kernelx)
            y = cv.filter2D(img, cv.CV_16S, kernely)
            # 转uint8
            absX = cv.convertScaleAbs(x)
            absY = cv.convertScaleAbs(y)
            Roberts = cv.addWeighted(absX, 0.5, absY, 0.5, 0)
            return Roberts

        img_edge = pic_Roberts_edge(img)
        img_sharp = img.astype(np.uint16) + img_edge.astype(np.uint16)  # 相加之前需要先扩充数据范围，否则数据将会被砍脖子
        img_sharp[img_sharp > 255] = 255  # 上限限幅
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("Roberts锐化滤波", figsize=(12, 7))
        plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title("原图"), plt.axis('off')
        plt.subplot(132), plt.imshow(img_edge, cmap='gray'), plt.title("Roberts提取边缘结果"), plt.axis('off')
        plt.subplot(133), plt.imshow(img_sharp, cmap='gray'), plt.title("叠加在原图上的锐化结果"), plt.axis('off')
        plt.show()

    def p4_sharpen_Prewitt(self,img):#用拉普拉斯算子锐化，提边缘后叠加在原图，则可以直接在模板阶段合并成一个
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        def pic_Prewitt_edge(img):
            kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
            kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
            x = cv.filter2D(img, cv.CV_16S, kernelx)
            y = cv.filter2D(img, cv.CV_16S, kernely)
            # 转uint8
            absX = cv.convertScaleAbs(x)
            absY = cv.convertScaleAbs(y)
            result_Prewitt = cv.addWeighted(absX, 0.5, absY, 0.5, 0)
            return result_Prewitt

        img_edge = pic_Prewitt_edge(img)
        print(img_edge)
        img_sharp = img.astype(np.uint16) + img_edge.astype(np.uint16)#相加之前需要先扩充数据范围，否则数据将会被砍脖子
        img_sharp[img_sharp > 255] = 255  # 上限限幅
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("Prewitt锐化滤波", figsize=(12, 7))
        plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title("原图"), plt.axis('off')
        plt.subplot(132), plt.imshow(img_edge, cmap='gray'), plt.title("Prewitt提取边缘结果"), plt.axis('off')
        plt.subplot(133), plt.imshow(img_sharp, cmap='gray'), plt.title("叠加在原图上的锐化结果"), plt.axis('off')
        plt.show()

    def p4_sharpen_Sobel(self,img):#用拉普拉斯算子锐化，提边缘后叠加在原图，则可以直接在模板阶段合并成一个
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        def pic_sobel_edge(img):#手写sobel边缘提取算法
            x = cv.Sobel(img, cv.CV_16S, 1, 0)
            y = cv.Sobel(img, cv.CV_16S, 0, 1)
            absx = cv.convertScaleAbs(x)
            absy = cv.convertScaleAbs(y)
            result_sobel = cv.addWeighted(absx, 0.5, absy, 0.5, 0)
            return result_sobel

        img_edge = pic_sobel_edge(img)
        img_sharp = img.astype(np.uint16) + img_edge.astype(np.uint16)#相加之前需要先扩充数据范围，否则数据将会被砍脖子
        img_sharp[img_sharp>255]=255#上限限幅
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("Sobel锐化滤波", figsize=(12, 7))
        plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title("原图"), plt.axis('off')
        plt.subplot(132), plt.imshow(img_edge, cmap='gray'), plt.title("Sobel提取边缘结果"), plt.axis('off')
        plt.subplot(133), plt.imshow(img_sharp, cmap='gray'), plt.title("叠加在原图上的锐化结果"), plt.axis('off')
        plt.show()

    def p4_sharpen_Laplace(self,img):#用拉普拉斯算子锐化，提边缘后叠加在原图，则可以直接在模板阶段合并成一个
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        kernel= np.array([[0,-1, 0],[-1,4,-1],[0,-1,0]])
        img_edge = self.self_defined_convolution(img, kernel,"sharp")
        img_sharp = img.astype(np.uint16) + img_edge.astype(np.uint16)  # 相加之前需要先扩充数据范围，否则数据将会被砍脖子
        img_sharp[img_sharp > 255] = 255  # 上限限幅
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("拉普拉斯锐化滤波", figsize=(12, 7))
        plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title("原图"), plt.axis('off')
        plt.subplot(132), plt.imshow(img_edge, cmap='gray'), plt.title("拉普拉斯锐化提取边缘"), plt.axis('off')
        plt.subplot(133), plt.imshow(img_sharp, cmap='gray'), plt.title("拉普拉斯锐化滤波"), plt.axis('off')
        plt.show()

    def p4_edge_canny(self,img):#用Canny算子提取边缘
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.GaussianBlur(img, (3, 3), 0)
        img_edge = cv.Canny(img,10,100)#200是可调的阈值
        img_sharp = img.astype(np.uint16) + img_edge.astype(np.uint16)  # 相加之前需要先扩充数据范围，否则数据将会被砍脖子
        img_sharp[img_sharp > 255] = 255  # 上限限幅
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("Canny边缘提取", figsize=(12, 7))
        plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title("原图"), plt.axis('off')
        plt.subplot(122), plt.imshow(img_edge, cmap='gray'), plt.title("Canny边缘提取算法"), plt.axis('off')
        plt.show()









