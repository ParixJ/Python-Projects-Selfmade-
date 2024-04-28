import sys 
for words in sys.stdin: 
    if 'quit' == words.rstrip(): 
        break
    print(f'Input : {words}') 
  
print("Exit!!")