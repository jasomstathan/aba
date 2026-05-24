import os, sys, subprocess, struct

desktop = os.path.expanduser("~/Desktop")

def create_url_shortcut(name, url):
    """Create a .url internet shortcut file"""
    path = os.path.join(desktop, f"{name}.url")
    with open(path, 'w', encoding='utf-8') as f:
        f.write("[InternetShortcut]\n")
        f.write(f"URL={url}\n")
        f.write("IconIndex=0\n")
    print(f"  {name}.url  [网页链接] -> {url}")

def create_lnk(name, target, args=""):
    """Create a .lnk shortcut using PowerShell"""
    ps_code = f'''
    $wshell = New-Object -ComObject WScript.Shell
    $sc = $wshell.CreateShortcut("{desktop}\\{name}.lnk")
    $sc.TargetPath = "{target}"
    $sc.Arguments = "{args}"
    $sc.Save()
    Write-Output "OK"
    '''
    r = subprocess.run(["powershell", "-Command", ps_code], capture_output=True, text=True, timeout=10)
    print(f"  {name}.lnk  {'[OK]' if 'OK' in r.stdout else '[FAILED]'}")

print("正在创建桌面快捷方式...\n")

# 1. OpenClaw Dashboard
create_url_shortcut("OpenClaw 控制台", "http://127.0.0.1:18789/")

# 2. Claude Code
create_lnk("Claude Code", r"C:\Windows\System32\cmd.exe", "/k claude")

# 3. CC-Switch Web UI
create_lnk("CC-Switch 模型切换", r"C:\Windows\System32\cmd.exe", "/k cc-switch web --open")

# 4. Obsidian
create_lnk("Obsidian 笔记库", r"C:\Users\xiang\AppData\Local\Programs\Obsidian\Obsidian.exe", "obsidian://vault/F:\\Obsidian\\项工开悟")

print("\n完成！桌面快捷方式列表：")
for f in os.listdir(desktop):
    if any(k in f for k in ["OpenClaw", "Claude", "CC-Switch", "Obsidian"]):
        print(f"  📌 {f}")
