Title: Markdown in Emacs
Date: 2014-08-20
Category: Programming

简单的一个笔记,我在OS X下的Emacs的Markdown配置

1.下载[Markdown-Model](http://jblevins.org/projects/markdown-mode/)，按照网页中的介绍下载、添加启动到.emacs文件中，这里有个问题是总是提示找不到markdown-mode文件，我的解决方法是，git clone 到\~/.emacs.d下，会在.emcas.d目录下生成一个markdown-mode目录，添加\~/.emacs.d/markdown-mode到load-path。最终调用markdown-mode的配置部分如下

    ;;Markdown-Mode
    (add-to-list 'load-path "~/.emacs.d/markdown-mode/")
    (autoload 'markdown-mode "markdown-mode" "Major mode for editing Markdown files" t)
    (add-to-list 'auto-mode-alist '("\\.markdown\\'". markdown-mode))
    (add-to-list 'auto-mode-alist '("\\.md\\'". markdown-mode))

2.经过上面的设置在Emacs中打开.md或是.markdown的文件，就可以有高亮显示并可以有多中快捷键使用，可参考markdown-mode的主页，也就是上面的下载页面。现在如果你使用C-c C-c p预览，或是C-c C-c m生成html，会提示没有markdown这个命令。这里使用[Homebrew](http://brew.sh)安装pandoc，使用pandoc将Markdown转换成html。创建一个名为markdown的脚本文件，内容如下，将其拷贝到/bin或/usr/bin目录下，并赋予可执行权限。至此就可以正常使用预览功能。

```
/usr/local/bin/pandoc -f markdown -t html -s --mathjax --highlight-style pygments $1
```

参考：[http://panqiincs.github.io/blog/2013/05/03/emacs-markdown-mode/](http://panqiincs.github.io/blog/2013/05/03/emacs-markdown-mode/)

<p>{{ page.date | date_to_string }}</p>