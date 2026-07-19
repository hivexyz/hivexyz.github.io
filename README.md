# hivexyz.github.io

基于 [Hugo](https://gohugo.io/) 的静态博客，使用 [PaperMod](https://github.com/adityatelange/hugo-PaperMod) 主题，部署到 GitHub Pages。

## 怎么用

### 1. 本地预览

首次克隆仓库后，先拉取主题子模块：

```bash
git submodule update --init --recursive
```

如果本机已安装 Hugo：

```bash
hugo server -D
```

如果没有安装 Hugo，可以直接用：

```bash
npx hugo-extended server -D
```

如果本机 `~/.npm` 缓存权限有问题，可以改用临时缓存目录：

```bash
npx --cache /private/tmp/npm-cache hugo-extended server -D
```

默认预览地址：

```
http://localhost:1313/
```

### 2. 新建一篇文章

普通纯文本文章可以直接创建：

```
content/posts/hello-hugo.md
```

如果文章里要放图片，必须使用 Hugo Page Bundle，也就是给这篇文章单独建目录。这个仓库已经提供了辅助脚本：

```bash
python3 scripts/create_post_dirs.py 2026q3/文章名
```

执行后会创建目录，并自动生成一个带 front matter 的 `index.md` 模板。

会创建：

```
content/posts/2026q3/文章名/
content/posts/2026q3/文章名/index.md
```

模板内容如下，`date` 会自动写入脚本执行时的当前时间：

```md
---
title: ""
date: 2026-07-19T12:00:56+0800
draft: false
description: ""
tags: ["", ""]
---
```

然后你只需要把图片放到同目录，例如：

```
content/posts/2026q3/文章名/image.png
```

推荐文章结构如下：

```
content/posts/2026q3/文章名/
├── index.md
└── image.png
```

### 3. 文章模板

`index.md` 或普通 Markdown 文章可以使用下面的 front matter：

```md
---
title: "文章标题"
date: 2026-07-19T09:00:00+08:00
draft: false
description: "一句话摘要"
tags: ["tag1", "tag2"]
---
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
npx hugo-extended --minify
```

如果 npm 缓存权限有问题：

```bash
npx --cache /private/tmp/npm-cache hugo-extended --minify
```

构建产物会输出到：

```
public/
```

你可以重点检查：

```
public/posts/
public/posts/你的文章路径/index.html
```

如果是带图文章，还要确认图片是否真的生成出来了，例如：

```
public/posts/2026q3/文章名/image.png
```

### 6. 发布

正常发布时，提交源文件即可：

```bash
git status
git add content static scripts .github README.md .nojekyll scripts
git commit -m "Update blog content"
git push origin main
```

推送后 GitHub Actions 自动构建并发布到 GitHub Pages。

### 7. 发布后检查

至少检查这几个地址：

```
https://hivexyz.github.io/
https://hivexyz.github.io/posts/
https://hivexyz.github.io/posts/你的文章路径/
```

如果文章里有图片，再检查图片是否能打开。

## 当前推荐工作流

以后写文章建议固定按这个顺序：

1. 如果有图片，先执行 `python3 scripts/create_post_dirs.py 2026q3/文章名`
2. 修改脚本自动生成的 `index.md`
3. 把图片直接放到同目录
4. 本地运行 `hugo server -D` 或 `npx hugo-extended server -D`
5. 确认页面和图片都正常
6. `git add` 后提交并推送
7. 到 GitHub Actions 检查 workflow 都成功

## 常见问题

### 本地能看到，线上图片不显示

优先检查这几个点：

- 图片是否和 `index.md` 在同一个目录
- Markdown 是否写成了 `![alt](image.png)` 这种相对路径
- 是否只提交了 `index.md`，却没提交图片文件
- GitHub Actions 里的构建是否成功

### 文章没有出现在首页

一般是下面几个原因：

- `draft: true`
- `date` 写成未来时间
- 文章放错目录

### 想知道文章最终 URL

可以直接看构建结果目录，例如：

```
public/posts/
```

如果文件在：

```
public/posts/2026q3/文章名/index.html
```

那么页面地址通常就是：

```
https://hivexyz.github.io/posts/2026q3/文章名/
```

### 主题配置

PaperMod 主题配置在 `hugo.toml` 中，支持搜索、目录、代码复制等功能。详细选项可参考 [PaperMod 文档](https://github.com/adityatelange/hugo-PaperMod/wiki)。

## 目录说明

| 目录 | 用途 |
|------|------|
| `content/` | 文章源文件 |
| `themes/PaperMod/` | PaperMod 主题（git submodule） |
| `static/` | 全站静态资源 |
| `assets/` | 自定义样式/脚本（Hugo Pipes 处理） |
| `scripts/` | 辅助脚本 |
| `public/` | 本地 Hugo 构建结果 |
| `.github/workflows/` | CI/CD 配置 |

## 仓库配置要求

GitHub 仓库里要确认：

1. `Settings > Pages > Build and deployment` 选择 `GitHub Actions`
2. 默认分支是 `main`
3. 不要手工编辑仓库根目录下的 `posts/`、`tags/`、`categories/` 等生成文件
