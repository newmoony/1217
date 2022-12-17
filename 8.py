def main():
    a=int(input("請輸入數學成績:"))
    ispass(a)
    b=int(input("請輸入英文成績:"))
    ispass(b)
    c=int(input("請輸入國文成績:"))
    ispass(c)

    sum=a+b+c
    average=sum/3
    print("總平均:",average)
    ispass(average)

def ispass(score):
    if score >=60:
        print("恭喜及格了")
        return True     
    elif score <=60:
        print("不及格")
        return False

main()
