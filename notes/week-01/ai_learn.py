#!/usr/bin/env python3
"""
AI × Web3 概念助手 — 最小可交互学习工具

作者: ShadowDoge
用途: 帮助复习 WCB AI × Web3 School Cohort 0 的 Week 1 概念

▸ 概念库数据来源:
  AI 辅助: 根据 WCB 课程材料生成初稿 + 补充 RAG/MCP/Agent Wallet 概念
  人工核实: ShadowDoge 逐条复核术语准确性,修正概念边界和例子表述

▸ 交互逻辑: 完全手动编写

用法:
  python3 ai_learn.py quiz          # 概念测验
  python3 ai_learn.py explain       # 查阅概念解释
  python3 ai_learn.py compare       # 概念对比
  python3 ai_learn.py explore       # 随机漫游模式
"""

import random
import sys
from typing import Dict, List, Tuple

# ── 概念库 ──────────────────────────────────────────────
# AI 辅助: 根据 WCB Week 1 笔记 + 课程材料生成初稿
# 人工核实: ShadowDoge 逐条复核并修正

CONCEPTS: Dict[str, Dict] = {
    "llm": {
        "name": "LLM（大型语言模型）",
        "one_liner": "通过海量文本训练、能理解和生成自然语言的概率预测系统",
        "detail": (
            "LLM 本质上是'预测下一个词'的统计模型，通过海量文本训练而来。"
            "它没有真正的理解或意识，而是在做极其复杂的模式匹配。"
            "GPT-4、Claude、Gemini 都是 LLM。"
        ),
        "example": "你问'帮我写一封请假邮件'，模型根据训练中见过的无数邮件格式，生成一封听起来合理的回复。",
        "pitfall": "很多人以为 LLM 在'思考'或'理解'，实际上它只是在做概率预测。它没有记忆、没有意图，也不会'知道'自己说的是否正确——这也是它会一本正经胡说（幻觉）的原因。",
        "category": "ai",
    },
    "prompt": {
        "name": "Prompt（提示词）",
        "one_liner": "你给 AI 的输入指令，写法直接影响输出质量",
        "detail": (
            "Prompt 是人和模型沟通的语言。好的 prompt 包含明确的角色设定、"
            "足够的上下文、和期望的输出格式。Prompt 工程是一项需要刻意练习的技能。"
        ),
        "example": "同样问天气：'今天天气怎么样？' vs '请用适合小学生理解的语言解释什么是梅雨季节，并举一个生活中的例子'——后者的结果差距很大。",
        "pitfall": "很多人以为 prompt 越短越'自然'越好。实际上，给 AI 足够的上下文、明确的角色设定和输出格式，往往能得到更准确的结果。",
        "category": "ai",
    },
    "context_window": {
        "name": "Context Window（上下文窗口）",
        "one_liner": "模型在一次对话中能'看到'并处理的最大文字量",
        "detail": (
            "超出 context window 的内容模型就'忘了'。"
            "每次请求都只能看到窗口内的内容，窗口外的一概不知。"
            "Context window 越大不一定越好——太长的 context 会让模型注意力分散。"
        ),
        "example": "假设 context window 是 8000 token（≈6000 汉字），聊了很长时间后，早期对话内容就会被'挤出'窗口，模型不再记得最初说过什么。",
        "pitfall": "很多人以为 AI 可以记住'所有'对话。实际上每次请求都只看到窗口内的内容，窗口外的一概不知。此外，context window 越大不一定越好——太长的 context 会让模型注意力分散。",
        "category": "ai",
    },
    "agent": {
        "name": "Agent（智能体）",
        "one_liner": "能自主规划、调用工具、执行多步骤任务的 AI 系统",
        "detail": (
            "Agent 的核心是'自主执行'——它有目标，会分解任务，会用工具，"
            "会根据结果调整下一步行动。普通聊天只是一问一答，Agent 则能独立完成复杂流程。"
        ),
        "example": "订机票 Agent 接到'帮我订下周五去上海的机票'后，自动搜索航班、比较价格、调用订票接口、发送确认邮件——无需人工介入每一步。",
        "pitfall": "很多人把'会聊天的 AI'和 Agent 混为一谈。Agent 失控的风险也比普通对话高，因为它会做出实际影响世界的操作（如调用支付 API、发送邮件）。",
        "category": "ai",
    },
    "tool_use": {
        "name": "Tool Use（工具调用）",
        "one_liner": "让 AI 能调用外部工具（搜索、代码、API）来突破模型自身局限",
        "detail": (
            "Tool use 由开发者预先定义好一组工具及其参数格式，模型判断何时需要用工具，"
            "调用后再把结果整合进回答。没有显式定义的工具，模型什么外部资源都调不了。"
        ),
        "example": "Claude 本身不知道'今天股价是多少'，但如果给它一个查询股票 API 的工具，它就能实时查询并回答。",
        "pitfall": "容易误以为工具调用是模型'自带'的能力。其实是开发者预先定义好工具和参数格式，模型才能选择调用。没有定义，模型什么外部工具都调不了。",
        "category": "ai",
    },
    "workflow": {
        "name": "Workflow（工作流）",
        "one_liner": "把多个 AI 调用或操作按逻辑顺序串联成可重复执行的自动化流程",
        "detail": (
            "Workflow 的步骤和路径通常是开发者预先设计好的（确定性更强），"
            "而 Agent 更灵活，能自己决定下一步（自主性更强）。实际项目中往往两者结合使用。"
        ),
        "example": "内容创作 workflow：生成大纲 → 逐段生成内容 → 审核语气和合规性 → 自动发布。每一步的输出是下一步的输入。",
        "pitfall": "Workflow 和 Agent 经常被混淆。Workflow 是预设路径（确定性），Agent 是自主决策（灵活性）。两者常结合使用。",
        "category": "ai",
    },
    "guardrails": {
        "name": "Guardrails（护栏）",
        "one_liner": "对 AI 输出进行约束和过滤，确保行为在安全合法范围内",
        "detail": (
            "Guardrails 不是一次设置就完事的。攻击者可以通过 prompt injection 绕过护栏。"
            "好的 guardrails 需要持续测试和迭代。"
        ),
        "example": "客服 AI 设置了'不能讨论竞争对手产品''不能提供法律建议'。用户问'你们和 XX 牌比哪个好？'，系统检测到限制话题，自动引导到其他回答。",
        "pitfall": "Guardrails 不是万能的，也不是一次设置就完事。攻击者可以通过精心设计的 prompt（prompt injection）绕过护栏。好的 guardrails 需要持续测试和迭代。",
        "category": "ai",
    },
    "human_in_the_loop": {
        "name": "Human-in-the-Loop（人在回路中）",
        "one_liner": "在 AI 流程关键节点加入人工审核或决策，避免完全依赖 AI",
        "detail": (
            "好的 HITL 设计是把人工介入聚焦在真正高风险、高价值的决策节点上，"
            "而不是每个步骤都让人审核。审核疲劳会导致人类敷衍了事。"
        ),
        "example": "AI 生成合同草稿，但在正式发送前系统暂停，要求律师审阅确认才能继续。这个'暂停→人工确认→继续'就是 HITL。",
        "pitfall": "很多人觉得'加了 human-in-the-loop 就安全了'。如果审核频率太高，人类会陷入审核疲劳，开始敷衍地点确认——结果和没有人工审核差不多。",
        "category": "ai",
    },
    "rag": {
        "name": "RAG（检索增强生成）",
        "one_liner": "让 AI 在回答前先检索外部知识库，用真实信息辅助生成",
        "detail": (
            "RAG 的核心流程：接收到问题 → 从知识库/向量数据库检索相关片段 → "
            "把检索结果作为上下文注入 prompt → LLM 基于检索到的信息生成回答。"
            "这样可以大幅减少幻觉，让 AI 基于你提供的数据说话。"
        ),
        "example": "一个公司内部知识库问答系统：员工问'我的年假还剩几天'，系统先从 HR 数据库中检索该员工的休假记录，再把数据作为 context 让 LLM 生成回答。",
        "pitfall": "RAG 的效果上限取决于检索质量——如果检索到的文档不相关或有误，LLM 再强也没用。'垃圾进，垃圾出'。",
        "category": "ai",
    },
    "mcp": {
        "name": "MCP（Model Context Protocol）",
        "one_liner": "AI 模型与外部工具/数据源之间的标准化通信协议",
        "detail": (
            "MCP（Model Context Protocol）是 Anthropic 提出的开放协议，"
            "定义了 AI 模型如何通过标准接口发现和调用外部工具、访问数据源。"
            "相当于给 AI 装了一个'USB 接口'——任何实现了 MCP 的服务都可以即插即用。"
        ),
        "example": "一个 MCP 服务器提供 GitHub API 工具，AI 客户端通过 MCP 协议自动发现'搜索仓库''创建 issue''查看 PR'等工具，无需手动配置每个工具的调用格式。",
        "pitfall": "MCP 还比较新（2024年底推出），生态在快速扩张中，不同实现之间的兼容性还在完善。目前主要在 Agent 框架（如 Claude Desktop、Hermes Agent）中使用。",
        "category": "ai",
    },
    "eoa": {
        "name": "EOA（外部账户）",
        "one_liner": "由私钥控制的链上账户——私钥即一切",
        "detail": (
            "EOA（Externally Owned Account）是区块链上最基础的账户类型。"
            "本质是公私钥对，私钥签名交易，公钥派生地址。没有代码、没有逻辑，"
            "纯粹由协议层定义。私钥丢失 = 账户丢失，没有恢复机制。"
        ),
        "example": "你在 MetaMask 里创建的第一个钱包就是 EOA。每次转账都需要用私钥签名交易。高频低值交易中 EOA 仍是最优解，因为简单=低风险、低 Gas。",
        "pitfall": "私钥单点故障——丢失或泄露则资产全失，无熔断机制。EOA 无法批量操作、无法编程化、无法恢复。",
        "category": "web3",
    },
    "smart_account": {
        "name": "智能账户（Smart Account / ERC-4337）",
        "one_liner": "运行在链上的合约账户，可通过代码自定义验证逻辑和策略",
        "detail": (
            "智能账户通过 ERC-4337 标准实现。核心能力：多验证策略（单签/2FA/社交恢复）、"
            "支出限额与白名单、会话密钥（低权限自动操作）、原子批处理、无气体验（Paymaster 代付 Gas）。"
            "逻辑即安全——代码写得好就安全，写不好就出事。"
        ),
        "example": "在游戏中授权一个会话密钥，让游戏可以在不弹窗确认的情况下自动扣减游戏内资源（如每日上限 100 笔，单笔不超过 0.01 ETH）。这就是智能账户的 session key 能力。",
        "pitfall": "合约漏洞（逻辑 bug、代理劫持）是主要风险；依赖基础设施（relayer、bundler）。复杂度高，攻击面比 EOA 更大。",
        "category": "web3",
    },
    "multisig": {
        "name": "多签账户（Multisig）",
        "one_liner": "需要 N 个预定义签名者中 M 个签名才能执行交易的合约账户",
        "detail": (
            "多签的核心是分布式信任——M 个签名者中必须 M 个都被攻破才出事。"
            "支持签名者管理（添加/移除通常需内部投票）、交易模拟、模块化扩展。"
            "Gnosis Safe（现 Safe）是最广泛使用的方案。"
        ),
        "example": "DAO 的国库管理：设置 3/5 多签钱包，任何转账需要 5 位签名者中至少 3 人确认。这样即使一个人的私钥泄露，攻击者也转不走资金。",
        "pitfall": "治理僵局（签名者失联/恶意）、签名者合谋风险、链上 Gas 成本高。EOA 是把钥匙挂脖子上，多签是把钥匙分给几个人——安全但每次开门都得等人到齐。",
        "category": "web3",
    },
    "agent_wallet": {
        "name": "Agent Wallet（智能体钱包）",
        "one_liner": "赋予 AI Agent 链上操作能力的权限受限钱包",
        "detail": (
            "Agent Wallet 不是普通钱包——它是有权限边界的。"
            "通过智能账户的 session key 或 spend limit 机制，给予 Agent 在限定范围内自主操作的能力。"
            "比如'只有权调用这 3 个合约''单日最多支出 0.1 ETH''不能转移 NFT'。"
        ),
        "example": "一个自动支付订阅费的 Agent：每周自动调用 USDT 转账合约给服务商，限额 50 USDT/周。用户提前授权这个行为，Agent 无需每次请求签名确认。",
        "pitfall": "Agent Wallet 的权限设置必须精确——给多了风险大，给少了 Agent 无法完成工作。权限应遵循最小原则：只给完成任务所必需的最低权限。",
        "category": "web3",
    },
}

