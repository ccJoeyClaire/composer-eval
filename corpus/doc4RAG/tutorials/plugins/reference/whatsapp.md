---
title: "WhatsApp plugin"
---

# WhatsApp plugin

::: tip 先看人话
这页是从 OpenClaw 官方最新文档同步来的专题参考。新手不要一口气背完，先看标题和第一段；真正要配置这个功能时，再按步骤慢慢做。
:::

Adds the WhatsApp channel surface for sending and receiving OpenClaw messages.

## Distribution

- Package: `@openclaw/whatsapp`
- Install route: npm; ClawHub

## Surface

channels: whatsapp

## Windows install note

On Windows, the WhatsApp plugin needs Git on `PATH` during npm install because one of its Baileys/libsignal dependencies is fetched from a git URL. Install Git for Windows, then restart the shell and rerun the install:

```powershell
winget install --id Git.Git -e
```

Portable Git also works if its `bin` directory is on `PATH`.

## Related docs

- [whatsapp](/tutorials/channels/whatsapp)
