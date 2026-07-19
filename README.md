# hivexyz.github.io

基于 [Hugo](https://gohugo.io/) 的静态博客，使用 [PaperMod](https://github.com/adityatelange/hugo-PaperMod) 主题，通过 GitHub Actions 自动部署到 GitHub Pages。

## 本地预览

```bash
# 首次克隆后拉取主题子模块
git submodule update --init --recursive

# 启动本地预览
hugo server -D

# 没有 Hugo？用 npx
npx hugo-extended server -D
```

预览地址：http://localhost:1313/

## 发布文章

### 无图文章

在 `content/posts/` 下直接创建 Markdown 文件：

```bash
# 文件路径决定 URL：/posts/文章slug/
# 例如 content/posts/my-post.md → https://hivexyz.github.io/posts/my-post/
```

文件内容：

```md
---
title: "文章标题"
date: 2026-07-19T09:00:00+08:00
draft: false
description: "一句话摘要"
tags: ["tag1", "tag2"]
---

正文内容...
```

### 有图文章

必须使用 Hugo Page Bundle（文章独占一个目录），用辅助脚本创建：

```bash
python3 scripts/create_post_dirs.py 2026q3/my-article
```

会生成：

```
content/posts/2026q3/my-article/
└── index.md          # 自动生成的模板，需编辑
```

然后编辑 `index.md`，把图片放到同目录，Markdown 中用相对路径引用：

```
content/posts/2026q3/my-article/
├── index.md
├── cover.png
└── screenshot.png
```

```md
---
title: "文章标题"
date: 2026-07-19T09:00:00+08:00
draft: false
description: "一句话摘要"
tags: ["tag1", "tag2"]
---

正文内容...

![封面](cover.png)

更多内容...

![截图](screenshot.png)
```

**图片路径规则：**
- 正确：`![alt](image.png)` — 相对路径，和 `index.md` 同目录
- 错误：`![alt](/images/xxx.png)` — 绝对路径，Page Bundle 下不会正确打包

### 目录命名建议

按 `年份+季度/文章名` 组织，例如 `2026q3/llm-safety`，方便归档管理。

### Front Matter 说明

| 字段 | 必填 | 说明 |
|------|------|------|
| `title` | 是 | 文章标题 |
| `date` | 是 | 发布时间，不要写未来时间否则文章不会生成 |
| `draft` | 是 | `false` 才会发布，`true` 为草稿 |
| `description` | 否 | 一句话摘要，显示在文章列表 |
| `tags` | 否 | 标签数组，自动生成标签页 |

## 发布流程

```
1. 写文章（无图直接建 .md，有图用脚本建 Page Bundle）
2. hugo server -D 本地预览确认
3. git add content/ && git commit -m "新增文章：xxx"
4. git push origin main
5. GitHub Actions 自动构建部署，等约 1 分钟
6. 检查 https://hivexyz.github.io/posts/你的文章路径/
```

## 目录结构

```
content/posts/          # 文章源文件
  hello-hugo.md         # 无图文章（单文件）
  2026q3/test_img/      # 有图文章（Page Bundle）
    index.md
    image.png
themes/PaperMod/        # PaperMod 主题（git submodule）
assets/css/extended/    # 自定义样式覆盖
layouts/partials/       # 自定义模板覆盖
scripts/                # 辅助脚本
.github/workflows/      # CI/CD（hugo.yml）
hugo.toml               # Hugo 配置
```

## 常见问题

### 本地能看到，线上图片不显示

- 图片是否和 `index.md` 在同一目录
- Markdown 是否用了 `![alt](image.png)` 相对路径
- 图片文件是否已 `git add` 并提交

### 文章没有出现在首页

- `draft` 是否为 `false`
- `date` 是否写成未来时间
- 文件是否放在 `content/posts/` 下

### 想知道文章 URL

文件路径 `content/posts/2026q3/my-article/index.md` 对应 URL：

```
https://hivexyz.github.io/posts/2026q3/my-article/
```

## 仓库配置

GitHub 仓库需确认：
1. `Settings > Pages > Build and deployment > Source` 选择 **GitHub Actions**
2. 默认分支为 `main`
3. 不要手动编辑仓库根目录下的 `posts/`、`tags/`、`categories/` 等生成文件
