# 西二考核综述

2024.9.20-2025.4.17，西二ai的考核告一段落。

总而来说，五轮考核，这半年多的学习对我来说受益匪浅。不过实际上并没有每天都在写这部分的内容。

第一轮的宝可梦我花了5天的时间，大致是在10月的中旬，每天1-2h。因为此前有一些基础，所以这部分对我来说主要是积累写项目的经验，并且学习一些python的特性，比如说装饰器之类的。与此同时，cs61a我也写了两个lab，最后还是没能坚持下去。

其实本来我以为自己宝可梦都过不去，但最后写的还行！

当然还有看李宏毅的ai导论，形成宏观概念受益匪浅。

第二轮有四个任务，爬取教务处那部分我花了一个晚上的时间，大致是11月中下旬的某天下午4点到凌晨两点，写出了第一个爬虫，纯使用正则实现。

第二个任务是知乎的爬取，这部分实际上我是放在了ddl前一周写的，大致是在12月末。因为是一个新的框架，而且爬的还很慢，最后十条甚至还没爬出来，这也是一个遗憾吧。

第三个任务是对第二轮第一个任务数据的处理，与第四个任务一起本来是要使用jupter book实现，不过最后我还是没使用。可能是当时在那边已经准备开始搞cs231n，看到了colab，就懒得搞jupter book了。我2.1爬了02年到24年的数据，所以分析的数据除了给定的要求外，额外增加了对月份以及对星期的分析。这部分大致是在12月初写的。

第四个任务没什么好说的，就是查询logic函数以及绘制，与第三个任务一并完成。

然后是第三到五轮，是做完公开课cs231n。

这门课主要是对底层的剖析，主要是让我知道大概现在ai是干嘛的，怎么搭起来的等等。

第三轮主要是学习了knn，svm，softmax，反向传播，以及如何搭双层神经网络。这部分的难点主要是——

第一，你看完课不知道你要干啥

第二，numpy

第三，反向传播

其实我觉得主要的难点是第一个，我看完了课之后完全不知道我要做什么。

反向传播也是，除了极少数的公式是自己推导的，大部分都是拾人牙慧。

其他其实没什么，知道了自己要做什么之后，其实就还好。

第四轮是实现三层卷积神经网络，引入了卷积核等概念。我大致是在三月末写完的。

这部分的难点我认为依旧是反向传播，不知道公式。因此公式这部分始终是拾人牙慧（

其他的实现其实也还好，知道自己要干嘛了之后其实比想象中的会简单。

在使用纯numpy搓完了a1.1-a2.4之后，a2.5告诉你之前的所有东西都可以用pytorch实现！

已经忘记当时的心情了，明明心里觉得确实应该是这样的学习流程，但是总感觉有种被耍了的感觉（

第五轮在4月中旬结束，这主要是介绍了rnn，transformer，gnn以及ssl。有了pytorch之后，实际上的难点就是对这些的理解，当然还有万恶的公式。

上述具体的详情内容，也就是具体的学习过程可以见具体的文件夹，这里只是一个综述罢了。

可能我还有一个别人没有的第“3.5”轮，在寒假期间（大约2至3月）参加了一个项目，号称是可以减轻点考核过程的，所以就来了（

在这个ai项目里我主要负责爬虫，服务端的实现（protobuf），环境配置（清理项目依赖等）以及撰写prompt。

由于这部分并不在正常考核范围之内，所以并没有写详细的学习过程，仅在综述里贴上。

服务端的实现（与ai无关）主要参考了这系列视频【grpc-python01--引言】 https://www.bilibili.com/video/BV1Bk4y167r8/?share_source=copy_web&vd_source=3fbbb3c2ad24817002f9c39fad247a3b ，环境配置等自己琢磨的，撰写prompt的主要思想来源来自于李宏毅的ai导论

这段经历对我来说十分重要，不只是能力的扩充，做项目的整个流程思路，更重要的收获了一个道理

不管现在会啥还是不会啥，保证ddl产出即可。

其实最后的结果比我想象中的好多了，主导项目的学长对我的评价也还不错？

应该吧（

没给大佬们拖后腿就很好了！

就这样吧！

希望明天能更好！

2025年4月17日23时59分星期四