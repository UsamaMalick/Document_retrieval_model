
import os , re , string
# Load library

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def load_inverted_index():
    path = "term_index.txt"
    file = None
    try:
        file = open(path , "r")
    except IOError:
        print("File Error occurred!")

    content = file.read().split('\n')


    print(content[10:2])


def query_pre_processing(query):
    preprocessed_query = []
    stop_words = stopwords.words('english') # loading stopwords from nltk
    for word in query:
        preprocessed_query.append(re.sub(r'\w*\d\w*', '',   word.lower())) # removing numeric entries and lowercase

    preprocessed_query = [word for word in preprocessed_query if word not in stop_words] # removing stop words
    ps = PorterStemmer()
    preprocessed_query = [ps.stem(word) for word in preprocessed_query] # stemming words

    return preprocessed_query


def get_queries():
    file = None
    try:
        file = open("query.txt" , "r")
    except IOError:
        print("File Error occurred!")

    query  = {}
    content = file.read().split('\n')
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation)) #mapping punctuation to space
    for line in content:
        line = line.translate(translator)
        query_temp = line.split()
        if query_temp != []:
            query[query_temp[0]] = {"words"  : []}
            query[query_temp[0]]["words"] = query_temp[1:]

    return query


def load_dictionary():
    corpus = {}
    path = "term_ids.txt"
    try:
        file = open(path , "r")
    except IOError:
        print("File Error occurred!")
        return -1  # return -1 if error occurs

    content = file.read().split()
    for i in range(0, len(content) , 2):
        corpus[content[i+1]] = content[i]

    return corpus


def load_doc_ids():
    doc_ids = {}
    path = "doc_ids.txt"
    try:
        file = open(path , "r")
    except IOError:
        print("File Error occurred!")
        return -1  # return -1 if error occurs

    content = file.read().split()
    for i in range(0, len(content) , 2):
        doc_ids[content[i+1]] = content[i]

    return doc_ids


queries = get_queries()
corpus = load_dictionary()
doc_ids = load_doc_ids()


query_list =  query_pre_processing(queries["701"]["words"])

load_inverted_index()

#
# for word in query_list:
#     if corpus[word] is not None:
#         print(corpus[word] + " : " + word)
#     else:
#         print(word + "does'nt exist in corpus.")
