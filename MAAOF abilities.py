x=0
global Death
global Bleeding
Death=False
Bleeding=False
damage=0
Hulk={"Name":"Hulk","Health":5970,"Stamina":4667,"Attack":1185,"Defense":1161,"Accuracy":968.0,"Evasion":909.0}
Thor={"Name":"Thor","Health":5982,"Stamina":5126,"Attack":1179,"Defense":1003,"Accuracy":1017.0,"Evasion":925.0}
Colossus={"Name":"Colossus","Health":5800,"Stamina":5264,"Attack":1025,"Defense":1218,"Accuracy":1052.0,"Evasion":929.0}
Quicksilver={"Name":"Quicksilver","Health":4678,"Stamina":6369,"Attack":970,"Defense":1040,"Accuracy":1160.0,"Evasion":1160.0}
Wolverine={"Name":"Wolverine","Health":5527,"Stamina":4519,"Attack":1268,"Defense":1086,"Accuracy":1041.0,"Evasion":946.0}
Sif={"Name":"Sif","Health":5523,"Stamina":5350,"Attack":1068,"Defense":1063,"Accuracy":1064.0,"Evasion":913.0, "Class":"Scrapper", "Bleeding":None}
#Player1=Wolverine
#Player2=Hulk
Hulk={"Name":"Hulk","Health":5970,"Stamina":4667,"Attack":1185,"Defense":1161,"Accuracy":968.0,"Evasion":909.0, "opponent":Wolverine, "Class":"Bruiser", "Bleeding":False}
Thor={"Name":"Thor","Health":5982,"Stamina":5126,"Attack":1179,"Defense":1003,"Accuracy":1017.0,"Evasion":925.0, "opponent":Wolverine, "Class":"Bruiser", "Bleeding":None}
Colossus={"Name":"Colossus","Health":5800,"Stamina":5264,"Attack":1025,"Defense":1218,"Accuracy":1052.0,"Evasion":929.0, "opponent":Wolverine, "Class":"Bruiser", "Bleeding":None}
Quicksilver={"Name":"Quicksilver","Health":4678,"Stamina":6369,"Attack":970,"Defense":1040,"Accuracy":1160.0,"Evasion":1160.0, "opponent":Wolverine, "Class":"Scrapper", "Bleeding":False}
Wolverine={"Name":"Wolverine","Health":5527,"Stamina":4519,"Attack":1268,"Defense":1086,"Accuracy":1041.0,"Evasion":946.0, "opponent":Sif, "Class":"Scrapper", "Bleeding":False}
Sif={"Name":"Sif","Health":5523,"Stamina":5350,"Attack":1068,"Defense":1063,"Accuracy":1064.0,"Evasion":913.0, "opponent":Wolverine, "Class":"Scrapper", "Bleeding":None}
def Hulk1():
  hit=1/(10**(-((Hulk["Accuracy"]+100)-Hulk["opponent"]["Evasion"])/400)+1)
  damage=round(Hulk["Attack"]-Hulk["opponent"]["Defense"]*(1-hit))
  Hulk["opponent"]["Health"]-=damage
  print Hulk["opponent"]["Name"],"'s health is",Hulk["opponent"]["Health"],"."
  Hulk["Stamina"]-=100
  Hulk["Attack"]+=100
  Hulk["Defense"]+=100
  Hulk["Accuracy"]+=100
  Hulk["Evasion"]+=100
  if (Hulk["opponent"]["Health"]<0):
    print Hulk["opponent"]["Name"],"died,",Hulk["Name"],"won."
    Death=True
    global Death
def Thor1():
  hit=1/(10**(-((Thor["Accuracy"]+100)-Thor["opponent"]["Evasion"])/400)+1)
  damage=round(Thor["Attack"]-Thor["opponent"]["Defense"]*(1-hit))
  Thor["opponent"]["Health"]-=damage
  print Thor["opponent"]["Name"],"'s health is",Thor["opponent"]["Health"],"."
  Thor["Stamina"]-=100
  if (Thor["opponent"]["Health"]<0):
    print Thor["opponent"]["Name"],"died,",Thor["Name"],"won."
    Death=True
    global Death
