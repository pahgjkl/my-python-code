#引入模块
import requests
guy = input('请import输入视频网址：')
#目标
url = guy
#爬取内容
ufghfu = requests.get(url).content
#创建文件并爬取内容储存在该文件
open('视频.mp4', 'wb').write(ufghfu)