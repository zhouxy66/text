# -*- coding: utf-8 -*-
import re
import json
s = """

                               <div class="photo-icon"></div>
                                <div class="titles">
                                   <div>联系Ta</div>
                                </div>
                           </a></span>
                </div>
                    </div>
    </div>
                        </div>
            <div class="section-sep"></div>
            
                            <div class="event_intro_title section-title has-bottom-border">活动介绍</div>
<div class="event_intro">
    <p style="margin:0;font-size:15px;font-weight:bold;"><span style="color:#000000;">【活动介绍】</span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">百里荒22℃的夏天 妥妥的夏季避暑好去处</span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">亲子民宿 帐篷露营 泥潭捉鱼 泡泡骑行 水枪大战…</span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">你准备好来参与了吗</span></p> <p><span style="color:#000000;"><img class="preview-image" name="imgs" src="https://upload.51bmb.com/ios/7e84741597749610968091.jpg?imageView2/2/w/640/interlace/1" data-src="https://upload.51bmb.com/ios/7e84741597749610968091.jpg?imageView2/2/w/640/interlace/1" data-gid="1" data-index="0"></span></p> <br> <br> <br> <p style="margin:0;font-size:15px;font-weight:bold;"><span style="color:#565a5c;">【活动内容】</span></p> <p><span style="color:#000000;"><img class="preview-image" name="imgs" src="https://upload.51bmb.com/ios/7e84741597749609968092.jpg?imageView2/2/w/640/interlace/1" data-src="https://upload.51bmb.com/ios/7e84741597749609968092.jpg?imageView2/2/w/640/interlace/1" data-gid="1" data-index="1"></span><span style="font-size:15px;color:#565a5c;">泥地捉鱼</span></p> <p><span style="color:#000000;"><img class="preview-image" name="imgs" src="https://upload.51bmb.com/ios/7e84741597760827692633.jpg?imageView2/2/w/640/interlace/1" data-src="https://upload.51bmb.com/ios/7e84741597760827692633.jpg?imageView2/2/w/640/interlace/1" data-gid="1" data-index="2"></span><span style="font-size:15px;color:#565a5c;">水枪泡沫大战</span></p> <p><span style="color:#000000;"><img class="preview-image" name="imgs" src="https://upload.51bmb.com/ios/7e84741597760827692634.jpg?imageView2/2/w/640/interlace/1" data-src="https://upload.51bmb.com/ios/7e84741597760827692634.jpg?imageView2/2/w/640/interlace/1" data-gid="1" data-index="3"></span><span style="font-size:15px;color:#565a5c;">荧光夜骑</span></p> <p><span style="color:#000000;"><img class="preview-image" name="imgs" src="https://upload.51bmb.com/ios/7e84741597760828692635.jpg?imageView2/2/w/640/interlace/1" data-src="https://upload.51bmb.com/ios/7e84741597760828692635.jpg?imageView2/2/w/640/interlace/1" data-gid="1" data-index="4"></span><span style="font-size:15px;color:#565a5c;">帐篷露营</span></p> <br> <br> <br> <br> <p style="margin:0;font-size:15px;font-weight:bold;"><span style="color:#565a5c;">【房型介绍】</span></p> <p><span style="color:#000000;"><img class="preview-image" name="imgs" src="https://upload.51bmb.com/ios/7e84741597749610968093.jpg?imageView2/2/w/640/interlace/1" data-src="https://upload.51bmb.com/ios/7e84741597749610968093.jpg?imageView2/2/w/640/interlace/1" data-gid="1" data-index="5"></span></p> <p><span style="color:#000000;"><img class="preview-image" name="imgs" src="https://upload.51bmb.com/ios/7e84741597749610968094.jpg?imageView2/2/w/640/interlace/1" data-src="https://upload.51bmb.com/ios/7e84741597749610968094.jpg?imageView2/2/w/640/interlace/1" data-gid="1" data-index="6"></span></p> <p><span style="color:#000000;"><img class="preview-image" name="imgs" src="https://upload.51bmb.com/ios/7e84741597800494979116.jpg?imageView2/2/w/640/interlace/1" data-src="https://upload.51bmb.com/ios/7e84741597800494979116.jpg?imageView2/2/w/640/interlace/1" data-gid="1" data-index="7"></span></p> <p><span style="color:#000000;"><img class="preview-image" name="imgs" src="https://upload.51bmb.com/ios/7e84741597800494979117.jpg?imageView2/2/w/640/interlace/1" data-src="https://upload.51bmb.com/ios/7e84741597800494979117.jpg?imageView2/2/w/640/interlace/1" data-gid="1" data-index="8"></span></p> <p><span style="color:#000000;"><img class="preview-image" name="imgs" src="https://upload.51bmb.com/ios/7e84741597800494979118.jpg?imageView2/2/w/640/interlace/1" data-src="https://upload.51bmb.com/ios/7e84741597800494979118.jpg?imageView2/2/w/640/interlace/1" data-gid="1" data-index="9"></span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">标间1.2米床 其他房型均为1.5米床</span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">套房配有麻将桌 每个房间配有浴室厕所 </span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">只有亲子星空房配有空调 其余房间可提供电扇 </span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">放心 晚上超凉快的～</span></p> <br> <br> <p style="margin:0;font-size:15px;font-weight:bold;"><span style="color:#000000;">【活动流程】</span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">29日 15:30自驾抵达民宿办理入住</span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">&nbsp; &nbsp; &nbsp; &nbsp; 16:00集合合影</span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;16:00—16:40泡沫水枪大战</span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">&nbsp; &nbsp; &nbsp; （换装休整时间）</span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;17:00—17:30泥潭捉鱼</span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">&nbsp; &nbsp; &nbsp;（换装休整时间）</span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;18:00晚餐</span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">&nbsp; &nbsp; &nbsp; &nbsp; 19:30—20:30草地荧光夜骑</span></p> <p style="margin:0;font-size:15px;font-weight:bold;"><span style="color:#f03442;">（若天气影响 以上活动也可能调整为30日上午开展 具体活动流程以现场为准）</span></p> <p><span style="color:#000000;"><img class="preview-image" name="imgs" src="https://upload.51bmb.com/ios/7e84741563373958989480.jpg?imageView2/2/w/640/interlace/1" data-src="https://upload.51bmb.com/ios/7e84741563373958989480.jpg?imageView2/2/w/640/interlace/1" data-gid="1" data-index="10"></span><span style="font-size:15px;color:#565a5c;">（百里荒景区内）</span></p> <p><span style="color:#000000;"><img class="preview-image" name="imgs" src="https://upload.51bmb.com/ios/7e84741563373958989481.jpg?imageView2/2/w/640/interlace/1" data-src="https://upload.51bmb.com/ios/7e84741563373958989481.jpg?imageView2/2/w/640/interlace/1" data-gid="1" data-index="11"></span><span style="font-size:15px;color:#565a5c;"> （百里荒景区内）</span></p> <p><span style="color:#000000;"><img class="preview-image" name="imgs" src="https://upload.51bmb.com/ios/7e84741563373958989482.jpg?imageView2/2/w/640/interlace/1" data-src="https://upload.51bmb.com/ios/7e84741563373958989482.jpg?imageView2/2/w/640/interlace/1" data-gid="1" data-index="12"></span><span style="font-size:15px;color:#565a5c;"> （百里荒景区内</span><span style="font-size:12px;color:#000000;">）</span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">30日白天可去百里荒景区自由活动</span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">民宿距离景区仅1KM</span></p> <br> <br> <br> <p><span style="font-size:15px;font-weight:bold;color:#000000;">活动时间</span><span style="font-size:15px;color:#000000;">：8月29日（周六）15:30</span></p> <p><span style="font-size:15px;font-weight:bold;color:#000000;">活动地点</span><span style="font-size:15px;color:#000000;">：夷陵区山与山寻亲子主题民宿</span></p> <p style="margin:0;font-size:15px;font-weight:bold;"><span style="color:#565a5c;">活动人数：</span><span style="color:#f03442;">满10组家庭开展活动 30组封顶</span></p> <p><span style="font-size:15px;font-weight:bold;color:#000000;">活动准备</span><span style="font-size:15px;color:#000000;">：住宿个人用品；长袖衣裤及外套；换洗衣服；水枪；防晒用品；驱蚊用品等</span></p> <p style="margin:0;font-size:15px;font-weight:bold;"><span style="color:#565a5c;">活动费用：</span><span style="color:#f03442;">报名费用默认两大一小 多退少补</span></p> <p style="margin:0;font-size:15px;font-weight:bold;"><span style="color:#f03442;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;非会员报名费另+100元</span></p> <p><span style="font-size:15px;font-weight:bold;color:#565a5c;">费用包含：</span><span style="font-size:15px;color:#565a5c;">住宿费；场地费；晚餐费；早餐费；道具物料费；幼儿保险费；工作人员费等</span></p> <br> <br> <br> <p style="margin:0;font-size:15px;font-weight:bold;"><span style="color:#565a5c;">【注意事项】</span></p> <p style="margin:0;font-size:15px;font-weight:bold;"><span style="color:#f03442;">请您确定好活动时间 报名成功后不可退 可自行转让名额 户外活动具有一定危险性 请家长自行照看好自己孩子</span></p> <p style="margin:0;font-size:15px;font-weight:bold;"><span style="color:#f03442;">自驾途中及活动中发生的所有事故由家长全部承担 </span></p> <p><span style="font-size:15px;font-weight:bold;color:#f03442;">报名本链接及视认可以上所有申明</span><span style="font-size:15px;color:#f03442;">⚠️</span><span style="font-size:15px;font-weight:bold;color:#f03442;"> </span><span style="font-size:15px;color:#f03442;">⚠️</span><span style="font-size:15px;font-weight:bold;color:#f03442;"> </span><span style="font-size:15px;color:#f03442;">⚠️</span></p> <br> <br> <p style="margin:0;font-size:15px;font-weight:bold;"><span style="color:#565a5c;">【关于拍摄及隐私】</span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">活动过程中会有工作人员进行拍摄，孩子们参与活动的照片，都有可能出现在俱乐部公众号和微信中出现，如果家长介意，请提前告知Luna老师，我们一定会配合保护宝宝的隐私。</span></p> <br> <br> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">其它疑问请扫码咨询Luna老师</span></p> <p><span style="color:#000000;"><img class="preview-image" name="imgs" src="https://upload.51bmb.com/ios/7e84741528030681553270.jpg?imageView2/2/w/640/interlace/1" data-src="https://upload.51bmb.com/ios/7e84741528030681553270.jpg?imageView2/2/w/640/interlace/1" data-gid="1" data-index="13"></span></p> <p style="margin:0;font-size:15px;"><span style="color:#565a5c;">❤️KOKUA—让孩子爱上运动❤️</span></p>
</div>
<div class="section-sep"></div>

            
                                                
        
                              
                                                                                                
                    
                <div class="download-banner zoom-out" data-ad-type="banner__detail_page_bottom" data-href="" data-event-id="hztr35db64a">
    <img>
    <div class="logo"></div>
    <div class="btn"></div>
    <div class="close-icon"></div>
</div>
            </div>
</div>
        <div class="detail-footer action-footer">
            
                
    
    <input type="hidden" value="false" id="isVoteEvent"/>
    <input type="hidden" value="" id="voteNum"/>
    <input type="hidden" value="hztr35db64a" id="activityId"/>
    <input type="hidden" value="false" id="countDown"/>
    <input type="hidden" value="5" id="payPath"/>
<div id="chargeLevels" style="display: none;">[{"appNum":2,"charge":268,"countNum":0,"appToPayNum":0,"description":"不订房自带帐篷","id":190805},{"appNum":2,"charge":498,"countNum":2,"appToPayNum":0,"description":"普通标间","id":190797},{"appNum":3,"charge":498,"countNum":3,"appToPayNum":0,"description":"普通单间","id":190798},{"appNum":3,"charge":598,"countNum":3,"appToPayNum":0,"description":"豪华单间","id":190799},{"appNum":8,"charge":598,"countNum":8,"appToPayNum":0,"description":"豪华标间","id":190800},{"appNum":2,"charge":698,"countNum":2,"appToPayNum":0,"description":"豪华套房","id":190801},{"appNum":1,"charge":698,"countNum":1,"appToPayNum":0,"description":"萤火虫主题房","id":190802},{"appNum":6,"charge":698,"countNum":6,"appToPayNum":0,"description":"亲子星空房","id":190803},{"appNum":1,"charge":798,"countNum":1,"appToPayNum":0,"descriptio

"""

