#!/usr/bin/env python3
"""测试江西/南昌招聘网站可访问性"""
import urllib.request, ssl, re, sys

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
hdr = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

sites = [
    ("南昌人才招聘网", "https://www.ncrczpw.com/"),
    ("江西人才人事网", "https://www.jxrcw.com/"),
    ("南昌人才网", "https://www.ncrcw.com.cn/"),
    ("江西人才网", "https://www.jxrc.com/"),
    ("江西人力资源网", "http://www.jxzp.cc/"),
    ("南昌市人社局", "http://rsj.nc.gov.cn/"),
    ("江西省人社厅", "http://rst.jiangxi.gov.cn/"),
    ("江西省国资委", "http://gzw.jiangxi.gov.cn/"),
    ("南昌市国资委", "http://gzw.nc.gov.cn/"),
    ("江西省住建厅", "http://zjt.jiangxi.gov.cn/"),
    ("南昌市建设局", "http://jsj.nc.gov.cn/"),
    ("南昌市交通局", "http://jtj.nc.gov.cn/"),
    ("南昌市水利局", "http://slj.nc.gov.cn/"),
    ("南昌市公共资源交易网", "https://www.ncggzy.com/"),
    ("南昌市政公用集团", "http://www.ncsz.com.cn/"),
    ("南昌市建设投资集团", "http://www.ncjt.com.cn/"),
    ("南昌轨道交通集团", "http://www.ncmtr.com/"),
    ("南昌水利投资集团", "http://www.ncst.cn/"),
    ("江西省公共资源交易网", "https://ggzy.jiangxi.gov.cn/"),
    ("江西人才服务网", "https://www.jxrcfw.com/"),
    ("南昌县人社局", "http://rsj.ncx.gov.cn/"),
    ("进贤县人社局", "http://rsj.jinxian.gov.cn/"),
    ("南昌招聘网", "http://www.517nc.com/"),
    ("江西中公教育-国企招聘", "https://jx.offcn.com/zggqzp/"),
]

for name, url in sites:
    try:
        req = urllib.request.Request(url, headers=hdr)
        r = urllib.request.urlopen(req, context=ctx, timeout=8)
        html = r.read()
        titles = re.findall(rb'<[^>]*title=[\x22]([^\x22]+)[\x22]', html)
        links = re.findall(rb'href=[\x22]([^\x22]+)[\x22]', html)
        t_cnt = len([t for t in titles if len(t) > 10])
        l_cnt = len([l for l in links if l.startswith(b"http")])
        print(f"[OK] {name}: {len(html)//1024}KB, {t_cnt}标题, {l_cnt}链接")
    except Exception as e:
        print(f"[--] {name}: {str(e)[:40]}")

print("\n提示：江西招聘信息也汇聚在智联招聘、前程无忧等全国平台")
