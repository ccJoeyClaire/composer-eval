---
title: "社区插件"
sidebarTitle: "社区插件"
---

# 社区插件

社区插件能让 OpenClaw 接入更多服务，但也要注意信任边界。

安装前问自己：

- 作者是谁？
- 插件要哪些权限？
- 会不会读取消息内容？
- 会不会执行命令？
- 会不会保存或转发密钥？

对不熟悉的插件，先在测试 Gateway 里试。

## 安装前检查

```bash
openclaw plugins inspect <id>
openclaw security audit
```

## 新手提醒

插件就是代码。安装插件等于允许别人写的代码在你的 OpenClaw 环境里运行。
来历不清、权限过大、要求关闭安全检查的插件，都要格外小心。
