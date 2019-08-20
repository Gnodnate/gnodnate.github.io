Title: macOS App 自动升级实现
Date: 2019-09-20
Category: Programming

# 0. 序

macOS 下 AppStore 外分发的 App 升级最常用的是 [Sparkle](https://sparkle-project.org)。
哪还有这边文章主要是因为，公司 Windows App 已经有一套升级服务器接口，不想再为 Mac App 单独设置一套接口，所以 Mac App这边只能自己实现自动升级了🤷🏻‍。然后就有了这边算是笔记吧。

# 1.开工

实现自动升级，可以分为3部分

1. 下载更新包
2. 用新版覆盖旧版App
3. 运行新版App

## 1.1下载更新包

这个，直接调 URLSession 下载就可以，或者你也可以像我一样骚气的用 XPC 实现也可以。关于 XPC 可以点击[这里](https://developer.apple.com/videos/play/wwdc2011/206/)

## 1.2 用新版覆盖旧版App

这部分，其实需要分成两部，

### 1.2.1 退出当前运行的旧版 App

退出旧版 App，直接调用 NSApp.terminal(nil) 就可以。

### 1.2.2 用新版覆盖旧版本

覆盖部分，就不能再当前进程处理了，所以这里应该要启动一个 helper 进程，在旧版本退出后，用新版覆盖旧版。

这里，我是用三行 shell 实现的, 如下，先 while 循环等待当前进程退出，然后删除旧版本，拷贝新版

```
:::shell
while /bin/kill -0 ${pid} >&/dev/null; do /bin/sleep 0.1; done; 
rm -fr ${oldVersion}
cp -r ${newVersion} ${oldVersion}
```

## 1.3 运行新版App

运行新版本，这里有个问题要注意，从网络下载的 App 会被系统标记为网络下载，直接打开会有下面提示框。 

![Warning]({filename}/images/warning.png)

在打开之前，使用下面 shell 命令先去除这个标记。

```
:::shell
/usr/bin/xattr -d -r com.apple.quarantine ${appPath}
```

然后就是直接调用 open 命令打开新版本 App 了

```
:::shell
/usr/bin/open ${appPath}
```

# 2.完整实现代码

最后附上 Swift 下的完整实现代码

```
:::swift
    func updateToNewVersion(at url:URL) {
        let task = Process()
        if #available(macOS 10.13, *) {
            task.executableURL = URL(fileURLWithPath: "/bin/sh")
        } else {
            task.launchPath = "/bin/sh"
        }
        let mountPoint = NSTemporaryDirectory().appending("\(arc4random())/")
        if !FileManager.default.fileExists(atPath: mountPoint) {
            do {
                try FileManager.default.createDirectory(atPath: mountPoint, withIntermediateDirectories: true, attributes: nil)
            } catch {
                assert(false)
                return
            }
        }
        let shellScript = String(format: "/usr/bin/hdiutil attach %@ -nobrowse -mountpoint %@", url.path.replacingOccurrences(of: " ", with: "\\ "), mountPoint)
        task.arguments = ["-c", shellScript]
        task.launch()
        task.waitUntilExit()
        if task.terminationStatus  == 0 {
            let enumer = FileManager.default.enumerator(atPath: mountPoint)
            while let fileName = enumer?.nextObject() as? String {
                if fileName.hasSuffix(".app") {
                    let newVersionAppPath = mountPoint.appending(fileName)
                    if let currentRuningAppPath = NSRunningApplication.current.bundleURL?.path {
                        let pid = ProcessInfo.processInfo.processIdentifier
                        // remove download from website flag, avoid popup warning window
                        let removeFlag = "/usr/bin/xattr -d -r com.apple.quarantine \"\(currentRuningAppPath)\""
                        
                        let script =
                            "while /bin/kill -0 \(pid) >&/dev/null; do /bin/sleep 0.1; done; rm -fr \"\(currentRuningAppPath)\" && cp -r \"\(newVersionAppPath)\" \"\(currentRuningAppPath)\" && \(removeFlag); /usr/bin/open \"\(currentRuningAppPath)\"; /usr/bin/hdiutil detach \(mountPoint) &"
                        let task = Process()
                        if #available(macOS 10.13, *) {
                            task.executableURL = URL(fileURLWithPath: "/bin/sh")
                        } else {
                            task.launchPath = "/bin/sh"
                        }
                        task.arguments = ["-c", script]
                        task.launch()
                        NSApp.terminate(nil)
                    }
                }
            }
        }
        Process.launchedProcess(launchPath: "/usr/bin/hdiutil", arguments: ["detach", mountPoint])
    }
```