CATEGORIES = {
    "ai": "🤖 AI 概念",
    "web3": "⛓️ Web3 概念",
}


# ── 交互逻辑（手动编写） ───────────────────────────────

def print_header(title: str):
    """打印格式化的标题"""
    width = 58
    print()
    print("╭" + "─" * width + "╮")
    print(f"│ {title:<{width - 1}s}│")
    print("╰" + "─" * width + "╯")
    print()


def print_menu():
    """打印主菜单"""
    print_header("🧠 AI × Web3 概念助手")
    print("  1. quiz     — 概念测验（根据描述猜概念名）")
    print("  2. explain  — 查阅概念解释")
    print("  3. compare  — 概念对比")
    print("  4. explore  — 随机漫游")
    print("  5. list     — 列出所有概念")
    print("  6. quit     — 退出")
    print()


def ask_choice(prompt: str, valid_options: List[str]) -> str:
    """带验证的用户输入"""
    while True:
        try:
            choice = input(f"\n  {prompt} ").strip().lower()
            if choice in valid_options:
                return choice
            print(f"  ⚠️  请输入: {'/'.join(valid_options)}")
        except (EOFError, KeyboardInterrupt):
            print()
            return "quit"


# ── 模式 1: 概念测验 ───────────────────────────────────

QUIZ_TYPES = [
    {
        "key": "one_liner",
        "prompt": "一句话解释",
        "format": lambda c: c["one_liner"],
    },
    {
        "key": "example",
        "prompt": "例子",
        "format": lambda c: c["example"],
    },
    {
        "key": "pitfall",
        "prompt": "常见误区",
        "format": lambda c: c["pitfall"],
    },
]


