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

#exp='a+g/u*(b*y+k)+f*r'
#print(postfix(exp))
