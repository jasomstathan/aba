# 🐶 啊吧资讯管家 — 自动化信息采集系统

## 概述

每日自动化采集多源信息，生成行业日报、晚间复盘、招聘简报，输出为 Word 文档。

## 项目结构

```
├── gen_news.py                   # 📰 AI科技早报生成器
├── gen_building.py               # 🏗️ 建筑行业日报生成器
├── gen_evening.py                # 🌙 晚间复盘生成器
├── multisource_collector.py      # 🕷️ 多源资讯采集器 v4（爬虫版）
├── side_hustle_report.py         # 💰 副业变现指南 PDF 生成
│
├── job_scraper.py                # 🔍 招聘采集器 v1
├── job_scraper_v2.py             # 🔍 招聘采集器 v2
├── job_scraper_v3.py             # 🔍 招聘采集器 v3（最新）
├── job_packager.py               # 📦 招聘信息打包 v1
├── job_packager_v2.py            # 📦 招聘信息打包 v2
│
├── create_notes.py               # 📝 Obsidian 笔记创建
├── create_notes2.py              # 📝 Obsidian 笔记创建 v2
│
├── test_*.py                     # 🧪 测试脚本集
├── check_result.py               # ✅ 结果检查
├── debug_extract.py              # 🔧 调试提取
├── make_shortcuts.py             # 🔗 快捷方式创建
│
├── snake_game.py                 # 🐍 贪吃蛇（娱乐）
│
├── 副业变现指南_专业报告.pdf      # 📄 已有输出报告
│
├── IDENTITY.md / USER.md / SOUL.md / TOOLS.md / AGENTS.md
└── README.md                     # ← 你在这
```

## 数据流

```
源网站（OSCHINA/住建部/水利部/智联招聘…）
    │
    ▼
multisource_collector.py / job_scraper_v3.py
    │
    ▼（去重 + 关键词筛选）
    │
gen_news.py / gen_building.py / gen_evening.py
    │
    ▼
D:\===每日资讯===\
    ├── AI科技早报\2026年5月\
    ├── 建筑行业日报\2026年5月\
    ├── 晚间复盘\2026年5月\
    └── _history.json
```

## 技术栈

- **Python 3** — 核心语言
- **python-docx** — Word 文档生成
- **fpdf2** — PDF 生成
- **urllib / re** — 网页爬取 + 解析
- **Obsidian CLI** — 笔记管理
- **Git** — 版本控制

## 输出目标（用户画像）

- 48岁 / 大专 / 工民建
- 一级建造师（建筑）+ 注册监理工程师（建筑 + 水利）
- 求职方向：总监 / 项目经理 / 技术负责人