def run_quiz():
    """概念测验模式"""
    print_header("📝 概念测验")
    print("  题目描述一个概念的特征/例子/误区，你回答概念名称。")
    print("  输入 'hint' 看提示，'skip' 跳过，'quit' 退出。")

    concepts_list = list(CONCEPTS.keys())
    random.shuffle(concepts_list)

    score = 0
    total = 0

    for key in concepts_list:
        concept = CONCEPTS[key]
        qtype = random.choice(QUIZ_TYPES)
        question = qtype["format"](concept)
        answer = concept["name"]

        total += 1
        print(f"\n  ─── 第 {total} 题 ({qtype['prompt']}) ───")
        print(f"\n  {question}")
        print()

        while True:
            user_input = input("  > ").strip().lower()
            if user_input == "quit":
                print(f"\n  📊 得分: {score}/{total - 1}")
                return
            elif user_input == "skip":
                print(f"  💡 答案是: {answer}")
                break
            elif user_input == "hint":
                cat = CATEGORIES[concept["category"]]
                print(f"  🔍 分类提示: {cat}")
                continue

            # 模糊匹配
            # 检查用户输入是否匹配概念的关键词
            concept_id = concept["name"].split("（")[0].lower()
            alt_keys = [k.lower() for k in key.split("_") if k.lower() != concept_id]
            if user_input == concept_id or user_input in alt_keys or any(
                word in user_input for word in [concept_id, *concept["name"].lower().split("（")[0].split()]
            ):
                # 严格的完全匹配验证
                norm_input = (
                    user_input.lower()
                    .replace("智能体", "agent")
                    .replace("提示词", "prompt")
                    .replace("提示工程", "prompt")
                    .replace("工作流", "workflow")
                    .replace("工具调用", "tool use")
                    .replace("工具使用", "tool use")
                    .replace("护栏", "guardrails")
                    .replace("人在回路", "human-in-the-loop")
                    .replace("检索增强生成", "rag")
                    .replace("上下文", "context window")
                    .replace("外部账户", "eoa")
                    .replace("智能账户", "smart account")
                    .replace("多签", "multisig")
                    .replace("智能体钱包", "agent wallet")
                    .replace("智能钱", "agent wallet")
                )
                correct_keywords = [concept_id, *key.split("_")]
                if any(kw in norm_input for kw in correct_keywords):
                    score += 1
                    print(f"  ✅ 正确！({score}/{total})")
                    break
                else:
                    print(f"  ❌ 不对，再想想？(输入 'hint' 或 'skip')")
            else:
                print(f"  ❌ 不对，再想想？(输入 'hint' 或 'skip')")

    # 结束
    print(f"\n  ═══ 完成！═══")
    pct = int(score / total * 100) if total > 0 else 0
    print(f"  📊 得分: {score}/{total} ({pct}%)")
    if pct == 100:
        print("  🏆 满分！你对这些概念掌握得很好！")
    elif pct >= 70:
        print("  👍 不错！再复习一下不熟的概念。")
    else:
        print("  💪 继续加油！多用 explain 模式复习。")
    print()


