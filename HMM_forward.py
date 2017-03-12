#coding=utf-8

#HMM向算法实现

from numpy import *

A=array([(0.5,0.2,0.3),(0.3,0.5,0.2),(0.2,0.3,0.5)])
B=array([(0.5,0.5),(0.4,0.6),(0.7,0.3)])
pi=array([(0.2),(0.4),(0.4)])
o=[0,1,0,1]   #观测序列：红，白，红，白
T=len(o)  	#观测序列长度
m=len(A)
n=len(B[0])

alph=array(zeros((T,m)))
for i in range(m) :
	alph[0][i]=pi[i] * B[i][o[0]]

for t in range(1,T):
	for i in range(m):
		temp=0
		for j in range(m):
			temp=temp+alph[t-1][j] * A[j][i]
		alph[t][i]=temp * B[i][o[t]]
print alph
result=0
for i in range(m):
	result=result + alph[T-1][i]

print result