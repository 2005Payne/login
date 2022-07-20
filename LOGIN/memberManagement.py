import passwordTool
caesar=passwordTool.Caesar()
class MemberManagement:
    def login(self,Id,passWord):
        #아이디 있는지 확인
        try:
            f=open("./member/{}.txt".format(Id),"r")
            f.close()
        #아이디 없음
        except:
            return 0
        else:
            #비밀번호 확인
            with open("./member/{}.txt".format(Id),"r") as f:
                pw=f.read()
            if caesar.decryption(str(pw))==passWord and str(pw)!=passWord:
                return 1
            else:
                return 0
    def join(self,Id,passWord):
        #비밀번호 확인
        abcAscii=list(map(chr,list(i for i in range(96,123) if i<91 or i>96)))
        for i in list(passWord):
            if not(i in abcAscii):
                return 0
        #아이디 중복확인
        try:
            f=open("member\{}.txt".format(Id),"r")
            f.close()
        #아이디 추가
        except:
            with open("member\{}.txt".format(Id),"w") as f:
                f.write(caesar.encryption(passWord))
            return 1
        else:
            return 0