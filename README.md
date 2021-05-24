# AutoXuexiQiangGuo
> 学习强国，坚持四个自信
Python自动化代码

> 本项目不再维护，已有新的解决方案，通过实机进行，目前能够较为稳定地看视频、阅读文章、评论、转发等功能，每天保底35分，答题功能暂时不够完善，但也能进行，如果有需要，可邮箱联系。

**PS：程序已打包，在Win7 32位和64位下测试通过**
**Mongodb文件过大，没有上传完成，会导致错误，请自行到 http://downloads.mongodb.org/win32/mongodb-win32-i386-3.2.22.zip 下载，将文件夹命名为mongodb，覆盖原文件。**如下图所示：

![image_1d7b8p6v1tkjqha108pqvj1tvd9.png-31.2kB][8]

# 2018年3月27日版本
## 1 配置运行
**首次运行**：
1. 下载“learn_xi”压缩包。将文件解压到D盘根目录下，地址如下图：
![解压地址][1]
2. ① 以管理员方式运行文件“1. 数据库测试(以管理员方式运行).bat”。
② 如果出现需要联网的情况，点击允许访问。如下图：
![允许联网][2]
③ 当出现下图时，表明mongodb数据库启动成功，**将该窗口关闭**。
![image_1d7937dek1ekvbcl11qt1qndas113.png-74.9kB][3]

3. 以管理员窗口方式运行文件“2. 数据库配置和恢复(以管理员方式运行).bat”。
如下图所示，则表明数据库导入成功。任意键退出该窗口。
![image_1d793b3rn19ub1krg1rlm1lmc16u21g.png-78.5kB][4]

4. 安装“learn_xi/soft/”目录下的Chrome浏览器安装包，建议覆盖安装，防止版本不一致影响学习。
![image_1d794bsb810f61tkj13qk1kfdrth2n.png-20.7kB][7]

5. 运行文件“4. 开始学习.bat”，出现需要联网，点击允许访问。
如下图所示，根据提示输入用户名和密码即可开始学习。
![image_1d793kukc1nup2pt1fubd5u66m1t.png-24.4kB][5]

**之后运行**
1. 管理员方式运行文件“3. 开启服务(以管理员方式运行)”，如下图所示，表示数据库服务启动完成。
![image_1d793pfh01s7e7a18mlde5qv02a.png-32.3kB][6]

2. 运行文件“4. 开始学习.bat”。输入用户名和密码开始学习。

## 2 目前完成功能
1. 3月28日学习强国官方修改规则，网页端每日积分由31分改为25分。（登录1分，阅读文章12分，视频观看12分）
2. 引入数据库，防止重复阅读文章和观看视频使得积分无法获取。
3. 实现用户名和密码模拟自动登录，不用手机手动扫码。

## 3. 接下来版本
1. 多线程运行，缩短学习时长。


  [1]: http://static.zybuluo.com/a5e64332/wvvqw4hp9glylxaf6wyg4ks7/image_1d792prb6127v2ft17j6f811a019.png
  [2]: http://static.zybuluo.com/a5e64332/luej85fwyzk1trsu4hrbiobb/image_1d7932u5d13m5tho12e4c9cjmem.png
  [3]: http://static.zybuluo.com/a5e64332/lz65cmwmtnjgmzxxvnfkf190/image_1d7937dek1ekvbcl11qt1qndas113.png
  [4]: http://static.zybuluo.com/a5e64332/v843lbmk2ocgtzdzzd4vbjk0/image_1d793b3rn19ub1krg1rlm1lmc16u21g.png
  [5]: http://static.zybuluo.com/a5e64332/ope1bc8keppdkbrazccrcxwo/image_1d793kukc1nup2pt1fubd5u66m1t.png
  [6]: http://static.zybuluo.com/a5e64332/trp0xrnd8her10e5monf7e4q/image_1d793pfh01s7e7a18mlde5qv02a.png
  [7]: http://static.zybuluo.com/a5e64332/qxpqn3bw19s6fa2zujqooik2/image_1d794bsb810f61tkj13qk1kfdrth2n.png
  [8]: http://static.zybuluo.com/a5e64332/26m8oyaou8n5qc5chtw1mc98/image_1d7b8p6v1tkjqha108pqvj1tvd9.png

# 2019年3月23日更新版本
## 1 配置运行
- python版本
安装python3.5版本
- pip包
pip install -v selenium==3.141
pip install -v urlib3==1.24.1
pip install -v pymongo==3.7.2
- chrome
本版本安装的为最新稳定版（73.0.3683.86）
- chromedriver版本
根据chrome进行选择，访问[chromedriver官网](http://chromedriver.chromium.org/downloads)。
- MongoDB版本
本版本安装的为最新版（4.0.6），访问[Mongodb官网](https://www.mongodb.com/download-center/community)

## 2 目前版本
1. 视频观看 √
2. 文章阅读 √
3. 获取总积分和今日积分 √
4. 可手工扫码登录或使用cookies登录（由于Cookies只能保持6小时，所以主版本暂时使用扫码登录） √
5. 每天最多可学习31分（登录1分，阅读文章14分，视频观看16分）。 √
6. 将文章数据和视频数据添加到mongodb数据库中。 √   （get_link.py）
7. 通过获取数据中的数据对文章进行阅读和对视频进行观看。 (interface_test.py) √

## 3 接下来版本
1. 模拟自动登录（可参考微信网页版登录方式进行测试）。
2. 继续模拟积分规则。

# 2019年3月15日版本
## 1 配置运行
- python版本
安装python3.5版本
- pip包
pip install -v selenium==3.141
pip install -v urlib3==1.24.1
- chrome
- chromedriver版本
根据chrome进行选择，访问[chromedriver官网](http://chromedriver.chromium.org/downloads)。

## 2 目前版本
1. 视频观看 √
2. 文章阅读 √
3. 获取总积分和今日积分 √
4. 可手工扫码登录或使用cookies登录（由于Cookies只能保持6小时，所以主版本暂时使用扫码登录） √
5. 每天最多可学习31分（登录1分，阅读文章14分，视频观看16分）。 √

## 3 接下来版本
1. 将视频链接和文章链接放入数据库，查重之后每天更新。
2. 每天播放不同的短视频和阅读不同的文章。（PS：获取积分判断有些迷，貌似是24小时内阅读的文章是算做同一篇文章，所以阅读不算积分，还在测试）
3. 模拟自动登录（可参考微信网页版登录方式进行测试）。
