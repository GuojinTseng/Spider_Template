# coding:utf8

# Author: Guojin Tseng
# Date: 2017.2.11

import url_manager, html_downloader, html_parser, final_outputer

class SpiderMain(object):

    def __init__(self):                                                                 #初始化总调度程序
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = final_outputer.OutPuter()

    def craw(self, root_url):                                                           #定义方法
        count = 1
        self.urls.add_new_url(root_url)                                                 #从入口URL开始，同时将入口URL添加进URL管理器的待爬取的URL列表
        while self.urls.has_new_url():                                                  #判断是否有新的URL
            try:
                new_url = self.urls.get_new_url()                                       #从URL管理器中的待爬取的URL列表中获取一个新的URL
                print 'craw %d: %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)                           #从这个新的URL中下载对应的网页
                new_urls, new_data = self.parser.parse(new_url, html_cont)              #从下载的网页中解析出html网页的内容
                self.urls.add_new_urls(new_urls)                                        #将解析出来的URL添加进待爬取的URL列表
                self.outputer.collect_data(new_data)                                    #将获取的有用数据添加进数据管理器
                if count == 5:
                    break
                count += 1
            except:
                print "fialed"
        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"                               #设定入口URL
    obj_spider = SpiderMain()                                                           #建立爬虫总调度程序对象
    obj_spider.craw(root_url)                                                           #从入口URL开始爬虫程序