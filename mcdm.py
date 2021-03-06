import sys
import pandas as pd
     
def main():
    dataset=pd.read_csv(sys.argv[1]).values
    weights=[int(i) for i in sys.argv[2].split(',')]
    maxmin=sys.argv[3].split(',')
    topsis(dataset,weights,maxmin)
    
if __name__=="__main__":
     main()
     
def topsis(dataset,weights,maxmin):
    #importing libraries
    import numpy as np
    import math as m
    
    #    #importing dataset
    #    dataset=pd.read_csv("E:/Mobiles - Sheet1.csv")
    
    #dataset as n d array
    a=dataset.iloc[:,:].values
    a=a.astype(dtype='float')
    
    #calculating no. of rows and no. of columns
    row_count=a.shape[0]
    col_count=a.shape[1]
    
    #    #initializing weights
    #    print("Enter weights: ")
    #    weights=[]
    #    for i in range(0,col_count):
    #        weights.append(float(input()))
        
    #    #entering + to maximize and - to minimize
    #    print("Entering + to maximize and - to minimize")
    #    maxmin=[]
    #    for i in range(0,col_count):
    #        maxmin.append(input())
    
    #normalizing matrix
    for j in range(0,col_count):
        s=0
        for i in range(0,row_count):
            s=s+a[i,j]*a[i,j]
        s=m.sqrt(s)
        for i in range(0,row_count):
            a[i,j]=a[i,j]/s
    
    #multiplying by weights
    for j in range(0,col_count):
        for i in range(0,row_count):
            a[i,j]=a[i,j]*weights[j]
    
    #calculating vj+ and vj-
    v_best=[]
    v_worst=[]
    for j in range(0,col_count):
        if(maxmin[j]=='+'):
            v_best.append(max(a[:,j]))
            v_worst.append(min(a[:,j]))
        elif(maxmin[j]=='-'):
            v_best.append(min(a[:,j]))
            v_worst.append(max(a[:,j]))
    
    #calculating si+ and si-
    s_best=[]
    s_worst=[]
    for i in range(0,row_count):
        t=0
        s=0
        for j in range(0,col_count):
            t=t+(a[i,j]-v_best[j])*(a[i,j]-v_best[j])
            s=s+(a[i,j]-v_worst[j])*(a[i,j]-v_worst[j])
        s_best.append(m.sqrt(t))
        s_worst.append(m.sqrt(s))
    
    #calculating topsis score
    pi=[]
    for i in range(0,row_count):
        pi.append(s_worst[i]/(s_worst[i]+s_best[i]))
    
    #copying pi
    pi_temp=pi.copy()
    
    #calculating rank
    rank=[]
    for i in range(0,row_count):
        rank.append(0);
    t=1;
    for i in range(0,row_count):
        d=pi_temp.index(max(pi_temp)) 
        pi_temp[d]=-1
        rank[d]=t
        t=t+1
    
    dataset['performance score']=pi
    dataset['rank as per topsis']=rank
    print(dataset)
    return dataset


    

    
    
    


