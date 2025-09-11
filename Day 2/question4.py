words_str=input("sentence: ")
sentence_list=[words for words in words_str.split()]
sentence_list.sort()
print(sentence_list)

file_name='Names_data.txt'
with open(file_name,'w') as writer:
    writer.write(f'List:{sentence_list}\n')

with open(file_name,'r') as reader:
    line_list=reader.readline()
    print(line_list)

