#第四章 频域图像增强

#频域谱 相位谱及重构
import cv2
import numpy as np
import matplotlib.pyplot as plt
pi=3.14159265
##########
class CH4_API:

    def p2tl_FFT_IFFT(self,img):
        # #检查是否适用默认路径的机制
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转成灰色图片
        print()
        # 傅里叶变换
        f = np.fft.fft2(img)
        # 对频谱进行移动，是0频率点在中心
        fshift = np.fft.fftshift(f)
        # 获得傅里叶变换的幅度谱
        s1 = np.log(np.abs(fshift))
        # 获得傅里叶变换的相位谱
        s2 = np.log(np.angle(fshift) * 180 / pi)
        # 用来正常显示中文标签
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.subplot(241), plt.imshow(img, 'gray'), plt.title('原图像')
        plt.xticks([]), plt.yticks([])
        plt.subplot(242), plt.imshow(s1, 'gray'), plt.title('图像幅度谱')
        plt.xticks([]), plt.yticks([])
        plt.subplot(243), plt.imshow(s2, 'gray'), plt.title('图像相位谱')
        plt.xticks([]), plt.yticks([])
        ################------------------------------------######################
        ################------------------------------------######################
        # 幅度谱重构
        f1shift = np.fft.ifftshift(np.abs(fshift))
        img_back1 = np.fft.ifft2(f1shift)
        img_back1 = np.abs(img_back1)
        # print("img_back1", img_back1)
        img_back1 = np.log(img_back1) * 30
        img_back1 = img_back1.astype(np.uint8)
        plt.subplot(245), plt.imshow(img_back1, 'gray'), plt.title('幅度谱重构')
        plt.xticks([]), plt.yticks([])
        #对重构结果通过进行直方图均衡化进行增强
        img_back1 = cv2.equalizeHist(img_back1)
        plt.subplot(246), plt.imshow(img_back1, 'gray'), plt.title('幅度谱重构' + '\n' + ' 直方均衡')
        plt.xticks([]), plt.yticks([])
        # 相位谱重构
        f2shift = np.fft.ifftshift(np.angle(fshift))
        img_back2 = np.fft.ifft2(f2shift)
        img_back2 = np.abs(img_back2)
        # print("img_back2",img_back2,type(img_back2))
        img_back2 = img_back2 * 100
        plt.subplot(247), plt.imshow(img_back2, 'gray'), plt.title('相位谱重构图')
        plt.xticks([]), plt.yticks([])

        img_back2 = img_back2.astype(np.uint8)
        img_back2 = cv2.equalizeHist(img_back2)
        img_back2 = img_back2

        plt.subplot(248), plt.imshow(img_back2, 'gray'), plt.title('相位谱重构 \n 直方均衡')
        plt.xticks([]), plt.yticks([])

        # 双谱重构
        s1 = np.abs(fshift)  # 取振幅
        s1_angle = np.angle(fshift)  # 取相位
        s1_real = s1 * np.cos(s1_angle)  # 取实部
        s1_imag = s1 * np.sin(s1_angle)  # 取虚部
        s2 = np.zeros(img.shape, dtype=complex)
        # 赋值给s2
        s2.real = np.array(s1_real)
        s2.imag = np.array(s1_imag)

        # 进行逆变换
        f2shift = np.fft.ifftshift(s2)
        img_back = np.fft.ifft2(f2shift)
        img_back = np.abs(img_back)

        plt.subplot(244), plt.imshow(img_back, 'gray'), plt.title('双谱重构图')
        plt.xticks([]), plt.yticks([])
        plt.show()

    def p2s1_FFT_shift(self,img):
        # 检查是否适用默认路径的机制
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转成灰色图片
        # 傅里叶变换
        f = np.fft.fft2(img)
        s1 = np.log(np.abs(f))
        # 获得傅里叶变换的相位谱
        s2 = np.log(np.angle(f) * 180 / pi)
        # 对频谱进行移动，是0频率点在中心
        fshift = np.fft.fftshift(f)
        # 获得傅里叶变换的幅度谱
        fs1 = np.log(np.abs(fshift))
        # 获得傅里叶变换的相位谱
        fs2 = np.log(np.angle(fshift) * 180 / pi)
        # 用来正常显示中文标签
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.subplot(231), plt.imshow(img, 'gray'), plt.title('原图像')
        plt.xticks([]), plt.yticks([])
        plt.subplot(232), plt.imshow(s1, 'gray'), plt.title('未中心化幅度谱')
        plt.xticks([]), plt.yticks([])
        plt.subplot(233), plt.imshow(s2, 'gray'), plt.title('未中心化相位谱')
        plt.xticks([]), plt.yticks([])
        plt.subplot(235), plt.imshow(fs1, 'gray'), plt.title('中心化后幅度谱')
        plt.xticks([]), plt.yticks([])
        plt.subplot(236), plt.imshow(fs2, 'gray'), plt.title('中心化后相位谱')
        plt.xticks([]), plt.yticks([])
        plt.show()
        return fshift

    def p2s2_amplitude_reconstruction(self,img,fshift):#幅度谱重构

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转成灰色图片
        f1shift = np.fft.ifftshift(np.abs(fshift))
        img_ar = np.fft.ifft2(f1shift)
        img_ar = np.abs(img_ar)
        # print("img_back1", img_back1)
        img_ar = np.log(img_ar) * 30
        img_ar = img_ar.astype(np.uint8)
        # 对重构结果通过进行直方图均衡化进行增强
        img_ar_he = cv2.equalizeHist(img_ar)
        plt.subplot(131), plt.imshow(img, 'gray'), plt.title('原图')
        plt.xticks([]), plt.yticks([])
        plt.subplot(132), plt.imshow(img_ar, 'gray'), plt.title('幅度谱重构图')
        plt.xticks([]), plt.yticks([])
        plt.subplot(133), plt.imshow(img_ar_he, 'gray'), plt.title('幅度谱重构 \n 直方均衡')
        plt.xticks([]), plt.yticks([])
        plt.show()

    def p2s3_phase_reconstruction(self,img,fshift):#相位谱重构
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转成灰色图片

        f2shift = np.fft.ifftshift(np.angle(fshift))
        img_pr = np.fft.ifft2(f2shift)
        img_pr = np.abs(img_pr)
        # print("img_back2",img_back2,type(img_back2))
        img_pr = img_pr * 100#将效果显示明显些
        img_pr = img_pr.astype(np.uint8)#直方图之前必须先将图像变为单通道且uint8类型，若果是刚变换回来的图会是double型，需要强制类型转换
        img_pr_he = cv2.equalizeHist(img_pr)

        plt.subplot(131), plt.imshow(img, 'gray'), plt.title('原图')
        plt.xticks([]), plt.yticks([])
        plt.subplot(132), plt.imshow(img_pr, 'gray'), plt.title('相位谱重构图')
        plt.xticks([]), plt.yticks([])
        plt.subplot(133), plt.imshow(img_pr_he, 'gray'), plt.title('相位谱重构 \n 直方均衡')
        plt.xticks([]), plt.yticks([])
        plt.show()

    def p2s4_double_reconstruction(self,img,fshift):  # 双谱重构
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转成灰色图片
        s1 = np.abs(fshift)  # 取振幅
        s1_angle = np.angle(fshift)  # 取相位
        s1_real = s1 * np.cos(s1_angle)  # 取实部
        s1_imag = s1 * np.sin(s1_angle)  # 取虚部
        s2 = np.zeros(img.shape, dtype=complex)
        s2.real = np.array(s1_real)
        s2.imag = np.array(s1_imag)
        # 进行逆变换
        f2shift = np.fft.ifftshift(s2)
        img_dr = np.fft.ifft2(f2shift)
        img_dr = np.abs(img_dr)
        img_delta=np.abs(img_dr-img)#求两图差异

        plt.subplot(131), plt.imshow(img, 'gray'), plt.title('原图')
        plt.xticks([]), plt.yticks([])
        plt.subplot(132), plt.imshow(img_dr, 'gray'), plt.title('双谱重构图')
        plt.xticks([]), plt.yticks([])
        plt.subplot(133), plt.imshow(img_delta, 'gray'), plt.title('两图差异')
        plt.xticks([]), plt.yticks([])
        plt.show()

    def p2_cross_reconstruction(self,img_p2, fshift):#双图混合
        import os
        base_address = os.path.dirname(__file__)  # 获得当前所在绝对路径（不知道用户会把此程序发在哪，需要随时重新更新）
        img_p1 = cv2.imread(base_address + '/pic/3.jpg')
        if np.ndim(img_p2) == 3:
            img_p2 = cv2.cvtColor(img_p2, cv2.COLOR_BGR2GRAY)
        if np.ndim(img_p1) == 3:
            img_p1 = cv2.cvtColor(img_p1, cv2.COLOR_BGR2GRAY)
        height, width = img_p1.shape[0], img_p1.shape[1]
        img_p2 = cv2.resize(img_p2, (width, height), interpolation=cv2.INTER_AREA)

        f1 = np.fft.fft2(img_p1)
        f1shift = np.fft.fftshift(f1)
        f1_A = np.abs(f1shift)  # 取振幅
        f1_P = np.angle(f1shift)  # 取相位

        f2 = np.fft.fft2(img_p2)
        f2shift = np.fft.fftshift(f2)
        f2_A = np.abs(f2shift)  # 取振幅
        f2_P = np.angle(f2shift)  # 取相位

        # 用图1的振幅和图2的相位重构
        img_new1_f = np.zeros(img_p1.shape, dtype=complex)
        img1_real = f1_A * np.cos(f2_P)  # 取实部
        img1_imag = f1_A * np.sin(f2_P)  # 取虚部
        img_new1_f.real = np.array(img1_real)
        img_new1_f.imag = np.array(img1_imag)
        f3shift = np.fft.ifftshift(img_new1_f)  # 进行逆变换
        img_new1 = np.fft.ifft2(f3shift)
        img_new1 = np.abs(img_new1)


        ##用图1的相位和图2的振幅重构
        img_new2_f = np.zeros(img_p1.shape, dtype=complex)
        img2_real = f2_A * np.cos(f1_P)  # 取实部
        img2_imag = f2_A * np.sin(f1_P)  # 取虚部
        img_new2_f.real = np.array(img2_real)
        img_new2_f.imag = np.array(img2_imag)
        f4shift = np.fft.ifftshift(img_new2_f)  # 进行逆变换
        img_new2 = np.fft.ifft2(f4shift)
        img_new2 = np.abs(img_new2)

        # 用来正常显示中文标签
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.subplot(221), plt.imshow(img_p1, 'gray'), plt.title('原始图像1')
        plt.xticks([]), plt.yticks([])
        plt.subplot(222), plt.imshow(img_p2, 'gray'), plt.title('原始图像2')
        plt.xticks([]), plt.yticks([])
        plt.subplot(223), plt.imshow(img_new1, 'gray'), plt.title('图像1振幅+图像2相位')
        plt.xticks([]), plt.yticks([])
        plt.subplot(224), plt.imshow(img_new2, 'gray'), plt.title('图像1相位+图像2振幅')
        plt.xticks([]), plt.yticks([])
        plt.show()

    # 频谱 相位 图像融合
    ############################  P3  ###########################
    def p3_show_ideal_low_pass(self,img,d):  #理想低通滤波器
        # 4.3.1理想低通滤波器
        if np.ndim(img) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_d1 = self.ideal_low_pass_filter(img, d)
        img_d2 = self.ideal_low_pass_filter(img, 2)
        img_d3 = self.ideal_low_pass_filter(img, 4)
        img_d4 = self.ideal_low_pass_filter(img, 16)
        img_d5 = self.ideal_low_pass_filter(img, 64)
        # 用来正常显示中文标签
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 显示图像
        plt.figure(figsize=(10, 5))  # width * height
        plt.subplot(231), plt.axis("off"), plt.title('原始图像'),plt.imshow(img, cmap="gray")
        plt.subplot(232), plt.axis("off"), plt.title('理想低通 D='+str(d)),plt.imshow(img_d1, cmap="gray")
        plt.subplot(233), plt.axis("off"),plt.title('理想低通  D=2'), plt.imshow(img_d2, cmap="gray")
        plt.subplot(234), plt.axis("off"),plt.title("理想低通  D=4"), plt.imshow(img_d3, cmap="gray")
        plt.subplot(235), plt.axis("off"),plt.title("理想低通  D=16"), plt.imshow(img_d4, cmap="gray")
        plt.subplot(236), plt.axis("off"),plt.title("理想低通  D=64 "), plt.imshow(img_d5, cmap="gray")
        plt.show()

    def p3_show_butterworth_low_pass(self,img,d,order):  # 巴特沃斯低通滤波器
        # 4.3.2 巴特沃斯低通滤波器
        if np.ndim(img) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        butter_1 = self.butterworth_low_pass(img, 2, order)
        butter_2 = self.butterworth_low_pass(img, 4, order)
        butter_3 = self.butterworth_low_pass(img, 16, order)
        butter_4 = self.butterworth_low_pass(img, 64, order)
        butter_5 = self.butterworth_low_pass(img, d, 1)
        butter_6 = self.butterworth_low_pass(img, d, 2)
        butter_7 = self.butterworth_low_pass(img, d, 4)
        butter_8 = self.butterworth_low_pass(img, d, 8)

        # 用来正常显示中文标签
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 显示图像
        plt.figure(figsize=(10, 5))  # width * height
        plt.subplot(251), plt.imshow(img, cmap="gray"),plt.title("原始图像"), plt.axis("off")
        plt.subplot(252), plt.imshow(butter_1, cmap="gray"),plt.title("巴特沃斯低通,\n D=2,n="+str(order)), plt.axis("off")
        plt.subplot(253), plt.imshow(butter_2, cmap="gray"),plt.title("巴特沃斯低通,\n D=4,n="+str(order)), plt.axis("off")
        plt.subplot(254), plt.imshow(butter_3, cmap="gray"),plt.title("巴特沃斯低通,\n D=16,n="+str(order)), plt.axis("off")
        plt.subplot(255), plt.imshow(butter_4, cmap="gray"),plt.title("巴特沃斯低通,\n D=64,n="+str(order)), plt.axis("off")
        plt.subplot(257), plt.imshow(butter_5, cmap="gray"),plt.title("巴特沃斯低通,\n D= "+str(d)+",n=1"), plt.axis("off")
        plt.subplot(258), plt.imshow(butter_6, cmap="gray"),plt.title("巴特沃斯低通,\n D= "+str(d)+",n=2"), plt.axis("off")
        plt.subplot(259), plt.imshow(butter_7, cmap="gray"),plt.title("巴特沃斯低通,\n D= "+str(d)+",n=4"), plt.axis("off")
        plt.subplot(2,5,10), plt.imshow(butter_8, cmap="gray"),plt.title("巴特沃斯低通,\n D= "+str(d)+",n=8"), plt.axis("off")
        plt.show()

    def p3_show_gaussian_low_pass(self,img, d):#高斯低通滤波
        # 4.3.3 高斯低通滤波器
        if np.ndim(img) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img_d1 = self.gaussian_low_pass_filter(img, d)
        img_d2 = self.gaussian_low_pass_filter(img, 2)
        img_d3 = self.gaussian_low_pass_filter(img, 4)
        img_d4 = self.gaussian_low_pass_filter(img, 16)
        img_d5 = self.gaussian_low_pass_filter(img, 64)


        # 用来正常显示中文标签
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 显示图像
        plt.figure(figsize=(10, 5))  # width * height
        plt.subplot(231), plt.axis("off"), plt.title('原始图像'),plt.imshow(img, cmap="gray")
        plt.subplot(232), plt.axis("off"),plt.title('高斯低通 D='+str(d)),plt.imshow(img_d1, cmap="gray")
        plt.subplot(233), plt.axis("off"),plt.title('高斯低通 D=2'), plt.imshow(img_d2, cmap="gray")
        plt.subplot(234), plt.axis("off"),plt.title("高斯低通 D=4"), plt.imshow(img_d3, cmap="gray")
        plt.subplot(235), plt.axis("off"),plt.title("高斯低通 D=16"), plt.imshow(img_d4, cmap="gray")
        plt.subplot(236), plt.axis("off"),plt.title("高斯低通 D=64"), plt.imshow(img_d5, cmap="gray")
        plt.show()

    def p3_show_ideal_high_pass(self,img, d):  # 理想低通滤波器
        # 4.4.1 理想高通滤波器
        if np.ndim(img) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img_d1 = self.ideal_high_pass_filter(img, d)
        img_d2 = self.ideal_high_pass_filter(img, 128)
        img_d3 = self.ideal_high_pass_filter(img, 64)
        img_d4 = self.ideal_high_pass_filter(img, 16)
        img_d5 = self.ideal_high_pass_filter(img, 4)

        # 用来正常显示中文标签
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 显示图像
        plt.figure(figsize=(10, 5))  # width * height
        plt.subplot(231), plt.axis("off"), plt.title('原始图像'),plt.imshow(img, cmap="gray")
        plt.subplot(232), plt.axis("off"), plt.title('理想高通 D='+str(d)),plt.imshow(img_d1, cmap="gray")
        plt.subplot(233), plt.axis("off"),plt.title('理想高通  D=128'), plt.imshow(img_d2, cmap="gray")
        plt.subplot(234), plt.axis("off"),plt.title("理想高通  D=64"), plt.imshow(img_d3, cmap="gray")
        plt.subplot(235), plt.axis("off"),plt.title("理想高通  D=16"), plt.imshow(img_d4, cmap="gray")
        plt.subplot(236), plt.axis("off"),plt.title("理想高通  D=4 "), plt.imshow(img_d5, cmap="gray")
        plt.show()

    def p3_show_butterworth_high_pass(self,img, d, order):  # 巴特沃斯低通滤波器
        # 4.4.2 巴特沃斯高通滤波器
        if np.ndim(img) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        butter_1 = self.butterworth_high_pass_kernel(img, 128, order)
        butter_2 = self.butterworth_high_pass_kernel(img, 64, order)
        butter_3 = self.butterworth_high_pass_kernel(img, 16, order)
        butter_4 = self.butterworth_high_pass_kernel(img, 4, order)
        butter_5 = self.butterworth_high_pass_kernel(img, d, 1)
        butter_6 = self.butterworth_high_pass_kernel(img, d, 2)
        butter_7 = self.butterworth_high_pass_kernel(img, d, 4)
        butter_8 = self.butterworth_high_pass_kernel(img, d, 8)

        # 用来正常显示中文标签
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 显示图像
        plt.figure(figsize=(10, 5))  # width * height
        plt.subplot(251), plt.imshow(img, cmap="gray"), plt.title("原始图像"), plt.axis("off")
        plt.subplot(252), plt.imshow(butter_1, cmap="gray"), plt.title("巴特沃斯高通,\n D=128,n=" + str(order)), plt.axis("off")
        plt.subplot(253), plt.imshow(butter_2, cmap="gray"), plt.title("巴特沃斯高通,\n D=64,n=" + str(order)), plt.axis("off")
        plt.subplot(254), plt.imshow(butter_3, cmap="gray"), plt.title("巴特沃斯高通,\n D=16,n=" + str(order)), plt.axis("off")
        plt.subplot(255), plt.imshow(butter_4, cmap="gray"), plt.title("巴特沃斯高通,\n D=4,n=" + str(order)), plt.axis("off")
        plt.subplot(257), plt.imshow(butter_5, cmap="gray"), plt.title("巴特沃斯高通,\n D= " + str(d) + ",n=1"), plt.axis("off")
        plt.subplot(258), plt.imshow(butter_6, cmap="gray"), plt.title("巴特沃斯高通,\n D= " + str(d) + ",n=2"), plt.axis("off")
        plt.subplot(259), plt.imshow(butter_7, cmap="gray"), plt.title("巴特沃斯高通,\n D= " + str(d) + ",n=4"), plt.axis("off")
        plt.subplot(2,5,10), plt.imshow(butter_8, cmap="gray"), plt.title("巴特沃斯高通,\n D= " + str(d) + ",n=8"), plt.axis("off")
        plt.show()

    def p3_show_gaussian_high_pass(self,img, d):#高斯高通滤波
        # 4.4.3 高斯高通滤波器
        if np.ndim(img) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img_d1 = self.gaussian_high_pass_filter(img, d)
        img_d2 = self.gaussian_high_pass_filter(img, 128)
        img_d3 = self.gaussian_high_pass_filter(img, 64)
        img_d4 = self.gaussian_high_pass_filter(img, 16)
        img_d5 = self.gaussian_high_pass_filter(img, 4)


        # 用来正常显示中文标签
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 显示图像
        plt.figure(figsize=(10, 5))  # width * height
        plt.subplot(231), plt.axis("off"), plt.title('原始图像'),plt.imshow(img, cmap="gray")
        plt.subplot(232), plt.axis("off"),plt.title('高斯高通 D='+str(d)),plt.imshow(img_d1, cmap="gray")
        plt.subplot(233), plt.axis("off"),plt.title('高斯高通 D=128'), plt.imshow(img_d2, cmap="gray")
        plt.subplot(234), plt.axis("off"),plt.title("高斯高通 D=64"), plt.imshow(img_d3, cmap="gray")
        plt.subplot(235), plt.axis("off"),plt.title("高斯高通 D=16"), plt.imshow(img_d4, cmap="gray")
        plt.subplot(236), plt.axis("off"),plt.title("高斯高通 D=4"), plt.imshow(img_d5, cmap="gray")
        plt.show()

    def p3_show_all_filter(self,img, d_lp,btorder_lp,d_hp,btorder_hp):
        if np.ndim(img) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_il = self.ideal_low_pass_filter(img, d_lp)
        img_bl = self.butterworth_low_pass(img, d_lp, btorder_lp)
        img_gl = self.gaussian_low_pass_filter(img, d_lp)
        img_ih = self.ideal_high_pass_filter(img, d_hp)
        img_bh = self.butterworth_high_pass_kernel(img, d_hp, btorder_hp)
        img_gh = self.gaussian_high_pass_filter(img, d_hp)

        plt.subplot(241), plt.axis("off"), plt.title('原始图像'), plt.imshow(img, cmap="gray")
        plt.subplot(242), plt.axis("off"), plt.title('理想低通 D=' + str(d_lp)), plt.imshow(img_il, cmap="gray")
        plt.subplot(243), plt.axis("off"),plt.title("巴特沃斯低通,\n D= " + str(d_lp) + ",n="+str(btorder_lp)),  plt.imshow(img_bl, cmap="gray")
        plt.subplot(244), plt.axis("off"), plt.title('高斯低通 D=' + str(d_lp)), plt.imshow(img_gl, cmap="gray")
        plt.subplot(246), plt.axis("off"), plt.title('理想高通 D=' + str(d_hp)), plt.imshow(img_ih, cmap="gray")
        plt.subplot(247), plt.axis("off"),plt.title("巴特沃斯高通,\n D= " + str(d_hp) + ",n="+str(btorder_hp)),  plt.imshow(img_bh, cmap="gray")
        plt.subplot(248), plt.axis("off"), plt.title('高斯高通 D=' + str(d_hp)), plt.imshow(img_gh, cmap="gray")
        plt.show()

    ######################## p3 底层滤波函数#############################
    def ideal_low_pass_filter(self,img, d):
        assert img.ndim == 2
        M, N = img.shape[0], img.shape[1]
        ####################################
        def low_pass_kernel(img, cut_off):
            assert img.ndim == 2
            r, c = img.shape[1], img.shape[0]
            u = np.arange(r)
            v = np.arange(c)
            u, v = np.meshgrid(u, v)
            low_pass = np.sqrt((u - r / 2) ** 2 + (v - c / 2) ** 2)
            low_pass[low_pass <= cut_off] = 1
            low_pass[low_pass >= cut_off] = 0
            return low_pass

        #####################################
        kernel = low_pass_kernel(img, d)
        gray = img.copy()
        gray = np.float64(gray)
        gray_fft = np.fft.fft2(gray)
        gray_fftshift = np.fft.fftshift(gray_fft)
        dst = np.zeros_like(gray_fftshift)
        dst_filtered = kernel * gray_fftshift
        dst_ifftshift = np.fft.ifftshift(dst_filtered)
        dst_ifft = np.fft.ifft2(dst_ifftshift)
        dst = np.abs(np.real(dst_ifft))
        dst = np.clip(dst, 0, 255)
        return np.uint8(dst)

    def butterworth_low_pass(self,src, d, n):
        assert src.ndim == 2
        ##############################################核函数定义
        def butterworth_low_pass_kernel(img, cut_off, butterworth_order=2):
            assert img.ndim == 2
            r, c = img.shape[1], img.shape[0]
            u = np.arange(r)
            v = np.arange(c)
            u, v = np.meshgrid(u, v)
            low_pass = np.sqrt((u - r / 2) ** 2 + (v - c / 2) ** 2)
            denom = 1.0 + (low_pass / cut_off) ** (2 * butterworth_order)
            low_pass = 1.0 / denom
            return low_pass

        ###############################################

        kernel = butterworth_low_pass_kernel(src, d, n)
        gray = np.float64(src)
        gray_fft = np.fft.fft2(gray)
        gray_fftshift = np.fft.fftshift(gray_fft)
        dst = np.zeros_like(gray_fftshift)
        dst_filtered = kernel * gray_fftshift
        dst_ifftshift = np.fft.ifftshift(dst_filtered)
        dst_ifft = np.fft.ifft2(dst_ifftshift)
        dst = np.abs(np.real(dst_ifft))
        dst = np.clip(dst, 0, 255)
        return np.uint8(dst)

    def gaussian_low_pass_filter(self,src, d):
        assert src.ndim == 2

        #############################################高斯核定义
        def gaussian_low_pass_kernel(img, cut_off):
            assert img.ndim == 2
            r, c = img.shape[1], img.shape[0]
            u = np.arange(r)
            v = np.arange(c)
            u, v = np.meshgrid(u, v)
            low_pass = np.sqrt((u - r / 2) ** 2 + (v - c / 2) ** 2)
            xp = -1 * (low_pass ** 2) / (2 * cut_off ** 2)
            low_pass = np.exp(xp)
            low_pass = np.clip(low_pass, 0, 1)
            return low_pass

        ###############################################
        kernel = gaussian_low_pass_kernel(src, d)
        gray = np.float64(src)
        gray_fft = np.fft.fft2(gray)
        gray_fftshift = np.fft.fftshift(gray_fft)
        dst = np.zeros_like(gray_fftshift)
        dst_filtered = kernel * gray_fftshift
        dst_ifftshift = np.fft.ifftshift(dst_filtered)
        dst_ifft = np.fft.ifft2(dst_ifftshift)
        dst = np.abs(np.real(dst_ifft))
        dst = np.clip(dst, 0, 255)
        return np.uint8(dst)

    def ideal_high_pass_filter(self,img, d):
        assert img.ndim == 2
        M, N = img.shape[0], img.shape[1]

        #######################################核函数
        def high_pass_kernel(img, cut_off):
            assert img.ndim == 2
            r, c = img.shape[1], img.shape[0]
            u = np.arange(r)
            v = np.arange(c)
            u, v = np.meshgrid(u, v)
            high_pass = np.sqrt((u - r / 2) ** 2 + (v - c / 2) ** 2)
            high_pass[high_pass <= cut_off] = 0
            high_pass[high_pass >= cut_off] = 1
            return high_pass

        #######################################
        kernel = high_pass_kernel(img, d)
        gray = img.copy()
        gray = np.float64(gray)
        gray_fft = np.fft.fft2(gray)
        gray_fftshift = np.fft.fftshift(gray_fft)
        dst = np.zeros_like(gray_fftshift)
        dst_filtered = kernel * gray_fftshift
        dst_ifftshift = np.fft.ifftshift(dst_filtered)
        dst_ifft = np.fft.ifft2(dst_ifftshift)
        dst = np.abs(np.real(dst_ifft))
        dst = np.clip(dst, 0, 255)
        return np.uint8(dst)

    def butterworth_high_pass_kernel(self,src, d, n):
        assert src.ndim == 2

        #######################################核函数
        def butterworth_low_pass_kernel(img, cut_off, butterworth_order=2):
            assert img.ndim == 2
            r, c = img.shape[1], img.shape[0]
            u = np.arange(r)
            v = np.arange(c)
            u, v = np.meshgrid(u, v)
            low_pass = np.sqrt((u - r / 2) ** 2 + (v - c / 2) ** 2)
            denom = 1.0 + (low_pass / cut_off) ** (2 * butterworth_order)
            low_pass = 1.0 / denom
            return low_pass

        #######################################
        kernel = 1 - butterworth_low_pass_kernel(src, d, n)
        gray = np.float64(src)
        gray_fft = np.fft.fft2(gray)
        gray_fftshift = np.fft.fftshift(gray_fft)
        dst = np.zeros_like(gray_fftshift)
        dst_filtered = kernel * gray_fftshift
        dst_ifftshift = np.fft.ifftshift(dst_filtered)
        dst_ifft = np.fft.ifft2(dst_ifftshift)
        dst = np.abs(np.real(dst_ifft))
        dst = np.clip(dst, 0, 255)
        return np.uint8(dst)

    def gaussian_high_pass_filter(self,src, d):
        assert src.ndim == 2

        #######################################核函数
        def gaussian_high_pass_kernel(img, cut_off):
            assert img.ndim == 2
            r, c = img.shape[1], img.shape[0]
            u = np.arange(r)
            v = np.arange(c)
            u, v = np.meshgrid(u, v)
            high_pass = np.sqrt((u - r / 2) ** 2 + (v - c / 2) ** 2)
            xp = -1 * (high_pass ** 2) / (2 * cut_off ** 2)
            high_pass = 1 - np.exp(xp)
            high_pass = np.clip(high_pass, 0, 1)
            return high_pass

        #######################################
        kernel = gaussian_high_pass_kernel(src, d)
        gray = np.float64(src)
        gray_fft = np.fft.fft2(gray)
        gray_fftshift = np.fft.fftshift(gray_fft)
        dst = np.zeros_like(gray_fftshift)
        dst_filtered = kernel * gray_fftshift
        dst_ifftshift = np.fft.ifftshift(dst_filtered)
        dst_ifft = np.fft.ifft2(dst_ifftshift)
        dst = np.abs(np.real(dst_ifft))
        dst = np.clip(dst, 0, 255)
        return np.uint8(dst)




