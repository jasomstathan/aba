import json, subprocess

jobs = [
    {'title':'注册监理工程师(安装/石油化工)', 'company':'某工程公司', 'salary':'4000-7000元', 'education':'大专', 'location':'烟台', 'source':'智联招聘', 'link':'https://www.zhaopin.com/sou/?kw=监理工程师&companyType=国企'},
    {'title':'监理工程师(国企)', 'company':'某国企工程服务公司100-299人', 'salary':'4000-8000元', 'education':'大专', 'location':'嘉峪关', 'source':'智联招聘', 'link':'https://www.zhaopin.com/sou/?kw=监理工程师&companyType=国企'},
    {'title':'注册监理工程师(安装)', 'company':'某股份制房产公司', 'salary':'6000-9000元', 'education':'大专', 'location':'昌吉', 'source':'智联招聘', 'link':'https://www.zhaopin.com/sou/?kw=监理工程师&companyType=国企'},
    {'title':'房建/市政/水利工程管理(国企)', 'company':'某国企房地产开发100-299人', 'salary':'5000-7000元', 'education':'大专', 'location':'南京鼓楼', 'source':'智联招聘', 'link':'https://www.zhaopin.com/sou/?kw=监理工程师&companyType=国企'},
    {'title':'注册监理工程师(房建/装饰)(国企)', 'company':'某国企房地产开发100-299人', 'salary':'7000-8000元', 'education':'本科', 'location':'厦门', 'source':'智联招聘', 'link':'https://www.zhaopin.com/sou/?kw=监理工程师&companyType=国企'},
    {'title':'光伏/风电/电网监理工程师(国企)', 'company':'某国企电力公司300-499人', 'salary':'10000-12000元·13薪', 'education':'大专', 'location':'阿坝', 'source':'智联招聘', 'link':'https://www.zhaopin.com/sou/?kw=监理工程师&companyType=国企'},
    {'title':'安全监理工程师(国企)', 'company':'某国企技术服务公司100-299人', 'salary':'8000-10000元', 'education':'大专', 'location':'鄂尔多斯', 'source':'智联招聘', 'link':'https://www.zhaopin.com/sou/?kw=监理工程师&companyType=国企'},
    {'title':'注册监理工程师+一级建造师(国企)', 'company':'某国企工程施工500-999人', 'salary':'3000-4000元', 'education':'大专', 'location':'肇庆', 'source':'智联招聘', 'link':'https://www.zhaopin.com/sou/?kw=监理工程师&companyType=国企'},
    {'title':'市政/房建/安装工程管理', 'company':'某股份制房产公司', 'salary':'5000-7000元', 'education':'大专', 'location':'青岛', 'source':'智联招聘', 'link':'https://www.zhaopin.com/sou/?kw=监理工程师&companyType=国企'},
    {'title':'工程监理/注册监理工程师', 'company':'某股份制技术服务公司', 'salary':'5000-7000元', 'education':'大专', 'location':'南京', 'source':'智联招聘', 'link':'https://www.zhaopin.com/sou/?kw=监理工程师&companyType=国企'},
]

data = json.dumps({'batch':'改进版演示','jobs':jobs})
r = subprocess.run(['python','C:\\Users\\xiang\\.openclaw\\workspaceaw\\job_packager_v2.py'],
                   input=data, capture_output=True, text=True, timeout=15)
result = json.loads(r.stdout)
print(f'压缩包: {result["zip"]}')
print(f'高度匹配: {result["high"]} 个')
print(f'中等匹配: {result["medium"]} 个')
