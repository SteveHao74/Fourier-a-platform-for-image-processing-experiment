#第五章 图像复原
from matplotlib import pyplot as plt
import numpy as np
from numpy import fft
import cv2 as cv
import math
# from pylab import mpl
pi=3.14159265
# mpl.rcParams['font.sans-serif'] = ['STZhongsong']    # 指定默认字体：解决plot不能显示中文问题


class CH5_API:
    #加性椒盐噪声：
    def __init__(self):
        self.additive_noise_pic=[]#p2
        self.periodic_noise_pic=[]#p3
        self.periodic_noise_fft=[]#p3

    def p2_additive_noise_pepper_salt(self,img,percentage,id):
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img_ps, img_pepper, img_salt = self.PepperandSalt(img, percentage)  # 椒盐噪声+椒噪声+盐噪声
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("加性噪声图像")
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title("原图"), plt.axis('off')
        if id == 0 :
            self.additive_noise_pic = img_pepper
            plt.subplot(122), plt.imshow(img_pepper, cmap='gray')
            plt.title("椒噪声"), plt.axis('off')
        elif id == 1:
            self.additive_noise_pic = img_salt
            plt.subplot(122), plt.imshow(img_salt, cmap='gray')
            plt.title("盐噪声"), plt.axis('off')
        elif id == 2:
            self.additive_noise_pic = img_ps
            plt.subplot(122), plt.imshow(img_ps, cmap='gray')
            plt.title("椒盐噪声"), plt.axis('off')
        plt.show()
    # 椒盐噪声
    def PepperandSalt(self , src, percetage):  # percetage：椒盐噪声生成百分比
        NoiseImg = src.copy()
        NoiseImg_1 = NoiseImg.copy()
        NoiseImg_2 = NoiseImg.copy()
        NoiseNum = int(percetage * src.shape[0] * src.shape[1])
        for i in range(NoiseNum):
            randX = np.random.random_integers(0, src.shape[0] - 1)  # 随机确定噪声坐标
            randY = np.random.random_integers(0, src.shape[1] - 1)
            if np.random.random_integers(0, 1) <= 0.5:  # 随机选取噪声种类（椒或盐）
                NoiseImg[randX, randY] = 0
            else:
                NoiseImg[randX, randY] = 255

            NoiseImg_1[randX, randY] = 0  # 随机位置生成椒噪声
            NoiseImg_2[randX, randY] = 255  # 随机位置生成盐噪声
        return NoiseImg, NoiseImg_1, NoiseImg_2
    ############################################
    def p2_additive_noise_gasuss(self,img,mean):
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img_gasuss = self.gasuss_noise(img, mean, 0.005)  # 高斯噪声
        self.additive_noise_pic = img_gasuss
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("加性噪声图像")
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title("原图"), plt.axis('off')
        plt.subplot(122), plt.imshow(img_gasuss, cmap='gray')
        plt.title("高斯噪声"), plt.axis('off')
        plt.show()
    #高斯噪声
    def gasuss_noise(self,img, mean, var):     #mean：高斯噪声均值； var：高斯噪声方差
        image=img.copy()
        image = np.array(image/255, dtype=np.float32)     #图像归一化到（0，1）
        noise = np.random.normal(mean, var ** 0.5, image.shape)       #生成高斯分布的随机噪声
        noiseImg = image + noise     #将噪声叠加到原图中
        if noiseImg.min() < 0:       #确定噪声图像下界
            low_clip = -1.
        else:
            low_clip = 0.
        noiseImg = np.clip(noiseImg, low_clip, 1.0)     #规定噪声图像上下界
        noiseImg = np.uint8(noiseImg*255)               #将图像归一化到（0， 255）
        return noiseImg

