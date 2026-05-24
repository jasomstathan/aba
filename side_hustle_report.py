#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成副业清单专业报告 PDF"""

from fpdf import FPDF
import os

FONT_DIR = os.path.join(os.environ['WINDIR'], 'Fonts')
YAHEI = os.path.join(FONT_DIR, 'msyh.ttc')
YAHEI_BOLD = os.path.join(FONT_DIR, 'msyhbd.ttc')
SIMHEI = os.path.join(FONT_DIR, 'simhei.ttf')
SIMFANG = os.path.join(FONT_DIR, 'simfang.ttf')

class ReportPDF(FPDF):
    def __init__(self):
        super().__init__('P', 'mm', 'A4')
        # Register Chinese fonts
        self.add_font('YH', '', YAHEI, uni=True)
        self.add_font('YH', 'B', YAHEI_BOLD, uni=True)
        self.add_font('FH', '', SIMFANG, uni=True)
        self.add_font('SH', '', SIMHEI, uni=True)

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font('YH', '', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 6, 'AI 副业变现指南 - 专业报告', align='L')
        self.cell(0, 6, f'第 {self.page_no()} 页', align='R', new_x='LMARGIN', new_y='NEXT')
        self.set_draw_color(200, 200, 200)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font('YH', '', 7)
        self.set_text_color(180, 180, 180)
        self.cell(0, 10, '本报告由 AI 生成，仅供参考。实际收益因个人能力和市场变化而异。', align='C')

    def cover_page(self):
        self.add_page()
        self.set_x(self.l_margin)
        self.ln(50)
        self.set_font('SH', '', 30)
        self.set_text_color(30, 60, 120)
        self.cell(self.epw, 15, 'AI 副业变现指南', align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(5)
        self.set_font('YH', '', 16)
        self.set_text_color(80, 80, 80)
        self.cell(self.epw, 10, '好操作 · 易变现 · 适合普通人', align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(15)
        self.set_draw_color(30, 60, 120)
        self.set_line_width(0.5)
        self.line(60, self.get_y(), 150, self.get_y())
        self.ln(15)
        self.set_font('YH', '', 12)
        self.set_text_color(100, 100, 100)
        items = [
            '📋 10 大热门副业方向',
            '💰 收入潜力 & 启动成本分析',
            '🛠️ 实操工具 & 变现路径',
            '⚡ 零基础入门攻略',
        ]
        for it in items:
            self.cell(self.epw, 10, f'  {it}', align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(25)
        self.set_font('YH', '', 9)
        self.set_text_color(140, 140, 140)
        self.cell(self.epw, 8, '生成日期：2026 年 5 月', align='C', new_x='LMARGIN', new_y='NEXT')
        self.cell(self.epw, 8, '由 OpenClaw AI 助手生成', align='C', new_x='LMARGIN', new_y='NEXT')

    def section_title(self, num, title):
        self.set_font('SH', '', 18)
        self.set_text_color(30, 60, 120)
        self.ln(6)
        self.cell(0, 12, f'{num}. {title}', new_x='LMARGIN', new_y='NEXT')
        self.set_draw_color(30, 60, 120)
        self.set_line_width(0.4)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def sub_title(self, title):
        self.set_x(self.l_margin)
        self.set_font('SH', '', 13)
        self.set_text_color(50, 50, 50)
        self.ln(3)
        self.cell(0, 8, title, new_x='LMARGIN', new_y='NEXT')
        self.ln(1)

    def body_text(self, text):
        self.set_x(self.l_margin)
        self.set_font('YH', '', 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(self.epw, 6, text)
        self.ln(2)

    def bullet(self, text, indent=15):
        self.set_x(indent)
        self.set_font('YH', '', 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(self.epw - indent + self.l_margin, 6, f'• {text}')

    def highlight_box(self, title, content):
        self.set_x(self.l_margin)
        self.set_fill_color(240, 245, 255)
        self.set_draw_color(30, 60, 120)
        y_start = self.get_y()
        self.set_font('YH', '', 9)
        lines = self.multi_cell(self.epw - 8, 5, content, dry_run=True, output="LINES")
        h = 12 + len(lines) * 5 + 4
        # Check page break
        if y_start + h > 270:
            self.add_page()
            y_start = self.get_y()
        self.rect(10, y_start, 190, h)
        self.set_xy(14, y_start + 2)
        self.set_font('YH', '', 9)
        self.set_text_color(50, 50, 50)
        self.multi_cell(self.epw - 8, 5, content)

    def table_header(self):
        self.set_font('YH', 'B', 9)
        self.set_fill_color(30, 60, 120)
        self.set_text_color(255, 255, 255)
        col_w = [8, 50, 28, 28, 28, 48]
        headers = ['#', '副业方向', '启动成本', '月收入潜力', '上手难度', '核心能力']
        for i, h in enumerate(headers):
            self.cell(col_w[i], 7, h, border=1, align='C', fill=True)
        self.ln()

    def table_row(self, cols):
        col_w = [8, 50, 28, 28, 28, 48]
        self.set_font('YH', '', 8.5)
        self.set_text_color(50, 50, 50)
        if self.get_y() > 260:
            self.add_page()
            self.table_header()
        h = 7
        x_start = self.l_margin
        y_start = self.get_y()
        for i, c in enumerate(cols):
            x = x_start + sum(col_w[:i])
            self.set_xy(x, y_start)
            self.cell(col_w[i], h, c, border=1, align='C')
        self.set_xy(x_start, y_start + h)


def build_report():
    pdf = ReportPDF()

    # ========== COVER ==========
    pdf.cover_page()

    # ========== TOC ==========
    pdf.add_page()
    pdf.set_font('SH', '', 20)
    pdf.set_text_color(30, 60, 120)
    pdf.cell(0, 12, '目  录', align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(8)
    toc = [
        ('一', '前言：副业时代的到来'),
        ('二', '副业速览一览表'),
        ('三', '十大副业详细拆解'),
        ('四', '副业选择决策矩阵'),
        ('五', '副业避坑指南'),
        ('六', '实战启动三步骤'),
        ('七', '结语 & 行动建议'),
    ]
    pdf.set_font('YH', '', 11)
    pdf.set_text_color(60, 60, 60)
    for num, title in toc:
        pdf.cell(0, 9, f'  {num}、{title}', new_x='LMARGIN', new_y='NEXT')

    # ========== SECTION 1 ==========
    pdf.add_page()
    pdf.section_title('一', '前言：副业时代的到来')
    pdf.body_text(
        '在 2026 年的今天，"副业刚需"已经成为越来越多人的共识。'
        '互联网基础设施的完善、AI 工具的普及、以及灵活用工模式的兴起，'
        '让普通人拥有一份甚至多份副业变得前所未有地容易。'
    )
    pdf.body_text(
        '本报告精选了 10 个"好操作、易变现"的副业方向，'
        '每个方向都经过以下维度评估：'
    )
    pdf.bullet('启动成本：需要投入多少资金')
    pdf.bullet('上手难度：零基础需要多久学会')
    pdf.bullet('收入潜力：稳定后的月收入范围')
    pdf.bullet('变现路径：如何把技能/时间变成钱')
    pdf.bullet('风险等级：有哪些坑需要避开')
    pdf.ln(4)
    pdf.body_text(
        '无论你是学生、上班族、还是全职宝妈，总有一款适合你。'
        '记住：最好的副业是"你已经会的东西 × 市场需求"。'
    )

    # ========== SECTION 2 ==========
    pdf.add_page()
    pdf.section_title('二', '副业速览一览表')
    pdf.ln(3)
    pdf.table_header()

    rows = [
        ('1', 'AI 内容创作',          '￥0',   '2K-20K',  '⭐⭐',  '写作能力 + AI 工具'),
        ('2', '短视频剪辑 / 切片',     '￥0-500', '3K-30K', '⭐⭐⭐', '剪辑软件基础'),
        ('3', '自媒体写作 & 公众号',   '￥0',   '1K-15K',  '⭐⭐',  '文字表达能力'),
        ('4', 'AI 绘画 & 设计接单',   '￥0-200', '2K-15K', '⭐⭐⭐', '审美 + AI 工具'),
        ('5', '知识付费 / 小报童',    '￥0',   '2K-50K',  '⭐⭐',  '专业领域经验'),
        ('6', '闲鱼 / 跨境电商',      '￥0-1000','2K-20K', '⭐⭐⭐', '选品眼光 + 运营'),
        ('7', '线上家教 / 技能培训',  '￥0',   '2K-12K',  '⭐⭐',  '专业知识 + 表达'),
        ('8', '小程序 / 工具站变现',  '￥200-2K','1K-50K', '⭐⭐⭐⭐','基础编程能力'),
        ('9', '问卷调查 & 微任务',    '￥0',   '500-3K',  '⭐',   '耐心 + 时间'),
        ('10', 'AI 数字人直播带货',   '￥500-3K','5K-50K','⭐⭐⭐', '口才 + 选品能力'),
    ]
    for r in rows:
        pdf.table_row(r)
        pdf.ln()

    # ========== SECTION 3 ==========
    # --- 1. AI 内容创作 ---
    pdf.add_page()
    pdf.section_title('三', '十大副业详细拆解')
    pdf.ln(2)

    pdf.sub_title('副业 1：AI 内容创作（公众号 / 头条号 / 知乎）')
    pdf.highlight_box('', '💰 收入潜力：2,000 - 20,000 元/月\n'
                     '⏱ 上手时间：1-2 周\n'
                     '🛠 必备工具：ChatGPT / DeepSeek + 微信公众号 / 头条号 / 知乎\n'
                     '📌 难度等级：⭐⭐（简单）')

    pdf.body_text('【方法】')
    pdf.body_text(
        '利用 AI 辅助写作，在各大内容平台发布文章赚取流量收益和广告分成。'
        '你不需要成为写作专家，AI 可以帮你完成选题、大纲、初稿和润色。'
    )
    pdf.bullet('注册微信公众号、头条号、百家号等平台')
    pdf.bullet('用 AI 生成文章框架，人工补充案例和观点')
    pdf.bullet('坚持日更，积累粉丝后开通流量主 / 广告分成')
    pdf.bullet('粉丝过万后可接品牌广告，单条报价 500-5000 元')
    pdf.body_text('【变现方式】流量主广告分成 + 平台补贴 + 品牌软文 + 付费专栏')
    pdf.body_text('【关键心得】AI 是放大器，但"选题 + 个人观点"才是核心竞争力。选一个垂直领域深耕，比什么都写强10倍。')

    # --- 2 ---
    pdf.add_page()
    pdf.sub_title('副业 2：短视频剪辑 & 切片')
    pdf.highlight_box('', '💰 收入潜力：3,000 - 30,000 元/月\n'
                     '⏱ 上手时间：1-3 周\n'
                     '🛠 必备工具：剪映 / CapCut + 抖音 / 快手 / 视频号\n'
                     '📌 难度等级：⭐⭐⭐（中等）')

    pdf.body_text('【方法】')
    pdf.body_text(
        '通过剪辑热门直播/综艺/影视内容做成切片视频，或者帮商家制作推广短视频。'
        '剪映已经内置了大量 AI 功能，自动字幕、智能抠图、一键成片。'
    )
    pdf.bullet('做直播切片：二创头部主播精彩片段，挂小黄车赚佣金')
    pdf.bullet('接剪辑单：在猪八戒/淘宝/闲鱼接单，50-500 元/条')
    pdf.bullet('做知识类短视频：用 AI 生成脚本+数字人播报')
    pdf.bullet('做带货视频：拍摄产品测评，挂小黄车赚分佣 10%-50%')
    pdf.body_text('【变现方式】直播带货佣金 + 接单剪辑 + 平台创作激励 + 广告植入')

    # --- 3 ---
    pdf.sub_title('副业 3：自媒体写作（深度长文/IP 打造）')
    pdf.highlight_box('', '💰 收入潜力：1,000 - 15,000 元/月\n'
                     '⏱ 上手时间：1-2 周\n'
                     '🛠 必备工具：微信公众号 + 知识星球 / 小报童\n'
                     '📌 难度等级：⭐⭐（简单）')

    pdf.body_text('【方法】')
    pdf.body_text(
        '写你擅长或感兴趣的领域——职场、理财、育儿、健身、科技、读书笔记……'
        '用 AI 辅助找选题和润色，保持每周 2-3 篇的节奏。'
    )
    pdf.bullet('公众号：开通流量主（500粉即可），靠阅读量吃饭')
    pdf.bullet('小报童：写付费专栏，定价 9.9-99 元，全部归你')
    pdf.bullet('知识星球：做付费社群，年费 99-999 元')
    pdf.bullet('约稿：写熟了会有编辑找你约稿，千字 200-2000 元')
    pdf.body_text('【变现方式】流量主 + 付费专栏 + 社群 + 约稿 + 广告')

    # --- 4 ---
    pdf.add_page()
    pdf.sub_title('副业 4：AI 绘画 & 设计接单')
    pdf.highlight_box('', '💰 收入潜力：2,000 - 15,000 元/月\n'
                     '⏱ 上手时间：2-4 周\n'
                     '🛠 必备工具：Midjourney / DALL·E / Stable Diffusion + 小红书 / 闲鱼\n'
                     '📌 难度等级：⭐⭐⭐（中等）')

    pdf.body_text('【方法】')
    pdf.body_text(
        '用 AI 生成插画、头像、LOGO、海报、壁纸等，在社交平台展示作品接单。'
        '不需要你会手绘，关键是用好 prompt。'
    )
    pdf.bullet('小红书 + 闲鱼接单：定制头像 30-200 元/张')
    pdf.bullet('LOGO 设计：200-2000 元/个（用 AI 生成多稿供客户选择）')
    pdf.bullet('壁纸/素材售卖：上传到图库平台（摄图网、千图网等）赚分成')
    pdf.bullet('AI 写真/婚纱照：小红书引流，200-500 元/套')
    pdf.body_text('【变现方式】接单设计 + 素材售卖 + 课程教学')
    pdf.body_text('【关键心得】审美比技术重要。多看优秀作品，提升 prompt 编写能力。小红书是 AI 绘画变现的最佳起盘平台。')

    # --- 5 ---
    pdf.sub_title('副业 5：知识付费 & 小报童专栏')
    pdf.highlight_box('', '💰 收入潜力：2,000 - 50,000 元/月\n'
                     '⏱ 上手时间：1-2 周\n'
                     '🛠 必备工具：小报童 / 知识星球 / 腾讯课堂\n'
                     '📌 难度等级：⭐⭐（简单）')

    pdf.body_text('【方法】')
    pdf.body_text(
        '把你会的技能打包成付费内容。不需要是行业大牛，'
        '只要你在某个领域比新手懂得多，就能卖。'
    )
    pdf.bullet('小报童写付费专栏：写 10-20 篇系统性内容，定价 9.9-49.9 元')
    pdf.bullet('知识星球做社群：每日分享干货+答疑，年费 99-999 元')
    pdf.bullet('在腾讯课堂/网易云课堂做付费课程：录制视频课程，定价 99-999 元')
    pdf.bullet('做一对一咨询：职场规划/副业指导/技能教学，100-500 元/小时')
    pdf.body_text('【变现方式】专栏订阅 + 社群年费 + 课程销售 + 咨询服务')

    # --- 6 ---
    pdf.add_page()
    pdf.sub_title('副业 6：闲鱼无货源 & 跨境电商')
    pdf.highlight_box('', '💰 收入潜力：2,000 - 20,000 元/月\n'
                     '⏱ 上手时间：2-4 周\n'
                     '🛠 必备工具：闲鱼 + 拼多多/1688 + AI 写文案\n'
                     '📌 难度等级：⭐⭐⭐（中等）')

    pdf.body_text('【方法】')
    pdf.body_text(
        '从 1688/拼多多找低价货源，加价挂到闲鱼/Temu/TikTok Shop 卖。'
        '不用囤货，买家下单后你再去上家下单发货（一件代发）。'
    )
    pdf.bullet('闲鱼：适合卖二手感商品、小众好物，0 保证金')
    pdf.bullet('Temu / TikTok Shop：面向海外市场，利润空间更大')
    pdf.bullet('选品策略：找高需求低竞争的蓝海品类，用 AI 分析热词')
    pdf.bullet('用 AI 写商品标题和详情，批量上架')
    pdf.body_text('【变现方式】商品差价 + 平台补贴 + 佣金')
    pdf.body_text('【关键心得】选品定生死。不要卖大路货，找有"信息差"的商品。闲鱼最火的是二手书、数码配件、手工制品。')

    # --- 7 ---
    pdf.sub_title('副业 7：线上家教 & 技能培训')
    pdf.highlight_box('', '💰 收入潜力：2,000 - 12,000 元/月\n'
                     '⏱ 上手时间：随时开始\n'
                     '🛠 必备工具：腾讯会议 / Zoom + PPT\n'
                     '📌 难度等级：⭐⭐（简单）')

    pdf.body_text('【方法】')
    pdf.body_text(
        '把你擅长的技能（英语/编程/乐器/健身/绘画/办公软件等）变成线上课程或一对一辅导。'
    )
    pdf.bullet('作业帮 / 学而思等平台接单：小学到高中各科辅导')
    pdf.bullet('教成年人：Excel/PPT/PS/AI 工具入门')
    pdf.bullet('教兴趣类：吉他/摄影/美妆/健身/瑜伽')
    pdf.bullet('利用 AI 辅助备课，效率翻倍')
    pdf.body_text('【变现方式】课时费（50-300 元/小时）+ 小班课 + 录播课重复售卖')

    # --- 8 ---
    pdf.add_page()
    pdf.sub_title('副业 8：小程序 / AI 工具站变现')
    pdf.highlight_box('', '💰 收入潜力：1,000 - 50,000+ 元/月\n'
                     '⏱ 上手时间：2-8 周（需基础编程）\n'
                     '🛠 必备工具：Cursor/Copilot + Vercel + 微信开放平台\n'
                     '📌 难度等级：⭐⭐⭐⭐（较难，但有 AI 编程助手段）')

    pdf.body_text('【方法】')
    pdf.body_text(
        '利用 AI 编程助手（Cursor、Copilot、Claude）快速开发小程序或在线工具，'
        '通过广告/会员/付费使用来变现。'
    )
    pdf.bullet('微信小程序：做实用工具类（计算器/生成器/打卡/问卷）')
    pdf.bullet('AI 写真/换脸/头像生成网站：调用 API 做套壳产品')
    pdf.bullet('Chrome 插件：解决某个小痛点，挂到商店卖')
    pdf.bullet('导航站/资源站：搜集整理特定资源，靠流量变现')
    pdf.body_text('【变现方式】广告收入 + 会员订阅 + 单次付费 + 卖插件')
    pdf.body_text('【关键心得】不需要写多复杂的代码。用 AI 编程，一个周末就能做出 MVP。关键是"解决一个小而痛的刚需"。')

    # --- 9 ---
    pdf.sub_title('副业 9：问卷调查 & 微任务平台')
    pdf.highlight_box('', '💰 收入潜力：500 - 3,000 元/月\n'
                     '⏱ 上手时间：立即开始\n'
                     '🛠 必备工具：手机 + 多个平台账号\n'
                     '📌 难度等级：⭐（极简单）')

    pdf.body_text('【方法】')
    pdf.body_text(
        '在各大问卷调查平台和微任务平台完成小任务赚取报酬。'
        '虽然单价不高，但胜在零门槛、随时可做。'
    )
    pdf.bullet('问卷平台：问卷星、腾讯问卷、调研吧，一份 2-20 元')
    pdf.bullet('微任务：阿里众包、百度众测、京东微工')
    pdf.bullet('语音标注/AI 数据标注：需要一点耐心，收入较高')
    pdf.bullet('App 试玩/试用：下载 App 试用几分钟得 1-5 元')
    pdf.body_text('【变现方式】任务佣金 + 推荐奖励')
    pdf.body_text('【注意】适合碎片时间利用，不适合作为主要收入来源。小心那些要你先交钱的平台。')

    # --- 10 ---
    pdf.add_page()
    pdf.sub_title('副业 10：AI 数字人直播带货')
    pdf.highlight_box('', '💰 收入潜力：5,000 - 50,000+ 元/月\n'
                     '⏱ 上手时间：2-4 周\n'
                     '🛠 必备工具：HeyGen / 腾讯智影 + 抖音/视频号小店\n'
                     '📌 难度等级：⭐⭐⭐（中等）')

    pdf.body_text('【方法】')
    pdf.body_text(
        '用 AI 生成数字人形象，7×24 小时自动直播带货。'
        '你只需要录制好话术、选好产品，AI 数字人替你出镜。'
    )
    pdf.bullet('选择数字人生成工具（HeyGen、腾讯智影、D-ID 等）')
    pdf.bullet('上传产品或精选联盟选品，设置自动讲解脚本')
    pdf.bullet('开通抖音小店/视频号小店，挂商品链接')
    pdf.bullet('多账号矩阵运营，扩大曝光')
    pdf.body_text('【变现方式】直播带货佣金 + 自营产品销售 + 代播服务')
    pdf.body_text('【关键心得】目前已有很多人用数字人 24 小时直播带货月入过万。核心是选品话术和直播间的运营策略。')

    # ========== SECTION 4 ==========
    pdf.add_page()
    pdf.section_title('四', '副业选择决策矩阵')
    pdf.ln(3)

    pdf.body_text(
        '不知道怎么选？按你的实际情况对号入座：'
    )
    pdf.ln(2)

    scenarios = [
        ('🕐 只有碎片时间（学生/在职）',
         '问卷调查 → AI 内容创作 → 闲鱼 → 短视频切片'),
        ('💰 急需变现（1 个月内）',
         '线上家教 → 设计接单 → 微任务 → AI 内容创作'),
        ('🎓 有一技之长',
         '知识付费 → 小报童专栏 → 一对一咨询 → 课程制作'),
        ('💻 懂点编程/技术',
         '小程序开发 → AI 工具站 → Chrome 插件 → 卖模板'),
        ('🎬 喜欢拍视频/出镜',
         '短视频带货 → 数字人直播 → 知识类 IP 打造'),
        ('🛒 有选品/销售天赋',
         '闲鱼无货源 → 跨境电商 → 直播带货'),
        ('🤖 不想跟人打交道',
         'AI 内容创作 → AI 绘画卖素材 → 小程序变现'),
    ]

    for scenario, rec in scenarios:
        pdf.set_font('YH', 'B', 10)
        pdf.set_text_color(30, 60, 120)
        pdf.cell(0, 7, scenario, new_x='LMARGIN', new_y='NEXT')
        pdf.set_font('YH', '', 10)
        pdf.set_text_color(50, 50, 50)
        pdf.cell(0, 7, f'  → 推荐：{rec}', new_x='LMARGIN', new_y='NEXT')
        pdf.ln(2)

    # ========== SECTION 5 ==========
    pdf.add_page()
    pdf.section_title('五', '副业避坑指南')
    pdf.ln(3)

    traps = [
        ('🚫 陷阱 1：先交钱才能做的项目',
         '任何要你先交押金/培训费/加盟费的，99% 是坑。真正的副业应该先赚到钱再花钱。'),
        ('🚫 陷阱 2：承诺"月入十万"的速成课',
         '如果真这么赚钱，他为什么还在卖课而不是闷声发大财？合理预期：副业前 3 个月收入在 0-3000 元很正常。'),
        ('🚫 陷阱 3：刷单/博彩/虚拟货币',
         '这些本质上不是副业，是赌博。不要碰，碰了大概率血本无归。'),
        ('🚫 陷阱 4：All in 副业，裸辞全职做',
         '在副业收入稳定超过主业 2 倍之前，不要辞职。副业是"+1"，不是"替代"。'),
        ('🚫 陷阱 5：同时做太多方向',
         '选 1-2 个方向深耕，做到有小成果再考虑扩展。"多即是少"在副业里是真理。'),
        ('🚫 陷阱 6：忽略税务问题',
         '收入超过一定额度需要报税。用正规平台支付，保留收入记录。'),
    ]

    for title, desc in traps:
        pdf.set_font('YH', 'B', 10)
        pdf.set_text_color(180, 50, 50)
        pdf.cell(0, 7, title, new_x='LMARGIN', new_y='NEXT')
        pdf.set_font('YH', '', 10)
        pdf.set_text_color(50, 50, 50)
        pdf.multi_cell(0, 6, desc)
        pdf.ln(3)

    # ========== SECTION 6 ==========
    pdf.add_page()
    pdf.section_title('六', '实战启动三步骤')
    pdf.ln(3)

    steps = [
        ('🟢 第一步：本周内完成（Day 1-7）',
         [
             '确定 1-2 个你想尝试的方向',
             '整理你已有的技能和资源（会什么？有什么工具？每天有多少时间？）',
             '对标 3-5 个已经做成功的人，拆解他们的模式',
             '注册相关平台账号，熟悉平台规则',
         ]),
        ('🟡 第二步：首月内完成（Week 2-4）',
         [
             '完成第一个最小可行性产出（第一篇文章/第一个视频/第一单设计）',
             '每天投入至少 1 小时在副业上',
             '记录数据（播放量/阅读量/询单量/转化率）',
             '根据数据反馈调整方向和方法',
         ]),
        ('🔵 第三步：三个月内完成（Month 2-3）',
         [
             '找到最有效的变现路径，开始佛系接单/收钱',
             '建立内容沉淀和粉丝基础',
             '优化流程，用 AI 工具替代重复劳动',
             '考虑放大——招助手/做矩阵/加预算',
         ]),
    ]

    for title, items in steps:
        pdf.set_font('SH', '', 12)
        pdf.set_text_color(30, 60, 120)
        pdf.cell(0, 8, title, new_x='LMARGIN', new_y='NEXT')
        pdf.ln(2)
        for it in items:
            pdf.bullet(it)
        pdf.ln(4)

    pdf.ln(4)
    pdf.highlight_box('', '⚡ 核心口诀：先完成，再完美。先跑通，再放大。先赚 1 块钱，再想着月入过万。')

    # ========== SECTION 7 ==========
    pdf.add_page()
    pdf.section_title('七', '结语 & 行动建议')
    pdf.ln(3)

    pdf.body_text(
        '副业的意义不只是多一份收入，更是一种"反脆弱"的生活策略。'
        '在 AI 快速迭代的 2026 年，拥有多元收入来源的人，比只靠一份工资的人更有安全感。'
    )
    pdf.body_text(
        '最后送你三句话：'
    )
    pdf.ln(2)
    quotes = [
        '"种一棵树最好的时间是十年前，其次是现在。"',
        '"副业的本质不是打工，是搭建你的收入系统。"',
        '"AI 不会取代你，但会用 AI 的人会。"',
    ]
    pdf.set_font('FH', '', 12)
    pdf.set_text_color(30, 60, 120)
    for q in quotes:
        pdf.cell(0, 9, f'  {q}', align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(5)
    pdf.set_font('YH', '', 10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, '选一个方向，从今天开始行动。哪怕只写 500 字、剪 1 个视频。', align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.cell(0, 8, '一个月后，你会感谢今天开始行动的自己。', align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(8)

    # --- Action Checklist ---
    pdf.set_fill_color(240, 245, 255)
    pdf.set_draw_color(30, 60, 120)
    pdf.set_font('SH', '', 14)
    pdf.set_text_color(30, 60, 120)
    y = pdf.get_y()
    pdf.rect(10, y, 190, 50)
    pdf.set_xy(14, y + 3)
    pdf.cell(0, 8, '📋 你的 7 天行动计划', new_x='LMARGIN', new_y='NEXT')
    pdf.set_x(14)
    pdf.set_font('YH', '', 10)
    pdf.set_text_color(50, 50, 50)
    checklist = [
        '☐ 选择 1 个副业方向（从决策矩阵里挑）',
        '☐ 注册对应平台账号',
        '☐ 研究 3 个对标账号/同行',
        '☐ 用 AI 产出第一个作品',
        '☐ 发布并观察数据',
        '☐ 每天投入至少 30 分钟',
        '☐ 一周后复盘，决定是否继续深耕',
    ]
    for chk in checklist:
        pdf.set_x(14)
        pdf.cell(0, 6, chk, new_x='LMARGIN', new_y='NEXT')

    # Save
    output_path = os.path.join(os.path.dirname(__file__), '副业变现指南_专业报告.pdf')
    pdf.output(output_path)
    print(f'PDF 报告已生成：{output_path}')
    return output_path

if __name__ == '__main__':
    build_report()
