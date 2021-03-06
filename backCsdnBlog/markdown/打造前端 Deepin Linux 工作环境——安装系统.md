---
title: "打造前端 Deepin Linux 工作环境——安装系统"
date: 2017-11-03 10:51:16 +0800
lastmod: 2017-11-03 10:51:16 +0800
author: fungleo
preview: "打造前端DeepinLinux工作环境——安装系统为什么选择DeepinLinux系统在linux操作系统的选择上，我个人不喜欢太花里胡哨的东西。曾经一度认为linux系统只应该跑在服务器上。但是archlinux改变了我的看法。可以作为一个很好的桌面系统的使用。在公司内部推广Arch的时候，还是遇到了一定的困难，虽然同事们都使用该操作系统工作，但是对于不能跑qq和"
tags: ["操作系统", "deepin", "linux", "前端"]
categories:
    - Linux\CentOS
---

# 打造前端 Deepin Linux 工作环境——安装系统

## 为什么选择 Deepin Linux 系统

在 `linux` 操作系统的选择上，我个人不喜欢太花里胡哨的东西。曾经一度认为 `linux` 系统只应该跑在服务器上。但是 `arch linux` 改变了我的看法。可以作为一个很好的桌面系统的使用。

在公司内部推广 `Arch` 的时候，还是遇到了一定的困难，虽然同事们都使用该操作系统工作，但是对于不能跑 `qq` 和 `photoshop` 还是耿耿于怀。另外，也是我个人太过于强求他们了，对于一个普通人来说，对于命令行操作还是感到一定的恐惧的。

虽然更好，但是，也需要一个过程不是么。

对于国产 `linux` 系统我个人一直不是很看好。原因是，这么多年，没哪一个做得好的。无论是当年的红旗系统，还是起点系统，亦或者乌七八糟的一堆分不清楚的麒麟系统。

直到 `Deepin` 的出现。让我真正的感受到，原来国内还真有一帮人，在非常认真的做 `linux` 系统。

经过在虚拟机的一些体验，我确实感受到了这个系统的优秀之处。虽然系统中有模仿，有羸弱的地方，但是以下的优点，还是让我决定推广这套系统。

1. 系统安装简单。`Arch Linux` 的安装我就不说了，能安装上就说明你是个高手了。
2. 界面可以设定 `windows` 或者 `Mac` 的任务栏风格，更加贴近普通用户的使用习惯。
3. 可以非常方便的安装 `qq`、`photoshop` 等 `windows` 软件。
4. 图形化程度非常高，让不熟悉命令行的朋友，也可以非常轻松的使用。
5. 同时，终端也非常好用，支持分屏，除了图标丑点，其他都完美。

还有很多很多的优点，就不详细赘述了。当然，缺点也是有的。我个人认为有以下几点：

1. 官方过于照顾新手，导致我想找点命令行操作的资料很费劲，找出来的全是图形化的东西。由于我对系统不是很熟悉，所以还是需要官方资料的支撑的。
2. 几乎所有的命名都是以**深度**开头，感觉有点全身全是`LOGO`的感觉。
3. 预装的软件有点多，这是优点也是缺点。


不管怎么样，决定安装系统了。

## 准备工作

首先，是到官方网站下载最新的系统镜像文件。

下载地址：https://www.deepin.org/download/

我下载的是 `15.4.1` 的版本，据说马上就要大版本升级了。

然后是制作系统盘。这里深度非常贴心的准备了制作工具和制作教程。

制作教程网址：https://wiki.deepin.org/index.php?title=%E5%8E%9F%E7%94%9F%E5%AE%89%E8%A3%85

制作工具下载：https://www.deepin.org/original/deepin-boot-maker/

由于我使用的是 `mac` 系统，所以我得额外下载 `mac` 版本的系统盘工具，上面的链接中也有下载。

> 有 `MAC` 版本的制作工具这一点让我非常惊讶，心中感动万分呀！

下载之后，我们打开制作软件，如下图所示：

![Deepin 系统盘制作工具](http://img.blog.csdn.net/20171103105007586?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvRnVuZ0xlbw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

制作工具非常简单，点击上面的光盘图标，选择我们刚刚下载的系统镜像光盘文件。点击下面的U盘图标，选择我们要写入的U盘，勾选格式化硬盘，点击**开始**,然后等待一分钟，就制作完成了。

系统安装盘制作完成之后，我们把U盘插到需要安装的系统上，选择U盘启动，然后进入系统的安装过程。

1. 选择语言
![](https://www.deepin.org/wp-content/uploads/2016/12/deepin-installer1.png)

2. 设置用户名密码
![](https://www.deepin.org/wp-content/uploads/2016/12/deepin-installer2.png)

3. 选择安装位置
![](https://www.deepin.org/wp-content/uploads/2016/12/deepin-installer3.png)

我推荐整块硬盘的安装，这样比较简单，就不用考虑更多的事情了。

然后就进入安装过程了，需要等待一会儿。

也可以观看官方的视频安装教程 https://deepin-web-resource.b0.upaiyun.com/install_cn.mp4

系统安装完成后，我们重新启动系统，就可以进入我们的 `Deepin Linux` 桌面了。

下一章，我们进行系统配置。

本文由 FungLeo 原创，允许转载，但转载必须保留首发链接。

