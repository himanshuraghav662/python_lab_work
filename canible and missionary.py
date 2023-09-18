M1=3
C1=3
M2=0
C2=0

print("Rule 1: One Missionary is selling boat from bank 1 to bank 2")
print("Rule 2: Two Missionary are selling boat from bank 1 to bank 2")
print("Rule 3: One MIssionary and one cannibal are selling boat from bank 1 to bank 2")
print("Rule 4: One Cannibal is selling boat from bank 1 to bank 2")
print("Rule 5: Two Cannibals are selling boat from bank 1 to bank 2")
print("Rule 6: One Missionary is selling boat from bank 2 to bank 1")
print("Rule 7: Two Missionary are selling boat from bank 2 to bank 1")
print("Rule 8: One Missionary and one vcannibal are selling boat from bank 2 to bank 1")
print("Rule 9: One Cannibals is selling boat from bank 2 to bank 1")
print("Rule 10: Two Cannibals are selling boat from bank 2 to bank 1")

while ((M2 != 3) or (C2!=3)):
    r = int(input("Enter rule"))
    if(r == 1):
        M1=M1-1
        M2=M2+1
        
    elif(r == 2):
        M1=M1-2
        M2=M2+2
        
    elif(r == 3):
        M1=M1-1
        C1=C1-1
        M2=M2+1
        C2=C2+1
        
    elif(r == 4):
        C1=C1-1
        C2=C2+1
        
    elif(r == 5):
        C1=C1-2
        C2=C2+2
        
    elif(r == 6):
        M2=M2-1
        M1=M1+1
        
    elif(r == 7):
        M2=M2-2
        M1=M1+2
        
    elif(r == 8):
        M2=M2-1
        C2=C2-1
        M1=M1+1
        C1=C1+1
        
    elif(r == 9):
        C2=C2-1
        C1=C1+1
        
    elif(r == 10):
        C2=C2-2
        C1=C1+2
    print(M1, C1)
    print(M2, C2)

    if((M1>0 and M1<C1) or (M2>0 and M2<C2)):
        print("dead")
        break
