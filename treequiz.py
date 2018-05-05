print "Welcome to the Tree Quiz!"

def play():
  money = 0
  print "You have ", money, " dollars"
  
  question1 = raw_input("What is a tree? ")
  if(question1.lower() == "plant"):
    money = money + 100
    print "Correct! You have", money, "dollars!"
  else:
    print "Wrong!"
    
  question2 = raw_input("Trees use seeds to..? ")
  if(question2.lower() == "reproduce"):
    money = money + 200
    print "Correct! You have", money, "dollars!"
  else:
    print "Wrong!"
    
  question3 = raw_input("What element do trees store large quantities of in their tissues? ")
  if (question3.lower() == "carbon"):
    money = money + 300
    print "Correct! You have", money, "dollars!"
  else:
    print "Wrong!"
    
  question4 = raw_input("A tree has many secondary branches supported by..? ")
  if(question4.lower() == "trunk"):
    money = money + 400
    print "Correct! You have", money, "dollars!"
  else:
    print "Wrong!"
  
  question5 = raw_input("Most tree trunks and branches are surrounded by a layer of..? ")
  if(question5.lower() == "bark"):
    money = money + 500
    print "Congrations! You have won", money, "dollars!"
  else:
    print "Wrong! Game over."
    print "You leave with", money, "dollars" 
    
play()