# -*- coding: utf-8 -*-
import emoji
import re
from selenium import webdriver
from lxml import etree
import time
import requests
import pymysql
import os


class Hdb(object):
    def __init__(self):
        self.page = 1
        self.kb_num = 0
        self.chrome()
        self.href_list = []
        self.db = SaveDB()

        self.cat_url_dict = {"亲子": "https://www.hudongba.com/quanguo/98-0-0-0-0-1/",
                             "互联网": "https://www.hudongba.com/quanguo/101-0-0-0-0-1/",
                             "创业": "https://www.hudongba.com/quanguo/110-0-0-0-0-1/",
                             "职业培训": "https://www.hudongba.com/quanguo/115-0-0-0-0-1/",
                             "兴趣培养": "https://www.hudongba.com/quanguo/107-0-0-0-0-1/",
                             "运动户外": "https://www.hudongba.com/quanguo/102-0-0-0-0-1/",
                             "交友": "https://www.hudongba.com/quanguo/103-0-0-0-0-1/",
                             "丽人": "https://www.hudongba.com/quanguo/104-0-0-0-0-1/",
                             "企业服务": "https://www.hudongba.com/quanguo/125-0-0-0-0-1/",
                             "演出": "https://www.hudongba.com/quanguo/105-0-0-0-0-1/",
                             "公益": "https://www.hudongba.com/quanguo/111-0-0-0-0-1/",
                             "行业活动": "https://www.hudongba.com/quanguo/108-0-0-0-0-1/",
                             "线上活动": "https://www.hudongba.com/quanguo/119-0-0-0-0-1/"}


    # 开启一个chrome
    def chrome(self):
        try:
            self.driver.quit()
        except:
            pass

        chrome_options = webdriver.ChromeOptions()

        prefs = {
            'profile.default_content_setting_values': {
                'images': 2,                           # 不加载图片
                # 'javascript': 2                      # 不执行js
            }
        }
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument('--headless')       # 隐藏浏览器
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.set_page_load_timeout(30)           # 超时时间

    # https://www.hudongba.com/quanguo/98-0-2-0-0-1/
    def run(self):
        for k, v in self.cat_url_dict.items():
            self.href_list = []
            self.kb_num = 0
            self.page = 0
            print("开始执行类目:", k)
            self.req_chrome(v.strip("1/"), k)

            self.write_text(k)

    def write_text(self, k):
        print(k, "总数:", len(self.href_list))
        with open("href_list.txt", "a", encoding="utf8") as f:
            for href in self.href_list:
                f.write(href+"\n")

    def req_chrome(self, url, cat=None):
        """
        循环page请求列表页
        :param url: 列表页链接
        :param cat: 类目名
        """
        while 1:
            self.driver.get(url+str(self.page))
            result = self.parse_list_page()

            self.page += 1

            if result == "不再翻页":
                break

            time.sleep(1)

    def parse_list_page(self):
        """
        解析列表页
        :return: "不在翻页"  or  无返回值不作处理
        """
        try:
            html = etree.HTML(self.driver.page_source)
            li_list= html.xpath("//ul[@class='find_main_ul dataViewClass']/li")
            over_num = 0   # 已结束活动计数

            for li in li_list:
                href = li.xpath("./a/@href")[0]
                b_time = li.xpath(".//div[@class='find_main_time']/p/text()")[0]

                if '已结束' not in b_time:
                    self.href_list.append(href)
                else:
                    over_num += 1

            # 当前页面已结束活动大于35不在翻页
            if over_num >= 35:
                return "不再翻页"

            # 连续空白 有空白页不代表到底,可能是页面问题
            if len(li_list) == 0:
                self.kb_num += 1
            else:
                self.kb_num = 0

            if self.kb_num >= 5:
                return "不再翻页"

        except Exception as e:
            print(e)
            with open("失败.txt", "w") as f:
                f.write(self.driver.current_url + "\n")

    def qc(self):
        """
        对获取的详情页链接进行去重
        """
        with open("href_list.txt", encoding="utf8") as f:
            items = f.readlines()
        print("去重前数量:", len(items))

        self.href_list = list(set(items))
        print("去重后数量:", len(self.href_list))

        with open("href_list.txt", "w", encoding="utf8") as f:
            for i in self.href_list:
                f.write(i)

    def index(self):
        """
        循环请求详情页链接
        """
        with open("href_list.txt", "r", encoding="utf8") as f:
            href_list = f.readlines()

        for href in href_list:
            try:
                print("正在抓取:", href)
                self.driver.get(href.strip("\n"))
                self.parse_item_page()
            except:
                print("未知错误")
                with open("失败url.txt", "a") as f:
                    f.write(href)
                self.chrome()       # 浏览器的卡死 重启

    def parse_item_page(self):
        """
        解析详情页
        """
        time.sleep(3)      # 防止页面渲染不全

        html = etree.HTML(self.driver.page_source)
        id = self.driver.current_url.split("/")[-1].strip(".html")    # url取值,唯一

        title = re.search("\S.*", "".join(html.xpath("//h1[@id='dt_title']/text()"))).group()   # 标题

        try:
            addr = html.xpath("//div[@class='detail_Attr']/a/text()")[0]      # 地址
        except:
            addr = html.xpath("//div[@class='detail_Attr']/span/text()")[0]

        info = re.search("var _info = ({[\s\S]*?})", self.driver.page_source).group(1)    # 带标签的文本

        sponsor = re.search("_publishUserName:\"(.*?)\"", info).group(1)   # 主办方

        secs_time = re.search("_party_dateTime:\"(.*?)\"", info).group(1)     # 发布时间
        time_array = time.localtime(int(secs_time) / 1000)
        p_time = time.strftime("%Y-%m-%d %H:%M", time_array)

        s_time = re.search("_oldStartDate:\"(.*?)\"", info).group(1)     # 开始时间
        if not s_time.startswith("20"):         # 没有年份默认2020
            s_time = "2020-" + s_time

        e_time = re.search("_oldEndDate:\"(.*?)\"", info).group(1)    # 结束时间
        if not e_time.startswith("20"):         # 没有年份默认2020
            e_time = "2020-" + e_time

        user_head_link = re.search("_publishUserHead:\"(.*?)\"", info).group(1) # 主办方头像

        poster_img_link = re.search("_poster_image:\"(.*?)\"", info).group(1)  # 海报

        tickets_list = html.xpath("//div[@class='tc_c_feiLi_box']//ul/li//span[@class='ticket_des']/text()")  # 票种
        if len(tickets_list) == 1:
            tickets = tickets_list[0]
        elif len(tickets_list) > 1:
            tickets = "|".join(tickets_list)
        else:
            tickets = "默认免费票"

        # 拿到内容
        content = re.search("<!--活动详情-->([\s\S]*?)<!-- 分享-->", self.driver.page_source).group(1)
        content = self.content_replace(content)
        # 那出内容里的图片链接
        self.download_img_content(content, id)



        u_name, p_name = self.download_img_user_poster(user_head_link, poster_img_link, id)   #头像,海报图片

        item = Item()
        item.id = id
        item.title = title  # 标题
        item.sponsor = sponsor  # 主办方
        item.addr = addr  # 地址
        item.p_time = p_time  # 发布时间
        item.s_time = s_time  # 开始时间
        item.e_time = e_time  # 结束时间
        item.tickets = tickets  # 票种    | 分割多票种
        item.content = content  # 内容
        item.user_head_img = u_name  # 主办方头像
        item.poster_img = p_name  # 海报

        self.db.save(item)


    #内容图片下载
    def download_img_content(self, content, id):
        content_img_link = re.findall("<img.*?>",content)
        img_list = []
        for img in content_img_link:
            img_link = re.search("https?://.*?\"", img).group().split("?")[0].strip("\"")    #?之后的参数为缩略图地址
            img_list.append(img_link)

        for img_link in img_list:
            print(img_link)
            for i in range(3):
                try:
                    img_content = requests.get(img_link, timeout=30).content
                    img_name = img_link.split("/")[-1]

                    if not os.path.exists("E://活动图片/" + id):
                        os.makedirs("E://活动图片/" + id)

                    with open("E://活动图片/" + id + "/" + img_name, "wb") as f:
                        f.write(img_content)
                    break
                except Exception as e:
                    if i == 2:
                        print("内容图片下载失败:",img_link)
                        print(e)
    #用户头像和海报下载
    def download_img_user_poster(self,user_head_link, poster_img_link,id):
        u_name = user_head_link.split("/")[-1].split("@")[0]
        p_name = poster_img_link.split("/")[-1].split("@")[0]

        if not os.path.exists("E://活动图片/" + id):
            os.makedirs("E://活动图片/" + id)

        for i in range(3):
            try:
                u_content = requests.get(user_head_link, timeout=30).content
                with open("E://活动图片/" + id + "/" + u_name, "wb") as f:
                    f.write(u_content)
                break
            except Exception as e:
                if i == 2:
                    print("头像下载失败:", e)
                    u_name = ""

        for i in range(3):
            try:
                p_content = requests.get(poster_img_link, timeout=30).content
                with open("E://活动图片/" + id + "/" + p_name, "wb") as f:
                    f.write(p_content)
                break
            except Exception as e:
                if i == 2:
                    print("海报下载失败:", e)
                    p_name = ""

        return u_name, p_name

    def content_replace(self,s):
        """
        替换和处理内容 部分标签要替换成换行符 否则格式会发生改变
        :param s: 内容
        :return: 处理后的内容
        """
        r = emoji.demojize(s)
        r = re.sub(u'[\U00010000-\U0010ffff]', "", r)
        r = re.sub("</p>", "\n", r)
        r = re.sub("<br ?/?>", "\n", r)
        r = re.sub("</a>", "\n", r)
        r = re.sub("</div>", "\n", r)
        r = re.sub('&nbsp;', "", r)
        r = re.sub('^\s+', "\n", r)
        r = re.sub('\s+$', "\n", r)

        r = re.sub('</?[a-hj-z].*?>', "", r)      # 匹配除img以外其他字母标签
        r = re.sub('<!--.*?-->', "", r)

        return r


