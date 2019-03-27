# IntermediateCodeGeneration
Python Program for Intermediate Code Generation From Compiler Design 

## POSTFIX CALCULATION

stk=[]
pre={'(':0,'+':1,'-':1,'*':2,'/':2,')':20,'=':-1}

def postfix(s):
	post=[]
	strpost=''
	stk.append('(')
	for i in s:
		if i=='(':
			stk.append(i)
		elif i=='+' or i=='-' or i=='*' or i=='/' or i==')':
			if pre[stk[-1]]>=pre[i]:
				while pre[stk[-1]]>=pre[i]:
					post.append(stk.pop())
				stk.append(i)
			elif i==')':
				while(stk[-1]!='('):
					post.append(stk.pop())
				stk.pop()
			else:
				stk.append(i)
		else:
			post.append(i)
	while(len(stk)!=1):
			post.append(stk.pop())
	for i in post:
		strpost+=i
	return strpost
  
  
  ## Intermediate Code GEneration
  
  import postfix as postfix

exp=input("Enter the Expression:")
post=postfix.postfix(exp)
code=[]
stk=[]
t=0
for i in post:
	if i.islower():
		stk.append(i)
	elif i=='+' or i=='-' or i=='*' or i=='/':
		b=stk.pop()
		a=stk.pop()
		code.append('t'+str(t)+'='+a+i+b)
		stk.append('t'+str(t))
		t+=1
b=stk.pop()
a=stk.pop()
code.append(a+"="+b)
print("\n===============INTERMEDIATE CODE==============\n")
for i in code:
	print('\t\t',i)
print("==============================================")
