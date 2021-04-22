
def keyschedule(kk,n,rc):
    newkey=[[0 for i in range(4)] for j in range(4)]
    one=[row[0] for row in kk]
    two=[row[1] for row in kk]
    three=[row[2] for row in kk]
    four=[row[3] for row in kk]
    f=four[1:]+four[:1]
    a=[0 for i in range(4)]
    for i in range(4):
        Aij=f[i]
        row=int(Aij[0],16)
        col=int(Aij[1],16)
        a[i]=S[row][col]
    temp=int(a[0],16)
    if n==1:
        rc=1
    else:
        if rc>=128:
            rc=(2*rc)^283
        else:
            rc=2*rc
    a[0]=hex(temp^rc)[2:]
    for i in range(4):
        one[i]=int(a[i],16)^int(one[i],16)
        two[i]=one[i]^int(two[i],16)
        three[i]=two[i]^int(three[i],16)
        four[i]=three[i]^int(four[i],16)
    for i in range(4):
        newkey[i][0]=hex(one[i])[2:].zfill(2)
        newkey[i][1]=hex(two[i])[2:].zfill(2)
        newkey[i][2]=hex(three[i])[2:].zfill(2)
        newkey[i][3]=hex(four[i])[2:].zfill(2)
    return newkey,rc
def given(text):
    count=1
    for i in range(32):
        if count%4==0:
            print(text[i],end=" ")
        else:
            print(text[i],end="")
        count+=1
def BS(output):
    a=[[0 for j in range(4)]for i in range(4)]
    for i in range(4):
        for j in range(4):
            Aij=hex(output[i][j])[2:].zfill(2)
            row=int(Aij[0],16)
            col=int(Aij[1],16)
            a[i][j]=S[row][col]
    return a
def shiftRow(A):
    for n in range(4):
        A[n]=A[n][n:]+A[n][:n]
    return A
def mixColumnSub(input,n):
    value=bin(int(input,16))[2:].zfill(8)
    place=0
    fx=27
    if n==1:
        value=int(value,2)
    elif n==2:
        c=0
        if value[0]=='1':
            c=1
        value=value[1:]+'0'
        value=int(value,2)
        if c==1:
            value=value^fx
    elif n==3:
        one=int(mixColumnSub(input,1))
        two=int(mixColumnSub(input,2))
        value=one^two
    return value
def mixColumn(A):
    Mul=[[0 for j in range(4)] for i in range(4)]
    M=[[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
    for i in range(4):
        for j in range(4):
            Mul[i][j]=0
            for k in range(4):
                ans=mixColumnSub(A[k][j],M[i][k])
                if k==0:
                    Mul[i][j]=ans
                else:
                    Mul[i][j]=Mul[i][j]^ans
    return Mul
def ark(first,second):
    out=[[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            first[i][j]=int(first[i][j],16)
            second[i][j]=int(second[i][j],16)
            out[i][j]=first[i][j]^second[i][j]
    return out
S=[['63','7c','77','7b','f2','6b','6f','c5','30','01','67','2b','fe','d7','ab','76'],
   ['ca','82','c9','7d','fa','59','47','f0','ad','d4','a2','af','9c','a4','72','c0'],
   ['b7','fd','93','26','36','3f','f7','cc','34','a5','e5','f1','71','d8','31','15'],
   ['04','c7','23','c3','18','96','05','9a','07','12','80','e2','eb','27','b2','75'],
   ['09','83','2c','1a','1b','6e','5a','a0','52','3b','d6','b3','29','e3','2f','84'],
   ['53','d1','00','ed','20','fc','b1','5b','6a','cb','be','39','4a','4c','58','cf'],
   ['d0','ef','aa','fb','43','4d','33','85','45','f9','02','7f','50','3c','9f','a8'],
   ['51','a3','40','8f','92','9d','38','f5','bc','b6','da','21','10','ff','f3','d2'],
   ['cd','0c','13','ec','5f','97','44','17','c4','a7','7e','3d','64','5d','19','73'],
   ['60','81','4f','dc','22','2a','90','88','46','ee','b8','14','de','5e','0b','db'],
   ['e0','32','3a','0a','49','06','24','5c','c2','d3','ac','62','91','95','e4','79'],
   ['e7','c8','37','6d','8d','d5','4e','a9','6c','56','f4','ea','65','7a','ae','08'],
   ['ba','78','25','2e','1c','a6','b4','c6','e8','dd','74','1f','4b','bd','8b','8a'],
   ['70','3e','b5','66','48','03','f6','0e','61','35','57','b9','86','c1','1d','9e'],
   ['e1','f8','98','11','69','d9','8e','94','9b','1e','87','e9','ce','55','28','df'],
   ['8c','a1','89','0d','bf','e6','42','68','41','99','2d','0f','b0','54','bb','16']]
#plaintexts="0000000000000000000000000000abc2"
#keys="1a0c24f2875495bcb7080e43920f5672"
plaintexts='00112233445566778899aabbccddeeff'
keys='000102030405060708090a0b0c0d0e0f'
plaintext=[[0 for i in range(4)] for j in range(4)]
key=[[0 for i in range(4)] for j in range(4)]
pos=0
for j in range(4):
    for i in range(4):
        key[i][j]=keys[pos:pos+2]
        plaintext[i][j]=plaintexts[pos:pos+2]
        pos+=2
print("---------------------------------------------------------------")
print("Assigned plaintext and key:",end="\n\t")
given(plaintexts)
print("(plaintext)",end="\n\t")
given(keys)
print("(key)",end="\n\t")
output=[[0 for i in range(4)] for j in range(4)]
print("\n""    ""The program is written in python 3.8.5 version on Windows OS \n---------------------------------------------------------------------\n\tKey Schedule Results for Each Round with the Original AES:\n---------------------------------------------------------------------")
rc=0
totalkey=[[0 for i in range(16)] for j in range(10)]
print("Round 0 :",end="\n""    ""  key : ")
for j in range(4):
    for i in range(4):
        print(key[i][j],end=" ")
print("\n")
for keyround in range(10):
    key,rc=keyschedule(key,keyround+1,rc)
    pos=0
    for j in range(4):
        for i in range(4):
            totalkey[keyround][pos]=key[i][j]
            pos+=1
for i in range(10):
    print("Round",i+1,":",end="\n""    ""  key : ")
    for j in range(16):
        print(totalkey[i][j],end=" ")
    print("\n")
print("\n---------------------------------------------------------------\n    Data Results for Each Round with the Original AES:\n---------------------------------------------------------------")
for round in range(11):
    print("Round",round,":",end="\n")
    if round!=0:
        A=BS(output)
        A=shiftRow(A)
        if round!=10:
            A=mixColumn(A)
        for i in range(4):
            for j in range(4):
                if round!=10:
                    A[i][j]=hex(A[i][j])[2:].zfill(2)
                key[i][j]=hex(key[i][j])[2:].zfill(2)
        pos=0
        for j in range(4):
            for i in range(4):
                key[i][j]=totalkey[round-1][pos]
                pos+=1
        output=ark(A,key)
    else:
        print("-----start:",end="   ")
        pos=0
        for j in range(4):
            for i in range(4):
                print(plaintexts[pos:pos+2],end=" ")
                pos+=2
        pos=0
        for j in range(4):
            for i in range(4):
                key[i][j]=keys[pos:pos+2]
                pos+=2
        print("\n")
        output=ark(plaintext,key)
    print("----output:",end="   ")
    for j in range(4):
        for i in range(4):
            print(hex(output[i][j])[2:].zfill(2),end=" ")
    print("\n")
print("---------------------------------------------------------------")
