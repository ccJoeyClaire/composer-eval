---
title: "Web Fetch"
sidebarTitle: "网页抓取"
---

# Web Fetch：读取一个网页正文

`web_fetch` 做的事情很简单：给它一个 URL，它去下载页面，然后尽量提取正文。

它和浏览器不同。`web_fetch` 不执行 JavaScript。

---

## 适合什么？

适合：

- 读取文章。
- 抓取文档页正文。
- 提取普通 HTML 页面内容。
- 快速查看一个链接在讲什么。

不适合：

- 登录后页面。
- 需要点击后才出现的内容。
- JavaScript 重度渲染的 SPA。
- 需要截图或交互的网页。

这些情况用 [浏览器工具](/tutorials/tools/browser)。

---

## 默认可用

`web_fetch` 默认开启，通常不需要额外配置。

工具内部会：

1. 发 HTTP GET。
2. 检查重定向和私有地址风险。
3. 用 Readability 提取正文。
4. 必要时使用 Firecrawl 回退。
5. 缓存短时间结果，减少重复抓取。

---

## 常见参数

| 参数 | 说明 |
|------|------|
| `url` | 要读取的网页 |
| `extractMode` | 输出 markdown 或 text |
| `maxChars` | 最多返回多少字符 |

---

## Firecrawl 回退

如果普通提取失败，而且你配置了 Firecrawl，OpenClaw 可以让 Firecrawl 帮忙处理更难抓的页面。

适合：

- 反爬较强的页面。
- 正文提取失败的页面。
- 需要更干净结构化内容的页面。

---

## 继续阅读

- [Web 网络工具](/tutorials/tools/web)
- [Firecrawl](/tutorials/tools/firecrawl)
- [浏览器工具](/tutorials/tools/browser)

