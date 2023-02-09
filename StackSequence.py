inputNum=int(input())

nList=[]
stack=[]
existList=set()
answerList=[]
cur=1

for i in range(inputNum):
    n=int(input())
    nList.append(n)

for i in range(inputNum):
    if nList[i] not in stack: #stack안에 입력한 숫자가 없는 경우
        for j in range(cur,inputNum+1): #반복
            if j not in existList: #existList에 없는 경우에만 추가
                stack.append(j) 
                answerList.append("+")
                existList.add(j)
                if nList[i] in stack: #원하는 숫자를 스택에 넣었으니 빼주고 break
                    n=stack.pop(-1)
                    answerList.append("-")
                    break

    else: #숫자가 이미 stack안에 있는 경우
        for j in range(inputNum):
            n=stack.pop(-1) 
            answerList.append("-")
            break
    
    cur=len(stack)
    
if len(stack) != 0:
    print("NO")
else:
    for i in range(len(answerList)):
        print(answerList[i])
                