# hivexyz.github.io

这是一个基于 Hugo 的静态博客仓库，部署目标为 GitHub Pages。

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

推送到 `main` 分支后，`.github/workflows/hugo.yml` 会自动构建并发布到 GitHub Pages。

仓库建议配置：

1. GitHub 仓库 `Settings > Pages > Build and deployment` 选择 `GitHub Actions`
2. 保持默认发布分支为 `main`

## 目录结构

- `content/`: 文章与页面内容
- `layouts/`: Hugo 模板
- `static/`: 静态资源
- `.github/workflows/hugo.yml`: GitHub Pages 自动部署工作流
