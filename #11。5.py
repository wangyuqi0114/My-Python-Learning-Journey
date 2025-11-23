#11.5课堂训练
#定义函数
def hello(name):
    '''功能：输入人名，显示hello信息'''
    str1="Hello"+name
    print(str1)
#调用函数
hello('周铉')
#练习


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
fun_bmi(1.66,50)


