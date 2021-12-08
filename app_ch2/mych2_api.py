import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
base_address = os.path.dirname(__file__)  # 获得当前所在绝对路径（不知道用户会把此程序发在哪，需要随时重新更新）
class CH2_API:
    def p21_imagereduction(index=1,path = base_address+'/pic/2.1.jpg'):#缩小
        img = cv2.imread(path)  # ('2.1.jpg') #1024*1024图像
        b, g, r = cv2.split(img)
        img = cv2.merge([r, g, b])
        # 获取图像的高度和宽度
        height,width = img.shape[0],img.shape[1]
        # 缩小, 象素关系重采样
        # 将1024*1024图像，逐渐减少采样数到 512*512 256*256 128*128 64*64 32*32
        if path == base_address+'/pic/2.1.jpg':
            img1 = cv2.resize(img, (width // 2, height // 2), interpolation=cv2.INTER_AREA)  # 1024*1024 to 512*512
            img2 = cv2.resize(img, (width // 4, height // 4), interpolation=cv2.INTER_AREA)  # 1024*1024 to 256*256
            img3 = cv2.resize(img, (width // 8, height // 8), interpolation=cv2.INTER_AREA)  # 1024*1024 to 128*128
            img4 = cv2.resize(img, (width // 16, height // 16), interpolation=cv2.INTER_AREA)  # 1024*1024 to 64*64
            img5 = cv2.resize(img, (width // 32, height // 32), interpolation=cv2.INTER_AREA)  # 1024*1024 to 32*32
            # 用来正常显示中文标签
            plt.rcParams['font.sans-serif'] = ['SimHei']
            # 显示图像
            plt.figure(figsize=(12, 7))  # width * height
            plt.subplot(231), plt.imshow(img, cmap='gray'), plt.title('原始图像 1024*1024')
            plt.subplot(232), plt.imshow(img1, cmap='gray'), plt.title('重采样 1024*1024 to 512*512')
            plt.subplot(233), plt.imshow(img2, cmap='gray'), plt.title('重采样 1024*1024 to 256*256')
            plt.subplot(234), plt.imshow(img3, cmap='gray'), plt.title('重采样 1024*1024 to 128*128')
            plt.subplot(235), plt.imshow(img4, cmap='gray'), plt.title('重采样 1024*1024 to 64*64')
            plt.subplot(236), plt.imshow(img5, cmap='gray'), plt.title('重采样 1024*1024 to 32*32')
            plt.show()
        else:
            img1 = cv2.resize(img, (width // index, height // index), interpolation=cv2.INTER_AREA)  #
            plt.rcParams['font.sans-serif'] = ['SimHei']
            plt.figure(figsize=(12, 7))  # width * height
            plt.subplot(231), plt.imshow(img, cmap='gray'), plt.title('原始图像 '+"X :"+str(width)+" , Y :"+str(height))
            plt.subplot(232), plt.imshow(img1, cmap='gray'), plt.title('重采样:边收缩 '+str(index)+"倍")
            plt.show()

    def p22_imagemagnification(selectmethod,index=1,path= base_address+'/pic/2.3.jpg'):#放大
        #先选择方法
        if selectmethod==0 : myinterpolation,strmethod=cv2.INTER_NEAREST,"INTER_NEAREST "
        else : myinterpolation,strmethod=cv2.INTER_LINEAR,"INTER_LINEAR "
        if path ==base_address+'/pic/2.3.jpg':
            img1 = cv2.imread(base_address+'/pic/2.3.jpg')  #128*128像素
            img2 = cv2.imread(base_address+'/pic/2.4.jpg')  #64*64像素
            img3 = cv2.imread(base_address+'/pic/2.5.jpg')  #32*32像素
            height1,height2,height3 = img1.shape[0],img2.shape[0],img3.shape[0]
            width1,width2,width3 = img1.shape[1],img2.shape[1],img3.shape[1]
            # 最近邻内插法分别将其放大到1024×1024像素
            newimg1 = cv2.resize(img1, (width1 * 8, height1 * 8), interpolation=myinterpolation)  # 128*128 to 1024*1024
            newimg2 = cv2.resize(img2, (width2 * 16, height2 * 16), interpolation=myinterpolation)  # 64*64 to 1024*1024
            newimg3 = cv2.resize(img3, (width3 * 32, height3 * 32), interpolation=myinterpolation)  # 32*32 to 1024*1024
            # 用来正常显示中文标签
            plt.rcParams['font.sans-serif'] = ['SimHei']
            plt.figure(figsize=(12, 6))  # width * height
            plt.subplot(131), plt.imshow(newimg1, cmap='gray')
            plt.title(strmethod+' 128*128 to 1024*1024')
            plt.subplot(132), plt.imshow(newimg2, cmap='gray')
            plt.title(strmethod+' 64*64 to 1024*1024')
            plt.subplot(133), plt.imshow(newimg3, cmap='gray')
            plt.title(strmethod + '32*32 to 1024*1024')
            plt.show()
        else:
            img = cv2.imread(path)  # 自定义照片
            b, g, r = cv2.split(img)
            img = cv2.merge([r, g, b])
            height,width = img.shape[0],img.shape[1]
            newimg = cv2.resize(img, (width * index, height * index), interpolation=myinterpolation)
            plt.rcParams['font.sans-serif'] = ['SimHei']
            plt.figure(figsize=(12, 6))  # width * height
            plt.subplot(131), plt.imshow(img, cmap='gray')
            plt.title(strmethod + "size x*y:"+str(width) +"* "+str(height))
            plt.subplot(132), plt.imshow(newimg, cmap='gray')
            plt.title(strmethod + "size x*y:"+str(width*index) +"* "+str(height*index))
            plt.show()

    def p3_imagegray(index=2,path=base_address+'/pic/2.2.jpg'):#灰度化图像
        img = cv2.imread(path)
        b, g, r = cv2.split(img)
        img = cv2.merge([r, g, b])
        # 获取图像高度和宽度
        height,width = img.shape[0],img.shape[1]
        # 创建一幅图像
        img.astype(np.int16)  # 防止叠加噪声后溢出
        new_img = np.zeros((height, width, 3), np.uint8)
        for i in range(height):
            for j in range(width):
                for k in range(3):  # 对应BGR三分量
                    gray =int(int(img[i, j][k]/(255/index))*255 /(index-1))
                    if gray>255 : gray = 255
                    new_img[i, j][k] = np.uint8(gray)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure(figsize=(12, 7))  # width * height
        plt.subplot(231), plt.imshow(img, cmap='gray'), plt.title('原始图像灰度级 ：' + "X :" + str(width) + " , Y :" + str(height))
        plt.subplot(232), plt.imshow(new_img, cmap='gray'), plt.title('自定义灰度级 ：  ' + str(index) )
        plt.show()

    
    # def imagebrightness(path, c, b):  # 图像亮度就是每个像素所有通道都加上b
    #     img1 = cv2.imread(path, cv2.IMREAD_COLOR)
    #     rows, cols, chunnel = img1.shape
    #     blank = np.zeros([rows, cols, chunnel], img1.dtype)  # np.zeros(img1.shape, dtype=uint8)
    #     dst = cv2.addWeighted(img1, c, blank, 1-c, b)
    #     plt.subplot(121),plt.imshow(img1),plt.title('origin_img')
    #     plt.subplot(122),plt.imshow(dst),plt.title('gray_img')
    #     plt.show()
    #
    # def imagerotate(path):#旋转
    #     img = Image.open(path) # 读取的图像显示的<matplotlib.image.AxesImage object at 0x7f9f0c60f7f0>
    #     region = img.transpose(Image.ROTATE_180) #翻转
    #     out1 = img.rotate(30) #旋转30度
    #     out2 = img.rotate(60) #旋转60度
    #     out3 = img.rotate(90) #旋转90度
    #
    #     plt.subplot(221),plt.imshow(img),plt.title('origin_img')
    #     plt.subplot(222),plt.imshow(out1),plt.title('rotate30_img')
    #     plt.subplot(223),plt.imshow(out2),plt.title('rotate60_img')
    #     plt.subplot(224),plt.imshow(out3),plt.title('rotate90_img')
    #     plt.show()
    #
    # def imagegrab(path):#截图
    #     img = Image.open(path)
    #     bbox = (760, 0, 1160, 1080)
    #     im = ImageGrab.grab()
    #     plt.subplot(121),plt.imshow(img),plt.title('origin_img')
    #     #im.save('a.jpeg')
    #     plt.subplot(122),plt.imshow(im),plt.title('grab_img')
    #     plt.show()
    #
    #


