# SEIBIE
Information Entropy Based Knowledge Graph Sensitive Entity Detection
#RUN preprocess.py 
python C:\Users\Dell\Desktop\preprocess.py --input "C:\\Users\\Dell\\Downloads\\KGdatasets-main\\UMLS\\train.txt" --K 5 --sep '\t' --output 'res.csv' 


parameters：
--input  entites triples
--K	 sensitive level
--sep    sep symbol between entities in input file
--output output result

numpy==1.23.5 scipy==1.10.0