# ── 模式 2: 概念解释 ───────────────────────────────────

def explain_concept(key: str):
    """显示单个概念的详细解释"""
    c = CONCEPTS[key]
    cat = CATEGORIES[c["category"]]

    print()
    print(f"  📌 {c['name']}")
    print(f"  🏷️  {cat}")
    print(f"  ── {c['one_liner']}")
    print()
    print(f"  📖 详细解释:")
    print(f"     {c['detail']}")
    print()
    print(f"  🎯 例子:")
    print(f"     {c['example']}")
    print()
    print(f"  ⚠️  常见误区:")
    print(f"     {c['pitfall']}")
    print()


def run_explain():
    """查阅概念解释模式"""
    print_header("📖 概念查阅")
    print("  输入概念名称查看详细解释。")

    while True:
        print("  可用概念:", ", ".join(CONCEPTS.keys()))
        choice = ask_choice("要查看哪个概念？(或 'back' 返回)", 
                          list(CONCEPTS.keys()) + ["back"])
        if choice == "back":
            return
        if choice in CONCEPTS:
            explain_concept(choice)


# ── 模式 3: 概念对比 ───────────────────────────────────

COMPARE_PAIRS = [
    ("agent", "workflow", "自主决策 vs 预设路径"),
    ("eoa", "smart_account", "私钥主权 vs 可编程主权"),
    ("eoa", "multisig", "单签 vs 多签"),
    ("smart_account", "multisig", "可编程 vs 多方共识"),
    ("llm", "rag", "纯生成 vs 检索增强"),
    ("tool_use", "mcp", "手动对接 vs 标准化协议"),
    ("agent", "human_in_the_loop", "自主 vs 人工监督"),
    ("guardrails", "human_in_the_loop", "输出约束 vs 流程约束"),
]


