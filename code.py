#you may see examples of the lines step by step in commemt
sent=str(input()) #go to run
n=0
newlist=list()
words=sent.split(" ") #words=('go','to','run')
while n<len(words):
 word=words[n] #word=('go')
 letters=list(word) #letters=('g','o')
 fl=letters[0] #fl=('g')
 ll=int(len(letters)) #ll=2
 newletters=letters.insert(ll,fl) #newletters=('g','o','g')
 newletters=letters[1:] #newletters=('o','g')
 newletters.append('ay') #newletters=('o','g','ay')
 newword="".join(newletters) #newword=('ogay')
 newlist.append(newword)
 n=n+1
print(" ".join(newlist))