def Colossus1():
  hit=1/(10**(-((Colossus["Accuracy"]+100)-Colossus["opponent"]["Evasion"])/400)+1)
  damage=round(Colossus["Attack"]-Colossus["opponent"]["Defense"]*(1-hit))
  Colossus["opponent"]["Health"]-=damage
  print Colossus["opponent"]["Name"],"'s health is",Colossus["opponent"]["Health"],"."
  Colossus["Stamina"]-=100
  if (Colossus["opponent"]["Health"]<0):
    print Colossus["opponent"]["Name"],"died,",Colossus["Name"],"won."
    Death=True
    global Death
def Quicksilver1():
  hit=1/(10**(-((Quicksilver["Accuracy"]+100)-Quicksilver["opponent"]["Evasion"])/400)+1)
  damage=round(Quicksilver["Attack"]-Quicksilver["opponent"]["Defense"]*(1-hit))
  Quicksilver["opponent"]["Health"]-=damage
  print Quicksilver["opponent"]["Name"],"'s health is",Quicksilver["opponent"]["Health"]
  Quicksilver["Stamina"]-=100
  hit=1/(10**(-((Quicksilver["Accuracy"]+100)-Quicksilver["opponent"]["Evasion"])/400)+1)
  damage=round(Quicksilver["Attack"]-Quicksilver["opponent"]["Defense"]*(1-hit))
  Quicksilver["opponent"]["Health"]-=damage
  print Quicksilver["opponent"]["Name"],"'s health is",Quicksilver["opponent"]["Health"]
  Quicksilver["Stamina"]-=100
  if (Quicksilver["opponent"]["Health"]<0):
    print Quicksilver["opponent"]["Name"],"died,",Quicksilver["Name"],"won."
    Death=True
    global Death
def Wolverine1():
  if (Wolverine["Bleeding"]==True):
    Wolverine["Bleeding"]=False
  hit=1/(10**(-((Wolverine["Accuracy"]+100)-Wolverine["opponent"]["Evasion"])/400)+1)
  damage=round(Wolverine["Attack"]-Wolverine["opponent"]["Defense"]*(1-hit))
  Wolverine["opponent"]["Health"]-=damage
  if (Wolverine["opponent"]["Bleeding"]!=None):
    Wolverine["opponent"]["Bleeding"]=True
  if (Wolverine["opponent"]["Bleeding"]==True):
    Wolverine["opponent"]["Health"]-=100
  print Wolverine["opponent"]["Name"],"'s health is",Wolverine["opponent"]["Health"],"."
  Wolverine["Stamina"]+=100
  Wolverine["Health"]+=100
  if (Wolverine["opponent"]["Health"]<0):
    print Wolverine["opponent"]["Name"],"died,",Wolverine["Name"],"won."
    Death=True
    global Death
def Sif1():
    hit=1/(10**(-((Sif["Accuracy"]+100)-Sif["opponent"]["Evasion"])/400)+1)
    damage=round(Sif["Attack"]-Sif["opponent"]["Defense"]*(1-hit))
    Sif["opponent"]["Health"]-=damage
    if (Sif["opponent"]["Bleeding"]!=None):
      Sif["opponent"]["Bleeding"]=True
    if (Sif["opponent"]["Bleeding"]==True):
      Sif["opponent"]["Health"]-=100
    print Sif["opponent"]["Name"],"'s health is",Sif["opponent"]["Health"],"."
    if (Sif["opponent"]["Health"]<0):
      print Sif["opponent"]["Name"],"died,",Sif["Name"],"won."
      Death=True
      global Death
def Fight():
  Sif1()
  if (Death!=True):
    Wolverine1()
while (Death!=True and x<10):
  x+=1
  Fight()