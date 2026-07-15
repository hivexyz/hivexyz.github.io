# hivexyz.github.io

这是一个基于 Hugo 的静态博客仓库，部署目标为 GitHub Pages。

## 更新文档流程

这个仓库目前采用两层内容结构：

- Hugo 源文件放在 `content/`、`layouts/`、`static/`
- 生成后的静态站点文件会被自动同步到仓库根目录，例如 `index.html`、`posts/`、`tags/`、`css/`

这样做的原因是：仓库既保留 Hugo 源码，方便长期维护；同时也把生成后的静态文件直接提交到仓库中，兼容 GitHub Pages 仓库根目录发布和 Actions 构建发布两种模式。

### 1. 新增或修改文章

文章放在 `content/posts/` 目录，例如：

```bash
content/posts/hello-hugo.md
```

一篇文章的基本格式如下：

```md
---
title: "文章标题"
date: 2026-07-14T09:00:00+08:00
draft: false
description: "一句话摘要"
tags: ["tag1", "tag2"]
---

正文内容写在这里。
```

注意事项：

- `draft: false` 才会被正式发布
- `date` 不要写成未来时间，否则 Hugo 默认不会生成该文章
- 标签写在 `tags` 中，会自动生成标签页

### 2. 本地预览

如果本机安装了 Hugo：

```bash
hugo server -D
```

如果没有全局安装 Hugo，可以使用：

```bash
npx hugo-cli@latest server -D
```

本地预览地址：

```bash
http://localhost:1313/
```

### 3. 生成静态页面

修改完内容后，可以先在本地重新构建静态站点确认结果：

如果本机安装了 Hugo：

```bash
hugo --minify
```

如果没有全局安装 Hugo：

```bash
npx hugo-cli@latest --minify
```

构建结果会输出到：

```bash
public/
```

### 4. 是否需要手工同步到仓库根目录

正常情况下，不需要手工同步。推送到 `main` 后：

- `Deploy Hugo site to Pages` 会直接把 `public/` 发布到 GitHub Pages
- `Sync generated site to repository root` 会把生成后的静态文件自动提交回仓库根目录

只有在你想本地预览“最终提交到根目录的产物”时，才需要手工执行：

```bash
cp -R public/* .
```

执行后，下面这些文件或目录会被更新：

- `index.html`
- `index.xml`
- `posts/`
- `tags/`
- `categories/`
- `css/`
- `images/`
- `sitemap.xml`

如果只想发布内容，直接提交源文件即可；自动 workflow 会负责构建和同步。

### 5. 提交并推送

建议按下面顺序检查和提交：

```bash
git status
git add content layouts static .github/workflows README.md .nojekyll
git commit -m "Update blog content"
git push origin main
```

推送后：

- `.github/workflows/hugo.yml` 会构建 `public/` 并发布到 GitHub Pages
- `.github/workflows/sync-static-to-root.yml` 会把 `public/` 中的产物自动同步到仓库根目录

### 6. 发布后验证

至少检查下面几个地址：

```bash
https://hivexyz.github.io/
https://hivexyz.github.io/posts/
https://hivexyz.github.io/posts/你的文章slug/
```

如果你不确定文章的 URL，可以看 Hugo 生成后的目录，例如：

```bash
public/posts/
```

或者直接查看生成文件：

```bash
public/posts/hello-hugo/index.html
```

### 7. 常见问题

`文章没有出现在首页或文章列表`

- 先检查 front matter 里是否写了 `draft: false`
- 再检查 `date` 是否是未来时间
- 最后确认是否执行了 `hugo --minify` 和 `cp -R public/* .`

`本地预览正常，但线上没更新`

- 检查是否已经 `git push origin main`
- 检查 GitHub Actions 里的 `Deploy Hugo site to Pages` 是否成功
- 检查 GitHub Actions 里的 `Sync generated site to repository root` 是否成功
- 如果文章使用 page bundle 图片，确认图片和 `index.md` 在同一个目录中，例如 `content/posts/foo/index.md` 与 `content/posts/foo/image.png`

`文章页 404`

- 通常是因为没有同步 `public/` 到仓库根目录
- 或者文章 slug 对应的目录没有生成成功

## 本地开发

如果本机安装了 Hugo，可直接运行：

```bash
hugo server -D
```

如果没有全局安装，也可以临时使用 npm 拉起：

```bash
npx hugo-cli@latest server -D
```

默认访问地址为 `http://localhost:1313/`。

## 发布方式

推送到 `main` 分支后：

- `.github/workflows/hugo.yml` 会自动构建并发布到 GitHub Pages
- `.github/workflows/sync-static-to-root.yml` 会自动把构建产物同步回仓库根目录

仓库建议配置：

1. GitHub 仓库 `Settings > Pages > Build and deployment` 选择 `GitHub Actions`
2. 保持默认发布分支为 `main`
3. 不要再手工编辑仓库根目录下的 `posts/`、`tags/`、`categories/`、`images/` 等生成文件

## 目录结构

- `content/`: 文章与页面内容
- `layouts/`: Hugo 模板
- `static/`: 静态资源
- `public/`: Hugo 本地构建产物目录
- `posts/`、`tags/`、`categories/`、`css/`: 已提交到仓库根目录的线上静态页面
- `.github/workflows/hugo.yml`: GitHub Pages 自动部署工作流
