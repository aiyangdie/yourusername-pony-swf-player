# 🎀 小马宝莉 SWF 播放器 🎀

一个可爱风格的SWF文件播放器，专为喜欢小马宝莉的用户设计。

## ✨ 功能特性

- 🎨 **可爱的小马宝莉风格界面**：粉色主题，彩虹元素，少女心满满
- 📁 **简单易用的文件选择**：一键选择本地SWF文件
- 🎬 **多种播放方式**：
  - 优先使用系统默认程序打开
  - 自动降级到浏览器+Ruffle模拟器
- 📋 **详细的状态反馈**：实时显示程序运行状态
- 📝 **完整的日志记录**：记录播放过程中的详细信息
- 🖼️ **美观的图标设计**：带有小马宝莉风格的图标
- 💻 **跨平台支持**：可在Windows、macOS和Linux上运行

## 📦 安装方法

### 方法一：直接下载使用（推荐）

1. 访问项目的 [GitHub Releases](https://github.com/aiyangdie/yourusername-pony-swf-player/releases) 页面
2. 下载最新版本的 `pony-swf-player.zip` 文件
3. 解压到任意目录
4. 双击 `swf_player_gui.exe` 即可运行

### 方法二：从源代码编译

1. 克隆本仓库：
   ```bash
   git clone https://github.com/aiyangdie/yourusername-pony-swf-player.git
   cd yourusername-pony-swf-player
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 运行程序：
   ```bash
   python swf_player_gui.py
   ```

4. （可选）打包成EXE文件：
   ```bash
   pyinstaller --onedir --windowed --icon=pony_icon.ico swf_player_gui.py
   ```

## 🚀 使用方法

1. 启动程序，你将看到可爱的小马宝莉风格界面
2. 点击 "🎀 选择 SWF 文件 🎀" 按钮，浏览并选择你想要播放的SWF文件
3. 点击 "✨ 播放 SWF 文件 ✨" 按钮，程序将自动选择合适的方式播放
4. 查看状态和日志信息，了解播放进度
5. 播放完成后，点击 "💤 退出播放器 💤" 按钮关闭程序

## 🛠️ 技术栈

- **编程语言**：Python 3.11.9
- **GUI框架**：Tkinter（Python内置）
- **打包工具**：PyInstaller
- **Flash模拟器**：Ruffle（通过CDN加载）
- **图标设计**：Pillow（用于生成ICO图标）

## 📁 项目结构

```
yourusername-pony-swf-player/
├── swf_player_gui.py      # 主程序文件
├── pony_icon.ico          # 小马宝莉风格ICO图标
├── README.md              # 项目说明文档
├── requirements.txt       # 项目依赖
└── .gitignore            # Git忽略文件列表
```

## 🎨 界面设计

- **主色调**：少女粉（#FF69B4）
- **辅助色**：浅粉色、紫色
- **字体**：Comic Sans MS（可爱风格）
- **图标**：小马宝莉风格，包含彩虹和星星元素
- **布局**：清晰直观，操作简便

## 📝 开发说明

### 环境要求

- Python 3.6 及以上
- Windows/macOS/Linux

### 依赖安装

```bash
pip install -r requirements.txt
```

### 运行程序

```bash
python swf_player_gui.py
```

### 打包程序

```bash
# 目录模式（推荐，较小的EXE文件）
pyinstaller --onedir --windowed --icon=pony_icon.ico swf_player_gui.py

# 单文件模式（较大的EXE文件）
pyinstaller --onefile --windowed --icon=pony_icon.ico swf_player_gui.py
```

## 🤝 贡献指南

欢迎大家贡献代码！如果你有任何改进建议或功能需求，欢迎：

1. Fork 本仓库
2. 创建你的特性分支：`git checkout -b feature/AmazingFeature`
3. 提交你的更改：`git commit -m 'Add some AmazingFeature'`
4. 推送到分支：`git push origin feature/AmazingFeature`
5. 开启一个 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 LICENSE 文件了解详情

## 🙏 致谢

- 感谢 [Ruffle](https://ruffle.rs/) 提供的Flash模拟器
- 感谢小马宝莉带来的灵感
- 感谢所有为这个项目做出贡献的人

## ❓ 常见问题

### Q: 为什么我的SWF文件无法播放？
A: 可能的原因：
1. 系统没有安装Flash播放器
2. 浏览器不支持WebAssembly
3. SWF文件损坏
4. 尝试重新启动程序或更换浏览器

### Q: 为什么程序启动后没有图标？
A: 可能是因为图标文件路径不正确。请确保 `pony_icon.ico` 文件与可执行文件在同一目录下。

### Q: 如何减小EXE文件的大小？
A: 我们推荐使用目录模式打包（`--onedir`），这样生成的EXE文件会更小。

## 📞 联系方式

如果你有任何问题或建议，欢迎通过GitHub Issues与我联系。

---

🎀 享受你的小马宝莉SWF播放之旅！🎀