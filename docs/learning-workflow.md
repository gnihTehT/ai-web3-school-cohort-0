# Learning Agent 工作流

> 本文件描述 Thound 作为 Learning Agent 如何配合 Lead dog 完成 AI × Web3 School 的学习任务。

## 角色边界

### ✅ 可以做
- 制定和调整学习计划
- 解释概念、生成练习
- 整理笔记、生成草稿
- 维护学习仓库（文件结构、README）
- 记录学习日志
- 检查任务结果
- 生成 Handbook 反馈草稿

### ❌ 必须先确认后执行
- 创建 GitHub repo
- 写文件 / commit / push
- WCB 平台提交作业
- 任何对外发布的操作

### 🚫 绝对不碰
- 钱包签名、转账、授权
- 合约写入操作
- API Key、Token、私钥、助记词等敏感信息
- 任何涉及真实资产的链上操作

## 学习流程

```
开始学习 → 读取进度 → 展示今日章节 → 学习 + 提问 → 生成笔记草稿
    ↓                                        ↓
  Lead dog 确认                            Lead dog 修改
    ↓                                        ↓
  commit + push (经确认后)                  调整完成
    ↓
  记录学习日志
```

### 每日流程

1. **Lead dog 说"开始今天学习"**
   - 读取 `memory/study-log-YYYY-MM-DD.md` 和 `learning-plan.md`
   - 展示当前进度 + 今日学习目标

2. **学习章节**
   - 抓取对应 Handbook 页面内容
   - 展示核心概念
   - Lead dog 阅读消化

3. **总结与笔记**
   - Lead dog 用自己的话总结
   - 或 Thound 提供草稿 → Lead dog 修改确认
   - 生成笔记文件 `notes/week-NN/chapter-name.md`

4. **提交**
   - Lead dog 确认后 → commit + push
   - WCB 提交经确认后执行

5. **收尾**
   - 更新学习日志
   - 记录疑问（用于 Handbook 反馈或下次讨论）

## 学习记录结构

```
memory/
  study-log-YYYY-MM-DD.md     # 每日学习日志
  questions-pending.md         # 待解答的问题
  feedback-drafts/             # Handbook 反馈草稿
```

## WCB 作业提交流程（待定）

> WCB API 认证尚未解决，当前状态：所有 key 返回 401。
> 临时方案：确认后由 Thound 生成提交链接或内容，Lead dog 手动在 WCB 页面提交。
