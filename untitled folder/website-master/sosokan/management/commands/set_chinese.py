# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from sosokan.models import Ad, AdImage, Category, User
import datetime
from unidecode import unidecode
import time
from django.conf import settings
from urlparse import urlparse
import urllib
from geoposition import Geoposition
from decimal import Decimal
from django.contrib.gis.geos import GEOSGeometry

characters=u"一丁七万三上下不与丑专且世丘业丛东丞两严並丨个中丰临丶丸丹为主丽举乃久么义之乌乍乎乏乐乔九也习乡书买乳乾了予争事二于云互五亚些亞交亥亦产亨享京亭亮亲人亿什仁仅今介仍从仑仓仔仕他付仙仟代令以仪们件价任仼份企伊伍伏休众优伙会伟传伤伦伯估伴似但位低住佐佑体何余佛作你佣佩佳併使侃來侈例供依侠侣侨便係促俄俊俐保俞信俢修俱倉個們倒候借倩倪倶债值假偉做停健偿傅備傢储催傳傷像僑價儒優儲儿允元兄充兆先光克免兒兔入內全兩八公六兰共关兴兵其具典养兼内冈冊册再冒写军冠冬冯冰冲决况冷冻净准凌凍减几凡凤凭凯凰凱凶出击刀分切刑划列刘则刚创初判別利别刮到制刷券刺刻剂削剋前剑剧剩剪副割劃劉劍力办功加务动助努励劲劳势勇勋勒動務勝勞募勢勤勾勿包化北匙匠匹区医區十千卅升午卉半华协卑卓協单卖南博占卡卢卧卫卯印即卵卷卿厂厅历压厘厚原厦厨去参參又叉及友双反发取受变叛口古另只叫召可台史右叶号司叹吃各合吉同名后向吕君否吧含听启吳吴吸吾吿呂告呎员周味呵呼命和咏咖咙咨咬咭咳咽品哈員哥哪哮哲唐售唯唱商問啡善喆喉喘喜喬單営喷嘉嘱器噴嚏嚤嚴囊四回因团园困围固国图圃圆國圍園圖團土圣在地场圾址均坊坐块坚坦坪垂垃型垫埃埋城埔域埠執培基堂堡報場塑塗塘塞填境墅墙增墟墨壁壇壓士壮声壶壹壽处夆备复夏夕外多夜够夠大天太夫央失头夸夹夾奇奈奋契奕奖套奠奢奥奧女奶她好如妆妇妈妙妥妮妳妹妻姆始姐委姚姜姨姻威娇娘娛娜娟娩娱娴婉婚婦婴婵婷媒媛媽嫂嫒子孔孕字存孙孝孟季学孩學宁它宅宇守安宋完宏宗官定宜宝实宠审客宣室宫宮害家容宽宾宿寅密富寐寓寝察實寧寨審寬寰寵寶寸对寺寻导寿専射将將專尉尊對導小少尔尖尙尚尝尤就尹尺尼尽尾尿局层居屋屏展属層履屬山岁岐岑岗岚岛岩岱岳岸峰島崇崔崙崧嵌嵛巍川州巡巢工左巧差己已巳巴巾币市布师希帐帘帝带師席帮帳帶常幅幕幣幫干平年并幼幽幾广庄庆庇床序库应底店庙府度座庫庭康廁廈廉廊廋廖廚廟廠廢廣廳延廷建廿开异式引弗弘弟张弯弱張強弹强彈归当录形彤彦彩彪彬彭影役彻往征径待很律後徐徒得從御微徴徵德心必忆志忘忙忠忧快忱念态怎怕思怡急性总恆恋恐恒恩恭息恳恶恺恼悄悅悉悠患悦您悬悸情惜惟惠惧惯想愈意愛感愿慈慎慕慢慧慼憶懂應懿戏成我戒或战戚截戲戴戶户房所扁手才扎打托扣执扩扫扬扭扰扶批找承技把抑抓投抗折抟护报抨披抵抹抽担拆拉拍拎拒拓拔拖招拜拥拨择括拳拼拿持挂指按挑挖挥振捆捐损换据捷掂掃授掌排掘探接控推描提插換握揭揽搔搜搬搭携摄摇摩摺撒撤播擀擅擇操擦擬擴擾攜攣支收改攻放政故效敎敏救敗敘教敞敢散敬数整數文斌斑斗料斜断斯新斷方於施旁旅旋族旗无既日旦旧旨早旭时旷旺昀昂昌明易星映春是显時晋晓晕晖晚晨普景晰晶智暑暖暨暴曬曰曲更書曹曼曾替最會月有朋服朗望朝期木未末本术朱机杂权杆杉李杏材村杜束条来杨杯杰東松板极构析枕林果枝枫架柏某染柔柜查柬柯柱柳査标栋树校栩样核根格桂桃框案桌桑档桥桶梁梅條梦梨梭梯械检棉棍棘棟棠森椅植椎椰楊楝楠業極楼概榕榨榮構槽槿樂樊樑樓模樣横樱樹橋機橡橱檔檢檯櫃櫥欄欠次欢欣欧欺款歇歌歡止正此步武歲歷殊残殖殴段殷毅母每毒比毕毛毯氏民气氣水永汁求汇汉汗江池汤汽沃沈沐沒沖沙沛沟没沧沪沫河油治沿況泄泉泊泌法泛泡波泥注泰泳泼泽洁洋洗洛津洪洲活洽派流测济浓浙浩浬浴海涅消涉涕涛润涨涯液涵涼淋淑淘淦淨深淳混淸添淼清渊減渠渣渥温港游湖湘湛湾湿溃源準溝溥溪溽滑滔滚满滢滤滨滩滲滿漂漆漏演漢漫漸潔潘潜潢潮澄澡澤澳激瀑瀚瀝灌灏灣火灯灰灸灿炊炎炒炮炯炸点為烁烂烈烘烟烦烧热烹焊焕無焦然煌煙煜煤照煮煲熇熊熙熟熱燈燎燒燕燙營爆爐爱爲父爷爽牆片版牌牙牛牟牡物牵特犯状犹狀狂狄狗独狱猛猪献猴獎獨獲玄率玉王玛玥玮环现玲玺玻珊珍珠班現球理琛琢琪琳琴瑛瑜瑞瑶璃璇璐璜環瓣瓦瓷甚甜生產用甩田由甲申电男画界畏留畢略畫畯當畸疆疏疑疗疡疤疫疮疹疼疾病症痒痔痕痘痛痣痧痫痰痹痿瘤瘾療癌癣癫登發白百的皆皇皓皮盆盈益盎监盒盖盗盘盛盟盡監目直相盼省看眞真眠眩眼眾着睛睡督睫知矫短石矶码砂砌砍研砖砰破础硅硕硬确碌碍碎碑碗碧碼磁磊磚磨示礼社祖祝神祥票祸祺禁福禮禹禺离秀私秉秋种科秒秘租秦积称移稅程税稞種稱稳穆積穗穩究穷空突窃窗窦立站竞章童竭端竹笑笔符第笼筆等筋筑答策筠筲筹签简算管箱範築篷簡簷簾簿籍籠籲类粉粗粤粮粵精糕糖糜糧系紀約紅紋納紐紗紙級素索紧累細紳組経結絕絡給統經維網線緣緬縫總繁織繪繫續纠红纤约级纪纯纲纳纵纷纸纺纽线练组细织终绍经绑结绘给络绝绞统继绩绪续绮维综绿缅编缘缚缝缪缺罐网罗罚罪置罰署羅羊美群翁習翔翠翰翻耀老考者耆而耐耳耶耿聊职联聖聘聚聛聞聪聯聲職肉肌肖肝肠股肢肤肥肩肯育肺肾肿胃胆背胎胚胜胞胡胰胱胶胸能脂脉脊脏脑脚脱脸腊腋腐腔腦腰腳腹腺腻腾腿膀膜膠臘臣臥臨自臭至致與舊舍舒舖舘舞舟航般舱艇良艰色艳艺艾节芙芝芦芬花芳芸苏苑苗若苦英苹范茅茜茨茲茵茶茹草荐荟荡荣药荷莉莊莎莫莱莲获莹菌菜華菲萄萊萍营萧萨萬落葉著葛葡董蒂蒋蒙蒸蓄蓝蔚蔡蔽薄薛薪藍藏藝藤藥蘇蘋蘭虎虐虑虔處虚號虹蛇蛋蜡融蠱血行術街衛衝衡衣补表衰衷袁被袭裁装裏裒裔裕裘補裝裤裴複褓褥西要覃規視親觀见观规视览觉角解言訂計訊訓記訪設許診註詢試話詳誉誚語誠說誰課調談請諧謂講證識警議護譽變讓计订认讨让训议讯记讲许论讼设访证评识诈诉诊词译试诚话诞询该详语误说请诸诺读诽课调谈谋谐谓谘谢谤谦谨谭谷豁豆豐象豪豫豬貌貝負財貨責貴買費貼貿資賓賞賣賨質賭賺購賽贝负贡财责贤账货质贫购贴贵贷贸费贺贽贾赁资赉赌赐赔赖赚赛赠赢赤赫走赴赵赶起超越趣足趴跃跆跌跖距跟跡跨路跳践跷跻踝蹈躁躍身車較輔輕輛輝輪輯轉车轩转轮软轶轻载较辅辆辉辐辑输辛辣辦辩辰边达迁迅过迈迎运近返还这进远违连迪迫述迷追退送适逆选逊透逐递途這通速造逢連週進逸逾遇遊運遍過道達違遗遞適遭選避邀還邊邓邝那邦邪邮邱邵邹邻郁郊郎郑郡部郭郵都鄧鄭鄰酉配酒酬酱酸醇醉醒醫采释里重量金針鉛鉴銀銷鋁鋪鋼錢錯鍋鎖鎭鏟鐘鐵鑫针钜钟钢钥钮钰钱钻铁铜铧铭银铺链销锁锂锅锈锊锋锐错锡锦键镇镜镭長长門開間闆關门闩闪闭问闯间闷闹闻闽阁阅队防阳阴阵阻阿附际陆陈降限院除险陪陳陶陸陽隆隊階随隐隔際障隨險隳隽难雁雄雅集雇雕雙雜雞離雨雪雯雲零雷電需震霍霞露靑青靓靖静靚靜非靠面鞋鞭韓韩音響頂項順須預頓頭頸頻題類顧页顶项顺须顽顾顿预领颈频颖颗题颜额颤风飛飞食飪飮飯飱餃餅養餐餡館饭饮饰饺饼馀馆首香馨馬駕駛験騙驗驛马驱驶驻驾验骑骥骨髓體高髙髮魅魏魚魯鮮鯉鱼鱿鲁鲍鲜鴻鸞鸡鸣鸭鸿鹏鹤鹰麒麗麟麦麵麻麼黃黄黎黏黑點鼎鼠鼻鼾齊齐齒齡齿龄龍龙龟"

FIREBASE_URL="https://firebasestorage.googleapis.com/v0/b/sosokan-1452b.appspot.com/o/images%2F"
class Command(BaseCommand):
    help = 'Resets Ads from Firebase'

    def handle(self, *args, **options):
        for ad in Ad.objects.all():
            for character in characters:
                #print character
                if character in ad.name or character in ad.description:
                    print "it's chinese!"
        