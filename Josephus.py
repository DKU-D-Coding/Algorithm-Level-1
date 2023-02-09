class Node: #연결리스트를 위한 클래스 정의
    def __init__(self,data,next=None,before=None):
        self.data=data
        self.next=next
        self.before=before

inputNum1, inputNum2=map(int,input().split())

nList=[]
answerList=[]

nList.append(Node(1))

for i in range(inputNum1-1): #이후로 Node(2)부터 추가
    nList.append(Node(i+2))
    nList[i].next=nList[i+1]
    nList[i+1].before=nList[i]

nList[0].before=nList[inputNum1-1] #맨 앞과 맨 뒤 연결
nList[inputNum1-1].next=nList[0]


n=nList[-1] #루프를 돌기 위한 변수 설정

for i in range(inputNum1):
    for i in range(inputNum2): #inputNum2번만큼 점프
        n=n.next

    answerList.append(n) #답 리스트에 추가한 후 빠진 것에 대한 연결 새로 설정
    n.before.next=n.next
    n.next.before=n.before
    n=n.before

print("<", end="")
for i in range(len(answerList)-1): # 출력
    print(answerList[i].data, end=", ")

print(answerList[-1].data,end="")
print(">")