#############################################part2空间域滤波#######################
##################均值###################
    #均值滤波：算术，几何
    def p2_mean_filter(self,img):
        size = 3
        img_means = cv.blur(img, (size, size))  # 算数均值滤波
        img_geomeans = self.Blur_Geomean(img, size)  # 几何均值滤波
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("均值滤波")
        plt.subplot(221), plt.imshow(img, cmap='gray')
        plt.title("噪声图像"), plt.axis('off')
        plt.subplot(223), plt.imshow(img_means, cmap='gray')
        plt.title("算术均值滤波（适用于均匀分布噪声）"), plt.axis('off')
        plt.subplot(224), plt.imshow(img_geomeans, cmap='gray')
        plt.title("几何均值滤波（适用于均匀分布噪声）"), plt.axis('off')
        plt.show()
    ############几何均值滤波
    def Blur_Geomean(self,image, size):
        edge = int((size - 1) / 2)
        image_Geomean = image.copy()
        value = []

        for i in range(edge, image.shape[0] - edge):    #遍历全图
            for j in range(edge, image.shape[1] - edge):
                for m in range(-edge, edge + 1):
                    for n in range(-edge, edge + 1):
                        value.append(image[i + m, j + n])
                value_array = np.array(value)
                value_array = value_array.astype(np.float32)
                value_product = np.prod(value_array)     #数组求积
                image_Geomean[i,j] = value_product ** (1/float(size*size))      #获取新的滤波值
                value.clear()
        image_Geomean = cv.convertScaleAbs(image_Geomean)

        return image_Geomean

######################谐波###############
    def p2_Harmonic_filter(self,img):
        image_Harmonic = self.Harmonic(img, size=3)  # 谐波滤波
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("谐波滤波")
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title("盐噪声图像"), plt.axis('off')
        plt.subplot(122), plt.imshow(image_Harmonic, cmap='gray')
        plt.title("谐波滤波"), plt.axis('off')
        plt.show()

    # #谐波滤波
    def Harmonic(self,image, size):  # size：窗口尺寸
        edge = int((size - 1) / 2)
        image_Harmonic = np.zeros(image.shape, dtype=np.float32)
        value = []

        for i in range(edge, image.shape[0] - edge):  # 遍历全图
            for j in range(edge, image.shape[1] - edge):
                for m in range(-edge, edge + 1):
                    for n in range(-edge, edge + 1):
                        value.append(image[i + m, j + n])
                value_array = np.array(value)
                value_array = value_array.astype(np.float32)
                value_sum = np.sum(1.0 / (value_array+0.01))
                image_Harmonic[i, j] = float(size * size) / value_sum  # 谐波滤波算法
                value.clear()
        cv.normalize(image_Harmonic, image_Harmonic, 0, 255, cv.NORM_MINMAX)  # 图像归一化
        image_Harmonic = cv.convertScaleAbs(image_Harmonic)
        return image_Harmonic

###################逆滤波###################
    def p2_inverse_Harmonic(self,img):
        img_Inverse_Harmonic_salt = self.Inverse_Harmonic(img, size=3, Q=-1.5)  # 逆谐波滤波：Q<0
        img_Inverse_Harmonic_pepper = self.Inverse_Harmonic(img, size=3, Q=1.5)  # 逆谐波滤波：Q>0
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("逆谐波滤波")
        plt.subplot(131), plt.imshow(img, cmap='gray')
        plt.title("噪声图"), plt.axis('off')
        plt.subplot(132), plt.imshow(img_Inverse_Harmonic_salt, cmap='gray')
        plt.title("逆谐波滤波（Q<0）\n适用于盐噪声"), plt.axis('off')
        plt.subplot(133), plt.imshow(img_Inverse_Harmonic_pepper, cmap='gray')
        plt.title("逆谐波滤波（Q>0）\n适用于椒噪声"), plt.axis('off')
        plt.show()


    # 逆谐波滤波
    def Inverse_Harmonic(self,image, size, Q):  # Q：逆谐波滤波参数
        value_1 = []
        value_2 = []
        edge = int((size - 1) / 2)
        image_xiebo = image.copy().astype(np.float32)
        for i in range(edge, image.shape[0] - edge):  # 遍历全图
            for j in range(edge, image.shape[1] - edge):
                for m in range(-edge, edge + 1):
                    for n in range(-edge, edge + 1):
                        point = image_xiebo[i + m, j + n] + 1
                        value_1.append(point ** (Q + 1))  # 逆谐波滤波算法
                        value_2.append(point ** Q)  # 当前点取 Q或 Q+1次方

                value_1_array = np.array(value_1)
                value_2_array = np.array(value_2)
                sum_1 = np.sum(value_1_array)  # 数组1求和
                sum_2 = np.sum(value_2_array)  # 数组2求和

                image_xiebo[i, j] = sum_1 / sum_2  # 确定新的像素点值
                value_1.clear()  # 元组1清空
                value_2.clear()  # 元组2清空
        image_xiebo = cv.convertScaleAbs(image_xiebo)
        return image_xiebo

