#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 15:51:36 2020

@author: SteliosMavrotas
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snb
import numpy
from datetime import datetime
import yfinance as yf
import numpy as np
import itertools


etfs=['SPY', 'IVV', 'VTI','VOO','QQQ','VWO','VEA','IEFA','EFA','AGG']
color="#E9F5FF"

data=pd.DataFrame([])
for i in etfs:
    a=yf.Ticker(i)
    prices=a.history(period='max',interval='1d')
    prices=prices.drop(prices.index[np.where(prices.index<'2012-10-24 00:00:00')])
    data[i]=prices['Close']
    

correlation=data[[i for i in etfs]]
    
correlation=pd.DataFrame({y:x for y,x in zip(etfs,np.corrcoef(correlation,rowvar=False))})
    
correlation["index"]=pd.DataFrame(etfs)
correlation=correlation.set_index("index")

    
combinations=np.array([i[0]+i[1] for i in list(itertools.product(etfs,repeat=2))])


fgr=plt.figure(2)
mask = np.zeros_like(correlation, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
ax=snb.heatmap(correlation,cmap="Oranges",linewidths=0,square=True, mask=mask,cbar_kws={"shrink": .5})
fgr.set_facecolor(color)
fgr.set_edgecolor(color)
ax.set_facecolor(color)
plt.ylabel("ETF Index")
plt.xlabel("ETF Index")
plt.xticks(rotation="vertical")
plt.yticks(rotation="horizontal")
fgr.savefig("Heatmap.png",dpi=500,edgecolor=color,facecolor=color,bbox_inches='tight')
