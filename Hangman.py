import random
manTemplate = ["|","____","   }","   O","  -|-","  ( )","==="]
wordsets = ["nouns.txt","potter.txt","avengers.txt","countries.txt"]

def wordGen(fileName,diff):
  lower = 3 + 3*(diff-1)
  upper = lower + 2
  if diff == 3 or diff == 4:
    upper = 30
  if diff == 4:
    lower = 4  
  with open (fileName, "r") as myfile:
    data=myfile.readlines()
  dict = data[0].split(" ")  
  pos = random.randint(0,len(dict))
  word = dict[pos]
  while len(word) > upper or len(word) < lower:
     pos = random.randint(0,len(dict))
     word = dict[pos]
  if "+" in word:
    word = word.replace("+"," ")       
  return word

def optionSelect(q,op1,op2,op3,op4):
  num = False
  while num == False:
    a = input("\n{0}\n 1.) {1}\n 2.) {2}\n 3.) {3}\n 4.) {4}\n \n ".format(q,op1,op2,op3,op4))
    if int(a) == 1 or int(a) == 2 or int(a) == 3 or int(a) == 4: 
      num = True
  a = int(a)    
  return a

def play(file,diff,p = 7,man = ["|"," "," "," "," "," "," "]):
  playing = True
  incorrect = []
  word = wordGen(file,diff)
  guesses = []
  for x in word:
    if x != " " or x != "(" or x!= ")":
      guesses.append("_")
  while playing:
    val = 7 - p
    if val == 1:
      man[6] = manTemplate[6]
    print("\n"+" ".join(guesses)+"\n")
    for x in range (1,len(man)):
      if val - 2 == x:
        man[x] = manTemplate[x]  
      if x > 1 and x != 6 and p < 6:
        print(man[0] + man[x])
      else:
        print(man[x])
    if p == 0:
      print("You Lose!\n The word was '{0}'".format(word))
      break
    if "".join(guesses) == word:
      print("You Win!")
      break
    guess = input("\nIncorrect Letters:{1}\nLives:{0}\nGuess a letter: ".format(p,incorrect))
    correct = False
    for x in range (0,len(word)):
      if guess == word[x].lower():
        guesses[x] = guess
        correct = True
    if correct == False and guess not in incorrect:
      p -=1
      incorrect.append(guess)
  return man, p

def endless(file,diff):
  p = 7
  man = ["|"," "," "," "," "," "," "]
  while p!= 0:
    man, p = play(file,diff,p,man)       
      
def main():
  looping = True
  while looping:
    print("\nPlay Hangman!\n ")
    w = optionSelect("Which wordset would you like to use?","Regular","Harry Potter","Avengers","World Countries") - 1 
    d = optionSelect("Which difficulty do you choose","Easy (3-5 letter words)","Medium (6-8 letter words)","Hard (9 letter words or more)","Endless Mode")
    if d == 4:
      func = endless
    else:
      func = play  
    func(wordsets[w],d)
    resp = input("\nPlay Again?\n \n")
    if resp[0].lower() == 'n':
      looping = False

main() 