def run_compare():
    """概念对比模式"""
    print_header("⚖️ 概念对比")

    while True:
        print("  预设对比组:")
        for i, (a_key, b_key, summary) in enumerate(COMPARE_PAIRS, 1):
            a = CONCEPTS[a_key]["name"]
            b = CONCEPTS[b_key]["name"]
            print(f"  {i}. {a} vs {b}  —  {summary}")

        print(f"\n  也可以输入两个概念名自行对比，如: 'agent tool_use'")
        choice = ask_choice("选编号、输入概念对，或 'back' 返回",
                          [str(i) for i in range(1, len(COMPARE_PAIRS) + 1)] + ["back"])

        if choice == "back":
            return

        if choice.isdigit() and 1 <= int(choice) <= len(COMPARE_PAIRS):
            a_key, b_key, desc = COMPARE_PAIRS[int(choice) - 1]
        else:
            parts = choice.split()
            if len(parts) != 2:
                print("  ⚠️  请输入两个概念名，用空格分隔")
                continue
            a_key, b_key = parts[0].strip().lower(), parts[1].strip().lower()
            if a_key not in CONCEPTS or b_key not in CONCEPTS:
                print("  ⚠️  概念名无效，可用: " + ", ".join(CONCEPTS.keys()))
                continue

        a = CONCEPTS[a_key]
        b = CONCEPTS[b_key]

        print()
        print(f"  ⚖️ {a['name']}  vs  {b['name']}")
        print(f"  ─{'─' * 25}┬{'─' * 25}┐")
        print(f"  {'':>26s}│{'':>25s}│")
        print(f"  {a['name'][:24]:>25s} │ {b['name'][:24]:<25s}│")
        print(f"  {'─' * 25}┼{'─' * 25}┤")
        print(f"  {'一句话':>25s} │ {b['one_liner'][:24]:<25s}│")
        print(f"  {a['one_liner'][:24]:>25s} │ {'':<25s}│")
        print(f"  {'─' * 25}┼{'─' * 25}┤")
        print(f"  {'类别':>25s} │ {'类别':<25s}│")
        print(f"  {CATEGORIES[a['category']]:>25s} │ {CATEGORIES[b['category']]:<25s}│")
        print(f"  {'─' * 25}┴{'─' * 25}┘")
        print()

        # 生成对比要点总结
        print(f"  📋 对比要点:")
        print(f"  ▸ {a['name']}: {a['one_liner']}")
        print(f"  ▸ {b['name']}: {b['one_liner']}")
        print()
        print(f"  🎯 {a['name']} 例子: {a['example'][:100]}...")
        print(f"  🎯 {b['name']} 例子: {b['example'][:100]}...")
        print()

        # 一句话总结
        a_short = a["name"].split("（")[0]
        b_short = b["name"].split("（")[0]
        if a_key == "agent" and b_key == "workflow":
            conclusion = f"{a_short} 是自己决定怎么走，{b_short} 是走设计好的路"
        elif a_key == "eoa" and b_key == "smart_account":
            conclusion = f"{a_short} 是把钥匙挂脖子上，{b_short} 是指纹锁——可恢复、可限额"
        elif a_key == "eoa" and b_key == "multisig":
            conclusion = f"{a_short} 是把钥匙挂脖子上，{b_short} 是把钥匙分给几个人"
        elif a_key == "smart_account" and b_key == "multisig":
            conclusion = f"{a_short} 侧重灵活编程，{b_short} 侧重多方共识，常结合使用"
        elif a_key == "llm" and b_key == "rag":
            conclusion = f"{a_short} 用训练知识生成，{b_short} 用检索知识生成——后者更可信"
        elif a_key == "tool_use" and b_key == "mcp":
            conclusion = f"{a_short} 是'我帮你配好这个工具'，{b_short} 是'你自己发现有什么工具可用'"
        elif a_key == "agent" and b_key == "human_in_the_loop":
            conclusion = f"{a_short} 想自己做，{b_short} 在某些关键节点让你确认"
        elif a_key == "guardrails" and b_key == "human_in_the_loop":
            conclusion = f"{a_short} 是 AI 自己遵守规则，{b_short} 是遇到难题喊你来判断"
        else:
            conclusion = "两者是不同的概念维度，根据场景选择或组合使用"

        print(f"  💡 一句话: {conclusion}")
        print()
        _ = input("  按 Enter 继续...")


