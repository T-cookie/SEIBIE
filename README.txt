运行文件 preprocess.py 格式为 
python C:\Users\Dell\Desktop\preprocess.py --input "C:\\Users\\Dell\\Downloads\\KGdatasets-main\\UMLS\\train.txt" --K 5 --sep '\t' --output 'res.csv' 注意：windows系统路径应转义

参数：
--input  需要识别的知识图谱，格式见示例 train.txt，注意只能为txt文件，其他格式需转换
--K	 需要分类的敏感等级，如分为3级，则K=3
--sep    实体之间的分隔符，默认为'\t'，一个制表符
--output 输出数据，结果示例见res.csv，只能输出csv格式

版本 numpy==1.23.5 scipy==1.10.0