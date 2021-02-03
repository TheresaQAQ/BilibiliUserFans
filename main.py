from Bilibili import Bilibili

def main():
    uid = input("请输入用户UID：")
    lv0,lv1,lv2,lv3,lv4,lv5,lv6 = 0,0,0,0,0,0,0

    B = Bilibili(uid)
    for i in range(1,6):
        list = B.get_fans(i)
        for id in list:
            Biliuser = Bilibili(id)
            level = int(Biliuser.get_level())

            if level == 0:
                lv0+=1
            elif level == 1:
                lv1+=1
            elif level == 2:
                lv2+=1
            elif level == 3:
                lv3+=1
            elif level == 4:
                lv4+=1
            elif level == 5:
                lv5+=1
            elif level == 6:
                lv6+=1

    print(lv0,lv1,lv2,lv3,lv4,lv5,lv6)

if __name__ == '__main__':
    main()