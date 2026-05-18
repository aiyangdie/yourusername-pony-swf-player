<div align="center">

# 🎀 小马宝莉 SWF 播放器

**可爱风格 SWF 文件播放器 — 粉色主题，彩虹元素，少女心满满**

[![GitHub](https://img.shields.io/badge/GitHub-Project-blue?logo=github)](https://github.com/aiyangdie/yourusername-pony-swf-player)
[![Python](https://img.shields.io/badge/Python-3.6+-3776AB?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## 📌 项目简介

小马宝莉 SWF 播放器是一款专为小马宝莉粉丝设计的桌面端 SWF 文件播放工具。采用 Python Tkinter 构建可爱粉色主题界面，支持双模式播放——优先使用系统默认程序打开，自动降级到浏览器 + Ruffle Flash 模拟器兼容模式。附带彩虹鬃毛小马图标，少女心满满。

---

## ✨ 核心特性

- 🎨 **小马宝莉风格界面** — 粉色渐变配色、Comic Sans MS 字体、Emoji 装饰
- 📁 **一键文件选择** — 浏览并选择本地 SWF 文件
- 🎬 **智能双模式播放**
  - 模式一：系统默认程序直接播放（Windows 优先）
  - 模式二：自动生成 HTML + Ruffle 模拟器在浏览器中播放（兼容降级）
- 📋 **实时状态反馈** — 清晰显示当前操作状态
- 📝 **完整日志记录** — 详细记录播放过程，方便排查问题
- 🖼️ **精美小马图标** — Pillow 程序化生成的彩虹鬃毛小马 ICO 图标
- 💻 **跨平台支持** — 兼容 Windows、macOS、Linux
- 📦 **可打包为 EXE** — 支持 PyInstaller 打包为独立可执行文件

---

## 🛠️ 技术栈

| 技术 | 用途 |
|------|------|
| Python 3.6+ | 主开发语言 |
| Tkinter | GUI 框架（Python 内置） |
| Ruffle | 开源 Flash 模拟器（CDN 加载） |
| Pillow | ICO 图标程序化生成 |
| PyInstaller | 打包为独立 EXE 可执行文件 |
| subprocess | 系统默认程序调用 |
| webbrowser | 浏览器启动控制 |
| tempfile | 临时 HTML 文件生成 |

---

## 🚀 快速开始

### 前置条件

- Python 3.6 及以上版本
- 现代浏览器（支持 WebAssembly，用于 Ruffle 模式）
- 网络连接（Ruffle 模式需要加载 CDN 资源）

### 安装步骤

```bash
git clone https://github.com/aiyangdie/yourusername-pony-swf-player.git
cd yourusername-pony-swf-player
pip install -r requirements.txt
```

### 运行命令

```bash
python swf_player_gui.py
```

### 打包为 EXE（可选）

```bash
# 目录模式（推荐，体积小约 1.7MB）
pyinstaller --onedir --windowed --icon=pony_icon.ico swf_player_gui.py

# 单文件模式（包含所有依赖，约 10MB）
pyinstaller --onefile --windowed --icon=pony_icon.ico swf_player_gui.py
```

### 生成图标（可选）

```bash
python create_icon.py
```

---

## 📂 项目结构

```
yourusername-pony-swf-player/
├── swf_player_gui.py      # 主程序（Tkinter GUI + 播放逻辑）
├── create_icon.py          # 图标生成脚本（Pillow 绘制小马图标）
├── pony_icon.ico           # 小马宝莉风格图标
├── requirements.txt        # 项目依赖
├── .gitignore              # Git 忽略配置
└── README.md               # 项目说明文档
```

---

## 🎨 界面配色

| 颜色 | 色值 | 用途 |
|------|------|------|
| 浅粉色 | `#FFE4E1` | 主背景 |
| 中粉色 | `#FFB6C1` | 按钮背景 |
| 深粉色 | `#FF69B4` | 标题栏 / 强调色 |
| 浅紫色 | `#E6E6FA` | 辅助背景 |
| 中紫色 | `#DDA0DD` | 退出按钮 |
| 深紫色 | `#8B008B` | 文字颜色 |

---

## 🤝 贡献与许可证

欢迎小马宝莉粉丝和开发者贡献代码！

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/CuteFeature`
3. 提交更改：`git commit -m 'Add some cute feature'`
4. 推送到分支：`git push origin feature/CuteFeature`
5. 开启 Pull Request

本项目采用 **MIT License** 开源协议，详情请见 [LICENSE](LICENSE) 文件。

---

<div align="center">

🎀 享受你的小马宝莉 SWF 播放之旅！🎀

Created with ❤️ for My Little Pony fans!

</div>
