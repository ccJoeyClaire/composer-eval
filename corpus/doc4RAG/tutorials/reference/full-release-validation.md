---
title: "Full Release Validation"
sidebarTitle: "完整发布验证"
---

# Full Release Validation

完整发布验证是维护者在发布前确认系统没有坏的清单。

可能覆盖：

- 构建。
- 单元测试。
- QA 场景。
- 真实通道冒烟。
- 安全审计。
- 文档构建。

普通用户升级后跑 `openclaw doctor` 即可。

## 维护者检查顺序

1. 构建和测试先通过。
2. CLI、Gateway、Control UI 能启动。
3. 关键插件能加载。
4. 通道冒烟不阻塞。
5. 安全和迁移检查没有高危问题。
6. 文档站能构建。

## 普通用户等价动作

你不用做完整发布验证。升级后跑：

```bash
openclaw status --all
openclaw doctor
openclaw channels status --probe
```
