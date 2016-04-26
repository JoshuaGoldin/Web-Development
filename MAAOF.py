import random
Hulk={"Name":"Hulk","Health":5970,"Stamina":4667,"Attack":1185,"Defense":1161,"Accuracy":968.0,"Evasion":909.0}
Thor={"Name":"Thor","Health":5982,"Stamina":5126,"Attack":1179,"Defense":1003,"Accuracy":1017.0,"Evasion":925.0}
Colossus={"Name":"Colossus","Health":5800,"Stamina":5264,"Attack":1025,"Defense":1218,"Accuracy":1052.0,"Evasion":929.0}
SheHulk={"Name":"She-Hulk","Health":5316,"Stamina":5138,"Attack":1102,"Defense":1006,"Accuracy":1025.0,"Evasion":947.0}
Thing={"Name":"Thing","Health":5602,"Stamina":5375,"Attack":1135,"Defense":1186,"Accuracy":983.0,"Evasion":967.0}
Hercules={"Name":"Hercules","Health":5965,"Stamina":5238,"Attack":1144,"Defense":1113,"Accuracy":1033.0,"Evasion":936.0}
CaptainBritain={"Name":"Captain Britain","Health":5440,"Stamina":5219,"Attack":1256,"Defense":1223,"Accuracy":1222.0,"Evasion":1112.0}
AntiVenom={"Name":"Anti-Venom","Health":6112,"Stamina":4752,"Attack":1096,"Defense":1048,"Accuracy":1049.0,"Evasion":1003.0}
Groot={"Name":"Groot","Health":6172,"Stamina":4869,"Attack":1078,"Defense":1098,"Accuracy":1098.0,"Evasion":894.0}
Punisher={"Name":"Punisher","Health":5375,"Stamina":5235,"Attack":1231,"Defense":1028,"Accuracy":1128.0,"Evasion":990.0}
Agent={"Name":"Agent","Health":5444,"Stamina":5420,"Attack":1409,"Defense":878,"Accuracy":1192.0,"Evasion":977.0}
IronMan={"Name":"Iron Man","Health":5114,"Stamina":4790,"Attack":1125,"Defense":1102,"Accuracy":1068.0,"Evasion":984.0}
DrStrange={"Name":"Dr. Strange","Health":5190,"Stamina":5166,"Attack":1275,"Defense":934,"Accuracy":1229.0,"Evasion":1084.0}
HumanTorch={"Name":"Human Torch","Health":5227,"Stamina":5347,"Attack":1334,"Defense":965,"Accuracy":1088.0,"Evasion":1123.0}
MsMarvel={"Name":"Ms. Marvel","Health":5106,"Stamina":4686,"Attack":1220,"Defense":1117,"Accuracy":1024.0,"Evasion":902.0}
Pheonix={"Name":"Pheonix","Health":4469,"Stamina":4512,"Attack":1160,"Defense":922,"Accuracy":1124.0,"Evasion":1092.0}
Storm={"Name":"Storm","Health":4857,"Stamina":4704,"Attack":1160,"Defense":999,"Accuracy":1035.0,"Evasion":1063.0}
ScarletWitch={"Name":"Scarlet Witch","Health":4646,"Stamina":5811,"Attack":1160,"Defense":1030,"Accuracy":1102.0,"Evasion":1037.0}
RocketRaccoon={"Name":"Rocket Raccoon","Health":5493,"Stamina":6037,"Attack":1112,"Defense":1049,"Accuracy":1159.0,"Evasion":1118.0}
Daredevil={"Name":"Daredevil","Health":5343,"Stamina":5679,"Attack":996,"Defense":1019,"Accuracy":1072.0,"Evasion":1107.0}
IronFist={"Name":"Iron Fist","Health":5220,"Stamina":5220,"Attack":1040,"Defense":968,"Accuracy":1059.0,"Evasion":1083.0}
LukeCage={"Name":"Luke Cage","Health":5665,"Stamina":5182,"Attack":1106,"Defense":1168,"Accuracy":1106.0,"Evasion":876.0}
Sif={"Name":"Sif","Health":5523,"Stamina":5350,"Attack":1068,"Defense":1063,"Accuracy":1064.0,"Evasion":913.0}
SpiderWoman={"Name":"Spider-Woman","Health":5196,"Stamina":4691,"Attack":1092,"Defense":1078,"Accuracy":1088.0,"Evasion":996.0}
Wolverine={"Name":"Wolverine","Health":5527,"Stamina":4519,"Attack":1268,"Defense":1086,"Accuracy":1041.0,"Evasion":946.0}
Quicksilver={"Name":"Quicksilver","Health":4678,"Stamina":6369,"Attack":970,"Defense":1040,"Accuracy":1160.0,"Evasion":1160.0}
Deadpool={"Name":"Deadpool","Health":5958,"Stamina":5278,"Attack":1209,"Defense":1045,"Accuracy":1073.0,"Evasion":991.0}
GhostRider={"Name":"Ghost Rider","Health":5382,"Stamina":5460,"Attack":1160,"Defense":1088,"Accuracy":1145.0,"Evasion":1061.0}
BlackWidow={"Name":"Black Widow","Health":4895,"Stamina":5316,"Attack":1022,"Defense":1027,"Accuracy":967.0,"Evasion":1160.0}
BlackCat={"Name":"Black Cat","Health":4363,"Stamina":6011,"Attack":983,"Defense":1092,"Accuracy":1258.0,"Evasion":1259.0}
InvisibleWoman={"Name":"Invisible Woman","Health":4722,"Stamina":4833,"Attack":1132,"Defense":1023,"Accuracy":1092.0,"Evasion":1092.0}
KittyPryde={"Name":"Kitty Pryde","Health":5024,"Stamina":6230,"Attack":1023,"Defense":1053,"Accuracy":1159.0,"Evasion":1221.0}
NightCrawler={"Name":"NightCrawler","Health":4837,"Stamina":6128,"Attack":900,"Defense":1010,"Accuracy":1290.0,"Evasion":1192.0}
SpiderMan={"Name":"Spider-Man","Health":4849,"Stamina":5668,"Attack":1105,"Defense":1103,"Accuracy":1066.0,"Evasion":1230.0}
Gambit={"Name":"Gambit","Health":5225,"Stamina":5953,"Attack":1055,"Defense":940,"Accuracy":1241.0,"Evasion":1170.0}
HawkEye={"Name":"HawkEye","Health":4761,"Stamina":5562,"Attack":1022,"Defense":1039,"Accuracy":1160.0,"Evasion":1218.0}
CaptainAmerica={"Name":"Captain America","Health":5756,"Stamina":5587,"Attack":1138,"Defense":1032,"Accuracy":1066.0,"Evasion":1001.0}
Cyclops={"Name":"Cyclops","Health":5415,"Stamina":5161,"Attack":1045,"Defense":1022,"Accuracy":1112.0,"Evasion":1080.0}
MrFantastic={"Name":"Mr. Fantastic","Health":4955,"Stamina":6045,"Attack":942,"Defense":1225,"Accuracy":1201.0,"Evasion":1122.0}
WarMachine={"Name":"War Machine","Health":5257,"Stamina":4898,"Attack":1274,"Defense":1112,"Accuracy":1046.0,"Evasion":984.0}
BlackPanther={"Name":"Black Panther","Health":5109,"Stamina":5592,"Attack":1017,"Defense":1042,"Accuracy":1059.0,"Evasion":1213.0}
DrDoom={"Name":"Dr. Doom","Health":9320,"Stamina":5869,"Attack":1250,"Defense":1236,"Accuracy":1174.0,"Evasion":1083.0}
Quake={"Name":"Quake","Health":4735,"Stamina":4638,"Attack":1160,"Defense":928,"Accuracy":1121.0,"Evasion":1044.0}
Rogue={"Name":"Rogue","Health":5139,"Stamina":5383,"Attack":1556,"Defense":1582,"Accuracy":1453.0,"Evasion":1355.0}
Beast={"Name":"Beast","Health":5198,"Stamina":5860,"Attack":1090,"Defense":1121,"Accuracy":1099.0,"Evasion":1130.0}
Angel={"Name":"Angel","Health":5444,"Stamina":5284,"Attack":1025,"Defense":1010,"Accuracy":1070.0,"Evasion":1153.0}
Players=[CaptainBritain, Hercules]
x=random.randint(0,1)
if x==0:
    y=1
