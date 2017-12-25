#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import argparse
import os
import imghdr
from PIL import Image

# 错误退出函数
def errMsn(msn):
    print('\033[31mError:\033[0m ' + msn)
    parser.print_usage()
    exit()

# 在源目录中找到所有图片并输出为数组
def findImg(sdir):
    res = []
    if not os.path.exists(sDir):
        errMsn('Source directory don\'t exist')
    for f in os.listdir(sdir):
        fp = os.path.join(sdir, f)
        if not os.path.isdir(fp):
            if imghdr.what(fp):
                res.append(fp)
    if len(res) == 0:
        errMsn('There is no image in the source directory')
    else:
        return res

# 循环缩放所有图片
def resizeImg(arr, size, tdir, imgQual):
    for img in arr:
        simg = Image.open(img)
        simg_w = simg.size[0]
        simg_h = simg.size[1]
        
        # 如果原图片宽高均小于设置尺寸，则将原图直接复制到目标目录中
        if simg_w <= size and simg_h <= size:
            simg.save(tdir + '/' + os.path.basename(img), quality=imgQual)
        else:
            timg_w = size
            timg_h = int(size * simg_h / simg_w)
            if simg_w < simg_h:
                timg_w = int(size * simg_w / simg_h)
                timg_h = size
            timg = simg.resize((timg_w, timg_h),Image.ANTIALIAS)
            timg.save(tdir + '/' + os.path.basename(img), quality=imgQual)
    print('\033[32mSuccess:\033[0m Task Finish')

# 如果目标目录为空时提示用户确认
def checkTargetDir(sdir, tdir):
    if not tdir:
        print('\033[33mWarning:\033[0m If the target directory isn\'t set, the processing '\
                'results will cover the picture in the source directory\n'\
                '\033[36mWhether to Continue(Y/n)\033[0m ')
        confirm = input('Confirm:')
        if confirm in ('', 'Y', 'y'):
            print('\033[34mInfo:\033[0m The target directory is ' + sdir)
            return sdir
        elif confirm in ('N', 'n'):
            exit()
        else:
            print('Input error, program exit')
            exit()

if __name__ == "__main__":
    # 设置命令行参数
    parser = argparse.ArgumentParser()
    parser.description='Output to the target directory after processing the picture\
            in the source directory based on the parameters'
    parser.add_argument("-v", "--version",action='version', version='%(prog)s 1.0')
    parser.add_argument('size', type=int, help='The max width or max height of a picture')
    parser.add_argument('sourceDir', help='Source directory')
    parser.add_argument('targetDir', help='Target directory', nargs='?')
    parser.add_argument('-q', '--quality', type=int, help='Save picture quality, default 60')
    args = parser.parse_args()

    size = args.size
    sDir = args.sourceDir
    tDir = args.targetDir or checkTargetDir(sDir,args.targetDir)
    imgQual = args.quality or 60
    # 执行处理 
    resizeImg(findImg(sDir), size, tDir, imgQual)