##################统计排序#######################
    def p2_statistic_sort_filter(self,img):
        img_median = cv.medianBlur(img, 3)  # 中值滤波
        img_max, img_min = self.MinAndMan_Blur(img, size=3)  # 最大最小值滤波
        img_ZhongDian = self.ZhongDian_Blur(img, size=5)  # 中点滤波
        img_Alpha = self.Alpha_Blur(img, size=5, d=4)  # 阿尔法滤波
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("统计排序滤波")
        plt.subplot(231), plt.imshow(img, cmap='gray')
        plt.title("噪声图像"), plt.axis('off')
        plt.subplot(232), plt.imshow(img_median, cmap='gray')
        plt.title("中值滤波"), plt.axis('off')
        plt.subplot(233), plt.imshow(img_max, cmap='gray')
        plt.title("最大值滤波"), plt.axis('off')
        plt.subplot(234), plt.imshow(img_min, cmap='gray')
        plt.title("最小值滤波"), plt.axis('off')
        plt.subplot(235), plt.imshow(img_ZhongDian, cmap='gray')
        plt.title("中点滤波"), plt.axis('off')
        plt.subplot(236), plt.imshow(img_Alpha, cmap='gray')
        plt.title("阿尔法滤波"), plt.axis('off')
        plt.show()

    #最大最小值滤波
    def MinAndMan_Blur(self,image, size):    #size：窗口尺寸
        value = []
        edge = int((size-1)/2)
        image_min = image.copy()
        image_max = image.copy()
        for i in range(edge, image.shape[0] - edge):        #遍历全图
            for j in range(edge, image.shape[1] - edge):
                for m in range(-edge, edge+1):
                    for n in range(-edge, edge+1):
                        value.append(image[i+m, j+n])
                value_array = np.array(value)
                value_max = np.max(value_array)     #获取窗口内像素的最大值
                value_min = np.min(value_array)     #获取窗口内像素的最小值

                if image_max[i, j] >= value_max:    #当前点大于最大值，赋值为最大值
                    image_max[i, j] = value_max
                if image_min[i, j] <= value_min:    #当前点小于最小值，赋值为最小值
                    image_min[i, j ] = value_min
                value.clear()
        return image_max, image_min

    #中点滤波
    def ZhongDian_Blur(self,image, size):
        edge = int((size - 1) / 2)
        image_zhongdina =np.zeros_like(image,np.float32)

        for i in range(edge, image.shape[0] - edge):        #遍历全图
            for j in range(edge, image.shape[1] - edge):
                value_max = int(np.max(image[i - edge: i + edge + 1, j - edge: j + edge + 1]) )  #获取窗口内像素的最大值
                value_min = int(np.min(image[i - edge: i + edge + 1, j - edge: j + edge + 1]) )  #获取窗口内像素的最小值
                image_zhongdina[i,j] = (value_min+ value_max)/ 2    #最大最小值求均值

        image_zhongdina = np.clip(image_zhongdina, 0,255)
        return image_zhongdina

    ############################阿尔法滤波
    def Alpha_Blur(self,image, size, d):
        value = []
        value_index = []
        edge = int((size - 1) / 2)

        image_Alpha = image.copy()
        for i in range(edge, image.shape[0] - edge):    #遍历全图
            for j in range(edge, image.shape[1] - edge):
                for m in range(-edge, edge + 1):
                    for n in range(-edge, edge + 1):
                        value.append(image[i + m, j + n])
                value_array = np.array(value)
                value_array_order = np.sort(value_array)    #数组重新排序

                for k in range(int(d/2)):
                    value_index.append(k)
                    value_index.append(len(value_array)-k-1)
                index = np.array(value_index)
                value_array_rest = np.delete(value_array_order, index)
                image_Alpha[i, j] = int(np.average(value_array_rest))
                value_index.clear()
                value.clear()

        return image_Alpha

