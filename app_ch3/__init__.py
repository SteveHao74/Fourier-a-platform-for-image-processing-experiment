#这个空文件事关重要，名为的空文件是跨目录调用模块的关键  https://blog.csdn.net/qq_28072715/article/details/80939699_init_.py

import  os
import  sys

BASE_DIR= os.path.abspath(os.path.dirname(__file__))
sys.path.append(BASE_DIR )