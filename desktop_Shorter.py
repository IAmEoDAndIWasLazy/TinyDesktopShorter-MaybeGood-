#!/usr/bin/env python3
# This software is released under the Unlicense (Public Domain).
# Feel free to use, modify, sell for commercial use. No permission needed.

import os
import shutil

# 配置区：文件后缀分类，按需自行增删
FILE_CATEGORIES = {
    "图片": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
    "文档": [".txt", ".md", ".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".odt"],
    "视频": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm"],
    "音频": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "压缩包": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "程序": [".exe", ".msi", ".apk", ".dmg", ".deb", ".rpm"]
}

# 忽略列表：匹配到名称就跳过，不会移动
IGNORE_LIST = [".git", "README", "desktop-sorter"]


def get_desktop_path() -> str:
    """自动获取当前用户桌面路径，跨平台"""
    home = os.path.expanduser("~")
    return os.path.join(home, "Desktop")


def get_file_category(file_ext: str) -> str:
    """根据文件后缀返回分类名称，不匹配归入「其他文件」"""
    ext = file_ext.lower()
    for category, suffix_list in FILE_CATEGORIES.items():
        if ext in suffix_list:
            return category
    return "其他文件"


def preview_files(desktop_path: str) -> list[tuple[str, str]]:
    """扫描桌面，返回待移动文件列表，只预览不执行移动"""
    move_list = []
    for entry_name in os.listdir(desktop_path):
        full_entry_path = os.path.join(desktop_path, entry_name)

        # 跳过文件夹
        if os.path.isdir(full_entry_path):
            continue

        # 跳过忽略列表中的文件
        if any(ignore_word in entry_name for ignore_word in IGNORE_LIST):
            continue

        _, ext = os.path.splitext(entry_name)
        category = get_file_category(ext)
        move_list.append((entry_name, category))
    return move_list


def sort_desktop(desktop_path: str, file_list: list[tuple[str, str]]):
    """执行文件移动，重名文件自动加后缀 _1 避免覆盖"""
    for filename, category in file_list:
        target_folder = os.path.join(desktop_path, category)
        os.makedirs(target_folder, exist_ok=True)

        src_file = os.path.join(desktop_path, filename)
        dst_file = os.path.join(target_folder, filename)

        # 处理目标目录存在同名文件
        if os.path.exists(dst_file):
            name_part, ext_part = os.path.splitext(filename)
            new_filename = f"{name_part}_1{ext_part}"
            dst_file = os.path.join(target_folder, new_filename)

        shutil.move(src_file, dst_file)
        print(f"✅ {filename}  →  {category}/")


def main():
    desktop = get_desktop_path()
    print(f"📂 正在扫描桌面路径：{desktop}\n")

    pending_files = preview_files(desktop)
    if not pending_files:
        print("✅ 扫描完成，没有需要整理的文件。")
        return

    print("===== 预览：即将整理的文件 =====")
    for name, cat in pending_files:
        print(f"• {name}  => 【{cat}】")

    user_input = input("\n确认执行移动文件？输入 y 确认，其他任意字符取消：").strip().lower()
    if user_input == "y":
        sort_desktop(desktop, pending_files)
        print("\n🎉 桌面整理全部完成！")
    else:
        print("\n❌ 操作已取消，未改动任何文件。")


if __name__ == "__main__":
    main()
