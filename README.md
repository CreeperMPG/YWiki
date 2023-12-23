# YWiki - 一个精简到极致的 Wiki Pages 管理系统

## 部署教程

下载此仓库，然后 `python3 app.py` 即可。

## 页面更新教程

*过后会有网页端修改 Wiki 内容的功能*

先在 `indexes.json` 编辑索引：

```json
[
    {
        "PageIndex": "/",
        "Title": "主页",
        "FileName": "home.md"
    },
    {
        "PageIndex": "/AboutUs",
        "Title": "关于",
        "FileName": "about.md"
    }
]
```

然后在服务端的 `pages` 文件夹中放入 `home.md` 和 `about.md` 即可。

这样访问 `/Wiki/` 会显示 `home.md`；访问 `/Wiki/AboutUs` 会显示 `about.md`。