from PIL import Image, ImageDraw

# 创建一个32x32的图标
icon = Image.new('RGBA', (32, 32), (255, 105, 180, 255))  # 粉色背景

draw = ImageDraw.Draw(icon)

# 绘制小马宝莉风格的简单图案
# 头部
circle_x, circle_y = 16, 16
radius = 12
draw.ellipse((circle_x - radius, circle_y - radius, circle_x + radius, circle_y + radius), fill="white")

# 眼睛
left_eye = (12, 14)
right_eye = (20, 14)

draw.ellipse((left_eye[0]-2, left_eye[1]-2, left_eye[0]+2, left_eye[1]+2), fill="black")
draw.ellipse((right_eye[0]-2, right_eye[1]-2, right_eye[0]+2, right_eye[1]+2), fill="black")

# 腮红
draw.ellipse((8, 18, 12, 22), fill=(255, 182, 193, 128))
draw.ellipse((20, 18, 24, 22), fill=(255, 182, 193, 128))

# 嘴巴
draw.arc((12, 18, 20, 22), 0, 180, fill="black", width=1)

# 彩虹鬃毛
rainbow_colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple"
]

for i, color in enumerate(rainbow_colors):
    y_offset = i * 2
    draw.line((6, 8 + y_offset, 16, 8 + y_offset), fill=color, width=2)

# 保存为ICO文件
icon.save("pony_icon.ico", format='ICO')

print("ICO图标文件已创建：pony_icon.ico")