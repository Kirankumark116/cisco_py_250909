words_str=input("Sentence: ")
sentence_list=[chr_list.upper() for chr_list in words_str.split()]
print(sentence_list)
sentence_tuple=tuple(sentence_list)
print(sentence_tuple)

file_name="sentence_data.txt"
with open(file_name,'w') as writer:
    writer.write(f'List:{sentence_list}\n')
    writer.write(f'Tuple:{sentence_tuple}\n')
    
with open(file_name,'r') as reader:
    line_list=reader.readline()
    line_tuple=reader.readline()
    print(line_list)
    print(line_tuple)

