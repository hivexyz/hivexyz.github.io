# hivexyz.github.io

这是一个基于 Hugo 的静态博客仓库，部署到 GitHub Pages。

当前仓库保留两类内容：

- Hugo 源文件：`content/`、`layouts/`、`static/`
- 生成后的静态站点：仓库根目录下的 `index.html`、`posts/`、`tags/`、`css/`、`images/`

推送到 `main` 后，GitHub Actions 会做两件事：

- 用 Hugo 构建 `public/` 并发布到 GitHub Pages
- 把生成结果自动同步回仓库根目录，保证仓库里的静态文件和线上一致

## 怎么用

### 1. 本地预览

如果本机已安装 Hugo：

```bash
hugo server -D
```

如果没有安装 Hugo，可以直接用：

```bash
npx hugo-cli@latest server -D
```

如果本机 `~/.npm` 缓存权限有问题，可以改用临时缓存目录：

```bash
npx --cache /private/tmp/npm-cache hugo-cli@latest server -D
```

默认预览地址：

```bash
http://localhost:1313/
```

### 2. 新建一篇文章

普通纯文本文章可以直接创建：

```bash
content/posts/hello-hugo.md
```

如果文章里要放图片，必须使用 Hugo Page Bundle，也就是给这篇文章单独建目录。这个仓库已经提供了辅助脚本：

```bash
python scripts/create_post_dirs.py 2026q3/my-post
```

执行后会创建：

```bash
content/posts/2026q3/my-post/
```

然后在这个目录下新增：

```bash
content/posts/2026q3/my-post/index.md
content/posts/2026q3/my-post/image.png
```

推荐文章结构如下：

```text
content/posts/2026q3/my-post/
├── index.md
└── image.png
```

### 3. 文章模板

`index.md` 或普通 Markdown 文章可以使用下面的 front matter：

```md
---
title: "文章标题"
date: 2026-07-15T09:00:00+08:00
draft: false
description: "一句话摘要"
tags: ["tag1", "tag2"]
---

正文内容写在这里。
```

注意：

- `draft: false` 才会发布
- `date` 不要写成未来时间，否则文章默认不会生成
- `tags` 会自动生成标签页

### 4. 图片怎么写

如果文章使用 Page Bundle，图片要和 `index.md` 放在同一个目录，Markdown 里直接写相对路径：

```md
![封面图](image.png)
```

正文里的图片会自动按文章内容区宽度缩放，在桌面端和手机端都会保持比例，不会再撑破版心。

不要写成：

```md
![封面图](/images/xxx.png)
```

也不要手工去改仓库根目录下 `posts/` 里的 HTML。正确做法是只维护 `content/posts/...` 里的源文件和图片。

### 5. 本地构建

如果你想先确认最终生成结果，可以手工构建：

```bash
hugo --minify
```

如果没有安装 Hugo：

```bash
npx hugo-cli@latest --minify
```

如果 npm 缓存权限有问题：

```bash
npx --cache /private/tmp/npm-cache hugo-cli@latest --minify
```

构建产物会输出到：

```bash
public/
```

你可以重点检查：

```bash
public/posts/
public/posts/你的文章路径/index.html
```

如果是带图文章，还要确认图片是否真的生成出来了，例如：

```bash
public/posts/2026q3/my-post/image.png
```

### 6. 发布

正常发布时，不需要手工执行 `cp -R public/* .`。只需要提交源文件即可：

```bash
git status
git add content layouts static .github/workflows README.md .nojekyll scripts
git commit -m "Update blog content"
git push origin main
```

推送后：

- `.github/workflows/hugo.yml` 会构建并发布 GitHub Pages
- `.github/workflows/sync-static-to-root.yml` 会自动把生成产物提交回仓库根目录

### 7. 发布后检查

至少检查这几个地址：

```bash
https://hivexyz.github.io/
https://hivexyz.github.io/posts/
https://hivexyz.github.io/posts/你的文章路径/
```

如果文章里有图片，再检查图片是否能打开。

## 当前推荐工作流

以后写文章建议固定按这个顺序：

1. 如果有图片，先执行 `python scripts/create_post_dirs.py 2026q3/文章名`
2. 在新目录里写 `index.md`
3. 把图片直接放到同目录
4. 本地运行 `hugo server -D` 或 `npx --cache /private/tmp/npm-cache hugo-cli@latest server -D`
5. 确认页面和图片都正常
6. `git add` 后提交并推送
7. 到 GitHub Actions 检查两个 workflow 都成功

## 常见问题

### 本地能看到，线上图片不显示

优先检查这几个点：

- 图片是否和 `index.md` 在同一个目录
- Markdown 是否写成了 `![alt](image.png)` 这种相对路径
- 是否只提交了 `index.md`，却没提交图片文件
- GitHub Actions 里的 `Deploy Hugo site to Pages` 是否成功
- GitHub Actions 里的 `Sync generated site to repository root` 是否成功

### 文章没有出现在首页

一般是下面几个原因：

- `draft: true`
- `date` 写成未来时间
- 文章放错目录

### 想知道文章最终 URL

可以直接看构建结果目录，例如：

```bash
public/posts/
```

如果文件在：

```bash
public/posts/2026q3/my-post/index.html
```

那么页面地址通常就是：

```bash
https://hivexyz.github.io/posts/2026q3/my-post/
```

## 仓库配置要求

GitHub 仓库里要确认：

1. `Settings > Pages > Build and deployment` 选择 `GitHub Actions`
2. 默认分支是 `main`
3. 不要手工编辑仓库根目录下的 `posts/`、`tags/`、`categories/`、`images/` 等生成文件

## 目录说明

- `content/`: 文章源文件
- `layouts/`: Hugo 模板
- `static/`: 全站静态资源
- `scripts/create_post_dirs.py`: 创建带图片文章目录的辅助脚本
- `public/`: 本地 Hugo 构建结果
- `posts/`、`tags/`、`categories/`、`css/`、`images/`: 已同步到仓库根目录的生成产物
- `.github/workflows/hugo.yml`: GitHub Pages 发布 workflow
- `.github/workflows/sync-static-to-root.yml`: 生成产物自动同步 workflow
