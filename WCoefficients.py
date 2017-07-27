#!/usr/bin/python
import os
import sys
import operator
import csv

topn=int(sys.argv[1])

def c(n,k):  
    return  reduce(operator.mul, range(n - k + 1, n + 1)) /reduce(operator.mul, range(1, k +1))

def N_K_a(n,k,i):
	if i in N_K_as[k]:
		return N_K_as[k][i]
	if i>k:
		N_K_as[k][i]=0
		for j in range(1,i-k+1):
			N_K_as[k][i]+=(-c(n-i+j,j))*N_K_a(n,k,i-j)
		return N_K_as[k][i]

def N_K_b(n,k,i):
	bi=0
	for j in range(k,i+1):
		bi+=c(n,j)*N_K_a(n,j,i)
	#print "("+str(n)+","+str(k)+") fork-join b_"+str(i)+": "+ str(bi)
	return bi

N_K_bs={ n:{ k:[0]*n  for k in range(1,n+1)} for n in range(1,topn+1)}
for n in N_K_bs:
	for k in range(1,n+1):
		N_K_as={ j:{j:1} for j in range(k,n+1)}
		sum_b=0
		for i in range(k,n+1):
			N_K_bs[n][k][i-1]=N_K_b(n,k,i)
	        	sum_b+=N_K_bs[n][k][i-1]
		#print "A of (%d, %d) FJ is: %d" %(n,k,sum_b)
#print N_K_bs
#print N_K_as #coefficients of ("+n+","+k+") fork-join queues

for (n,ks) in N_K_bs.items():
	for (k,i_s) in ks.items():
		print str(n)+","+str(k)+","+",".join(str(x) for x in i_s)
