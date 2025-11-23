#题目二 修改后
print("这是一款为大三女生设计的体测查询程序，请输入你的相关信息")
while True:
    sex = input("请输入你的性别(如女):")
    grade = input("请输入你的年级（如大三）:")
    # 先判断是否是大三女生
    if sex == "女" and grade == "大三":
        print("请看清你的各项成绩并在以下题目中输入")
        Longrun = float(input("请输入你的800m跑成绩，如4.35:"))
        Shortrun = float(input("请输入你的50m跑成绩（单位秒），如8.2:"))
        Jump = float(input("请输入你的跳远成绩（单位厘米），如180:"))
        Up_sit = float(input("请输入你的仰卧起坐成绩（单位个），如35:"))
        Tiqq = float(input("请输入你的体前屈成绩（单位厘米），如19:"))
        Lungs = float(input("请输入你的肺活量成绩，如2345:"))
        Height = float(input("请输入你的身高（单位米），如1.60:"))
        Weight = float(input("请输入你的体重（单位千克），如50:"))
        BMI = Weight / (Height * Height)
        
        # 对照成绩参照表，进行赋分
        # 800m跑 
        if Longrun <= 3.16:
            scLo = 100
        elif Longrun <= 3.22:
            scLo = 95
        elif Longrun <= 3.28:
            scLo = 90
        elif Longrun <= 3.35:
            scLo = 85
        elif Longrun <= 3.42:
            scLo = 80
        elif Longrun <= 3.47:
            scLo = 78
        elif Longrun <= 3.52:
            scLo = 76
        elif Longrun <= 3.57:
            scLo = 74
        elif Longrun <= 4.02:
            scLo = 72
        elif Longrun <= 4.07:
            scLo = 70
        elif Longrun <= 4.12:
            scLo = 68
        elif Longrun <= 4.17:
            scLo = 66
        elif Longrun <= 4.22:
            scLo = 64
        elif Longrun <= 4.27:
            scLo = 62
        elif Longrun <= 4.32:
            scLo = 60
        elif Longrun <= 4.42:
            scLo = 50
        elif Longrun <= 4.52:
            scLo = 40
        elif Longrun <= 5.02:
            scLo = 30
        elif Longrun <= 5.12:
            scLo = 20
        elif Longrun <= 5.22:
            scLo = 10
        else:
            scLo = 0
        
        # 50m跑 
        if Shortrun <= 7.4:
            scSh = 100
        elif Shortrun <= 7.5:
            scSh = 95
        elif Shortrun <= 7.6:
            scSh = 90
        elif Shortrun <= 7.9:
            scSh = 85
        elif Shortrun <= 8.2:
            scSh = 80
        elif Shortrun <= 8.4:
            scSh = 78
        elif Shortrun <= 8.6:
            scSh = 76
        elif Shortrun <= 8.8:
            scSh = 74
        elif Shortrun <= 9.0:
            scSh = 72
        elif Shortrun <= 9.2:
            scSh = 70
        elif Shortrun <= 9.4:
            scSh = 68
        elif Shortrun <= 9.6:
            scSh = 66
        elif Shortrun <= 9.8:
            scSh = 64
        elif Shortrun <= 10.0:
            scSh = 62
        elif Shortrun <= 10.2:
            scSh = 60
        elif Shortrun <= 10.4:
            scSh = 50
        elif Shortrun <= 10.6:
            scSh = 40
        elif Shortrun <= 10.8:
            scSh = 30
        elif Shortrun <= 11.0:
            scSh = 20
        elif Shortrun <= 11.2:
            scSh = 10
        else:
            scSh = 0
        
        # 立定跳远
        if Jump >= 208:
            scJu = 100
        elif Jump >= 202:
            scJu = 95
        elif Jump >= 196:
            scJu = 90
        elif Jump >= 189:
            scJu = 85
        elif Jump >= 182:
            scJu = 80
        elif Jump >= 179:
            scJu = 78
        elif Jump >= 176:
            scJu = 76
        elif Jump >= 173:
            scJu = 74
        elif Jump >= 170:
            scJu = 72
        elif Jump >= 167:
            scJu = 70
        elif Jump >= 164:
            scJu = 68
        elif Jump >= 161:
            scJu = 66
        elif Jump >= 158:
            scJu = 64
        elif Jump >= 155:
            scJu = 62
        elif Jump >= 152:
            scJu = 60
        elif Jump >= 147:
            scJu = 50
        elif Jump >= 142:
            scJu = 40
        elif Jump >= 137:
            scJu = 30
        elif Jump >= 132:
            scJu = 20
        elif Jump >= 127:
            scJu = 10
        else:
            scJu = 0
        
        # 仰卧起坐
        if Up_sit >= 57:
            scUp = 100
        elif Up_sit >= 55:
            scUp = 95
        elif Up_sit >= 53:
            scUp = 90
        elif Up_sit >= 50:
            scUp = 85
        elif Up_sit >= 47:
            scUp = 80
        elif Up_sit >= 45:
            scUp = 78
        elif Up_sit >= 43:
            scUp = 76
        elif Up_sit >= 41:
            scUp = 74
        elif Up_sit >= 39:
            scUp = 72
        elif Up_sit >= 37:
            scUp = 70
        elif Up_sit >= 35:
            scUp = 68
        elif Up_sit >= 33:
            scUp = 66
        elif Up_sit >= 31:
            scUp = 64
        elif Up_sit >= 29:
            scUp = 62
        elif Up_sit >= 27:
            scUp = 60
        elif Up_sit >= 25:
            scUp = 50
        elif Up_sit >= 23:
            scUp = 40
        elif Up_sit >= 21:
            scUp = 30
        elif Up_sit >= 19:
            scUp = 20
        elif Up_sit >= 17:
            scUp = 10
        else:
            scUp = 0
        
        # 体前屈
        if Tiqq >= 26.3:
            scTi = 100
        elif Tiqq >= 24.4:
            scTi = 95
        elif Tiqq >= 22.4:
            scTi = 90
        elif Tiqq >= 21.0:
            scTi = 85
        elif Tiqq >= 19.5:
            scTi = 80
        elif Tiqq >= 18.2:
            scTi = 78
        elif Tiqq >= 16.9:
            scTi = 76
        elif Tiqq >= 15.6:
            scTi = 74
        elif Tiqq >= 14.3:
            scTi = 72
        elif Tiqq >= 13.0:
            scTi = 70
        elif Tiqq >= 11.7:
            scTi = 68
        elif Tiqq >= 10.4:
            scTi = 66
        elif Tiqq >= 9.1:
            scTi = 64
        elif Tiqq >= 7.8:
            scTi = 62
        elif Tiqq >= 6.5:
            scTi = 60
        elif Tiqq >= 5.7:
            scTi = 50
        elif Tiqq >= 4.9:
            scTi = 40
        elif Tiqq >= 4.1:
            scTi = 30
        elif Tiqq >= 3.3:
            scTi = 20
        elif Tiqq >= 2.5:
            scTi = 10
        else:
            scTi = 0
        
        # 肺活量
        if Lungs >= 3450:
            scLu = 100
        elif Lungs >= 3400:
            scLu = 95
        elif Lungs >= 3350:
            scLu = 90
        elif Lungs >= 3200:
            scLu = 85
        elif Lungs >= 3050:
            scLu = 80
        elif Lungs >= 2950:
            scLu = 78
        elif Lungs >= 2850:
            scLu = 76
        elif Lungs >= 2750:
            scLu = 74
        elif Lungs >= 2650:
            scLu = 72
        elif Lungs >= 2550:
            scLu = 70
        elif Lungs >= 2450:
            scLu = 68
        elif Lungs >= 2350:
            scLu = 66
        elif Lungs >= 2250:
            scLu = 64
        elif Lungs >= 2150:
            scLu = 62
        elif Lungs >= 2050:
            scLu = 60
        elif Lungs >= 2010:
            scLu = 50
        elif Lungs >= 1970:
            scLu = 40
        elif Lungs >= 1930:
            scLu = 30
        elif Lungs >= 1890:
            scLu = 20
        elif Lungs >= 1850:
            scLu = 10
        else:
            scLu = 0
        
        # BMI
        if BMI >= 28:
            scB = 60
        elif BMI >= 24:
            scB = 80
        elif BMI >= 17.2:
            scB = 100
        else: 
            scB = 80
        
        # 计算总分并打印
        score = 0.20*scLo +0.20* scSh + 0.1*scJu +0.1* scUp + 0.1*scTi + 0.15*scLu + 0.15*scB
        print("你的分数是：" + str(score))
        
        break
    else:
        print("什么眼神？没看到是给大三女生设计的吗？")