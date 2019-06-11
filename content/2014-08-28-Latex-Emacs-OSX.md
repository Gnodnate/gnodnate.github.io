Title: Latex with Emacs on OS X
Date: 2014-08-28
Category: Writing

记录在OS X下使用Emacs编辑LATEX

### 0.安装LATEX

Mac版的Tex可以网站[https://tug.org/mactex/](https://tug.org/mactex/)获得，这里有提供一个2.4G的完整安装包，包括编辑器、预览等一整套立等可取软件套装，可以直接拿来编辑Latex。这里我们主要是用Emacs编辑Latex所以，只需要 下载基础安装包[BasicTex.pkg](https://tug.org/mactex/morepackages.html)并安装。

### 1.安装AUCTEX

AUCTEX是一个提供给GNU Emacs和XEmacs使用来书写和格式化的TEX的插件，提供各种宏，包括AMS-TEX, LATEX, Texinfo, ConTEXT和docTEX[(英文)](http://www.gnu.org/software/auctex/)真的不是太好翻译Orz。这里可以用源码安装，也可以使用brew安装，偷懒仍然使用brew安装。

```
brew install auctex
```

### 2.添加AUCTEX到Emacs配置文件中

在用brew安装完AUCTEX，最后会友好的提示

```
To activate, add the following to your .emacs:
  (add-to-list 'load-path "/usr/local/share/emacs/site-lisp")
  (require 'tex-site)
```

将上面的两行添加到.emacs，这是用Emacs打开或创建.tex文件，则可以在菜单栏上看到LaTex菜单，有工具栏里也有LATEX特有的Run LaTex, Run Viewer和Run BibTex三个按钮。

### 3.修改Emacs中Shell的环境变量PATH
至此可以使用Emacs编辑Tex文件，但是还有问题，编译或是预览时会提示找不到命令。这里才发现Emacs里的Shell的PATH并没有包含/usr/texbin，这里正是我们LATEX命令的目录，所以需要添加/usr/texbin到PATH中。添加如下，这里顺便添加了brew安装目录/usr/local/bin。

```
;; Set $PATH
(setenv "PATH"
        (concat
         "/usr/local/bin" ":"
         "/usr/texbin" ":"
         (getenv "PATH")))
```

至此，Emacs下才是真正的编辑LATEX。

