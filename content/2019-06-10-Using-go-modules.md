Title: Go Module 使用
Date: 2019-06-11
Category: Programming

## 0.开始

本文主内容用翻译自[官方博客](https://blog.golang.org/using-go-modules)，加上在使用过程中遇到的问题

## 1.介绍

Go 在1.11 和 1.12 加入了依赖管理 module。一个 module 是一个根目录有个 **go.mod** 文件的包（package）。 module 不依赖 $GOPATH，不需要将包放到 *$GOPATH/src* 目录下。

在 GO 1.11 里， 如果在工作目录或者其上级目录存在 **go.mod** 文件，并且不在 *$GOPATH/src* 目录下， module 相关命令自动打开。在 *$GOPATH/src* 目录下，需要设置环境变量 ***export GO111MODULE=on***,或者在每条语句前面加上 **GO111MODULE=on**，不然会遇到下面的错误：

```
go: modules disabled inside GOPATH/src by GO111MODULE=auto; see 'go help modules'
```

在未来的 Go 1.13 版本中， module 会默认打开。

## 2.命令

### 1.新建一个 module

跟新建包一样，只是这次不在 *$GOPATH/src* 目录下创建。这次以我写的一个 v2ray 管理 module 为例，可以从[这里](https://github.com/Gondnat/v2raymanager)找到。

目录结构如下：
```
.
├── LICENSE
├── README.md
├── go.mod
├── go.sum
├── states
│   ├── states.go
│   └── states_test.go
└── usermanager
    ├── add.go
    ├── remove.go
    └── usermanager_test.go
```

### 2.生成 **go.mod** 文件，添加依赖

首先在根目录运行

```
go mod init github.com/Gondnat/v2raymanager
```

生成 **go.mod** 文件，此时文件里只有 module 名和 Go 版本号

```
module github.com/Gondnat/v2raymanager

go 1.12
```

分别进入 states 和 usermanager 目录，运行

```
go test
```

此时应该获得类似下面的输出,

```
$ go test
go: finding github.com/golang/protobuf/proto latest
go: finding v2ray.com/core/testing/scenarios latest
...
PASS
ok  	github.com/Gondnat/v2raymanager/states	3.666s
```

此时 **go.mod** 内容应该已经变成如下，并且生成了 **go.sum** 文件, 用来存放校验值（如果没有变化，如果是在 *$GOPATH/src* 目录下，要设置环境变量 ***GO111MODULE=on***，这里 go test 并不会提示错误。）。

```
$ cat go.mod
module github.com/Gondnat/v2raymanager

go 1.12

require (
	github.com/golang/protobuf v1.3.1
	google.golang.org/grpc v1.21.1
	v2ray.com/core v4.15.0+incompatible
)
```

```
$ cat go.sum 
cloud.google.com/go v0.26.0/go.mod h1:aQUYkXzVsufM+DwF1aE+0xfcU+56JwCaLick0ClmMTw=
github.com/BurntSushi/toml v0.3.1/go.mod h1:xHWCNGjB5oqiDr8zfno3MHue2Ht5sIBksp03qcyfWMU=
github.com/client9/misspell v0.3.4/go.mod h1:qj6jICC3Q7zFZvVWo7KLAzC3yx5G7kyvSDkc90ppPyw=
...
```

### 3.其他操作

#### 显示所有依赖

```
$ go list -m all
github.com/Gondnat/v2raymanager
cloud.google.com/go v0.26.0
github.com/BurntSushi/toml v0.3.1
...
```

#### 升级依赖

比如我们想升级上面列出来的依赖 *github.com/BurntSushi/toml*， 运行 go get：
```
$ go get github.com/BurntSushi/toml
```

#### 删除无用依赖

```
$ go mod tidy
```

<p>{{ page.date | date_to_string }}</p>