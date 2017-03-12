#coding=utf-8


#HMM后向算法实现

from numpy import *

A=array([(0.5,0.2,0.3),(0.3,0.5,0.2),(0.2,0.3,0.5)])
B=array([(0.5,0.5),(0.4,0.6),(0.7,0.3)])
pi=array([(0.2),(0.4),(0.4)])
o=[0,1,0,1]   #观测序列：红，白，红，白
T=len(o)  	#观测序列长度
m=len(A)
n=len(B[0])



print A
print B
print pi
print o

bata=array(zeros((T,m)))

print bata

for i in range(m):
	bata[T-1][i]=1

t=T-2
while(t>=0):
	for i in range(m):
		for j in range(m):
			bata[t][i]+=A[i][j] * B[j][o[t+1]] * bata[t+1][j]
	t=t-1

print bata

result=0

for i in range(m):

	result=result+pi[i]*B[i][o[0]]*bata[0][i]


print bata
print result








