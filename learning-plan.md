# 📚 学习计划 — ShadowDoge

> 基于 WCB 实际课程数据。每天 0.5~1h，4 周冲刺黑客松 Demo
> 方向：综合探索 AI × Web3，产出可演示原型

---

## ✅ 已完成

| Phase | Chapter | 进度 |
|-------|---------|------|
| Phase 1: The Landscape | Bridge Connection | ✅ Done |
| Phase 2: AI Basics | LLM | ✅ Done |
| **合计** | **2/24 章节** | **8%** |

---

## 🎯 4 周冲刺路线

```
剩余时间：3.5 周（5/23 周末 → 6/14）
```

### 📅 本周末 5/23(六)~5/24(日) — AI 收尾

**目标：** 快速扫完 Phase 2 剩余章节，补概念盲区

| Day | 章节 | 耗时 | 做什么 |
|-----|------|------|--------|
| 今晚 | **Prompt** | ~20min | 快速过，确认无盲区 |
| 今晚 | **Context** | ~20min | 上下文窗口/过期/可信度 |
| 周日 | **Agent** | ~30min | **重点** — tool calling、multi-step |
| 周日 | RAG + MCP + Eval | ~20min | 概念了解，3 合一快速过 |

> 🔑 重点：Context 和 Agent 是你的 Demo 基石，值得多花时间

---

### 📅 Week 2: 5/25(一)~5/31(日) — Web3 基础

**目标：** 补齐 Web3 侧知识短板，重点 AA 和 Security

| Day | 章节 | 优先级 | 实操 |
|-----|------|--------|------|
| 一 | **Network** | 🟢 回顾 | 区块/L2/RPC |
| 二 | **Crypto + Wallet** | 🟡 重点 | 用 viem/ethers 写签名脚本 |
| 三 | **Smart Contract** | 🟡 重点 | 部署一个合约到测试网 |
| 四 | **Account Abstraction** | 🔴 **关键** | Smart Account / Session Key |
| 五 | **Indexing** | 🟢 了解 | 事件索引 |
| 六 | **Security** | 🔴 **关键** | 权限与风险边界 |
| 日 | 周回顾 | 🎯 | 更新进度 + 选 Demo 方向概念 |

---

### 📅 Week 3: 6/1(一)~6/7(日) — Bridge 核心交叉 🔥

**目标：** 精读 Bridge 核心章节，锁定 Demo 技术方案

| Day | 章节 | 优先级 | 为什么重要 |
|-----|------|--------|-----------|
| 一 | **Chain-aware Context** | 🔴 必读 | Agent 如何读取链上状态 |
| 二 | **Web3 Tool Use** | 🔴 必读 | RPC/钱包/合约工具编排 |
| 三 | **Agent Workflow** | 🔴 必读 | 人机协作边界 |
| 四 | **Agent Wallet** | 🔴 必读 | Agent 权限管理 |
| 五 | **Machine Payment** + **Settlement** | 🟡 重点 | 自动支付与结算 |
| 六 | **AI Security** + **Verifiable AI** | 🟡 重点 | 安全与可验证 |
| 日 | **定方向！** | 🎯 | 锁定 Demo 方案 |

> 🔑 前四天必须吃透，后半根据 Demo 方向选读

---

### 📅 Week 4: 6/8(一)~6/14(日) — Demo 冲刺 🚀

**目标：** 从概念到可演示的黑客松原型

| 阶段 | 内容 | 产出 |
|------|------|------|
| 一 ~ 二 | 技术选型 + 架构 + 核心代码 | 可运行最小版本 |
| 三 ~ 四 | 功能完善 + 边角处理 | 稳定版本 |
| 五 ~ 六 | Demo 打磨 + README + 录屏 | 交付物打包 |

### Demo 方向候选

1. **链上 Agent 助手** — Agent 查链上状态、解释交易、自动签名
   - 技术栈：Agent Framework + viem/ethers + Smart Account
   - 参考：Chain-aware Context, Web3 Tool Use, Agent Wallet

2. **AI 自动结算系统** — Agent 完成服务后自动触发支付
   - 技术栈：Agent + Smart Contract + Session Key
   - 参考：Machine Payment, Settlement, AA

3. **智能体安全沙箱** — 演示 Agent 权限管控
   - 技术栈：Account Abstraction + Permission Layer
   - 参考：AA, AI Security, Agent Wallet

4. **链上数据问答** — 自然语言查链上数据
   - 技术栈：RAG + Indexing + LLM
   - 参考：RAG, Chain-aware Context

---

## 📊 总进度追踪

```
Phase 1 (Landscape):  ■■■■■■■■■■ 100% (1/1) ✅
Phase 2 (AI):         ■■░░░░░░░░  14% (1/7) 
Phase 3 (Web3):       ░░░░░░░░░░   0% (0/7)
Phase 4 (Bridge):     ░░░░░░░░░░   0% (0/12)
Phase 5 (Hackathon):  ░░░░░░░░░░   0%
────────────────────────────────────
Total:                 ■░░░░░░░░░   8%
```

---

## 🎯 4 周后验收

- [ ] Phase 2~4 全部章节完成
- [ ] 所有学习笔记在 `daily/` 下
- [ ] Week 3 结束前锁定 Demo 方向
- [ ] Week 4 结束前 Demo 可演示
- [ ] 提交 ≥1 份 Handbook Feedback
