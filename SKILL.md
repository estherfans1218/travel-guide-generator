---
name: travel-guide-generator
description: 旅游攻略生成器。当用户想生成某个目的地（城市/地区/国家/线路）的旅游攻略时使用此技能。典型触发：用户说出一个地名并希望得到攻略，例如"帮我生成成都的旅游攻略""做个日本东京攻略""我要川西路线攻略""XX 几天怎么玩"。该技能联网搜索（优先参考小红书热门推荐）目的地的实时信息，默认生成攻略正文（Markdown，含图片占位符）。当用户明确用于闲鱼等平台售卖时，可选生成上架文案和差异化补充清单。支持设置出发地、到达/离开时间与交通方式。跨平台通用，详见 AGENT_GUIDE.md。
agent_created: true
---

# 旅游攻略生成器

本技能的完整工作指令见同目录 `AGENT_GUIDE.md`。触发时请先读取该文件，并按其流程执行旅游攻略生成。

参考资料在 `references/` 目录下：
- `references/search-strategy.md` — 联网搜索策略（小红书优先）
- `references/guide-structure.md` — 攻略标准结构与图片占位符规范
- `references/listing-copy.md` — 闲鱼上架文案（售卖模式用）

本技能跨平台通用（WorkBuddy / Claude Code / Codex / Cursor / Trae 等），各 agent 的使用方式见 `AGENT_GUIDE.md` 和 `README.md`。
