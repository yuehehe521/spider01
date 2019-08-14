import scrapy
from scrapy import cmdline
from spider01.items import Spider01Item
import sys

class MySpider(scrapy.Spider):
    name = "tieba_spider"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "http://tieba.baidu.com/f?kw=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB&ie=utf-8",
    ]

    def parse(self, response):
        a = response.xpath('//*[@id="thread_list"]/li[2]/div')

        titles = response.xpath("//div[@class = 'threadlist_title pull_left j_th_tit ']/a/text()")
        authors = response.xpath("//span[@class = 'frs-author-name-wrap']/a/text()")
        replys  = response.xpath("//span[@class = 'threadlist_rep_num center_text']/text()")

        #// *[ @ id = "thread_list"] / li[2] / div / div[2] / div[1] / div[1] 只是精确取到某一条数据
        length = len(authors)
        #取到响应的数组类型的数据，可在cmd
        print("length: "+str(length))
        print("titles:" + str(titles))
        print("authors:" + str(authors))
        print("replys:"+str(replys))
        print("===========================")

        #从0开始，就是从第一条取
        for i in range(0,length):
            #第一条是置顶的贴 导致作者和回复数都需要取下一条:（i+1）
            print("title: "+titles[i].extract())
            print("author: "+authors[i+1].extract())
            print("reply: "+replys[i+1].extract())
            print("@@@@@@@@@@@@@@@@")

        # print("aa"+str(a))
        # for line in a:
        #     item = Spider01Item()
        #
        #     item['title'] = line.xpath(
        #         '//*[@id="thread_list"]/li[2]/div/div[2]/div[1]/div[1]/a/text()').extract()
        #     item['author'] = line.xpath(
        #         '//*[@id="thread_list"]/li[2]/div/div[2]/div[2]/div[1]/div/text()').extract()
        #     item['reply'] = line.xpath(
        #         '//*[@id="thread_list"]/li[2]/div/div[1]/span/text()').extract()
        #     yield item



if __name__=='__main__':
    cmdline.execute("scrapy crawl tieba_spider -o item.json --nolog ".split())
