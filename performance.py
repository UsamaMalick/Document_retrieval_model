

def read_file_data(filename):
    output = {}
    try:
        output_file = open(filename, "r")
    except IOError:
        print("File Error occurred!")
        return
    content = output_file.read().split('\n')

    for i in range(701 , 851):
        output[str(i)] = []


    for entries in content:
        entries =  entries.split()
        if entries != []:
            output[entries[0]].append(entries[1])

    return output


output = read_file_data("output.txt")
my_output = read_file_data("my_output.txt")



false_positive = 0  #false positive is when a good quality item gets rejected
false_negative = 0  #false negative is when a poor quality item gets accepted

true_positive = 0  #true positive is an outcome where we correctly predicts the positive class.
true_negative = 0  #true negative is an outcome where we correctly predicts the negative class.

my_results = []
total = 0
accuracy_sum = 0
precision_sum = 0
recall_sum = 0

for i in range(701 , 851):

    if my_output[str(i)] != [] :
        true_positive = abs(len(list(set(output[str(i)]) & set(my_output[str(i)]))))
        false_negative = abs(len(list(set(my_output[str(i)]) - set(output[str(i)]))))
        false_positive = abs(len(list(set(output[str(i)]) - set(my_output[str(i)]))))
        irrelevant = 6376 - abs(len(set(output[str(i)])))
        true_negative = irrelevant - false_negative

        #accuracy
        nominator = true_positive + true_negative
        denominator = nominator + false_negative + false_positive
        accuracy = round(  (nominator/denominator ) * 100 )
        accuracy_sum = accuracy_sum + accuracy

        #precision
        nominator = true_positive
        denominator = true_positive + false_positive
        precision = round( (nominator/denominator) * 100 )
        precision_sum = precision_sum + precision

        #recall
        nominator = true_positive
        denominator = true_positive + false_negative
        recall = round(  (nominator/denominator) * 100 )
        recall_sum = recall_sum + recall

        writing = str(i) + '\t' + str(accuracy) + '\t' + str(precision) + '\t' + str(recall) + '\n'
        my_results.append(writing)
        # performance_file.write(writing)

        total = total + 1

    else: print(i)


recall_average = recall_sum/total
accuracy_average = accuracy_sum/total
precision_average = precision_sum/total


average = str(accuracy_average) + '\t' + str(precision_average) + '\t' + str(recall_average) + '\n'


try:

    performance_file = open("performance.txt", "w")
    average_file = open("average.txt" , "w")

    for lines in my_results:
        performance_file.write(lines)

    print(average)
    average_file.write(average)
except:
    print("File Error")

# print(average)
