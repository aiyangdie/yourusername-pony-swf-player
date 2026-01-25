# 🎀 小马宝莉 SWF 播放器 🎀

一个专为小马宝莉粉丝设计的可爱风格SWF文件播放器，粉色主题，彩虹元素，少女心满满！

## ✨ 功能特性

- 🎨 **可爱的小马宝莉风格界面**：粉色渐变背景，彩虹装饰，星星点缀
- 📁 **简单易用的文件选择**：一键浏览并选择本地SWF文件
- 🎬 **智能播放方式**：
  - 优先使用系统默认程序流畅播放
  - 自动降级到浏览器+Ruffle模拟器兼容模式
- 📋 **实时状态反馈**：清晰显示程序运行状态
- 📝 **完整日志记录**：详细记录播放过程，方便调试
- 🖼️ **精美小马宝莉图标**：彩虹鬃毛小马头像图标
- 💻 **跨平台支持**：兼容Windows、macOS和Linux
- 🎉 **无广告纯净体验**：专注于SWF播放，无任何广告

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

1. 启动程序，看到可爱的小马宝莉风格界面
2. 点击 "🎀 选择 SWF 文件 🎀" 按钮
3. 浏览并选择你想要播放的SWF文件
4. 点击 "✨ 播放 SWF 文件 ✨" 按钮
5. 查看状态和日志信息，了解播放进度
6. 播放完成后，点击 "💤 退出播放器 💤" 按钮关闭程序

## 🎨 界面预览

- **主色调**：少女粉 (#FF69B4)
- **辅助色**：浅粉色 (#FFE4E1)、中粉色 (#FFB6C1)、紫色 (#DDA0DD)
- **字体**：Comic Sans MS（可爱风格）
- **装饰元素**：彩虹、星星、小马元素
- **布局**：简洁直观，操作流畅

## 🛠️ 技术实现

- **编程语言**：Python 3.11.9
- **GUI框架**：Tkinter（Python内置，无需额外安装）
- **打包工具**：PyInstaller 6.18.0
- **Flash支持**：Ruffle 开源Flash模拟器（通过CDN加载）
- **图标设计**：Pillow 生成的小马宝莉风格ICO图标

## 📁 项目结构

```
yourusername-pony-swf-player/
├── swf_player_gui.py      # 主程序文件
├── pony_icon.ico          # 小马宝莉风格图标
├── create_icon.py         # 图标生成脚本
├── README.md              # 项目说明文档
├── requirements.txt       # 项目依赖
└── .gitignore            # Git忽略文件列表
```

## 📝 开发说明

### 环境要求

- Python 3.6 及以上版本
- 现代操作系统（Windows/macOS/Linux）
- 网络连接（用于加载Ruffle模拟器）

### 依赖列表

```
pillow>=12.0.0      # 用于生成图标（可选）
pyinstaller>=6.0.0   # 用于打包EXE文件（可选）
```

### 运行程序

```bash
python swf_player_gui.py
```

### 打包选项

```bash
# 目录模式（推荐，EXE文件较小，约1.7MB）
pyinstaller --onedir --windowed --icon=pony_icon.ico swf_player_gui.py

# 单文件模式（包含所有依赖，约10MB）
pyinstaller --onefile --windowed --icon=pony_icon.ico swf_player_gui.py
```

## 🤝 贡献指南

欢迎小马宝莉粉丝和开发者贡献代码！

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/CuteFeature`
3. 提交更改：`git commit -m 'Add some cute feature'`
4. 推送到分支：`git push origin feature/CuteFeature`
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证，自由使用，自由修改，自由分享！

## 🙏 致谢

- 感谢 [Ruffle](https://ruffle.rs/) 提供的开源Flash模拟器
- 感谢小马宝莉动画带来的灵感和快乐
- 感谢所有喜欢这个项目的粉丝们

## ❓ 常见问题

### Q: 为什么SWF文件无法播放？
A: 可能的原因：
1. 系统缺少Flash播放器
2. 浏览器不支持WebAssembly
3. SWF文件本身损坏
4. 网络连接问题（加载Ruffle需要网络）

### Q: 如何解决播放卡顿？
A: 尝试：
1. 关闭其他占用资源的程序
2. 确保网络连接稳定
3. 更新浏览器到最新版本

### Q: 程序启动后没有图标怎么办？
A: 确保 `pony_icon.ico` 文件与 `swf_player_gui.exe` 在同一目录下

## 🌟 特别说明

这个播放器是为了方便小马宝莉粉丝播放SWF格式的小马宝莉动画而创建的，希望能给大家带来快乐！

---

🎀 享受你的小马宝莉SWF播放之旅！🎀

Created with ❤️ for My Little Pony fans!