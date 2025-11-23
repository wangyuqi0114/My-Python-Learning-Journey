# My-Python-Learning-Journey
## 11.5second work

```
#定义函数
def hello(name):
    '''功能：输入人名，显示hello信息'''
    str1="Hello"+name
    print(str1)
#调用函数
hello('周铉')
#实操
def favorite_book(title):
    print("One of my favorite books is",title)
favorite_book("heihei")

def surf_a(chang,kuan,gao):
    s=(chang*kuan+kuan*gao+chang*gao)*2
    print("长方体的表面积是"+str(s))
surf_a(8,4,5)

def mymax(a,b,c,d,e):
    m=max(a,b,c,d,e)
    print("这里面最大的数是"+str(m))
mymax(123,312,2434,323,434)

#指定参数及输出
def fun_bmi(height,weight,person="某某"):
    bmi=weight/(height*height)
    if bmi<18.5:
        print(person,"your BMI is",str(bmi),"体重过轻")
    elif bmi<24.9:
        print(person,"your BMI is",str(bmi),"正常范围")
    elif bmi<29.9:
        print(person,"your BMI is",str(bmi),"体重过重")
    else:
        print(person,"your BMI is",str(bmi),"肥不死你")
fun_bmi(1.66,50) #输出身高为1.66，体重为50的人的bmi
```
该项目涉及了如何定义和调用函数、其中定义的函数有测算长方体表面积、输出五个数中最大的数、测算bmi并反馈。
##学习心得与规划
学习启发
浏览GitHub项目让我意识到规范的项目结构、清晰的文档和持续的commit记录对展示个人能力至关重要。通过本次任务，我学会了如何用具体项目系统化展示编程技能。
未来规划
我将把这个仓库作为Python学习历程的完整记录：
按技术主题分目录（基础语法、实战项目等）、通过commit记录学习轨迹、建立个人技术成长档案
让这个仓库成为我编程能力的动态证明和持续学习的见证。
