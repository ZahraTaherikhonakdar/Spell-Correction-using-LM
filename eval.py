import json

import pytrec_eval
sent= open('APPLING1DAT.643','r').readlines()

misspell=[]
correct=[]
sub_sent=[]
sentence=[]
j=0
for x in sent:

    if (x[0].startswith("$")):
        pass;
    else:
        j +=1
        data=[]
        #data[j]=[]
        misspell.append(x.split()[0])
        correct.append(x.split()[1])
        i=(len(x.split())+2)
        for i in range(2,len(x.split())):
            if x.split()[i]=="*":
                break;
            else:
                data.append(x.split()[i])
        sub_sent.append(data)
        sentence.append(data)

evaluator = pytrec_eval.RelevanceEvaluator(correct, {'success_1', 'success_5', 'success_10'})
n_gram=[1]
for n in n_gram:
  with open('top_10/{}_gram_top10.json'.format(n), 'r') as f:
       data_result=json.load(f)
  for key, value in data_result.items():
    print("key issssssssssssssss:" ,value[0]['top_10_sentence_0'])
