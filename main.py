
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
    if term in corpus:
        # print(corpus[term] + " : " + term)
        return corpus[term]
    else:
        print("The ( " + term + " ) does'nt exist in corpus.")
        return None

def get_DocName(ID):
    for key , value in doc_ids.items():
        if value == ID:
            return key

    return -1

def query_pre_processing(query):
    preprocessed_query = []
    stop_words = stopwords.words('english') # loading stopwords from nltk
    for word in query:
        preprocessed_query.append(re.sub(r'\w*\d\w*', '',   word.lower())) # removing numeric entries and lowercase

    preprocessed_query = [word for word in preprocessed_query if word not in stop_words] # removing stop words
    ps = PorterStemmer()
    preprocessed_query = [ps.stem(word) for word in preprocessed_query] # stemming words

    for new_words in preprocessed_query:
        term_ID = get_termID(new_words)
        if term_ID is None:
            preprocessed_query.remove(new_words)

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


def my_output(document_IDs):
    print(document_IDs)
    try:
        my_output = open("my_output.txt", "w")
    except IOError:
        print("File Error occurred!")
        return

    for key , value in document_IDs.items():
        print(len(value))
        for IDs in value:
            name = get_DocName(str(IDs))
            if name != -1:
                entry = key + " " + str(name) + '\n'
                my_output.write(entry)
            else: print("Name not found")

    my_output.close()

def search_query_docs(query_words):

    keys_list = []
    temp_keys_list = []
    intersection_list = []
    first_loop = True
    for word in query_words: # this for loop will make a list of all the documents that have the query words
        term_ID = get_termID(word)
        if term_ID is not None:
            doc_and_pos = hash_inverted_index[term_ID]["doc_pos"]
            for key in doc_and_pos:
                temp_keys_list.append(int(key))

            if first_loop == True:
                keys_list  = [value for value in temp_keys_list]
                first_loop = False
            else:
                for numbers in temp_keys_list:
                    if numbers in keys_list:
                        intersection_list.append(numbers)
                # intersection_list = [value for value in keys_list if value in temp_keys_list]
                temp_keys_list.clear()
                keys_list.clear()
                keys_list = [value for value in intersection_list]
                intersection_list.clear()

    term_pos_list = {}
    document_with_queries = []

    for doc_num in keys_list:
        # print("Checking for Document number : " + str(doc_num))
        term_pos_list.clear()
        for word in query_words:
            term_ID = get_termID(word)
            if term_ID is not None:
                if doc_num is not None:
                    if int(doc_num) in hash_inverted_index[term_ID]["doc_pos"] :
                        term_pos_list[term_ID] = hash_inverted_index[term_ID]["doc_pos"][int(doc_num)]

        dic_keys = list(term_pos_list.keys())
        length = len(dic_keys)
        present = True

        match_number = -2
        for i in range(length-1):
            list1 = term_pos_list[dic_keys[i]]
            list2 = term_pos_list[dic_keys[i+1]]
            match_number = match_number + 1

            for item in list1:
                if match_number == -1:
                    match_number = int(item) + 1

                if str(match_number) in list2:
                    present = True
                    break
                else:
                    match_number = -1
                    present = False

            if present == False:
                break

        document_with_queries.append(doc_num)

    return document_with_queries



queries = get_queries()
corpus = load_dictionary()
doc_ids = load_doc_ids()
inverted_index = load_inverted_index()

hash_inverted_index  = restructuring_inverted_index()

def main():

    document_IDs = {}
    for key , value in queries.items():
        query_ID = key

        query_words =  query_pre_processing(queries[query_ID])

        print("Checking for query : " + str(query_words))
        #checking query as tri-words
        tri_word = []

        temp_query_words = [value for value in query_words]
        document_IDs[query_ID] = []
        for k in range(len(temp_query_words)-2):
            i = 0
            tri_word.clear()
            for item in temp_query_words:
                tri_word.append(item)
                i = i + 1
                if i == 3:
                    temp_query_words.remove(temp_query_words[0])
                    break

            document = search_query_docs(tri_word)
            document_IDs[query_ID] = [value for value in document if value not in document_IDs]

            document_IDs[query_ID] = list(dict.fromkeys(document_IDs[query_ID]))

        print("Documents find with tri words")


        if document_IDs[query_ID] == []:
            #check for query as bi-words
            bi_word = []
            temp_query_words = [value for value in query_words]
            for k in range(len(temp_query_words)-1):
                i = 0
                bi_word.clear()
                for item in temp_query_words:
                    tri_word.append(item)
                    i = i + 1
                    if i == 2:
                        temp_query_words.remove(temp_query_words[0])
                        break
                #fucntion call
                print(bi_word)
                document = search_query_docs(bi_word)
                document_IDs[query_ID] = [value for value in document if value not in document_IDs]
                document_IDs[query_ID] = list(dict.fromkeys(document_IDs[query_ID]))


    my_output(document_IDs)
    print("The End")




main()

