#!/usr/bin/env python3
"""测试各大招聘网站可访问性"""
import urllib.request, ssl, sys, json, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
hdr = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def test(name, url):
    try:
        req = urllib.request.Request(url, headers=hdr)
        r = urllib.request.urlopen(req, context=ctx, timeout=10)
        html = r.read().decode("utf-8", errors="replace")
        links = re.findall(r'href=["\']([^"\']+)["\']', html)
        print(f"[OK] {name}: {len(html)}字, {len(links)}个链接")
        return True, html
    except Exception as e:
        print(f"[NO] {name}: {str(e)[:80]}")
        return False, ""

sites = [
    ("国聘网", "https://www.iguopin.com/"),
    ("人社部-高校毕业生就业", "http://www.mohrss.gov.cn/SYrlzyhshbzb/rdzt/SYgaoxiaobiyeshengjiuye/"),
    ("中国公共招聘", "http://job.mohrss.gov.cn/"),
    ("国务院国资委", "http://www.sasac.gov.cn/"),
    ("国资小新招聘", "https://www.iguopin.com/job?keyword=国企&pageNo=1&pageSize=20"),
]

for name, url in sites:
    test(name, url)
    print()
