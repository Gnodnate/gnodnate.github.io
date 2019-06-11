Title: Get Spec from RPM file
Date: 2015-10-29
Category: Linux

## 0. 前言
常言道程序猿的成长道路就是Ctrl-C ＋ Ctrl-V (OS X用户自动切换到⌘-C + ⌘-V). Coding之路上少不了要借鉴前辈的code，这也是开源的好处之一。

## 1. 原因
因为要给一个Qt开发的程序打rpm包，以支持SUSE和RedHat，so 如果用户的桌面环境不是基于Qt的KDE之类的，就有可能系统中没有Qt的运行库，所以要在安装包里声明需要安装Qt的运行库, 在RPM平台上是 libQtGui.so.4, 本来以为可以像deb包写道Requires后面，像这样：

    Requires: libQtGui4 >= 4.8.0

但是，这样是万万不行滴，然后发现SUSE下 libQtGui.so.4 的包名是 libqt4-x11，在RedHat下这个包是qt4-x11。所以就想这个是不是要区分对待。Google下得到了这篇[openSUSE:Build Service cross distribution howto](https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto)，然后写成这样

    %if 0%{?suse_version} > 0
    Requires: libqt4-x11
    %else
    Requires: qt4-x11
    %endif

结果经过两天悲剧的发现，这个判断是在打包时进行的判断(说多了都是泪啊)。

## 2. 解决
然后想想还是看看前辈们是怎么弄的吧，解压rpm包发现，没有spec文件，然后再Google下，在[stackoverflow](http://stackoverflow.com)找到了这篇[extract the spec file from rpm package](http://stackoverflow.com/questions/5613954/extract-the-spec-file-from-rpm-package)
总结下就是：

0. 安装rpmrebuild

1. 直接从rpm获取spec用这句：

    rpmrebuild --package --notest-install -e [targetrpmfile]


2. 获取已安装的软件的spec文件用这句：

    rpmrebuild -s [outputSpecFileName].spec [softwareName]

获取了下Google chrome浏览器的spec如下：

    Provides:      google-chrome = 46.0.2490.80
    Provides:      google-chrome-stable = 46.0.2490.80-1
    Provides:      google-chrome-stable(x86-64) = 46.0.2490.80-1
    Requires:      lsb >= 4.0
    Requires:      libcurl.so.4()(64bit)
    Requires:      libnss3.so(NSS_3.14.3)(64bit)
    Requires:      wget
    Requires:      xdg-utils
    Requires:      zlib
    Requires:      ld-linux-x86-64.so.2()(64bit)
    Requires:      ld-linux-x86-64.so.2(GLIBC_2.2.5)(64bit)
    Requires:      ld-linux-x86-64.so.2(GLIBC_2.3)(64bit)
    Requires:      libasound.so.2()(64bit)
    Requires:      libatk-1.0.so.0()(64bit)
    Requires:      libcairo.so.2()(64bit)
    Requires:      libc.so.6()(64bit)
    Requires:      libc.so.6(GLIBC_2.11)(64bit)
    Requires:      libc.so.6(GLIBC_2.2.5)(64bit)
    Requires:      libc.so.6(GLIBC_2.3.2)(64bit)
    Requires:      libc.so.6(GLIBC_2.3.4)(64bit)
    Requires:      libc.so.6(GLIBC_2.3)(64bit)

可以看到Requires后面跟的是库的名字，写法应该是这样：

    Requires: libQtGui.so.4

#### 参考链接:

[openSUSE:Build Service cross distribution howto](https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto)

[extract the spec file from rpm package](http://stackoverflow.com/questions/5613954/extract-the-spec-file-from-rpm-package)

<p>{{ page.date | date_to_string }}</p>