# ####################################################################################
# ####################################################################################
#
# #频域谱 相位谱
#
# pi=3.14159265
# #读取为灰度图像
# img1 = cv2.imread('1.jpg',0)
# img2 = cv2.imread('2.jpg',0)
# img3 = cv2.imread('3.jpg',0)
# #傅里叶变换
# f1 = np.fft.fft2(img1)
# f2 = np.fft.fft2(img2)
# f3 = np.fft.fft2(img3)
# #对频谱进行移动，是0频率点在中心
# fshift1 = np.fft.fftshift(f1)
# fshift2 = np.fft.fftshift(f2)
# fshift3 = np.fft.fftshift(f3)
# #获得傅里叶变换的幅度谱和相位谱
# s1 = np.log(np.abs(fshift1))
# p1 = (np.angle(fshift1)*180/pi)
# s2 = np.log(np.abs(fshift2))
# p2 = (np.angle(fshift2)*180/pi)
# s3 = np.log(np.abs(fshift3))
# p3 = (np.angle(fshift3)*180/pi)
#
# #用来正常显示中文标签
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.subplot(331),plt.imshow(img1,'gray'),plt.title('原图像')
# plt.xticks([]),plt.yticks([])
# plt.subplot(332),plt.imshow(s1,'gray'),plt.title('图像幅度谱')
# plt.xticks([]),plt.yticks([])
# plt.subplot(333),plt.imshow(p1,'gray'),plt.title('图像相位谱')
# plt.xticks([]),plt.yticks([])
# plt.subplot(334),plt.imshow(img2,'gray'),plt.title('原图像')
# plt.xticks([]),plt.yticks([])
# plt.subplot(335),plt.imshow(s2,'gray'),plt.title('图像幅度谱')
# plt.xticks([]),plt.yticks([])
# plt.subplot(336),plt.imshow(p2,'gray'),plt.title('图像相位谱')
# plt.xticks([]),plt.yticks([])
# plt.subplot(337),plt.imshow(img3,'gray'),plt.title('原图像')
# plt.xticks([]),plt.yticks([])
# plt.subplot(338),plt.imshow(s3,'gray'),plt.title('图像幅度谱')
# plt.xticks([]),plt.yticks([])
# plt.subplot(339),plt.imshow(p3,'gray'),plt.title('图像相位谱')
# plt.xticks([]),plt.yticks([])
# plt.show()
#
# #########################################################
# #########################################################

#
#
# #4.1 傅里叶变换
#
# import numpy as np
# import cv2
# from matplotlib import pyplot as plt
# from PIL import Image, ImageGrab
#
#
#
# #读取图像
# img = cv2.imread('4.1.jpg', 0)
#
# #傅里叶变换
# dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
#
# #将频谱低频从左上角移动至中心位置
# dft_shift = np.fft.fftshift(dft)
#
# #频谱图像双通道复数转换为0-255区间,乘以20使得结果更大
# result = 20*np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1]))
#
# #用来正常显示中文标签
# plt.rcParams['font.sans-serif']=['SimHei']
# #显示图像
# plt.figure(figsize=(10, 5))  # width * height
# plt.subplot(121), plt.imshow(img, cmap = 'gray')
# plt.title('原始图像'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(result, cmap = 'gray')
# plt.title('傅里叶变换'), plt.xticks([]), plt.yticks([])
# plt.show()
#