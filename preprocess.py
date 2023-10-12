# -*- coding: utf-8 -*-
"""
Created on Sun May 21 09:49:33 2023

@author: Richbinbin
"""
from entropy import entropy
from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt
#from sklearn.metrics import silhouette_score
#from scipy.spatial.distance import cdist
import argparse  
  
parser = argparse.ArgumentParser(description='Process some integers.')  
parser.add_argument('--input', type=str, help='Input value')  
parser.add_argument('--output', type=str, help='Output value')  
parser.add_argument('--K', type=int, help='K clusters')
parser.add_argument('--sep', type=str, help='sep symbol')
args = parser.parse_args()  

#pd.set_option('display.max_columns', None)
#np.set_printoptions(threshold=160)
def preprocess(datas_path,sepstr='\t',k=3):
    res=entropy(datas_path,sepstr)
    res=res.fillna(value=0)
    
    res['sum']=res[['r-h','r-t']].sum(axis=1)
    #print(res)
    array = np.array(res['sum']).reshape(-1, 1)
    #print(array)
    #K=range(2,3)
    score=[]
    sse_result=[]
    # for k in K:
    #     kmeans=KMeans(n_clusters=k)
    #     kmeans.fit(array)
    #     sse_result.append(sum(np.min(cdist(array,kmeans.cluster_centers_,'euclidean'),axis=1))/array.shape[0])
    #     score.append(silhouette_score(array,kmeans.labels_,metric='euclidean'))
    #plt.plot(K,score,'r*-')
    #print (sse_result)
    km = KMeans(n_clusters=k).fit(array)
    label=km.labels_
    res['label']=label
    #   0是非敏感级，  1是敏感级  2是较敏感级
    return res
   
    #print(km)
if __name__=="__main__":
   
    pre=preprocess(args.input,args.sep,args.K)
    pre.to_csv(args.output,columns=['e','label'],index=False)
    
   