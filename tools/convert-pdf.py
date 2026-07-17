#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""旅游攻略 Markdown 转 PDF 工具

用法:
  python convert-pdf.py 承德            # 自动找 承德-旅游攻略.md
  python convert-pdf.py 承德-旅游攻略.md  # 直接指定 md 文件

依赖:
  - pandoc（需在 PATH 中，输入 pandoc --version 能看到版本）
  - Chrome 或 Edge 浏览器（自动查找）

输出:
  同目录下生成 {名称}.html 和 {名称}.pdf
"""
import sys
import os
import subprocess
import pathlib
import shutil


def find_browser():
    """自动查找 Chrome 或 Edge 浏览器路径"""
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    for b in ["google-chrome", "chromium", "microsoft-edge", "chromium-browser"]:
        p = shutil.which(b)
        if p:
            return p
    return None


def main():
    if len(sys.argv) < 2:
        print("用法: python convert-pdf.py <目的地名|md文件>")
        print("示例: python convert-pdf.py 承德")
        print("      python convert-pdf.py 承德-旅游攻略.md")
        sys.exit(1)

    name = sys.argv[1]
    md = name if name.endswith(".md") else f"{name}-旅游攻略.md"
    if not os.path.exists(md):
        print(f"错误: 找不到文件 {md}")
        sys.exit(1)

    base = os.path.splitext(md)[0]
    html = f"{base}.html"
    pdf = f"{base}.pdf"
    css = "guide.css"
    css_arg = ["--css", css] if os.path.exists(css) else []

    # 1. pandoc: md -> html（内嵌样式，独立文件）
    print(f"[1/2] 生成 HTML: {html}")
    subprocess.run(
        ["pandoc", md, "-o", html, "--standalone", "--embed-resources",
         *css_arg, "--metadata", f"title={base}"],
        check=True
    )

    # 2. 浏览器无头模式: html -> pdf
    browser = find_browser()
    if not browser:
        print(f"[2/2] 未找到 Chrome/Edge，HTML 已生成: {html}")
        print("    请用浏览器打开 HTML，按 Ctrl+P 打印成 PDF")
        return

    print(f"[2/2] 生成 PDF: {pdf}  (浏览器: {os.path.basename(browser)})")
    html_url = pathlib.Path(html).resolve().as_uri()
    subprocess.run(
        [browser, "--headless", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf}", html_url],
        check=True
    )
    print(f"\n完成! PDF 已生成: {pdf}")


if __name__ == "__main__":
    main()