####################### 自适应中值滤波##########
    def p2_adaptive_median_filter(self,img):
        img_median = cv.medianBlur(img, 3)  # 中值滤波
        img_median_adapt = self.adaptiveMedianDeNoise(img, size_max=8)  # 自适应中值滤波
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("中值滤波对比")
        plt.subplot(221), plt.imshow(img, cmap='gray')
        plt.title("噪声图"), plt.axis('off')
        plt.subplot(223), plt.imshow(img_median, cmap='gray')
        plt.title("中值滤波"), plt.axis('off')
        plt.subplot(224), plt.imshow(img_median_adapt, cmap='gray')
        plt.title("自适应中值滤波"), plt.axis('off')
        plt.show()

    def adaptiveMedianDeNoise(self,image, size_max):
        startWindow = 3  # 初始窗口大小
        edge = int(size_max)  # 卷积范围
        image = cv.copyMakeBorder(image, edge, edge, edge, edge, cv.BORDER_REPLICATE)  # 增加图像边缘，便于卷积处理
        height, width = image.shape
        image_new = np.zeros(image.shape)
        for i in range(edge + 1, height - (edge + 1)):  # 遍历全图
            for j in range(edge + 1, width - (edge + 1)):
                k = int(startWindow / 2)
                value_median = np.median(image[i - k:i + k + 1, j - k:j + k + 1])  # 获取窗口内像素的中值
                value_min = np.min(image[i - k:i + k + 1, j - k:j + k + 1])  # 获取窗口内像素的最大值
                value_max = np.max(image[i - k:i + k + 1, j - k:j + k + 1])  # 获取窗口内像素的最小值
                if value_min < value_median < value_max:  # 满足条件新图像赋值
                    if value_min < image[i, j] < value_max:
                        image_new[i, j] = image[i, j]
                    else:
                        image_new[i, j] = value_median
                else:  # 不满足条件，扩大窗口大小
                    while True:  # 重复以上步骤，直至找到合适的值或到达窗口尺寸上限
                        startWindow = startWindow + 2  # 跳出循环返回以上步骤
                        if value_min < value_median < value_max or startWindow > size_max:
                            break
                        k = int(startWindow / 2)
                        value_median = np.median(image[i - k:i + k + 1, j - k:j + k + 1])
                        value_min = np.min(image[i - k:i + k + 1, j - k:j + k + 1])
                        value_max = np.max(image[i - k:i + k + 1, j - k:j + k + 1])

                    if value_min < value_median < value_max or startWindow > size_max:
                        if value_min < image[i, j] < value_max:
                            image_new[i, j] = image[i, j]
                        else:
                            image_new[i, j] = value_median
        image_new = image_new[edge + 1: height - (edge + 1), edge + 1: width - (edge + 1)]
        image_new = cv.convertScaleAbs(image_new)
        return image_new

##############################part3 频率域滤波################3
    '''
    gaussian_bandstop
    gaussian_bandpass
    Butterworth_Stop
    gaussian_notch
    Butterworth_notch
    Butterworth_Pass_notch
    '''
    ####添加周期性噪声
    def p3_periodic_noise(self,img,T,Amp):
        if np.ndim(img) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img_gray = img.copy()
        img_gray.astype(np.int16)#防止叠加噪声后溢出
        for i in range(0,img.shape[0]):#在X,Y两轴方向分别加正弦噪声
            for j in range(0, img.shape[1]):
                img_gray[i][j]=img_gray[i][j]+Amp*math.sin(2*pi/T*i)+Amp*math.sin(2*pi/T*j)
        img_gray   = np.clip(img_gray, 0,255)     #规定噪声图像上下界
        img_gray.astype(np.uint8)#防止叠加噪声后溢出
        self.periodic_noise_pic = img_gray
        # 傅里叶变换
        f1 = np.fft.fft2(img)
        # 对频谱进行移动，是0频率点在中心
        fshift1 = np.fft.fftshift(f1)
        # 获得傅里叶变换的幅度谱
        fft_1 = np.log(np.abs(fshift1))
        # 傅里叶变换
        f2 = np.fft.fft2(img_gray)
        # 对频谱进行移动，是0频率点在中心
        result1 = np.zeros_like(img_gray)
        result2 = np.zeros_like(img_gray)
        fshift2 = np.fft.fftshift(f2)
        # 获得傅里叶变换的幅度谱
        self.periodic_noise_fft = np.log(np.abs(fshift2))
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("中值滤波对比")
        plt.subplot(221), plt.imshow(img, cmap='gray')
        plt.title("原图"), plt.axis('off')
        plt.subplot(222), plt.imshow(self.periodic_noise_pic, cmap='gray')
        plt.title("X,Y正交正弦噪声\n叠加结果"), plt.axis('off')
        plt.subplot(223), plt.imshow(fft_1, cmap='gray')
        plt.title("原图 傅里叶变换幅度谱"), plt.axis('off')
        plt.subplot(224), plt.imshow(self.periodic_noise_fft, cmap='gray')
        plt.title("叠加结果幅度谱"), plt.axis('off')
        plt.show()