else:
    y=0
print "Player x is",Players[x]["Name"]
print "Player y is",Players[y]["Name"]
staminax=Players[x]["Stamina"]
staminaxo=staminax
staminay=Players[y]["Stamina"]
staminayo=staminay
while (Players[x]["Health"]>=0 or Players[y]["Health"]>=0):
    #Players[x]["Health"]=Players[x]["Health"]*(staminax/staminaxo)
    Players[x]["Accuracy"]=Players[x]["Accuracy"]*(staminax/staminaxo)
    Players[y]["Evasion"]=Players[y]["Evasion"]*(staminay/staminayo)
    strike=1/(10**(-((Players[x]["Accuracy"]+100)-Players[y]["Evasion"])/400)+1)
    damage=round(Players[x]["Attack"])
    defend=round((1-strike)*Players[y]["Defense"])
    dealt=damage-defend
    if dealt<0:
        dealt=Players[x]["Attack"]*.01
    print Players[x]["Name"],"dealt",dealt,"damage."
    Players[y]["Health"]=round(Players[y]["Health"]-dealt)
    print Players[y]["Name"],"'s health is",Players[y]["Health"]
    if Players[y]["Health"]<=0:
        print Players[y]["Name"],"died."
        print Players[x]["Name"],"won."
        break
    staminax=staminax-100.0
    staminay=staminay-100.0
    #print staminax
    #print (staminax/staminayo),"%"
    #print (staminay/staminayo),"%"
    #Players[y]["Health"]=Players[y]["Health"]*(staminay/staminayo)
    Players[y]["Accuracy"]=Players[y]["Accuracy"]*(staminay/staminayo)
    Players[x]["Evasion"]=Players[x]["Evasion"]*(staminax/staminaxo)
    strike=1/(10**(-((Players[y]["Accuracy"]+100)-Players[x]["Evasion"])/400)+1)
    damage=round(Players[y]["Attack"])
    defend=round((1-strike)*Players[x]["Defense"])
    dealt=damage-defend
    if dealt<0:
        dealt=Players[y]["Attack"]*.01
    print Players[y]["Name"],"dealt",dealt,"damage."
    Players[x]["Health"]=round(Players[x]["Health"]-dealt)
    print Players[x]["Name"],"'s health is",Players[x]["Health"]
    staminax=staminax-100
    staminay=staminay-100
    if Players[x]["Health"]<=0:
        print Players[x]["Name"],"died."
        print Players[y]["Name"],"won."
        break