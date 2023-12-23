# 配置文件

## 索引文件 `indexes.json`

```json
[
    {
        "PageIndex": "页面的路径，网页路径 /Wiki/[PageIndex]",
        "Title": "标题（可有可无）",
        "FileName": "Markdown 文件路径，对应服务器中 ./pages/[FileName]"
    },
    {
        "PageIndex": "页面的路径，网页路径 /Wiki/[PageIndex]",
        "Title": "标题（可有可无）",
        "FileName": "Markdown 文件路径，对应服务器中 ./pages/[FileName]"
    },
    ......
]
```

**例如：**

```json
[
    {
        "PageIndex": "/",
        "Title": "主页",
        "FileName": "home.md"
    },
    {
        "PageIndex": "/FileConfig",
        "FileName": "config.md"
    }
]
```

此时，服务端文件结构应该为这样：

```
|----pages // 页面文件夹
|---|
|---|---home.md
|---|---config.md
|
|---app.py // 服务器文件
|---indexes.json // 索引文件
```

然后访问 `/Wiki/` 会访问 `home.md`

访问 `/Wiki/FileConfig` 会访问 `config.md`

