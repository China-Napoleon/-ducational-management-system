import time
def add_stu():
    while True:
        stu_nub = input("请输入学生学号(11位数字):")
        if stu_nub.isdigit():
            a=len(stu_nub)
            if a<11:
                pass
            else:
                break

    while True:
        stu_name = input("请输入学生名字:")
        b=len(stu_name)
        if b==0:
            pass
        else:
            break

    while True:
            stu_phon =input("请输入学生手机号(11位数字):")
            if stu_phon.isdigit():
                b=len(stu_phon)
                if b<11:
                    pass
                else:
                        break

    while True:
        stu_grade =input("请输入学生总分(至少3位数字):")
        if stu_grade.isdigit():
            c = len(stu_grade)
            if c<3:
                pass
            else:
                break

    while True:
        stu_address = input("请输入家庭住址:")
        b=len(stu_address)
        if b==0:
            pass
        else:
            break

    while True:
        a = input("是否保存当前操作,输入6进行保存,输入其他则继续添加学生信息：")
        if a == "6":
            with open('学生数据中心.txt', 'a', encoding="UTF-8") as f:
                f.write(stu_nub)
                f.write("         " + stu_name)
                f.write("       " + stu_phon)
                f.write("         " + stu_grade)
                f.write("         " + stu_address+"\n")
                time.sleep(2)
                print("添加成功")
                break
        else:
            break


def del_stu():
    with open('学生数据中心.txt', 'r', encoding="UTF-8") as f:
        a = f.readlines()
        b = input("请输入要删除的学号:")
        if b.isdigit():
            for new_list in a:
                new_list.strip()
                c = new_list.split()
                if c[0] == b:
                    a.remove(new_list)
            aa = input("是否保存当前操作,输入6进行保存,输入其他则删除学生信息：")
            if aa == "6":
                save()
                with open("学生数据中心.txt", "w", encoding='UTF-8') as f_w:
                    for i in a:
                        f_w.write(i)
                        time.sleep(2)
                print("删除成功")

def Modify_stu():
    import time
    with open('学生数据中心.txt', 'r', encoding="utf-8") as f:
        a = f.readlines()
        b = input("请输入要修改的学号:")
        if b.isdigit():
            for i in range(0, len(a)):
                a[i].replace('\n', '')
                c = a[i].split()
                if c[0] == b:
                    print(c)
                    xg = int(input("请输入你要修改的内容：0(修改学号) 1(修改名字) 2(修改电话) 3(修改总成绩) 4(修改住址):"))
                    if xg == 0:
                        c[0] = input("请输入新的学生学号:")
                    elif xg == 1:
                        c[1] = input("请输入新的学生名字:")
                    elif xg == 2:
                        c[2] = input("请输入新的学生电话:")
                    elif xg == 3:
                        c[3] = input("请输入新的学生总成绩:")
                    elif xg == 4:
                        c[4] = input("请输入新的学生住址:")
                    c = "       ".join(c)
                    a.pop(i)
                    a.insert(i, c + "\n")
                    print("正在修改中，请稍后......")
                    time.sleep(2)
                    aa = input("是否保存当前操作,输入6进行保存：")
                    if aa == "6":
                        # save()
                        with open("学生数据中心.txt", "w", encoding='utf-8') as f_w:
                            for i in a:
                                f_w.write(i)
                                time.sleep(2)
                        print("修改成功")
def save():
    print("-*-*"*8+"正在保存中"+"-*-*"*8)


def Query_stu():
    with open('学生数据中心.txt', 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        a = input("请输入需要查询的学生学号：")
        if a.isdigit():
            for i in range(0,len(lines)):
                lines[i].strip()
                b=lines[i].split()
                if a==b[0]:
                    print("  stu_nub        stu_name          stu_phon         stu_grade     stu_address")
                    print(lines[i])
                    break
            else:
                print("输入的学号不存在")

def display_stu():
    print("  stu_nub        stu_name          stu_phon         stu_grade     stu_address")
    with open('学生数据中心.txt', 'r',encoding="UTF-8") as f:
        a=f.readlines()
        for i in range(0,len(a)):
            print(a[i].replace('\n',''))

def main():
    print('                                                                                                                      ')
    print("-**-"*15+"教务学生管理系统"+"-**-"*20)
    while True:
        print("-*-*"*8+"1添加学号"+"    "+"2 删除学生"+"    "+"3 修改学生"+"    "+"4 查询学生"+"    "+"5 显示所有的学生"+"    "+"6 保存操作"+"    "+"7 退出系统"+"-*-*"*8)
        ac=input("请输入你要执行的操作对应的数字:")
        if ac.isdigit():
            if ac=="1":
                add_stu()
            elif ac=="2":
                del_stu()
            elif ac=="3":
                Modify_stu()
            elif ac=="4":
                Query_stu()
            elif ac=="5":
                display_stu()
            elif ac=="6":
                save()
            elif ac == "7":
                break

main()