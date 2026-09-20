---
title: "WSL2 + Windows 远程 Chrome 排查"
sidebarTitle: "WSL2 远程 Chrome"
---

# WSL2 + Windows 远程 Chrome 排查

很多开发者会这样部署：

- OpenClaw Gateway 跑在 WSL2 里。
- Chrome 跑在 Windows 里。
- 控制 UI 从 Windows 浏览器打开。
- Agent 想通过 CDP 控制 Windows Chrome。

这条链路跨了两个环境，所以排查时要分层看。

---

## 推荐架构

```text
Windows 浏览器打开 Control UI
        |
        v
WSL2 Gateway 127.0.0.1:18789
        |
        v
Windows Chrome CDP 9222
```

关键点是：WSL2 必须能访问 Windows Chrome 暴露出来的 CDP 地址。

---

## 第 1 层：Windows Chrome 是否开了 CDP

在 Windows 里启动 Chrome：

```powershell
chrome.exe --remote-debugging-port=9222
```

然后在 Windows 里测试：

```powershell
curl http://127.0.0.1:9222/json/version
curl http://127.0.0.1:9222/json/list
```

如果 Windows 自己都访问不了，先别改 OpenClaw。

---

## 第 2 层：WSL2 能否访问 Windows

在 WSL2 里测试你准备写进配置的地址：

```bash
curl http://WINDOWS_HOST_OR_IP:9222/json/version
curl http://WINDOWS_HOST_OR_IP:9222/json/list
```

能返回 JSON，才说明网络层通了。

如果不通，常见原因是：

- Windows 防火墙拦了。
- 地址写错。
- Chrome 只监听了 Windows 本机。
- WSL2 到 Windows 的网络路由没配好。

---

## 第 3 层：配置 OpenClaw profile

示意配置：

```json5
{
  browser: {
    enabled: true,
    defaultProfile: "remote",
    profiles: {
      remote: {
        cdpUrl: "http://WINDOWS_HOST_OR_IP:9222",
        attachOnly: true
      }
    }
  }
}
```

`cdpUrl` 要写 WSL2 能访问的地址，不一定是 Windows 里能访问的 `127.0.0.1`。

---

## 控制 UI 地址也要正确

Windows 上打开控制台时，优先用：

```text
http://127.0.0.1:18789/
```

不要随手用 LAN IP。普通 HTTP 的 LAN 地址可能触发浏览器安全限制，让你误以为是 CDP 坏了。

---

## 继续阅读

- [浏览器工具](/tutorials/tools/browser)
- [浏览器控制 API](/tutorials/tools/browser-control)
- [Web 控制 UI](/tutorials/web/)