# ── 模式 4: 随机漫游 ───────────────────────────────────

def run_explore():
    """随机漫游模式"""
    print_header("🎲 随机漫游")
    print("  每次随机展示一个概念，可以: 展开细节 / 下一题 / 退出")
    print()

    keys = list(CONCEPTS.keys())
    random.shuffle(keys)

    for key in keys:
        concept = CONCEPTS[key]
        print(f"  🔮 {concept['name']}")
        print(f"  🏷️  {CATEGORIES[concept['category']]}")
        print(f"  ── {concept['one_liner']}")
        print()

        while True:
            action = ask_choice("[d] 展开详情  [n] 下一个  [q] 退出", ["d", "n", "q"])
            if action == "d":
                explain_concept(key)
                break
            elif action == "n":
                break
            elif action == "q":
                return

    print("  🎉 逛完全部概念了！")
    print()


# ── 模式 5: 列表 ───────────────────────────────────────

def list_concepts():
    """列出所有概念"""
    print_header("📋 概念总览")
    for cat_key, cat_name in CATEGORIES.items():
        print(f"  {cat_name}:")
        for key, c in CONCEPTS.items():
            if c["category"] == cat_key:
                print(f"    • {c['name']}")
        print()
    print(f"  共 {len(CONCEPTS)} 个概念")


# ── 主入口 ──────────────────────────────────────────────

def main():
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        mode_map = {
            "quiz": run_quiz,
            "explain": run_explain,
            "compare": run_compare,
            "explore": run_explore,
            "list": list_concepts,
        }
        if mode in mode_map:
            mode_map[mode]()
            return
        else:
            print(f"未知模式: {mode}")
            print("可用模式: quiz / explain / compare / explore / list")
            sys.exit(1)

    # 交互模式
    while True:
        print_menu()
        mode = ask_choice("选择模式 (输入数字或名称):",
                        ["1", "2", "3", "4", "5", "6",
                         "quiz", "explain", "compare", "explore", "list", "quit"])
        mode_map = {
            "1": run_quiz, "quiz": run_quiz,
            "2": run_explain, "explain": run_explain,
            "3": run_compare, "compare": run_compare,
            "4": run_explore, "explore": run_explore,
            "5": list_concepts, "list": list_concepts,
            "6": None, "quit": None,
        }
        fn = mode_map.get(mode)
        if fn is None:
            print("\n  👋 再见！继续学习吧！")
            break
        fn()


if __name__ == "__main__":
    main()
