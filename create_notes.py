#!/usr/bin/env python3
import os, subprocess

CLI = r"C:\Users\xiang\AppData\Local\Programs\Obsidian\Obsidian.com"

def create(name, content):
    cmd = [CLI, "create", f"name={name}", f"content={content}"]
    r = subprocess.run(cmd, capture_output=True, text=False, timeout=15)
    out = r.stdout.decode('utf-8', errors='replace').strip() if r.stdout else ""
    err = r.stderr.decode('utf-8', errors='replace').strip() if r.stderr else ""
    print(f"{name}: {out or err}")

# === 工具篇 ===
create("AI工具-Claude Code", """# Claude Code

## 概述
Anthropic 推出的终端原生 AI 编程助手，深度集成开发环境。

## 特性
- **终端原生**：直接在终端中理解整个代码库
- **文件操作**：创建、编辑、删除文件
- **命令执行**：运行测试、git 操作、部署
- **MCP 协议**：连接外部工具和数据源
- **长上下文**：支持大型代码库分析

## 安装
```bash
npm install -g @anthropic-ai/claude-code
```

## 配置管理（CC-Switch）
通过 CC-Switch 管理多套配置，可切换不同模型：
```bash
npm install -g @hobeeliu/cc-switch
cc-switch init          # 初始化
cc-switch new 配置名    # 创建配置
cc-switch use 配置名    # 切换配置
```

## 国产模型接入
配合 CC-Switch + 国产 API 实现：
- 通义千问：替换 base URL 为阿里云 DashScope 端点
- 智谱 GLM：使用智谱开放平台 API
- 小米 MiMo：小米大模型 API

## 推荐配置
```json
{
  "apiKey": "your-api-key",
  "model": "deepseek-v4-flash",
  "baseUrl": "https://api.deepseek.com"
}
```""")

create("AI工具-Cursor与Copilot", """# Cursor & Copilot

## Cursor
- AI-first 代码编辑器，VS Code 分支
- 内置 Claude / GPT 集成
- Tab 补全、内联编辑、自然语言编程
- 支持整库理解和重构

## GitHub Copilot
- 最早的 AI 编程助手
- 深度 VS Code / JetBrains 集成
- Copilot Chat：对话式代码辅助
- Copilot Agent：自动修复 Issue

## Windsurf
- Codeium 推出的 AI IDE
- 流式编程体验
- 多文件重构能力

## 对比
| 工具 | 特点 | 价格 |
|------|------|------|
| Cursor | AI-first IDE | $20/月 |
| Copilot | IDE 插件 | $10/月 |
| Claude Code | 终端原生 | 按量付费 |
| Windsurf | 流式编程 | $15/月 |""")

create("AI工具-AI编程工具演进", """# AI 编程工具演进

## 发展阶段

### 第一阶段：补全（2021-2022）
- GitHub Copilot 发布
- 基于上下文的代码补全
- 单行或多行自动完成

### 第二阶段：对话（2023-2024）
- ChatGPT 引发 AI 编程革命
- Cursor 诞生，AI-first IDE
- 自然语言描述需求生成代码
- 内联编辑和代码解释

### 第三阶段：Agent（2024-2025）
- Claude Code：终端原生 Agent
- Cursor Agent：自主规划多步骤
- Copilot Agent：自动修复 Issue
- 自主编码、调试、部署

### 第四阶段：全栈自主（2025-2026）
- 多 Agent 协作系统
- 端到端项目生成
- AI 驱动的代码审查和测试
- 从需求到部署全流程

## 趋势展望
- 编程门槛大幅降低
- 从写代码到"审核代码"的转变
- AI 原生开发工具取代传统 IDE
- 自然语言成为主要编程接口""")

# Continue from last success - skip already created ones
# === Already created above ===

