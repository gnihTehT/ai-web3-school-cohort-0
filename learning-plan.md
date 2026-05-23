# 📚 学习计划 — ShadowDoge

> 每天 0.5~1h，**4 周**冲刺黑客松 Demo  
> 方向：综合探索 AI × Web3，产出可演示原型

---

## 总体路线

```
第1周 ─ AI 基础查漏补缺 ─→ LLM / Prompt / Context / Agent (快速过)
                    ↓
第2周 ─ Web3 基础补齐 ──→ Wallet / Smart Contract / AA 
                    ↓
第3周 ─ 交叉核心 ──→ Chain-aware Context / Web3 Tool Use / Agent Wallet → 锁定 Demo 方向
                    ↓
第4周 ─ Demo 冲刺 ──→ 黑客松原型开发 + 打磨
```

---

## 📅 Week 1 — AI 基础查漏补缺

**目标**：快速确认 AI 模块的知识无盲区，重点吃透 Agent 相关章节。

| Day | 主题 | Handbook 链接 | 做什么 |
|-----|------|--------------|--------|
| 1 | LLM | [ai/llm/](https://aiweb3.school/zh/handbook/ai/llm/) | 快速过，查漏补缺 |
| 2 | Prompt | [ai/prompt/](https://aiweb3.school/zh/handbook/ai/prompt/) | 试一个熟悉的结构化 prompt |
| 3 | Context | [ai/context/](https://aiweb3.school/zh/handbook/ai/context/) | 上下文窗口、过期、可信度 |
| 4 | RAG | [ai/rag/](https://aiweb3.school/zh/handbook/ai/rag/) | RAG vs 纯 Context |
| 5 | Agent | [ai/agent/](https://aiweb3.school/zh/handbook/ai/agent/) | **重点**：tool calling、multi-step |
| 6 | MCP / Evaluation | [ai/mcp/](https://aiweb3.school/zh/handbook/ai/mcp/) / [ai/evaluation/](https://aiweb3.school/zh/handbook/ai/evaluation/) | 了解协议层和评估 |

**周产出**：确认最想结合 Demo 的 AI 能力方向

---

## 📅 Week 2 — Web3 基础补齐

**目标**：补齐 Web3 侧知识短板，重点 Account Abstraction。

| Day | 主题 | Handbook 链接 | 做什么 |
|-----|------|--------------|--------|
| 1 | Network | [web3/network/](https://aiweb3.school/zh/handbook/web3/network/) | 区块/共识/L2/RPC 概念回顾 |
| 2 | Crypto + Wallet | [web3/cryptography/](https://aiweb3.school/zh/handbook/web3/cryptography/) + [web3/wallet/](https://aiweb3.school/zh/handbook/web3/wallet/) | **实操**：用 ethers/viem 写签名脚本 |
| 3 | Smart Contract | [web3/smart-contract/](https://aiweb3.school/zh/handbook/web3/smart-contract/) | 部署一个简单合约到测试网 |
| 4 | Account Abstraction | [web3/account-abstraction/](https://aiweb3.school/zh/handbook/web3/account-abstraction/) | **重点**：Smart Account / Session Key |
| 5 | Indexing | [web3/indexing/](https://aiweb3.school/zh/handbook/web3/indexing/) | 事件索引与链上数据查询 |
| 6 | Security | [web3/security/](https://aiweb3.school/zh/handbook/web3/security/) | 权限与风险边界 |

**周产出**：确认 Demo 的链上交互方案

---

## 📅 Week 3 — AI × Web3 Bridge（核心交叉）

**目标**：精读 Bridge 核心章节，锁定 Demo 技术方案。

按优先级阅读：

| Day | 主题 | 优先级 | 为什么重要 |
|-----|------|--------|-----------|
| 1 | [Chain-aware Context](https://aiweb3.school/zh/handbook/bridge/chain-aware-context/) | 🔴 必读 | Agent 怎么"看到"链上状态 |
| 2 | [Web3 Tool Use](https://aiweb3.school/zh/handbook/bridge/web3-tool-use/) | 🔴 必读 | RPC/钱包/合约工具编排 |
| 3 | [Agent Workflow](https://aiweb3.school/zh/handbook/bridge/agent-workflow/) | 🔴 必读 | 哪些自动化、哪些留人环 |
| 4 | [Agent Wallet](https://aiweb3.school/zh/handbook/bridge/agent-wallet/) 🔹 [AI Security](https://aiweb3.school/zh/handbook/bridge/ai-security/) | 🔴 必读 | Agent 权限与安全边界 |
| 5 | [Machine Payment](https://aiweb3.school/zh/handbook/bridge/machine-payment/) | 🟡 重点 | AI 自动支付场景 |
| 6 | [Settlement & Escrow](https://aiweb3.school/zh/handbook/bridge/settlement-and-escrow/) 🎯 **定方向** | 🟡 重点 | 结算 + 锁定 Demo 方向 |

**周产出**：选定 Demo 方向，在 `hackathon/` 下输出技术方案文档

---

## 📅 Week 4 — Demo 冲刺

**目标**：从概念到可演示的黑客松原型

| 阶段 | 内容 | 产出 |
|------|------|------|
| Day 1-2 | 技术选型 + 架构 + 核心 Sprint | 可运行的最小版本 |
| Day 3-4 | 功能完善 + 边角处理 | 稳定版本 |
| Day 5-6 | Demo 打磨 + README + 录屏 | 交付物准备 |

### Demo 方向建议

基于你的画像，以下方向值得考虑：

1. **链上 Agent 助手** — Agent 查链上状态、解释交易、自动签名执行
   - 技术栈：Agent SDK + viem/ethers + Smart Account
   - 参考章节：Chain-aware Context, Web3 Tool Use, Agent Wallet

2. **AI 自动化支付/结算** — Agent 完成服务后自动触发支付
   - 技术栈：Agent Framework + Smart Contract + Session Key
   - 参考章节：Machine Payment, Settlement & Escrow, AA

3. **智能体安全沙箱** — 演示 Agent 权限管控、Session Key、Policy
   - 技术栈：Account Abstraction + Permission Layer
   - 参考章节：Account Abstraction, AI Security, Agent Wallet

4. **链上数据聊天机器人** — 用自然语言查链上数据
   - 技术栈：RAG + Indexing + LLM
   - 参考章节：RAG, Indexing, Chain-aware Context

---

## 📋 每日打卡

每天在 `daily/` 下创建 `YYYY-MM-DD.md`
- 打卡用中文，关键术语保留英文
- 每天 0.5~1h，不求多求持续
- 遇到问题立刻记下来
- 每周末回顾 + 调整下周计划

---

## 🎯 Week 4 结束验收

- [ ] 读完 Handbook 核心章节（至少 Bridge 必读部分）
- [ ] Week 3 结束前锁定 Demo 方向
- [ ] Week 4 结束前 Demo 可演示
- [ ] GitHub 有 15+ 天的打卡记录
- [ ] 提交至少 1 份 Handbook Feedback