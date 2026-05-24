#!/usr/bin/env python3
import os, subprocess, sys

CLI = r"C:\Users\xiang\AppData\Local\Programs\Obsidian\Obsidian.com"

def create(name, content):
    cmd = [CLI, "create", f"name={name}", f"content={content}"]
    r = subprocess.run(cmd, capture_output=True, text=False, timeout=15)
    out = r.stdout.decode('utf-8', errors='replace').strip() if r.stdout else ""
    err = r.stderr.decode('utf-8', errors='replace').strip() if r.stderr else ""
    print(f"[{name}] => {out or err}")

# ========== 最新动态篇 ==========
create("AI动态-2026趋势", """# 2026 年 AI 趋势

## 核心趋势

### 1. Agent 元年
- 从对话式 AI 到自主行动的 Agent
- 多 Agent 协作系统成熟
- MCP 协议成为工具交互标准
- AI 从工具演变为"同事"

### 2. 开源模型崛起
- DeepSeek、Qwen、LLaMA 等开源模型性能逼近闭源
- 中小企业和个人可以本地部署
- 社区驱动迭代速度加快

### 3. 长上下文竞争
- 上下文窗口从 4K 增至 1M+ tokens
- 整本书、整个代码库一次输入
- RAG 技术被长上下文部分替代

### 4. 多模态融合
- 文本+图像+音频+视频原生处理
- AI 理解物理世界的能力增强
- 端侧多模态模型成熟

### 5. AI 编程民主化
- 自然语言成为编程接口
- 编程门槛大幅降低
- 从"写代码"到"审代码"转变

### 6. 成本急速下降
- API 价格年降 80%+
- 推理成本趋近于零
- 高质量模型免费使用""")

create("AI动态-DeepSeek生态", """# DeepSeek 生态

## 公司背景
- 中国 AI 初创公司，深度求索
- 开源路线，技术领先
- 极低的 API 定价策略

## 模型家族

### DeepSeek-V4 Flash
- 旗舰推理模型，速度极快
- 价格：输入￥0.14/M tokens，输出￥0.28/M tokens
- 上下文：1M tokens
- 性价比之王

### DeepSeek-V4 Pro
- 大型推理模型，综合能力强
- 价格：输入￥1.74/M tokens，输出￥3.48/M tokens
- 适合复杂任务

### DeepSeek-R1
- 推理增强模型
- 数学、逻辑、代码推理突出
- 开源，可本地部署

## 优势
- 中文理解能力优秀
- 价格极低（约为 GPT 的 1/50）
- 完全开源，可商用
- 长上下文支持

## 生态工具
- DeepSeek API：OpenAI 兼容接口
- DeepSeek App：移动端对话
- 第三方集成：Cursor、Continue、OpenClaw""")

create("AI动态-Claude与OpenAI", """# Claude & OpenAI 发展

## OpenAI 2025-2026
- **GPT-4.1**：1M 上下文，更强指令遵循
- **o1 / o3**：推理模型系列
- **Agents SDK**：官方 Agent 开发框架
- **ChatGPT 搜索**：集成实时搜索
- **Sora**：视频生成

## Anthropic / Claude
- **Claude 4 (Opus/Sonnet)**：安全优先，推理能力强
- **Claude Code**：终端编程 Agent
- **MCP 协议**：模型上下文协议
- **宪法 AI**：价值观对齐方法
- **长上下文**：200K tokens

## 市场竞争
- OpenAI vs Anthropic：两大闭源阵营
- DeepSeek / Qwen：开源挑战者
- Google Gemini：生态整合
- 价格战白热化""")

# ========== 实战指南篇 ==========
create("AI实战-AI工具链配置", """# AI 工具链配置

## 我的工具链

### 当前配置
| 工具 | 状态 | 用途 |
|------|------|------|
| OpenClaw | 运行中 | AI 助手主入口，QQ Bot 对接 |
| DeepSeek-V4 Flash | 已接入 | 主力模型，日常使用 |
| Obsidian CLI | 已激活 | 知识库管理 |
| Claude Code | 已安装 | AI 编程 Agent（需升级系统） |
| CC-Switch | 已安装 | 模型配置切换 |
| Claudian | 已注册 | OpenClaw 的 Claude Code 桥接层 |

### 配置备忘
1. Obsidian CLI：设置 > 通用 > 高级 > 命令行接口（已开启）
2. CC-Switch 配置目录：~/.claude/profiles/
3. Claudian 插件：OpenClaw 配置已注册
4. API Key 储存位置：（请勿明文写入笔记）

### 下一步
- 升级 Windows 10 至 22H2 以启动 Claude Code
- 配置 CC-Switch 接入国产模型（需 API Key）
- 配置 Claudian 使 OpenClaw 调用 Claude Code""")

create("AI实战-国产模型接入", """# 国产模型接入指南

## 主流国产模型 API

### 1. 通义千问（阿里云 DashScope）
- 官网：dashscope.aliyun.com
- 兼容 OpenAI API 格式
- 模型：qwen-max、qwen-plus、qwen-turbo
- 费用：约 ￥1-10 / M tokens

### 2. 智谱 GLM（智谱AI）
- 官网：open.bigmodel.cn
- 兼容 OpenAI API 格式
- 模型：glm-4-plus、glm-4-air
- 费用：约 ￥1 / M tokens

### 3. DeepSeek
- 官网：platform.deepseek.com
- 完全兼容 OpenAI API 格式
- 模型：deepseek-v4-flash、deepseek-v4-pro、deepseek-reasoner
- 费用：￥0.14-1.74 / M tokens（最便宜）

### 4. 小米 MiMo
- 小米大模型平台
- 具体接入方式以官网为准

## 通用接入方案（CC-Switch）

### 创建 DeepSeek 配置
```bash
cc-switch new deepseek
# 配置 API Key 和 Base URL
cc-switch use deepseek
```

### 创建通义千问配置
```bash
cc-switch new qwen
# 配置 API Key 和 Base URL: https://dashscope.aliyuncs.com/compatible-mode/v1
cc-switch use qwen
```""")

create("AI实战-Prompt工程", """# Prompt 工程指南

## 核心原则

### 1. 明确角色（Role）
- 给 AI 一个明确的身份定位
- 示例："你是一位资深 Python 开发者"

### 2. 具体任务（Task）
- 清晰描述要完成的任务
- 示例："请分析这段代码的性能问题"

### 3. 输出格式（Format）
- 指定返回的格式和结构
- 示例："用表格列出优化建议"

### 4. 上下文（Context）
- 提供充分的背景信息
- 示例："这是一个电商网站的订单模块"

### 5. 约束条件（Constraints）
- 明确限制和要求
- 示例："不要使用外部库，仅用标准库"

## 常用模板

### 代码审查
```
请审查以下代码，关注：
1. 潜在 Bug
2. 性能问题
3. 安全漏洞
4. 代码风格
5. 改进建议

[粘贴代码]
```

### 问题解决
```
我正在解决 [具体问题]。
环境：[OS/语言/版本]
已尝试：[已做的尝试]
错误信息：[贴错误]
请帮我分析原因并提供解决方案。
```

### 学习新知识
```
请用简单的语言解释 [概念]，
给出 3 个实际例子，
并与 [相关概念] 对比。
```

## 技巧
- 用 AI 优化你的 Prompt（元提示）
- 分步骤提问复杂问题
- 要求 AI 列出不确定之处
- 用示例示范期望的输出""")

print("\\n=== 全部创建完成！ ===")
