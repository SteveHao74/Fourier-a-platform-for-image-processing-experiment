#第九章 形态学图像处理



import cv2
import numpy as np
import matplotlib.pyplot as plt
import  os



class CH9_API:
    def __init__(self):
        self.img_pre = np.mat([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 255, 255, 255, 255, 0, 0, 0],
            [0, 0, 0, 0, 0, 255, 255, 255, 0, 0, 0],
            [0, 0, 0, 255, 255, 255, 255, 255, 0, 0, 0],
            [0, 0, 0, 255, 255, 0, 255, 255, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], np.uint8)
        # #手写结构元
        # kernel_1 = cv2.getStructuringElement(cv2.MORPH_CROSS,(3, 3),(1,1))
        # kernel_2=np.array([[1],[1]])
        # kernel_3 = np.zeros((3,3),np.uint8)
        # kernel_3[1,0]=1;
        # kernel_3[1,1]=1;
        # kernel_3[1,2]=1;
        # kernel_4 = np.ones((2,2),np.uint8)
        # kernel_5=np.array([[1,1]])

    #【9.1基础操作】 腐蚀，膨胀，开，闭操作:
    # #传参：核，锚点，图像
    def basic_operation(self,kernel,anchor,img=[]):
        if img ==[]:#使用以上默认像素图
            img =self.img_pre
        # 腐蚀图像
        img_eroded = cv2.erode(img, kernel,iterations = 1,anchor=(anchor[1],anchor[0]))
        #膨胀图像
        img_dilated= cv2.dilate(img, kernel,iterations = 1,anchor=(anchor[1],anchor[0]))
        #将两幅图像相减获得边；cv2.absdiff参数：(膨胀后的图像，腐蚀后的图像)
        absdiff_img = cv2.absdiff(img_dilated, img_eroded);
        #上面得到的结果是灰度图，将其二值化以便观察结果
        retval, threshold_img = cv2.threshold(absdiff_img, 40, 255, cv2.THRESH_BINARY);
        img_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)#开或关操作内部抵消不需要标记锚点
        img_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)  # 图像闭运算，
        #用来正常显示中文标签
        plt.rcParams['font.sans-serif']=['SimHei']
        kernel[anchor[0]][anchor[1]]=127#把锚点标出来
        plt.figure(figsize=(10, 5))  # width * height
        plt.subplot(241), plt.imshow(img, cmap = 'gray'),plt.title('原始图像'),plt.axis("off")
        plt.subplot(242), plt.imshow(kernel, cmap='gray'), plt.title('核，灰色为锚点'), plt.axis("off")
        plt.subplot(243), plt.imshow(img_eroded, cmap = 'gray'),plt.title('图像腐蚀'),plt.axis("off")
        plt.subplot(244), plt.imshow(img_dilated, cmap='gray'), plt.title('图像膨胀'), plt.axis("off")
        plt.subplot(245), plt.imshow(threshold_img, cmap='gray'), plt.title('内外边界：膨胀-腐蚀'), plt.axis("off")
        plt.subplot(246), plt.imshow(img_open, cmap = 'gray'),plt.title('图像开操作'),plt.axis("off")
        plt.subplot(247), plt.imshow(img_close, cmap='gray'), plt.title('图像闭操作'), plt.axis("off")
        plt.show()

    #【9.2】形态学处理进行区域填充（孔洞填充）
    def hole_filling(self,kernel,anchor,iteration,img =[]):#pic/9.4.jpg
        #读取图像
        print(kernel)
        if img ==[]:#使用以上默认像素图
            base_address=os.path.dirname(__file__)#获得当前所在绝对路径（不知道用户会把此程序发在哪，需要随时重新更新）
            img =cv2.imread(base_address+"/pic/9.4.jpg")#这里使用实时灵活的绝对路径导入图片
        # 二值化
        # imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgray=img
        imgray[imgray < 100] = 0
        imgray[imgray >= 100] = 255
        # 对原图取补得到MASK图像
        mask = 255 - imgray
        # 构造Marker图像
        marker = np.zeros_like(imgray)
        marker[0, :] = 255
        marker[-1, :] = 255
        marker[:, 0] = 255
        marker[:, -1] = 255
        marker_0 = marker.copy()
        # 形态学重建
        #设置卷积核

        # 矩形：MORPH_RECT;
        #
        # 交叉形：MORPH_CROSS;
        #
        # 椭圆形：MORPH_ELLIPSE;
        # kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        i=0
        while True:
            marker_pre = marker
            dilation = cv2.dilate(marker, kernel,(anchor[1],anchor[0]))#通过传参的方式共享第二部分的核
            marker = np.min((dilation, mask), axis=0)
            if (marker_pre == marker).all():
                break
            i = i + 1
            if i%iteration==0:
                plt.rcParams['font.sans-serif'] = ['SimHei']
                plt.figure(figsize=(16, 5))
                plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title('原始图像'), plt.axis("off")
                plt.subplot(1, 3, 2), plt.imshow(kernel, cmap='gray'), plt.title('核'), plt.axis("off")
                plt.subplot(1, 3, 3), plt.imshow(marker, cmap='gray'), plt.title('区域填充第'+str(i)+'次迭代的marker图\n未完待续'), plt.axis("off")
                plt.show()

        result = 255 - marker
        #用来正常显示中文标签
        plt.rcParams['font.sans-serif']=['SimHei']
        # 图像显示
        plt.figure(figsize=(16, 5))  # width * height
        plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('原始图像'), plt.axis("off")
        plt.subplot(1, 2, 2), plt.imshow(result, cmap='gray'), plt.title('填充完成,共'+str(i)+"次迭代\n最终图像通过对marker取反得到"), plt.axis("off")
        plt.show()



