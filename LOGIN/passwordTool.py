class Caesar:
    def __init__(self):  
        self.abcAscii=list(i for i in range(96,123) if i<91 or i>96)
    #52개
    def encryption(self,str):
        #문자열을 아스키코드로 변환
        keyCode=0
        #encStr=list(ord(i) for i in list(str.lower()))
        encStr=list(map(ord,str.lower()))
        #문자 인덱스 변환
        for i in range(len(encStr)):
            for j in range(len(self.abcAscii)):
                if encStr[i]==self.abcAscii[j]:
                    encStr[i]=j
                    keyCode+=self.abcAscii[j]-97
        #키코드 생성
        keyCode=keyCode%26
        
        #키코드를 아스키코드에 더하기
        encStr=list(chr(self.abcAscii[(i+keyCode)%26]) for i in encStr)
        #키코드를 리스트 끝에 추가
        encStr.append(chr(keyCode+97))

        return "".join(encStr)

    def decryption(self,str):
        #다시
        decStr=list(str)
        #키코드를 분리
        keyCode=ord(decStr[-1])-97
        del decStr[-1]
        #키코드만큼 다시 빼고 문자열로 변화        
        decStr=list(chr(self.abcAscii[(ord(i)-97-keyCode)%26]) for i in decStr)
        return "".join(decStr)
if __name__=="__main__":
    a=Caesar()
    print(a.encryption("xyz"))
    print(a.decryption(a.encryption("xyz")))