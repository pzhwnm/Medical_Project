import pandas as pd
import os

from tqdm import tqdm


from time import sleep


filename=os.listdir("./categories/")
for name in tqdm(filename):
    sleep(0.1)
    with open("./categories/"+name,'r') as file:
        Symptoms_Item=[]
        for line in file:
            Symptoms_Item.append(line.strip())
        if len(Symptoms_Item)==0:
            data_item=[["时间",'姓名','年龄','性别','职业','联系方式','血压','疗程','治疗结果']+['诊疗过程']]
        else:
            data_item=[["时间",'姓名','年龄','性别','职业','联系方式','血压','疗程','治疗结果']+Symptoms_Item+['诊疗过程']]
        df1 = pd.DataFrame(data_item)
        df1.to_csv('./database/'+name[:-3]+'csv', mode='a',encoding='gb18030')
    sleep(0.1)
