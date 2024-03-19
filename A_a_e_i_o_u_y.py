Len=int(input())
word=input()

vowels=['a', 'e', 'i', 'o', 'u', 'y']
corrected_word=word[0]
for i in range(1,Len):
    if word[i] in vowels and word[i-1] in vowels:
        continue
    else:
        corrected_word+=word[i]
print(corrected_word)