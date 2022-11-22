#sentence = "Just an example here move along" 
sentence = str(input("\nEnter Your Sentence :"))

print(sentence.split())
count = len(sentence.split())
print("Number of words : " , count)