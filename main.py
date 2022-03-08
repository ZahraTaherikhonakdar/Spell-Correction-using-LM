from nltk.corpus import brown
from nltk import word_tokenize
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE
import dill as pickle
import json

path="Models"
df=brown.words(categories='news')

# Preprocess the tokenized text for 3-grams language modelling
tokenized_text = [sent.lower() for sent in df]

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


n_gram=[5,10]
for n in n_gram:
    k = n
    top_10 = {}
    top_10['{}_gram'.format(n)] = []
    with open('Models/{}_gram_model.pkl'.format(n), 'rb') as fin:
        model = pickle.load(fin)

    for a in range(len(sentence)):
        result={}
        result['top_10_sentence_{}'.format(a)]=[]
        sort_array = {}
        sort_array['sentences_{}'.format(a)]=[]
        for token in tokenized_text:
            set = []
            set_reversed = []
            if k > len(sentence[a]):
                list1 = []
                if len(sentence[a]) != 0:
                    num = model.counts[sentence[a]][token]
                    list1.append(num)
                    list1.append(token)
                    # print("whole ",num,'one')
                if len(list1) != 0:
                    sort_array['sentences_{}'.format(a)].append(list1)
            else:
                for p in range(len(sentence[a]) - 1, len(sentence[a]) - k - 1, -1):
                    set.append(sentence[a][p])
            list2 = []
            if len(set) != 0:
                for r in reversed(set):
                    set_reversed.append(r)

                num2 = model.counts[sentence[a]][token]
                list2.append(num2)
                list2.append(token)
                # print("partial ", num2, 'one')
            if len(list2) != 0:
                sort_array['sentences_{}'.format(a)].append(list2)

       # print(f'sentect{a}',sort_array)
        y = sorted(sort_array['sentences_{}'.format(a)], key=lambda x: x[0], reverse=True)[:10]

        result['top_10_sentence_{}'.format(a)].append(y)
       # print(result)
        top_10['{}_gram'.format(n)].append(result)
    #print(top_10)
    sen_json = json.dumps(top_10)
    with open('top_10/{}_gram_top10.json'.format(n), 'w') as f:
       f.write(sen_json)

    print(f'finish {n}_gram')
#load models

