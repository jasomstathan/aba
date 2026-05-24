import json, subprocess

# 今天的智联招聘真实数据（模拟采集结果）
jobs = [
    {"title":"注册监理工程师(安装/石油化工)", "company":"某民营工程公司","salary":"4000-7000元","education":"大专","location":"烟台","source":"智联招聘","link":"https://www.zhaopin.com/"},
    {"title":"监理工程师(国企)", "company":"某国企工程服务公司","salary":"4000-8000元","education":"大专","location":"嘉峪关","source":"智联招聘","link":"https://www.zhaopin.com/"},
    {"title":"注册监理工程师(安装)", "company":"某股份制公司","salary":"6000-9000元","education":"大专","location":"昌吉","source":"智联招聘","link":"https://www.zhaopin.com/"},
    {"title":"房建/市政/水利工程管理(国企)", "company":"某国企房地产","salary":"5000-7000元","education":"大专","location":"南京","source":"智联招聘","link":"https://www.zhaopin.com/"},
    {"title":"注册监理工程师(国企)", "company":"某国企房地产","salary":"7000-8000元","education":"本科","location":"厦门","source":"智联招聘","link":"https://www.zhaopin.com/"},
    {"title":"光伏/风电监理工程师(国企)", "company":"某国企电力公司","salary":"10000-12000元","education":"大专","location":"阿坝","source":"智联招聘","link":"https://www.zhaopin.com/"},
    {"title":"注册安全监理工程师(国企)", "company":"某国企技术服务","salary":"8000-10000元","education":"大专","location":"鄂尔多斯","source":"智联招聘","link":"https://www.zhaopin.com/"},
    {"title":"注册监理工程师+一级建造师(国企)", "company":"某国企工程施工","salary":"3000-4000元","education":"大专","location":"肇庆","source":"智联招聘","link":"https://www.zhaopin.com/"},
    {"title":"市政/房建/安装工程管理", "company":"某股份制公司","salary":"5000-7000元","education":"大专","location":"青岛","source":"智联招聘","link":"https://www.zhaopin.com/"},
    {"title":"工程监理/注册监理工程师", "company":"某股份制技术服务","salary":"5000-7000元","education":"大专","location":"南京","source":"智联招聘","link":"https://www.zhaopin.com/"},
    {"title":"总监理工程师(项目总监)", "company":"某大型国企工程集团","salary":"15000-20000元","education":"大专","location":"成都","source":"智联招聘","link":"https://www.zhaopin.com/"},  # 理想岗位
    {"title":"水利工程总监", "company":"某国企水利投资集团","salary":"18000-25000元","education":"本科","location":"武汉","source":"智联招聘","link":"https://www.zhaopin.com/"},  # 水利稀缺
    {"title":"一级建造师(项目经理)", "company":"某央企建筑工程局","salary":"12000-18000元","education":"本科","location":"广州","source":"智联招聘","link":"https://www.zhaopin.com/"},
    {"title":"土建工程师", "company":"某民营建筑公司","salary":"6000-8000元","education":"大专","location":"郑州","source":"智联招聘","link":"https://www.zhaopin.com/"},
]

data = json.dumps({"batch":"严格测试","jobs":jobs})
r = subprocess.run(["python","C:\\Users\\xiang\\.openclaw\\workspaceaw\\job_packager_v2.py"],
                   input=data, capture_output=True, text=True, timeout=15)
print(r.stdout)
print("---")
print(r.stderr[:200] if r.stderr else "")