#
# #
# #
# # #【8.5】使用形态学进行连通分量的提取
# #
#
# #第一步：阈值处理
#
# img = Image.open('pic/9.5.jpg')
# # 模式L”为灰色图像
# Img = img.convert('L')
# # 自定义灰度界限，大于这个值为黑色，小于这个值为白色
# threshold = 200  #阈值
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# # 图片二值化
# photo = Img.point(table, '1')
# photo.save('pic/9.6.jpg')
#
# #第二步：图像腐蚀
#
# img1 = cv2.imread('pic/9.6.jpg')  #经阈值处理后的图像
# #设置卷积核
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
# eroded = cv2.erode(img1, kernel)
# cv2.imwrite('pic/9.7.jpg', eroded)
#
# #第三步：求连通分量中的像素数
#
# img_A = cv2.imread('pic/9.7.jpg')
# gray_A = cv2.cvtColor(img_A, cv2.COLOR_BGR2GRAY) #转换成灰度图
# # ret, thresh_A = cv2.threshold(gray_A, 50, 255, cv2.THRESH_BINARY_INV) #此处推测写错
# ret, thresh_A = cv2.threshold(gray_A, 50, 255, cv2.THRESH_BINARY)
# thresh_A_copy = thresh_A.copy() #复制thresh_A到thresh_A_copy
# thresh_B = np.zeros(gray_A.shape, np.uint8) #thresh_B大小与A相同，像素值为0
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))#3×3结构元
#
# count = [ ] #为了记录连通分量中的像素个数
# #循环，直到thresh_A_copy中的像素值全部为0
# while thresh_A_copy.any():
#     Xa_copy, Ya_copy = np.where(thresh_A_copy > 0) #thresh_A_copy中值为255的像素的坐标
#     thresh_B[Xa_copy[0]][Ya_copy[0]] = 255 #选取第一个点，并将thresh_B中对应像素值改为255
#
#     #连通分量算法，先对thresh_B进行膨胀，再和thresh_A执行and操作（取交集）
#     while True:
#         last_thresh_B = thresh_B
#         dilation_B = cv2.dilate(thresh_B, kernel, iterations=1)
#         thresh_B = cv2.bitwise_and(thresh_A, dilation_B)
#         if (last_thresh_B==thresh_B).all():
#             break
#     #取thresh_B值为255的像素坐标，并将thresh_A_copy中对应坐标像素值变为0
#     plt.rcParams['font.sans-serif'] = ['SimHei']
#     # 图像显示
#     plt.figure(figsize=(12, 5))  # width * height
#     plt.subplot(1, 3, 1), plt.imshow(eroded, cmap='gray'), plt.title('原始图像'), plt.axis("off")
#     plt.subplot(1, 3, 2), plt.imshow(thresh_B, cmap='gray'), plt.title('新图像'), plt.axis("off")
#     plt.show()
#     Xb, Yb = np.where(thresh_B > 0)
#     thresh_A_copy[Xb, Yb] = 0
#     #显示连通分量及其包含像素数量
#     count.append(len(Xb))
#     if len(count) == 0:
#         print("无连通分量")
#     if len(count) == 1:
#         print("第1个连通分量包含的像素数{}".format(count[0]))
#     if len(count) >= 2:
#         print("第{}个连通分量包含的像素数{}".format(len(count), count[-1] - count[-2]))
#
# #用来正常显示中文标签
# plt.rcParams['font.sans-serif']=['SimHei']
# # 图像显示
# plt.figure(figsize=(12, 5))  # width * height
# plt.subplot(1, 4, 1), plt.imshow(img, cmap='gray'), plt.title('原始图像'), plt.axis("off")
# plt.subplot(1, 4, 2), plt.imshow(img1, cmap='gray'), plt.title('阈值处理'), plt.axis("off")
# plt.subplot(1, 4, 3), plt.imshow(eroded, cmap='gray'), plt.title('腐蚀处理'), plt.axis("off")
# plt.subplot(1, 4, 4), plt.imshow(thresh_B, cmap='gray'), plt.title('所有均联通完毕，共有'+str(len(count) )+"个连通对象"), plt.axis("off")
# plt.show()
