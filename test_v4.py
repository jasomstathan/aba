# -*- coding: utf-8 -*-
"""Test job_scraper_v4 functions"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from job_scraper_v4 import *

print("=== Match test ===")
tests = [
    ("某国企招聘总监理工程师", True),
    ("南昌市建设投资集团2026年社会招聘公告", True),
    ("江西省水利投资集团招聘公告", True),
    ("南昌轨道交通集团运营分公司招聘", True),
    ("今日菜价行情", False),
    ("天气预报", False),
]
for title, expected in tests:
    r = is_eligible(title)
    ok = r == expected
    print("  %s '%s' -> %s" % ("OK" if ok else "FAIL", title[:40], r))

print("\n=== Edge cases ===")
for title in ["关于2026年度公开招聘工作人员的通知",
              "中建某局社会招聘",
              "聚才江西招聘求职发布公告"]:
    print("  %s -> rec:%s match:%s eligible:%s" % (title[:40],
        is_recruitment(title), is_matching(title), is_eligible(title)))

print("\n=== WeChat search test ===")
arts = search_wechat_articles("南昌国企招聘", 1)
print("  Found %d articles" % len(arts))
for a in arts[:5]:
    el = is_eligible(a["title"])
    print("  [%s] %s | %s" % ("*" if el else " ", a["title"][:50], a["source"]))

print("\n=== Gov site test ===")
for name, url in LOCAL_GOV_SITES[:3]:
    if not url: continue
    jobs = scrape_government_site(name, url)
    print("  [%s] %d links, %d eligible" % (name, len(jobs),
          len([j for j in jobs if is_eligible(j["title"])])))

print("\n=== Output dir test ===")
print("  BASE_DIR: %s" % BASE_DIR)
print("  Output: %s" % make_output_dir())

print("\nDone")