r = re.search('活动介绍</div>[\s\S]*?section-sep', s).group()
r = re.sub(u'[\U00010000-\U0010ffff]', "", r)
r = re.sub("<span.*?>", "", r)
r = re.sub("<ul.*?>", "", r)
r = re.sub("<li.*?>", "", r)
r = re.sub("</span>", "", r)
r = re.sub("</ul>", "", r)
r = re.sub("</li>", "", r)
r = re.sub("<p.*?>", "", r)
r = re.sub("</p>", "\n", r)
r = re.sub("<br ?/?>", "\n", r)
r = re.sub("<a.*?>", "", r)
r = re.sub("</a>", "\n", r)
r = re.sub("<div.*?>", "\n", r)
r = re.sub("</div>", "\n", r)
r = re.sub('&nbsp;', "", r)
r = re.sub('<strong.*?>', "", r)
r = re.sub('</strong>', "", r)
r = re.sub('<font.*?>', "", r)
r = re.sub('</font>', "", r)
r = re.sub('</?em>', "", r)
r = re.sub('</section>', "", r)
r = re.sub('</tr>', "", r)
r = re.sub('<tr.*?>', "", r)
r = re.sub('</td>', "", r)
r = re.sub('<td.*?>', "", r)
r = re.sub('</table>', "", r)
r = re.sub('<table.*?>', "", r)
r = re.sub('</tbody>', "", r)
r = re.sub('<tbody.*?>', "", r)
r = re.sub('</?iframe.*?>', "", r)
r = re.sub('<section.*?>', "", r)
r = re.sub('^\s+', "\n", r)
r = re.sub('\s+$', "\n", r)

r = re.sub('</?[a-hj-z].*?>', "", r)      #匹配除img以外其他字母标签  上面的不影响所以不修改
r = re.sub('<!--.*?-->', "", r)
r = re.sub("\n\s*?\n+", "\n", r)

print(r)
