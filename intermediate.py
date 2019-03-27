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
