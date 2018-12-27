import pandas as pd
import progressbar

p = progressbar.ProgressBar()
sam = pd.read_csv("../data/sample_submission.csv")
re = pd.read_csv("result.csv")
for index in p(range(len(re))):
    a = re.iloc[index,1]
    fm = a[1:83].split(", ")
    fml=list(map(int,fm))
    k=[]
    for i, item in enumerate(fml):
        if item==1:
            k.append(i)
    res=' '.join(map(str,k))
    sam.iloc[index,1]=res
sam.to_csv("submission.csv",index=False)
