https://blog.csdn.net/qq_38091632/article/details/121346036

需要动态打开代码中最前端定义的LOG_NDEBUG，关闭注释则log文件中可以看到该code中的等级为v的log。
可是有时候需要git pull代码，就需要退回去，很麻烦，所以编写了一个python脚本，动态修改dynamic_log_file_path.txt中列出来code路径文件的宏定义，取消掉注释。

根据该dynamic_log_file_path.txt文件中第一个cpp文件，然后决定后续文件是打开log还是关闭log。
如果第一个文件中该宏定义为注释掉，则后续会将所有的code文件都取消掉该注释（打开log）。第二次运行该python脚本则再加上注释（关闭log）。
PS:不用担心执行两次打开或执行两次关闭。
————————————————
版权声明：本文为CSDN博主「飞鸟厌鱼」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_38091632/article/details/121346036