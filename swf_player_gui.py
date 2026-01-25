import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import subprocess
import tempfile
import webbrowser

class SWFPlayerApp:
    def __init__(self, root):
        # 初始化主窗口
        self.root = root
        self.root.title("🎀 小马宝莉 SWF 播放器 🎀")
        self.root.geometry("500x380")  # 调整窗口大小，更合适的比例
        
        # 小马宝莉风格配色方案
        self.pink_light = "#FFE4E1"      # 浅粉色
        self.pink_medium = "#FFB6C1"    # 中粉色
        self.pink_dark = "#FF69B4"      # 深粉色
        self.purple_light = "#E6E6FA"    # 浅紫色
        self.purple_medium = "#DDA0DD"   # 中紫色
        self.white = "#FFFFFF"           # 白色
        self.text_color = "#8B008B"      # 深紫色文字
        
        # 设置窗口样式
        self.root.configure(bg=self.pink_light)
        self.root.resizable(False, False)
        
        # 添加窗口图标（如果存在）
        try:
            # 尝试加载ico图标文件
            self.root.iconbitmap("pony_icon.ico")
        except:
            # 如果图标文件不存在，使用默认图标
            pass
        
        # 创建主框架，添加粉色圆角边框
        self.main_frame = tk.Frame(self.root, bg=self.white, bd=5, relief=tk.RAISED)
        self.main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        self.main_frame.configure(bg=self.pink_light)
        
        # 创建装饰性顶部框架
        self.header_frame = tk.Frame(self.main_frame, bg=self.pink_dark, height=40)
        self.header_frame.pack(fill=tk.X, pady=10, padx=10)
        
        # 创建标题标签 - 小马宝莉风格
        self.title_label = tk.Label(
            self.header_frame, 
            text="🌈 小马宝莉 SWF 播放器 🌈", 
            font=("Comic Sans MS", 18, "bold"),
            bg=self.pink_dark,
            fg=self.white,
            relief=tk.RAISED,
            bd=3
        )
        self.title_label.pack(pady=5)
        
        # 创建按钮框架
        self.button_frame = tk.Frame(self.main_frame, bg=self.pink_light)
        self.button_frame.pack(fill=tk.X, pady=10, padx=20)
        
        # 创建选择文件按钮 - 粉色渐变效果
        self.select_button = tk.Button(
            self.button_frame,
            text="🎀 选择 SWF 文件 🎀",
            command=self.select_swf,
            font=("Comic Sans MS", 14, "bold"),
            bg=self.pink_medium,
            fg=self.text_color,
            activebackground=self.pink_dark,
            activeforeground=self.white,
            relief=tk.RAISED,
            bd=4,
            height=2
        )
        self.select_button.pack(fill=tk.X, pady=5)
        
        # 创建播放按钮 - 粉色渐变效果
        self.play_button = tk.Button(
            self.button_frame,
            text="✨ 播放 SWF 文件 ✨",
            command=self.play_swf,
            font=("Comic Sans MS", 14, "bold"),
            bg=self.pink_medium,
            fg=self.text_color,
            activebackground=self.pink_dark,
            activeforeground=self.white,
            relief=tk.RAISED,
            bd=4,
            height=2,
            state=tk.DISABLED
        )
        self.play_button.pack(fill=tk.X, pady=5)
        
        # 创建状态和日志框架
        self.status_frame = tk.Frame(self.main_frame, bg=self.pink_light)
        self.status_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=20)
        
        # 创建状态标签
        self.status_label = tk.Label(
            self.status_frame,
            text="💖 状态：就绪 💖",
            font=("Comic Sans MS", 12, "bold"),
            bg=self.pink_light,
            fg=self.text_color,
            anchor=tk.W
        )
        self.status_label.pack(fill=tk.X, pady=5)
        
        # 创建日志区域 - 粉色边框和背景
        self.log_text = scrolledtext.ScrolledText(
            self.status_frame,
            height=6,
            wrap=tk.WORD,
            font=("Comic Sans MS", 10),
            bg=self.white,
            fg=self.text_color,
            insertbackground=self.pink_dark,
            relief=tk.RAISED,
            bd=3
        )
        self.log_text.pack(fill=tk.BOTH, expand=True, pady=5)
        self.log_text.insert(tk.END, "✨ SWF播放器已启动 ✨\n")
        self.log_text.config(state=tk.DISABLED)
        
        # 创建退出按钮
        self.exit_button = tk.Button(
            self.main_frame,
            text="💤 退出播放器 💤",
            command=self.root.quit,
            font=("Comic Sans MS", 12, "bold"),
            bg=self.purple_medium,
            fg=self.white,
            activebackground=self.pink_dark,
            activeforeground=self.white,
            relief=tk.RAISED,
            bd=3,
            height=1
        )
        self.exit_button.pack(fill=tk.X, pady=10, padx=20)
        
        # 存储选中的SWF文件路径
        self.swf_path = None
    
    def log(self, message):
        """记录日志"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        self.root.update()
    
    def select_swf(self):
        """选择SWF文件"""
        file_path = filedialog.askopenfilename(
            title="选择SWF文件",
            filetypes=[("SWF文件", "*.swf"), ("所有文件", "*.*")]
        )
        if file_path:
            self.swf_path = file_path
            file_name = os.path.basename(file_path)
            self.status_label.config(text=f"状态：已选择文件 - {file_name}")
            self.log(f"已选择文件：{file_path}")
            self.play_button.config(state=tk.NORMAL)
    
    def play_swf(self):
        """播放SWF文件"""
        if not self.swf_path:
            messagebox.showwarning("警告", "请先选择SWF文件")
            return
        
        try:
            self.status_label.config(text="状态：正在准备播放...")
            self.log("正在准备播放SWF文件...")
            
            # 确保文件路径是绝对路径
            swf_abs_path = os.path.abspath(self.swf_path)
            self.log(f"SWF文件绝对路径：{swf_abs_path}")
            
            # 使用更可靠的方式播放SWF
            if os.name == 'nt':  # Windows
                self.log("使用系统默认程序打开SWF文件...")
                # 尝试直接用系统默认程序打开
                result = subprocess.run(['start', '', swf_abs_path], shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    self.log("SWF文件已成功打开")
                    messagebox.showinfo("成功", f"已使用系统默认程序打开SWF文件\n{os.path.basename(self.swf_path)}")
                else:
                    self.log("直接打开失败，尝试使用HTML方式...")
                    # 如果直接打开失败，尝试HTML方式
                    self._play_via_html(swf_abs_path)
            else:
                # 非Windows系统直接使用webbrowser
                self._play_via_html(swf_abs_path)
                
            self.status_label.config(text="状态：播放完成")
            self.log("播放操作完成")
            
        except Exception as e:
            error_msg = f"播放失败：{str(e)}"
            self.log(error_msg)
            self.status_label.config(text="状态：播放失败")
            messagebox.showerror("错误", error_msg)
    
    def _play_via_html(self, swf_path):
        """通过HTML和Ruffle播放SWF"""
        try:
            # 处理文件路径，转换为file://协议
            file_url = swf_path.replace('\\', '/')
            file_url = f"file:///{file_url}" if not file_url.startswith('file://') else file_url
            self.log(f"转换为file://协议：{file_url}")
            
            # 创建一个临时HTML文件，使用Ruffle播放器
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>SWF播放器</title>
                <style>
                    body {{ 
                        margin: 0; 
                        padding: 20px; 
                        background-color: #f0f0f0; 
                        font-family: Arial, sans-serif;
                    }}
                    .container {{ 
                        display: flex; 
                        justify-content: center; 
                        align-items: center; 
                        min-height: 90vh;
                    }}
                    #player {{ 
                        border: 2px solid #333; 
                        background-color: white;
                    }}
                    .instructions {{ 
                        text-align: center; 
                        margin-bottom: 10px; 
                        color: #666;
                    }}
                </style>
            </head>
            <body>
                <div class="instructions">SWF播放器 - 使用Ruffle Flash模拟器</div>
                <div class="container">
                    <div id="ruffle-container"></div>
                </div>
                <script>
                    // 使用最新的Ruffle
                    window.RufflePlayer = window.RufflePlayer || {{}};
                    window.RufflePlayer.config = {{ 
                        autoplay: true, 
                        quality: "high",
                        scale: "showAll"
                    }};
                    
                    // 动态加载Ruffle
                    (function() {{ 
                        const script = document.createElement('script');
                        script.src = 'https://unpkg.com/@ruffle-rs/ruffle@latest/web/ruffle.js';
                        script.onload = function() {{ 
                            const ruffle = window.RufflePlayer.newest();
                            const player = ruffle.createPlayer();
                            const container = document.getElementById('ruffle-container');
                            container.appendChild(player);
                            player.load("{file_url}");
                        }};
                        document.body.appendChild(script);
                    }})();
                </script>
            </body>
            </html>
            """
            
            # 创建临时HTML文件
            with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
                f.write(html_content)
                temp_html_path = f.name
            
            self.log(f"已创建临时HTML文件：{temp_html_path}")
            
            # 先处理路径，再放入f-string
            html_file_url = temp_html_path.replace('\\', '/')
            webbrowser.open(f"file:///{html_file_url}")
            
            messagebox.showinfo("成功", "SWF文件已在浏览器中打开\n请确保您的浏览器支持WebAssembly")
            self.log("浏览器已成功打开")
            
        except Exception as e:
            raise Exception(f"HTML播放方式失败：{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SWFPlayerApp(root)
    root.mainloop()