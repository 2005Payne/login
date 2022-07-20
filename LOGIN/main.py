import memberManagement
import time
mM=memberManagement.MemberManagement()
clean=lambda :print("\n"*15)
#CUI

while True:
    loginMode='0'
    print("""
    ==============================
    = 1. 로그인                  =
    = 2. 회원가입                =
    = 나머지. 종료               =
    ==============================
    """)
    mode=input("숫자를 입력하세요: ")
    if mode=='1' or mode=='2'and loginMode!='1':
        while True:
            clean
            #아이디 비밀번호 입력받기
            print("==========","로그인" if mode=='1' else "회원가입","==========")
            Id=input("아이디: ")
            password=input("비밀번호: ")
            if mode=='1':
                if mM.login(Id,password)==1:
                    loginMode='1'
                clean
                print("로그인","완료" if loginMode=='1' else "실패!!")
                time.sleep(2)
                break
            else:
                if(mM.join(Id,password)==1):
                    clean
                    mode='1'
                    print("회원가입 완료")
                else:
                    clean
                    print("회원가입 실패!!")
                    break
    else:
        clean
        break