import csv
import sys
import pandas as pd
import numpy as np
from random import shuffle
from numpy.random import seed, rand
import pdb

csv.field_size_limit(100000000)
seed(43)

filename = ['rw_label.tsv','cp_label.tsv']  #,'oci_text_par.tsv'
# print(np.random.randint(1))

def ranwrite(row):
    # print(type(row))
    # pdb.set_trace()
    ran = rand(1)
    if ran <= 0.2:
        with open('dev.tsv','a',encoding='utf-8') as f:
            writer = csv.writer(f,delimiter='\t')
            writer.writerow(row)
            # f.write(row + '\n')
    elif ran >= 0.8:
        with open('test.tsv','a',encoding='utf-8') as f:
            writer = csv.writer(f,delimiter='\t')
            writer.writerow(row)
    else:
        with open('train.tsv','a',encoding='utf-8') as f:
            writer = csv.writer(f,delimiter='\t')
            writer.writerow(row)
    pass

def realwrite(row):
    with open('alltext.tsv','a',encoding='utf-8') as f:
        writer = csv.writer(f,delimiter='\t')
        writer.writerow(row)
    pass

def allwrite():
    for file in filename:
        with open(file,'r',encoding='utf-8') as f:
            reader = csv.reader(f,delimiter='\t')
            for row in reader:
                realwrite(row)
    pass

def allshuffle():
    df = pd.read_csv('alltext.tsv','r',encoding='utf-8',header=None)
    df = df.values
    shuffle(df)
    pdb.set_trace()
    np.savetxt('allshuffle.tsv',df,fmt='%s')
    pass

def shf():
    lines = open('alltext.tsv').readlines()
    shuffle(lines)
    open('alltext_sf.tsv','w').writelines(lines)
    pass

def main():
    # allwrite()
    # allshuffle()
    # shf()
    with open('all.tsv','r',encoding='utf-8') as f:
        reader = csv.reader(f,delimiter='\t')
        for row in reader:
            if len(row) ==2 and len(row[0]) >= 10 and rand(1) <= 0.4:
                ranwrite(row)


if __name__ == "__main__":
    main()

# for file in filename:
#     with open(file,'r',encoding='utf-8') as f:
#         reader = csv.reader(f,delimiter='\t')
#         for row in reader:
#             # pdb.set_trace()
#             if row[-1] != 0.5:
#                 row[-1] = int(float(row[-1]))
#                 if type(row[-1]) == float:
#                     print(row)
#                     pdb.set_trace()
#                 realwrite(row)