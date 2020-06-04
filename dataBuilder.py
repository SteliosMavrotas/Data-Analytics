#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 10:28:43 2020
numpy.random.rand(3,)
@author: SteliosMavrotas
"#C3E0FA"
#8adeeb
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbrn
import numpy
from datetime import datetime

data=pd.read_excel('Data.xlsx')
data['index']=data.index    
data.index=data['Unnamed: 0']

business=data[['Business Chapter 7 ', 'Business Chapter 11','Business Chapter 13 ','index']]
nonbusiness=data[['Non-Business  Chapter 7', 'Non-Business  Chapter 11','Non-Business  Chapter 13 ','index']]

color="#E9F5FF"
count=1

for i in business.columns[:-1]:
    fgr=plt.figure(count)
    ax=sbrn.regplot(x='index',y=i,data=business,color="#3B50A4")
    fgr.set_facecolor(color)
    fgr.set_edgecolor(color)
    ax.set_facecolor(color)
    '''ax.set_facecolor('#8adeeb')
    ax.patch.set_alpha(0.5)'''
    ax.set_xticklabels([0]+[datetime.strftime(i,'%b-%y') for i in business.index if int(str(i)[5:7])%2>0])
    plt.ylabel("No. of Bankruptcies")
    plt.title('Business '+str(i[9:]))
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    count+=1    
    
    if i!="Business Chapter 7 ":
        plt.tick_params(labelbottom=True,bottom=False,left=False)
        plt.xlabel("")
    else:
        ax.spines['bottom'].set_visible(False)
        plt.tick_params(labelbottom=True,bottom=False,left=False)
        plt.xlabel("Date")
        
    plt.savefig(str(i[9:])+".png",dpi=1000,edgecolor=color,facecolor=color)

for i in nonbusiness.columns[:-1]:
    fgr=plt.figure(count)
    ax=sbrn.regplot(x='index',y=i,data=nonbusiness,color="#3B50A4")
    fgr.set_facecolor(color)
    fgr.set_edgecolor(color)
    ax.set_facecolor(color)
    ax.set_xticklabels([0]+[datetime.strftime(i,'%b-%y') for i in nonbusiness.index if int(str(i)[5:7])%2>0 ])
    '''ax.set_facecolor('#8adeeb')'''
    plt.ylabel("No. of Bankruptcies")
    plt.title('Non-Business'+str(i[12:]))  
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    
    if i!="Non-Business  Chapter 7":
        plt.tick_params(labelbottom=True,bottom=False,left=False)
        plt.xlabel("")
    else:
        ax.spines['bottom'].set_visible(False)
        plt.tick_params(labelbottom=True,bottom=False,left=False)
        plt.xlabel("Date")
        
    plt.savefig(str(i[9:])+".png",dpi=1000,edgecolor=color,facecolor=color)
    count+=1    