####################构建带阻滤波器################
    def p3_band_stop_filter(self,img,D_in):
        fft_img, fft_Butterworth_Stop, img_Butterworth_Stop = self.Filter_band(img, D0=D_in, n=2, W=25, ftype="Butterworth_Stop")  # 不同参数下的巴特沃斯带阻滤波
        _, fft_gaussian_Stop, img_gaussian_Stop = self.Filter_band(img, D0=D_in, n=2, W=25, ftype="gaussian_bandstop")
        fft_img = np.log(np.abs(fft_img))
        fft_Butterworth_Stop = np.log(np.abs(fft_Butterworth_Stop))
        fft_gaussian_Stop = np.log(np.abs(fft_gaussian_Stop))
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("带阻滤波")
        plt.subplot(231), plt.imshow(img, cmap='gray'),plt.title("周期噪声图像"), plt.axis('off')
        plt.subplot(232), plt.imshow(img_Butterworth_Stop, cmap='gray'),plt.title("巴特沃斯带阻滤波(D="+str(D_in) +")"), plt.axis('off')
        plt.subplot(233), plt.imshow(img_gaussian_Stop, cmap='gray'),plt.title("高斯带阻滤波(D=65)"), plt.axis('off')
        plt.subplot(234), plt.imshow(fft_img, cmap='gray'),plt.title("滤波前傅里叶变换"), plt.axis('off')
        plt.subplot(235), plt.imshow(fft_Butterworth_Stop, cmap='gray'),plt.title("巴特沃斯带阻滤波后\n傅里叶变换"), plt.axis('off')
        plt.subplot(236), plt.imshow(fft_gaussian_Stop, cmap='gray'),plt.title("高斯带阻滤波后\n傅里叶变换"), plt.axis('off')
        plt.show()
    #########
    def Filter_band(self,img, D0, n, W,ftype):
        assert img.ndim == 2  # 执行判断：当图像为两通道时，执行以下语句
        if ftype == "gaussian_bandstop" or ftype == "gaussian_bandpass" or ftype == "Butterworth_Stop":
            kernel = self.kernel_band(img, D0, W, n, ftype)
        elif ftype == "None":
            return
        gray = np.float64(img)
        gray_fft = np.fft.fft2(gray)  # 图像傅里叶变换
        gray_fftshift = np.fft.fftshift(gray_fft)
        dst_filtered = kernel * gray_fftshift  # 图像频域滤波
        dst_ifftshift = np.fft.ifftshift(dst_filtered)  # 图像傅里叶逆变换
        dst_ifft = np.fft.ifft2(dst_ifftshift)
        dst = np.abs(np.real(dst_ifft))  # 提取矩阵实部并取绝对值
        dst = np.clip(dst, 0, 255)  # 规定矩阵元素的上下界
        return gray_fftshift, dst_filtered, np.uint8(dst)  # 原图傅里叶，滤波后的傅里叶，滤波后的图

    ########
    def kernel_band(self,img,D0,W,n,ftype):
        kernel = np.ones(img.shape, dtype=np.float32)
        r,c = img.shape
        for i in np.arange(r):
            for j in np.arange(c):
                distance = np.sqrt((i - r / 2) ** 2 + (j - c / 2) ** 2)
                #高斯带阻滤波
                if ftype == "gaussian_bandstop":
                    kernel[i, j] = -np.exp(-0.5 * (((distance ** 2 - D0**2) / (distance *W + 1.0e-5))**2))
                # 高斯带通滤波
                elif ftype == "gaussian_bandpass":
                    kernel[i, j] = 1 - np.exp(-0.5 * (((distance ** 2 - D0**2) / (distance *W + 1.0e-5))**2))
                # 巴特沃斯带阻滤波
                elif ftype == "Butterworth_Stop":
                    kernel[i, j] = kernel[i, j] = 1 / (1 + (distance * W / (distance ** 2 - D0 ** 2)) ** (2 * n)+0.01)
        return kernel

