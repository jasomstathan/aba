#!/usr/bin/env python3
"""测试网站可访问性"""
import urllib.request, ssl, re, sys

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
hdr = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

sites = [
    ("OSCHINA开源中国", "https://www.oschina.net/news/industry"),
    ("IT之家", "https://www.ithome.com/"),
    ("CSDN资讯", "https://news.csdn.net/"),
    ("新浪科技", "https://tech.sina.com.cn/"),
    ("腾讯科技", "https://tech.qq.com/"),
    ("36氪", "https://36kr.com/"),
    ("虎嗅", "https://www.huxiu.com/"),
    ("雷锋网", "https://www.leiphone.com/category/ai"),
    ("品玩", "https://www.pingwest.com/"),
    ("量子位", "https://www.qbitai.com/"),
    ("机器之心", "https://jiqizhixin.com/"),
    ("澎湃科技", "https://www.thepaper.cn/"),
    ("新华网科技", "http://www.xinhuanet.com/tech/"),
    ("人民网科技", "http://scitech.people.com.cn/"),
    ("中国科技网", "http://www.stdaily.com/"),
    ("Donews", "https://www.donews.com/"),
    ("网易科技", "https://tech.163.com/"),
    ("搜狐科技", "https://it.sohu.com/"),
    ("百度新闻", "https://news.baidu.com/"),
    ("知乎每日", "https://www.zhihu.com/hot"),
    ("国家能源局", "http://www.nea.gov.cn/"),
    ("住建部", "https://www.mohurd.gov.cn/"),
    ("国资委", "http://www.sasac.gov.cn/"),
    ("发改委", "https://www.ndrc.gov.cn/"),
    ("水利部", "http://www.mwr.gov.cn/"),
]

results = []
for name, url in sites:
    try:
        req = urllib.request.Request(url, headers=hdr)
        r = urllib.request.urlopen(req, context=ctx, timeout=8)
        html = r.read().decode("utf-8", "replace")
        titles = re.findall(r"<[^>]*title=[\"']([^\"']+)[\"']", html)
        hrefs = re.findall(r"href=[\"']([^\"']+)[\"']", html)
        t_cnt = len([t for t in titles if len(t.strip()) > 6 and "javascript" not in t])
        sys.stdout.reconfigure(encoding="utf-8")
        print(f"[OK] {name}: {len(html)//1024}KB, {t_cnt}个有效标题")
        results.append((name, url, True))
    except Exception as e:
        print(f"[--] {name}: {str(e)[:50]}")
        results.append((name, url, False))

print(f"\n可用站点：{sum(1 for _,_,ok in results if ok)}/{len(results)}")
