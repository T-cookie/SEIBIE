# -*- coding: utf-8 -*-
"""
Created on Sat May 20 09:45:42 2023

@author: Dell
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
#pd.set_option('display.max_columns', None)
import time
import argparse  
  
parser = argparse.ArgumentParser(description='Process some integers.')  
parser.add_argument('--input', type=str, help='Input value')  
parser.add_argument('--output', type=str, help='Output value')  
parser.add_argument('--K', type=int, help='K clusters')
parser.add_argument('--sep', type=str, help='sep symbol')
args = parser.parse_args()  
time_start = time.perf_counter()  # 记录开始时间

def get_entropy(data_df,columns = None):
    if (columns is None) and (data_df.shape[1] > 1) :
        raise "the dim of data_df more than 1, the columns must be not empty!"    
    # 信息值
    pe_value_array = data_df[columns].unique()
    ent = 0.0
    for x_value in pe_value_array:
        p = float(data_df[data_df[columns] == x_value].shape[0]) / data_df.shape[0]
        logp = np.log2(p)
        ent -= p * logp
    
    return ent

    
    
def get_sensitive(datas):
    d=[]
    
    #res = pd.DataFrame(None,columns=['r','r-h','r-t'])
    class_list = list(datas['r'].drop_duplicates())
    for i in class_list:
        rdata = datas[datas['r']==i]
        lens=len(rdata)
        #print(rdata)
        #e.append(rdata)
        
        [h_e,t_e]=[get_entropy(rdata,'h'),get_entropy(rdata,'t')]
        [h_s,t_s]=[1-h_e/np.log2(lens),1-t_e/np.log2(lens)]
        ent_arr=[i,h_s,t_s]
        d.append(ent_arr)
    res=pd.DataFrame(d,columns=['r','r-h','r-t'])
    #res.to_csv(r"C:\Users\Dell\Downloads\KGdatasets-main\UMLS\re_en.csv",index=False)
    #print (res)
    return res


def init_kg(datas):
    
    #ids.insert(loc=2, column='ent', value=0)
    ent=get_sensitive(datas)
    
    init=pd.merge(datas,ent,how='outer',on='r') 
    
    groupedh = init.groupby('h').sum() # 以r-h 为key 求和
    groupedh['e']=groupedh.index
    groupedh.drop('r-t',axis=1,inplace=True)
    groupedt = init.groupby('t').sum()
    groupedt['e']=groupedt.index
    groupedt.drop('r-h',axis=1,inplace=True)
    merge=pd.merge(groupedh,groupedt,how='outer',on='e')
     #groupedh['r-t']=groupedt['r-t']
    #print(groupedt)
    #print(merge)
    
    return merge
    #groupedh.columns = ['e','r-h']
    #ph=pd.DataFrame(groupedh)
    
    #print(ph)
  
    #return pd.merge(groupedh,groupedt,how='outer',on='e')

    #for j in ids['e']:
        #print (datas['h']==j)
#金融数据集读取分割符号为" "，UMLS数据集读取分割符号为"\t"
def entropy(datas_path,sepstr):
    datas = pd.read_csv(datas_path, names=['h','r','t'], header=None, sep=sepstr) # 获取日期数据
    #datas.to_csv(r"C:\Users\Dell\Downloads\KGdatasets-main\UMLS\datas.csv",index=False)
    #ids = pd.read_csv(ids_path, names=['e','id'], header=None, sep="\t") # 获取日期数据
    return init_kg(datas)    
if __name__=="__main__":
    #datas_path=r"C:\Users\Dell\Downloads\KGdatasets-main\UMLS\train.txt"
    
    #ids_path=r"C:\Users\Dell\Downloads\KGdatasets-main\UMLS\entity2id.txt"
    
    res=entropy(args.input,args.sep)
    res=res.fillna(value=0)
    time_end = time.perf_counter()  # 记录结束时间
    time_sum = time_end - time_start  # 计算的时间差为程序的执行时间，单位为秒/s
    
    
    
#datas.set_index('r')
#print(datas)
#print(datas.index)
#relation = datas['r'].unique()
#print(relation)
