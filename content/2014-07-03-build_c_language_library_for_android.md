Title: Build C Language Library for Android
Date: 2016-07-03
Category: Programming

### 0.Introduction
Android apps are written in Java, Java have provide [JNI(Java Native Interface)](http://en.wikipedia.org/wiki/Java_Native_Interface) to call or be called by native applications and libraries written in other language such as C/C++ and assembly. Android provide NDK(Native Development Kit) to support native development in C/C++.

### 1.Installing NDK

The NDK can be download from [Android Developer Website](http://developer.android.com/tools/sdk/ndk/index.html). After downloaded, we get an archive package, unpack it to whereever you want, and replace the full path with *`<NDK-Path>`* in below.

### 2.Use Mobile Print Project as an example

Step 0: Read *<NDK-Path>/docs/OVERVIEW.html* is helpful to understand the below steps.

Step 1: Create a project directory named "exampleProject", and a subdir named "jni", copy the C/C++ code to "jni"
>exampleProject can be change whatever you want

Step 2: Create a file named "Android.mk", contains is likely as follow:

```
LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)
LOCAL_MODULE := PMX_MobilePrinter
LOCAL_SRC_FILES := test.c \
test1.c
LOCAL_C_INCLUDES := test.h
include $(BUILD_STATIC_LIBRARY)
```
The last line means, the output will be a static library, BUILD\_SHARED_LIBRARY is for shared library.

### 3.Build for different platform

By default, the library is build for arm.Platforms are define in file "`Application.mk`" under *jni* directory, contains as follow:

	APP_ABI := all
	
We need build for all platform, so the value after APP_ABI is `all`, which can be changed to `armabi/armabi-v7a/x86/mips`. Need to support different platform one time, just write as below, split with blank space.
	
	APP_ABI := armabi armabi-v7a x86 mips
	
### 4.Build the library
Go to the "jni", run build command *<NDK-path>/ndk-build* in Terminal(Mac/Linux)/CMD(Windows). Then you will find our library in *`exampleProject/obj/local/<PlatformName>/libPMX_MobilePrinter.a`*. Build shared library is placed in *`exampleProject/libs/<PlatformName>/libPMX_MobilePrinter.so`*.

