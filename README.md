# TinyDesktopShorter-MaybeGood-
My Desktop just messy.So I decide do this thing.You may need it
# desktop-sorter
> Simple desktop file sorter written in Python.
自动整理桌面文件，按文件类型归类，一键清理杂乱桌面。

## ✨ Features
- 🗂️ 按后缀自动分类：图片 / 文档 / 视频 / 音频 / 压缩包 / 程序 / 其他
- 👀 预览模式：先列出所有将要移动的文件，确认后才操作，安全不翻车
- 🚫 跳过文件夹和白名单文件，不会误移项目文件夹
- 💻 Cross-platform: Windows / macOS / Linux
- 🧩 轻量无依赖，仅使用 Python 标准库

## 📦 Requirements
Python 3.6+
> 不需要额外 pip 包！

## 🚀 Quick Start
1. Clone this repo
```bash
git clone https://github.com/IAmEoDAndIWasLazy/TinyDesktopShorter-MaybeGood-
cd desktop-sorter

##🚀 How to Run（Detailed Tutorial）
 
#1. Install Python
 
1. Download Python: python.org/downloads

2. Important: Check  Add Python to PATH  during installation

3. Verify installation (open CMD/PowerShell/Terminal):
 
 
 
If Python version appears, the installation is successful.
 
#2. Run the script
 
##Method 1: Command line run (Recommended)
 
1. Download this project file  desktop_sorter.py 

2. Open terminal,  cd  to the file folder
 
 
 
#3. Execute the program
 
 
 
##Method 2: Double-click to run (Windows lazy mode)
 
Directly double-click  desktop_sorter.py  to start.
 
#3. Operation steps
 
1. The program will automatically scan your desktop and list all files to be sorted

2. Check the preview list carefully

3. Input  y  and press Enter → Start sorting

4. Input any other key → Cancel operation (no file changes)
 
##📦 Custom Rules
 
Edit the config area in the code to add/delete file suffixes:
 
 
 
Add file names you want to ignore to  IGNORE_LIST .
 
##🎯 Pack to EXE (Optional)
 
Make a single exe file, run on any Windows computer without Python:
 
 
 
The executable file is in the  dist  folder.
 
##⚠️ Safety Instructions
 
- This program will never delete any files

- Duplicate files will be renamed automatically ( xxx_1.ext )

- Preview first, execute later, 100% safe
