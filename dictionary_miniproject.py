print("Welcome to pythonlife DICTIONARY!")
print('-'*25)
x=int(input("enter number:"))
dictinoary_data={}
for i in range (x):
  word=input("enter the word:")
  Meaning=input("enter the meaning:")
  dictinoary_data[word]=Meaning
  print(dictinoary_data)
mode=int(input("enter the number:"))
if mode==1:
    word=input("enter the word:")
    print(dictinoary_data.get(word))
elif mode==2:
      print(dictinoary_data.items())
elif mode==3:
    print(dictinoary_data.keys())
elif mode==4:
    print(dictinoary_data.values())
elif mode==5:
    word=input("enter the word:")
    print(dictinoary_data.pop(word))
    word=input("enter the word:")
    print(dictinoary_data.pop(word))
elif mode == 6:
    newword = input("Enter the word: ")
    if newword in dictinoary_data:
        new_Meaning = input("Enter the new meaning: ")
        dictinoary_data[newword] = new_Meaning
        print("Updated Dictionary:", dictinoary_data)
    else:
        print("Word not found")
else:
    print("exit the program")