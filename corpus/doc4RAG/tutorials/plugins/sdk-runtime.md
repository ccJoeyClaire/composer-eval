---
title: "SDK Runtime"
sidebarTitle: "SDK Runtime"
---

# SDK Runtime

runtime 是插件真正注册能力的地方。manifest 只是身份证，runtime 才是工作现场。

runtime 可能注册：

- tools。
- channels。
- providers。
- hooks。
- capability implementations。

runtime 代码要小心处理错误。插件加载失败不应该把用户搞得一头雾水。

## 新手写法建议

runtime 入口只做注册，不要一加载就做重活。
比如 provider 插件可以先注册 provider，真正发 API 请求时再初始化客户端。

这样 Gateway 启动更快，插件出错也更容易定位。