################陷波滤波器#################
    def p3_notch_filter(self,img,coordinate_X,coordinate_Y,D_in):
        _, fft_Butterworth_notch, img_Butterworth_notch = self.Filter_notch(img, coordinate_X,coordinate_Y,D0=D_in, n=2, ftype="Butterworth_notch")
        fft_img, fft_gaussian_notch, img_gaussian_notch = self.Filter_notch(img, coordinate_X,coordinate_Y,D0=D_in, n=2, ftype="gaussian_notch")
        fft_img = np.log(np.abs(fft_img))
        fft_Butterworth_notch = np.log(np.abs(fft_Butterworth_notch))
        fft_gaussian_notch = np.log(np.abs(fft_gaussian_notch))

        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure("陷波滤波")
        plt.subplot(231), plt.imshow(img, cmap='gray'),plt.title("周期噪声图像"), plt.axis('off')
        plt.subplot(232), plt.imshow(img_Butterworth_notch, cmap='gray'),plt.title("巴特沃斯陷波滤波(D="+str(D_in) +")"), plt.axis('off')
        plt.subplot(233), plt.imshow(img_gaussian_notch, cmap='gray'),plt.title("高斯陷波滤波(D="+str(D_in) +")"), plt.axis('off')
        plt.subplot(234), plt.imshow(fft_img, cmap='gray'),plt.title("滤波前傅里叶变换"), plt.axis('off')
        plt.subplot(235), plt.imshow(fft_Butterworth_notch, cmap='gray'),plt.title("巴特沃斯陷波滤波后\n傅里叶变换"), plt.axis('off')
        plt.subplot(236), plt.imshow(fft_gaussian_notch, cmap='gray'),plt.title("高斯陷波滤波后\n傅里叶变换"), plt.axis('off')
        plt.show()

    def Filter_notch(self,img, coordinate_X,coordinate_Y,D0, n, ftype):
        assert img.ndim == 2  # 执行判断：当图像为两通道时，执行以下语句
        if ftype == "gaussian_notch" or ftype == "Butterworth_notch":
            kernel = self.kernel_notch(img,coordinate_X,coordinate_Y, D0, n, ftype)
        elif ftype == "None":
            return

        gray = np.float64(img)
        gray_fft = np.fft.fft2(gray)  # 图像傅里叶变换
        gray_fftshift = np.fft.fftshift(gray_fft)
        dst_filtered = kernel * gray_fftshift  # 图像频域滤波
        dst_ifftshift = np.fft.ifftshift(dst_filtered)  # 图像傅里叶逆变换
        dst_ifft = np.fft.ifft2(dst_ifftshift)
        dst = np.abs(np.real(dst_ifft))  # 提取矩阵实部并取绝对值
        dst = np.clip(dst, 0, 255)  # 规定矩阵元素的上下界
        return gray_fftshift, np.abs(dst_filtered), np.uint8(dst)  # 原图傅里叶，滤波后的傅里叶，滤波后的图

    # 构建陷波滤波器
    def kernel_notch(self,img,coordinate_X,coordinate_Y,D0,n,ftype):
        kernel = np.ones(img.shape, dtype=np.float32)
        r, c = img.shape
        u = np.array([0, 0, coordinate_Y, -coordinate_Y])
        v = np.array([coordinate_X, -coordinate_X, 0, 0])
        distance_1 = np.array([0, 0, 0, 0])
        distance_2 = np.array([0, 0, 0, 0])

        for i in np.arange(r):
            for j in np.arange(c):
                for k in range(len(u)):
                    distance_1[k] = np.sqrt((i - r / 2 + u[k]) ** 2 + (j - c / 2 + v[k]) ** 2)
                    distance_2[k] = np.sqrt((i - r / 2 - u[k]) ** 2 + (j - c / 2 - v[k]) ** 2)
                    #巴特沃斯陷波滤波
                    if ftype == "Butterworth_notch" or "Butterworth_Pass_notch":
                        kernel[i, j] *= 1 / ((1 + (D0 / (distance_1[k]+0.01)) ** (2 * n)) * (1 + (D0 / (distance_1[k]+0.01)) ** (2 * n)))
                    # 高斯陷波滤波
                    elif ftype == "gaussian_notch":
                        kernel[i, j] *= 1 - np.exp((distance_1 * distance_2) / (D0 ** 2) * (-0.5))
        if  ftype == "Butterworth_Pass_notch":
            kernel = 1- kernel
        return kernel
#
# img = cv.imread("pic/boat.jpg")
# CH5_API=CH5_API()
# if np.ndim(img) == 3:
#     img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#
# CH5_API.p3_periodic_noise(img,200,20)
# # CH5_API.p3_notch_filter(CH5_API.periodic_noise_pic,100,10)
# CH5_API.p3_band_stop_filter(CH5_API.periodic_noise_pic,img.shape[0]/200)
