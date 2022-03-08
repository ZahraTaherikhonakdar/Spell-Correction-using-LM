from nltk.corpus import brown
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE
import dill as pickle

path="Models"
df=brown.words(categories='news')

# Preprocess the tokenized text for 3-grams language modelling
tokenized_text = [sent.lower() for sent in df]

n_gram=[1,2,3,5,10]
for n in n_gram:
    train_data, padded_sents = padded_everygram_pipeline(n, [tokenized_text])
    print(f'train a {n}_gram model')
    model = MLE(n)
    model.fit(train_data, padded_sents)
    with open('{}/{}_gram_model.pkl'.format(path,n), 'wb') as save:
        pickle.dump(model, save)
        print(f'saved {n}_gram model ...{path}')