class SaveDB(object):
    def __init__(self):

        self.db = pymysql.connect(host="localhost", user="root", password="123456", db="huodong", port=3306, charset="utf8")
        self.cur = self.db.cursor()

    def save(self, item):

        try:
            # 表情删除
            title = re.sub(u'[\U00010000-\U0010ffff]', "", item.title)
            sponsor = re.sub(u'[\U00010000-\U0010ffff]', "", item.sponsor)

            sql = """insert into huodongba (id,title,sponsor,addr,p_time,s_time,e_time,tickets,content,user_head_img,poster_img) 
                     values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")"""

            self.cur.execute(sql, (item.id, title, sponsor, item.addr, item.p_time, item.s_time, item.e_time, item.tickets, item.content, item.user_head_img, item.poster_img))
            self.db.commit()
        except Exception as e:
            print("存入数据库失败:", e)


class Item(object):
    def __init__(self):
        self.id = ""        # url取值  唯一
        self.title = ""     # 标题
        self.sponsor = ""   # 主办方
        self.addr = ""      # 地址
        self.p_time = ""    # 发布时间
        self.s_time = ""    # 开始时间
        self.e_time = ""    # 结束时间
        self.tickets = ""   # 票种    | 分割多票种
        self.content = ""   # 内容

        self.user_head_img = ""     # 主办方头像
        self.poster_img = ""        # 海报

hdb = Hdb()
hdb.run()
hdb.qc()
hdb.index()