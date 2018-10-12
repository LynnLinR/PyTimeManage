# 时间管理

- 类型：工作、汇报、空闲、睡觉、学习、查资料

## python 做app----时间管理软件

> __最近感觉自己大部分时间都浪费在了发呆\走神和等待,实际做事效率非常低__
- 需求大体:
    1. 时间状态:睡觉、创造性工作、日常学习、工作汇报、食物、空闲、运动、其他[后期支持拓展]
    2. 初期单任务进行，后期多任务进行分配专注度
    3. 每周将所有时间汇总成饼图
    4. 后期获取root权限，手机动作监控(安卓机)如果可行的话
    5. 桌面端和app端口同步

### button大体思路

- 需要用到的插件：tkin、exwrite、exread、time获取时间差
- 15分钟一个单元，每个动作都是通过桌面右边的button进行操作
    > 通过button进行时间存储，通过exwrite进行增量的添加时间表到excel中。  
__excel形式成功后切换为数据库-MySQL__

### python学习-tkiner桌面应用

> [___python图形应用GUI开发框架___](https://blog.csdn.net/tTU1EvLDeLFq5btqiK/article/details/78693348)  
[python模块tkinter介绍](https://docs.python.org/3.7/library/tkinter.html#how-tk-and-tkinter-are-related)
[pyQt模块](https://www.cnblogs.com/archisama/p/5444032.html)

#### ***问题解决***

- VS code中PyQt报错问题:<https://www.jianshu.com/p/73d41faaf469>

- 界面只有6个button 和 汇报按钮

### 汇报功能

- 需要用到的模块：pyecharts
- 对excel数据进行读取和处理后通过pyecharts以网页形式展示
    > 形式：柱状图:Bar 每个类型总时间  
饼图（类型之间的比例）  Pie
日历热力图：HeatMap  
每日时间轴对比:Bar 变形
分析工作专注度：Liquid
最佳工作时间：Pie(每日的指定时间的工作专注度)
最佳工作时间：Polar

### 后期加入探索

- 提醒任务，短信、桌面、app提示推送
- 日历对应时间轴
- 任务对应时间轴进行效率计算
- 监控动作（需要获取桌面句柄得到当前做的事情）

## 学习部分

[PyQt5使用Designer设计UI的两种实现方式](https://blog.csdn.net/chlk118/article/details/72595325)

## 待办事项

- [ ] PyQt学习
    - [x] 调用窗体弹出
    - [x] 信号与槽
    - [x] UI界面的调用
    - [x] 父窗体弹出子窗体
    - [ ] 主界面先隐藏弹出登录窗体
    - [ ] 登录成功关闭子窗体弹出父窗体
- [ ] 计时功能
- [ ] 初步实现开始计时和结束计时
- [ ] 到处记录时间段为excel
- [ ] 设置多个计时选项
- [ ] 测试多个选项导出的excel
- [x] 项目打包成Windows.exe

## 项目打包

- EXE生成代码：

```EXE生成代码：
pyinstaller.exe --specpath .\outputExe\ --workpath .\outputEXE\ .\Test.py --distpath .\
```