create("AI应用-AI内容创作", """# AI 内容创作

## 应用场景
- **文章写作**：公众号、头条号、知乎专栏
- **营销文案**：广告语、产品描述、邮件
- **视频脚本**：短视频、口播稿、解说词
- **社交媒体**：微博、小红书、抖音文案
- **翻译润色**：多语言翻译、文本优化

## 工具推荐
- **ChatGPT / DeepSeek**：通用写作辅助
- **Claude**：长文写作、深度分析
- **Midjourney / DALL-E**：AI 配图
- **剪映 / CapCut**：AI 视频剪辑
- **HeyGen**：数字人视频生成

## 变现模式
- 公众号流量主
- 付费专栏（小报童）
- 品牌软文接单
- 短视频带货
- AI 绘画接单
""")

create("AI应用-AI数据分析", """# AI 数据分析

## 能力
- **数据清洗**：自动处理缺失值、异常值
- **统计分析**：描述统计、假设检验、回归分析
- **可视化**：自动生成图表
- **报告生成**：自动撰写分析报告
- **预测建模**：机器学习模型训练与评估

## 工具链
- **Python + AI**：Pandas + ChatGPT/Claude
- **Jupyter + Copilot**：交互式数据探索
- **AI BI 工具**：Tableau AI、Power BI Copilot
- **自然语言查询**：用自然语言问数据问题
""")

print("=== 应用篇创建完成 ===")

# === 最新动态篇 ===
create("AI动态-2026趋势", """# 2026 年 AI 趋势

## 核心趋势

### 1. Agent 元年
- 从对话式 AI 到自主行动的 Agent
- 多 Agent 协作系统成熟
- MCP 协议成为工具交互标准
- AI 从工具演变为"同事"

### 2. 开源模型崛起
- DeepSeek、Qwen、LLaMA 等开源模型性能逼近闭源
- 中小企业和个人可以本地部署")}, """# AI 辅助编程

## 当前能力
- **代码生成**：自然语言描述需求，自动生成完整代码
- **代码审查**：自动检查 Bug、安全漏洞、性能问题
- **代码重构**：优化结构、提取函数、重命名
- **测试生成**：自动编写单元测试、集成测试
- **文档生成**：自动生成 API 文档、注释
- **Bug 修复**：分析报错，自动修复

## 最佳实践
1. **明确需求**：描述越清晰，输出越准确
2. **小步迭代**：逐步构建，每次验证
3. **提供上下文**：附上相关代码和错误信息
4. **审查输出**：AI 写的代码仍需人工审查
5. **建立规范**：用提示词模板统一输出风格

## 局限
- 复杂架构设计仍需人类
- 安全敏感代码需严格审查
- 领域特定逻辑可能出错
- 依赖训练数据的时效性""")

create("AI应用-AI内容创作", """# AI 内容创作

## 应用场景
- **文章写作**：公众号、头条号、知乎专栏
- **营销文案**：广告语、产品描述、邮件
- **视频脚本**：短视频、口播稿、解说词
- **社交媒体**：微博、小红书、抖音文案
- **翻译润色**：多语言翻译、文本优化

## 工具推荐
- **ChatGPT / DeepSeek**：通用写作辅助
- **Claude**：长文写作、深度分析
- **Midjourney / DALL-E**：AI 配图
- **剪映 / CapCut**：AI 视频剪辑
- **HeyGen**：数字人视频生成

## 变现模式
- 公众号流量主
- 付费专栏（小报童）
- 品牌软文接单
- 短视频带货
- AI 绘画接单""")

create("AI应用-AI数据分析", """# AI 数据分析

## 能力
- **数据清洗**：自动处理缺失值、异常值
- **统计分析**：描述统计、假设检验、回归分析
- **可视化**：自动生成图表（matplotlib、plotly）
- **报告生成**：自动撰写数据分析报告
- **预测建模**：机器学习模型训练与评估

## 工具链
- **Python + AI**：Pandas + ChatGPT/Claude
- **Jupyter + Copilot**：交互式数据探索
- **AI BI 工具**：Tableau AI、Power BI Copilot
- **自然语言查询**：用自然语言问数据问题""")

print("=== 工具和应用篇创建完成 ===")
