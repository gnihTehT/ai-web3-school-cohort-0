# 学习产物：最小可交互 AI × Web3 概念助手

## 任务

Week 1 学了 10+ AI 概念和多个 Web3 概念，被动阅读笔记容易看完就忘。需要一个能主动交互的复习工具。

## 产物

**文件：** `notes/week-01/ai_learn.py`
**GitHub：** https://github.com/gnihTehT/ai-web3-school-cohort-0/blob/main/notes/week-01/ai_learn.py

### 形式

Python 3 CLI 交互工具（无外部依赖），支持参数模式和交互菜单两种启动方式。

### 功能（5 种模式）

| 模式 | 命令 | 作用 |
|------|------|------|
| 🧠 概念测验 | `python3 ai_learn.py quiz` | 根据描述（解释/例子/误区）猜概念名，自动计分 |
| 📖 概念查阅 | `python3 ai_learn.py explain` | 输入概念名看详细解释+例子+常见误区 |
| ⚖️ 概念对比 | `python3 ai_learn.py compare` | 预设 8 组对比 + 自定义对比，并排显示，一句话总结 |
| 🎲 随机漫游 | `python3 ai_learn.py explore` | 随机展示概念，可展开详情，适合碎片时间 |
| 📋 概念列表 | `python3 ai_learn.py list` | 一览全部 14 个概念 |

### 覆盖概念（14 个）

- **AI 侧（10）：** LLM、Prompt、Context Window、Agent、Tool Use、Workflow、Guardrails、Human-in-the-Loop、RAG、MCP
- **Web3 侧（4）：** EOA、Smart Account (ERC-4337)、Multisig、Agent Wallet

### AI 辅助说明

| 部分 | 由谁完成 | 说明 |
|------|----------|------|
| 概念库初稿 | AI 生成 | 根据 Week 1 笔记 + 课程大纲生成每个概念的 one-liner、解释、例子和误区 |
| 概念准确性复审 | **我逐条复核** | 全部对照已完成的笔记文件进行核实 |
| RAG/MCP/Agent Wallet 补充 | AI 初稿 → 我复核 | 这些概念笔记里还未覆盖，由 AI 根据课程大纲补充，我做了术语准确性检查 |
| **交互逻辑代码** | **全部手工编写** | 菜单系统、测验评分、模糊匹配、对比排版、输入验证——一切代码纯手写 |

### 交互示例

**测验模式：**
```
  ─── 第 1 题 (例子) ───

  Claude 本身不知道'今天股价是多少'，但如果给它一个查询股票 API 的工具，它就能实时查询并回答。

  > tool_use
  ✅ 正确！(1/1)
```

**查阅模式：**
```
  > agent

  📌 Agent（智能体）
  🏷️  🤖 AI 概念
  ── 能自主规划、调用工具、执行多步骤任务的 AI 系统

  📖 详细解释: Agent 的核心是'自主执行'——它有目标，会分解任务...
  🎯 例子: 订机票 Agent 自动搜索航班、比较价格、调用订票接口...
  ⚠️  常见误区: 很多人把'会聊天的 AI'和 Agent 混为一谈...
```

**对比模式：**
```
  ⚖️ Agent（智能体） vs Workflow（工作流）
  ──────────────────────────┬─────────────────────────┐
  Agent（自主规划）           │ Workflow（预设路径）        │
  ─────────────────────────┼─────────────────────────┤
  能自主规划、调用工具、执行多步骤  │ 按逻辑顺序串联 AI 调用      │
  ─────────────────────────┴─────────────────────────┘

  💡 一句话: Agent 是自己决定怎么走，Workflow 是走设计好的路
```

### 限制与改进

- 概念库目前静态，不联网
- 未来可接入真实 API 做"AI 提示助手"模式
- 可添加 Anki 闪卡导出功能

## 提交链接

https://github.com/gnihTehT/ai-web3-school-cohort-0/blob/main/notes/week-01/ai_learn.py
