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

- [PyQt5使用Designer设计UI的两种实现方式](https://blog.csdn.net/chlk118/article/details/72595325)
- 让我纠结下sys.exit(app.exec_())和app.exec_()的区别，为什么第一个会报错 = =
    > 报错如下, Exception has occurred: SystemExit 0  
    > ***ps:这个exit(0)在python中不是正常退出的语句莫...***
    - app.exec_():是QApplication的方法,作用是"进入程序的主循环直到exit()被调用"
    - 只使用app.exec_()，程序一样可以正常运行，但是关闭窗口后进程却不会退出，尝试print输出app.exec_()的结果，返回0，于是再做修改：
    - [详细解释](https://stackoverflow.com/questions/25719524/difference-between-sys-exitapp-exec-and-app-exec)

## 待办事项

- [x] PyQt学习-初步实现窗体关系
    - [x] 调用窗体弹出
    - [x] 信号与槽
    - [x] UI界面的调用
    - [x] 父窗体弹出子窗体
    - [x] 主界面先隐藏弹出登录窗体
    - [x] 登录成功关闭子窗体弹出父窗体
- [ ] 按钮的UI
- [ ] 计时功能
- [ ] 初步实现开始计时和结束计时
- [ ] 到处记录时间段为excel
- [ ] 设置多个计时选项
- [ ] 测试多个选项导出的excel
- [x] 项目打包成Windows.exe

## 项目打包

- EXE生成代码：
- **注意**
    - -F：生成单个可执行文件
    - -w：生成文件为Windows窗体

```EXE生成代码：
pyinstaller.exe -F -w --specpath .\outputExe\ --workpath .\outputEXE\ .\main.py --distpath .\
```