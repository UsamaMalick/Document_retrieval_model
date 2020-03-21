
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

    inverted_index = {}

    for data in content:
        data = data.split()
        if data != []:
            if data[0] is not None:
                    inverted_index[data[0]] = {"total_occ": data[1],
                                     "total_doc":data[2],
                                     "doc_pos": data[3:]}

    return inverted_index

def restructuring_inverted_index():
    restructured_inverted_index = inverted_index
    for key , value in inverted_index.items():
        doc_pos = {}
        pos_list = []
        pre_doc_value = 0
        position = 0
        for doc_pos_list in value["doc_pos"]:

            doc_pos_list = doc_pos_list.split(',')
            pre_doc_value = int(doc_pos_list[0]) + pre_doc_value

            if int(doc_pos_list[0]) != 0:
                pos_list = []
                position = int(doc_pos_list[1])
            else:
                position = int(doc_pos_list[1]) + position

            pos_list.append(position)
            doc_pos[pre_doc_value] = pos_list

        restructured_inverted_index[key]["doc_pos"] = doc_pos

    return restructured_inverted_index


def get_termID(term):
    if corpus[term] is not None:
        print(corpus[term] + " : " + term)
        return corpus[term]
    else:
        print(term + "does'nt exist in corpus.")
        return None


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
            query[query_temp[0]]= query_temp[1:]

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

def search_query_docs(query_words):

    query_len = len(query_words)
    print(query_words)
    print(query_len)
    # for term in query_words:
    #     term_ID = get_termID(term)
    #     if term_ID is not None:
    #         doc_and_pos = hash_inverted_index[term_ID]["doc_pos"]
    #         print(doc_and_pos)
            # for value in doc_and_pos:
            #     value = value.split(',')



queries = get_queries()
corpus = load_dictionary()
doc_ids = load_doc_ids()
inverted_index = load_inverted_index()

# hash_inverted_index  = restructuring_inverted_index()

def main():
    query_words =  query_pre_processing(queries["701"])
    search_query_docs(query_words)

main()



# i = 1
# for key , value in queries.items():
#     query_words =  query_pre_processing(value)
#     for word in query_words:
#         if corpus[word] is not None:
#             print(corpus[word] + " : " + word)
#         else:
#             print(word + "does'nt exist in corpus.")
#
#
#     i = i + 1
#     if i > 2:
#         break
