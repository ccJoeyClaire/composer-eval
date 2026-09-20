---
title: "Exec Approvals Advanced"
sidebarTitle: "高级执行审批"
---

# 高级执行审批：safeBins、解释器和转发审批

基础执行审批请先看 [执行审批](/tutorials/tools/exec-approvals)。这一页只讲进阶配置。

---

## safeBins 是什么？

`safeBins` 是一小组只允许处理 stdin 的低风险命令，例如：

```text
cut
uniq
head
tail
tr
wc
```

它们适合做文本流处理，比如把上一条命令输出截取前几行。

---

## 不要把解释器放进 safeBins

不要把这些放进 safeBins：

```text
python3
node
ruby
bash
sh
zsh
```

原因很简单：解释器可以执行代码、读文件、调用子命令。它们不是“安全小工具”，而是“万能工具箱”。

这类命令应该走明确 allowlist 和审批。

---

## trusted dirs

safeBins 只应该从可信目录解析，比如：

```text
/bin
/usr/bin
```

如果你的命令在 Homebrew、Snap 或其他目录，需要显式配置可信路径。不要自动信任整个 `PATH`。

---

## 审批转发

团队环境里，执行审批可以转发到 Slack、Discord、Telegram 等通道，让负责人确认。

适合：

- Gateway 在服务器上。
- 操作者不在机器旁边。
- 需要审计谁批准了什么。

---

## 新手建议

如果你不确定某个命令安全不安全，就不要放进 safeBins。
宁愿多一次审批，也不要让 Agent 获得过大的默认命令权限。

---

## 继续阅读

- [执行审批](/tutorials/tools/exec-approvals)
- [Exec 命令工具](/tutorials/tools/exec)
- [Gateway 安全说明](/tutorials/gateway/security)

