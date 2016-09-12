Title: 单例的实现
Date: 2016-08-25
Category: Programming

## 0. 前言

最近在面试iOS，被问到单例，我当时就蒙（这个名字似曾相识，但是真的其想不起啦，背景本人Objtive-C完全是照着将Category翻译成类别的书本和Apple的官方文档学的）。后来晚上回家上网搜了搜，这不就是单一实例对象么。讲真，我用这个功能完全是我懒得一遍遍的写alloc＋init。

## 1.Objective-C下的实现

因为这个问题是在面试iOS被问到，所以先写Objective-C下的，也是最蛋疼的一个。看看C++有多好写就知道了。
最简单的写法：

```
id A;

@implementation ClassA

+ (instancetype)shareA {
    if (A == nil) {
        A = [[self alloc]init];
    }
    return A;
}

@end

```

解释： id A是个全局变量，程序运行时候，全局变量被创建，注意这里A是个指针，我说的创建是指针变量被创建，就是存储指针的变量被创建，不是A指向的ClassA对象被创建。

这个指针是最简单的实现，只是图自己方便，不考虑被非法使用，比方说extern一下A，还有就是多线程可能存在两个线程同时调用shareA，结果生成两份A。

对于第一个extern的问题，添加static就可以限制被在其他源码文件中使用，但是请注意我这个A是在.m文件中创建的，所以你要是跑到.h声明的话，加了static，那可就是N份A了。如果你实在不太明白，请补习一下C的知识。

多线程的问题，加锁就可以。So easy。

在考虑到extern和多线程情况下，代码就改成这样：

```
static id A;

@implementation ClassA
 
+ (instancetype)shareA {
    @synchronized (A) {
        if (A == nil) {
            A = [[self alloc]init];
        }
    }
    return A;
}

@end
```
当然网上有好多把copyWithZone，allocWithZone也重写，比方说这个<http://www.cocoachina.com/cms/wap.php?action=article&id=16661>， 对于互斥锁可以参考Apple的官方文档<https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/Multithreading/ThreadSafety/ThreadSafety.html>

## 2.C++, Swift

昨天面试一下C++，好久没正经写过C++了，有点手生，面试官也让写个C++的单例，当时还想着Objective-C的单例，就写了下面这个

```
class ClassA;
static ClassA *A = NULL;
class ClassA {
public:
    static ClassA* sharedA() {
        if (NULL == A) {
            *A = ClassA();
        }
        return A;
    }
};
```

这个样写倒也没啥，就是你还得添加线程锁，太麻烦。后来回到家里，翻了下《C++ Primer》，看看拷贝构造函数（复制构造函数），和赋值函数（好吧，我承认我比较水，被问到这个的时候，我就没答得很好，就凭印象说了一通)。想来，Objective-C只有对象指针，C++可不是。

```
class ClassA {
public:
    static ClassA &sharedA() {
        return A;
    };
private:
    static ClassA A;
};

ClassA ClassA::A = ClassA();
```

Swift就更简单了，你要用的时候它已经安安静静的在那里等你了。

```
class ClassA {
    static let sharedA = ClassA()
}
    
```
