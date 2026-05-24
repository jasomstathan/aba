import re, ssl, urllib.request
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
hdr = {"User-Agent": "Mozilla/5.0"}
r = urllib.request.urlopen(urllib.request.Request("https://www.ncrczpw.com/", headers=hdr), context=ctx, timeout=10)
html = r.read().decode("utf-8","replace")

ats = re.findall(r"<a[^>]*>([^<]{8,30})</a>", html)
print("前30个a标签文本:")
for t in ats[:30]:
    print(f"  {t}")

print("\n检查关键词命中:")
kws = ["总监", "监理", "工程", "施工", "建筑", "建造师"]
for t in ats[:100]:
    for k in kws:
        if k in t:
            print(f"  匹配'{k}': {t}")
            break
