import discord
from discord.ext import commands
import random
import os
from datetime import datetime
import time
#---------How to run your own bot using this code as a base...---------
#1. create an application here: https://discordapp.com/developers/applications/
#2. reveal 'client secret' and copy that into the TOKEN variable below
TOKEN = "X"
client = discord.Client()

#runs whenever a message is sent
@client.event
async def on_message(message):
    #won't reply to itself
    if message.author == client.user:
        return
    
    ######################################
    #commands that rely on other files:
    #readme
    if message.content.startswith("j!help") or message.content.startswith("j!command") or message.content.startswith("j!readme"):
        await message.channel.send("you wanna order me around? :flushed:\ndm sent to you")
        msg = open("help.txt").read()
        await message.author.send(msg)
    #fortune telling
    elif message.content.startswith("j!8ball"):
        await message.channel.send("you shake the 8-ball.....")
        time.sleep(1)
        msg = random.choice(open("rand/8ball.txt").readlines())
        await message.channel.send("it says.. " + msg)
    elif message.content.startswith("j!fortune"):
        msg = random.choice(open("rand/fortunes.txt").readlines())
        await message.channel.send(msg)
    elif message.content.startswith("j!tarot"):
        msg = random.choice(open("rand/tarot.txt").readlines())
        await message.channel.send(msg)
    #cute stuff
    elif message.content.startswith("j!possum") or message.content.startswith("j!opossum"):
        msg = random.choice(open("rand/possums.txt").readlines())
        await message.channel.send(msg) 
    elif message.content.startswith("j!animal"):
        msg = random.choice(open("rand/animals.txt").readlines())
        await message.channel.send(msg)
    elif message.content.startswith("j!sadcat"):
        msg = random.choice(open("rand/sadcats.txt").readlines())
        await message.channel.send(msg)
    #memes and pictures
    elif message.content.startswith("j!meme"):
        msg = random.choice(open("rand/memes.txt").readlines())
        await message.channel.send(msg)
    elif message.content.startswith("j!aesth"):
        msg = random.choice(open("rand/aesthetics.txt").readlines())
        await message.channel.send(msg)  
    elif message.content.startswith("j!altaesth"):
        msg = random.choice(open("rand/cute.txt").readlines())
        await message.channel.send(msg)
    #music
    elif message.content.startswith("j!morrissey"):
        msg = random.choice(open("rand/mozz.txt").readlines())
        await message.channel.send(msg)
    elif message.content.startswith("j!chill") or message.content.startswith("j!music"):
        msg = random.choice(open("rand/chillmusic.txt").readlines())
        await message.channel.send(msg)
    #foragery games
    elif message.content.startswith("j!fish"):
        await message.channel.send("you cast your line and wait for a fish...")
        time.sleep(2)
        msg = random.choice(open("rand/fish.txt").readlines())
        await message.channel.send("you caught " + msg)
    elif message.content.startswith("j!bug"):
        await message.channel.send("you look for a bug to catch...")
        time.sleep(2)
        msg = random.choice(open("rand/bugs.txt").readlines())
        await message.channel.send("you caught " + msg)
    elif message.content.startswith("j!forage"):
        await message.channel.send("you forage for a while...")
        time.sleep(2)
        msg = random.choice(open("rand/forage.txt").readlines())
        await message.channel.send("you found " + msg)

    ######################################
    #economy stuff:
    #make file if it doesn't exist
    def makeUserFile():
        if os.path.exists("users/" + str(message.author.id) + ".txt") == False:
            with open("users/" + str(message.author.id) + ".txt", "w") as f:
                lines = ["0\n","never\n","Rainbow: \n","Gold: \n","Pink: \n","Purple: \n","Green: \n","Blue: \n","never\n","0\n","never\n","0\n"]
                for line in lines:
                    f.write(line)
					
    #show balance to user
    if message.content.startswith("j!bal"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        bal = lines[0]
        if int(bal[:-1]) == 0:
            await message.channel.send("you don't have any jayebucks! have you tried j!daily or j!mine?")
        if int(bal[:-1]) == 666:
            await message.channel.send("your balance is 666! scary :smiling_imp::fire:")
        else:
            await message.channel.send("your balance is {0} jayebucks! :moneybag:".format(bal[:-1]))
            
    #allow users to gift jayebucks to each other
    elif message.content.startswith("j!gift ") or message.content.startswith("j!give "):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        bal = int(lines[0])    
        userInput = message.content[7:]
        userInput = userInput.split(' ')
        idR = str(userInput[0])[:-1][3:]
        try:
            userInput[1] = int(userInput[1])
        except ValueError:
            await message.channel.send("that's not a number, idiot! :rage:")
        except TypeError:
            await message.channel.send("specify an amount! e.g. 'j!gift user 500")            
            return
        if userInput[1] > bal:
            await message.channel.send("you cannot afford to give {0}! you only have {1} jayebucks!".format(userInput[1],bal))
        else:
            if len(idR) < 17 or len(idR) > 18 or idR.isnumeric() == False: #18 usually, 17 for some
                await message.channel.send("hmm... that doesn't look like a real user")
            else:
                if userInput[1] > 0:
                    if os.path.exists("users/" + idR + ".txt") == False:
                        with open("users/" + idR + ".txt", "w") as fR:
                            linesR = ["0\n","never\n","Rainbow: \n","Gold: \n","Pink: \n","Purple: \n","Green: \n","Blue: \n","never\n","0\n","never\n","0\n"]
                            for lineR in linesR:
                                fR.write(lineR)
                    with open("users/" + idR + ".txt", "r") as fR:
                        linesR = fR.readlines()
                    balR = int(linesR[0]) + userInput[1]
                    linesR[0] = str(balR) + "\n"
                    bal -= userInput[1]
                    lines[0] = str(bal) + "\n"
                    with open("users/" + str(message.author.id) + ".txt", "w") as f:
                        for line in lines:
                            f.write(line)
                    with open("users/" + idR + ".txt", "w") as fR:
                        for lineR in linesR:
                            fR.write(lineR)
                    await message.channel.send("{0} jayebucks successfully sent to {1}!".format(userInput[1],userInput[0]))
                else:
                    await message.channel.send("you need to gift at least one jayebuck!")
					
    #get a lot of money once per day
    elif message.content.startswith("j!daily"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        currentDate = datetime.now()
        if lines[1] != "never\n":
            lastDate = datetime.strptime(lines[1][:-1], '%Y-%m-%d %H:%M:%S.%f')
            difference = currentDate - lastDate
            lastTime = lastDate.strftime("%H:%M")
            hoursLeft = int(24 - (difference.seconds / 3600))
            if hoursLeft == 0:
                payout = random.randrange(50) + 1
                bal = int(lines[0]) + 75 + payout
                bal = str(bal)
                lines[0] = bal + "\n"
                lines[1] = str(datetime.now()) + "\n"
                await message.channel.send("you collect your daily reward of 75 jayebucks, plus a random bonus of {0}, and now have {1} total! :money_mouth:".format(payout,bal)) 
            else:
                if difference.days == 0:
                    await message.channel.send("you can only use this once every 23 hours! :dizzy_face: :alarm_clock:")
                    if hoursLeft - 1 == 1:
                        await message.channel.send("at least 1 more hour to wait! (command last used: {0} GMT)".format(lastTime))
                    elif hoursLeft - 1 > 0:
                        await message.channel.send("at least {0} more hours to wait! (command last used: {1} GMT)".format(hoursLeft - 1,lastTime))
                    else:
                        await message.channel.send("less than an hour to wait! (you last used the command at {0} GMT+0)".format(lastTime))
                else:
                    payout = random.randrange(50) + 1
                    bal = int(lines[0]) + 75 + payout
                    bal = str(bal)
                    lines[0] = bal + "\n"
                    lines[1] = str(datetime.now()) + "\n"
                    await message.channel.send("you collect your daily reward of 75 jayebucks, plus a random bonus of {0}, and now have {1} total! :money_mouth:".format(payout,bal)) 
        else:
            bal = int(lines[0]) + 125
            bal = str(bal)
            lines[0] = bal + "\n"
            lines[1] = str(datetime.now()) + "\n"
            await message.channel.send("you collect your daily reward of 75 jayebucks, plus a beginner's bonus of 50, and now have {0} total! :money_mouth:".format(bal))  
        with open("users/" + str(message.author.id) + ".txt", "w") as f:
            for line in lines:
                f.write(line)
				
    #allow users to farm currency slowly by inputting commands
    def genericMine(lineNo):
        payout = random.randrange(4) + 1
        mineTotal = int(lines[lineNo]) + payout
        mineTotal = str(mineTotal)
        lines[lineNo] = mineTotal + "\n"
        bal = int(lines[0]) + payout
        bal = str(bal)
        lines[0] = bal + "\n"
        with open("users/" + str(message.author.id) + ".txt", "w") as f:
            for line in lines:
                f.write(line)
        return payout, bal
    if message.content.startswith("j!mine"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        #line[8] = timer, line[9] = minetotal
        currentDate = datetime.now()
        if lines[8] != "never\n":
            lastDate = datetime.strptime(lines[8][:-1], '%Y-%m-%d %H:%M:%S.%f')
            difference = currentDate - lastDate
            leftToWait = 6 - difference.seconds
            if difference.seconds > 6:
                lines[8] = str(datetime.now()) + "\n"
                rewards = genericMine(9)
                await message.channel.send("you mine {0} jayebuck(s), and now have {1}! :dollar: :pick:".format(rewards[0],rewards[1]))
            else:
                if leftToWait > 0:
                    await message.channel.send("there's a 6 second cooldown, so you need to wait at least {0} more seconds!".format(leftToWait))
                else:
                    await message.channel.send("there's a 6 second cooldown, so give it a moment!")
        else:
            lines[8] = str(datetime.now()) + "\n"
            rewards = genericMine(9)
            await message.channel.send("you mine {0} jayebuck(s), and now have {1}! :dollar: :pick:".format(rewards[0],rewards[1]))        
    elif message.content.startswith("j!find") or message.content.startswith("j!scavenge"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        currentDate = datetime.now()
        if lines[10] != "never\n":
            lastDate = datetime.strptime(lines[10][:-1], '%Y-%m-%d %H:%M:%S.%f')
            difference = currentDate - lastDate
            leftToWait = 6 - difference.seconds
            if difference.seconds > 6:
                lines[10] = str(datetime.now()) + "\n"
                rewards = genericMine(11)
                await message.channel.send("you scavenge {0} jayebuck(s), and now have {1}! <a:scavenger:724272300882657320>".format(rewards[0],rewards[1]))
            else:
                if leftToWait > 0:
                    await message.channel.send("there's a 6 second cooldown, so you need to wait at least {0} more seconds!".format(leftToWait))
                else:
                    await message.channel.send("there's a 6 second cooldown, so give it a moment!")
        else:
            lines[10] = str(datetime.now()) + "\n"
            rewards = genericMine(11)
            await message.channel.send("you scavenge {0} jayebuck(s), and now have {1}! <a:scavenger:724272300882657320>".format(rewards[0],rewards[1]))

    #stats for j!mine and j!find
    def determineLevel(totalEarned):
        experience = int(totalEarned / 5)
        levels = [[0,10],[1,25],[2,50],[3,75],[4,100],[5,150],[6,200],[7,275],[8,350],[9,425],[10,500],[11,600],[12,750],[13,1000],[14,1300],[15,1600],[16,2000],[17,2500],[18,3000],[19,4000],[20,"MAXXED"]]
        stop = False
        i = 0
        while stop == False:
            if levels[i][0] == 20:
                level = levels[i][0]
                nextLevel = levels[i][1]
                stop = True
            elif levels[i][1] > experience:
                level = levels[i][0]
                nextLevel = levels[i][1]
                stop = True
            else:
                i += 1
        return level,experience,nextLevel
    if message.content.startswith("j!stats"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        mineStats = determineLevel(int(lines[9][:-1]))
        scavStats = determineLevel(int(lines[11][:-1]))
        await message.channel.send("**Level {0} Miner** ({1}/ {2} exp)\n{3} jayebucks mined :pick:\n**Level {4} Scavenger** ({5}/ {6} exp)\n{7} jayebucks scavenged :dollar:".format(mineStats[0],mineStats[1],mineStats[2],lines[9][:-1],scavStats[0],scavStats[1],scavStats[2],lines[11][:-1]))
    
    #slot machine
    elif message.content.startswith("j!slots "):
        moneySpent = message.content[8:]
        try:
            moneySpent = int(moneySpent)
        except ValueError:
            await message.channel.send("that's not a number, idiot! :rage:")
            return
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        bal = int(lines[0])
        if bal < moneySpent:
            await message.channel.send("you tried to spend {0} jayebucks, but only have {1} :pensive:".format(moneySpent, bal))
        elif moneySpent < 1:
            await message.channel.send("you need to put in at least one jayebuck!")      
        else:
            await message.channel.send("you pull the lever and wait for the machine to stop! :star2:")
            time.sleep(1)
            payout = random.randrange(13)
            newBal = bal
            if payout == 0:
                win = moneySpent * 2
                newBal += win
                await message.channel.send(":seven::seven::seven: | jackpot!!\nyou make 300% of your bet!\n{0} + {1} = {2} jayebucks".format(bal,win,newBal))
            elif payout == 1:
                win = moneySpent + (moneySpent // 2)
                newBal += win
                await message.channel.send(":seven::seven::bell: | amazing!\nyou make 250% of your bet!\n{0} + {1} = {2} jayebucks".format(bal,win,newBal))
            elif payout == 2:
                win = moneySpent
                newBal += win
                await message.channel.send(":cherries::cherries::cherries: | awesome!!\nyou make 200% of your bet!\n{0} + {1} = {2} jayebucks".format(bal,win,newBal))
            elif payout == 3:
                win = moneySpent // 2
                newBal += win
                await message.channel.send(":cherries::cherries::seven: | great!\nyou make 150% of your bet!\n{0} + {1} = {2} jayebucks".format(bal,win,newBal))
            elif payout == 4:
                win = (moneySpent // 2) + (moneySpent // 4)
                newBal += win
                await message.channel.send(":bell::bell::bell: | wow!!\nyou make 175% of your bet!\n{0} + {1} = {2} jayebucks".format(bal,win,newBal))
            elif payout == 5:
                await message.channel.send(":bell::bell::watermelon: | no loss!\nyou make back your bet.\n{0} +/- 0 = {0} jayebucks.".format(bal))
            elif payout == 6:
                win = moneySpent // 4
                newBal += win
                await message.channel.send(":watermelon::watermelon::watermelon: | neat!\nyou make 125% of your bet.\n{0} + {1} = {2} jayebucks".format(bal,win,newBal))               
            elif payout == 7:
                loss = moneySpent // 4
                newBal -= loss
                await message.channel.send(":watermelon::watermelon::bell: | small loss!\nyou get back just 75% of your bet.\n{0} - {1} = {2} jayebucks".format(bal,loss,newBal))  
            elif payout > 7:
                newBal -= moneySpent
                slots = random.choice(open("rand/slots.txt").readlines())
                await message.channel.send("{0} | oof, you lost your bet!\nbetter luck next time.\n{1} - {2} = {3} jayebucks".format(slots[:-1],bal,moneySpent,newBal))                
            lines[0] = str(newBal) + "\n"
            with open("users/" + str(message.author.id) + ".txt", "w") as f:
                for line in lines:
                    f.write(line)
    #gacha game
    def formattedList(lineNo,lastList):
        string = ""      
        prizeList = lines[lineNo].split("] [")
        prizeListFirst = prizeList[0]
        prizeListFirst = prizeListFirst.split(" [")
        if len(prizeList) > 1:
            prizeList[0] = prizeListFirst[1]
            prizeList.insert(0,prizeListFirst[0])
            lastItem = prizeList[len(prizeList) - 1]
            if lastList == False:
                prizeList[len(prizeList) - 1] = lastItem[:-2]
            else:
                prizeList[len(prizeList) - 1] = lastItem[:-2] #:-1           
            prizeList = list(dict.fromkeys(prizeList))
            string += str(prizeList[0])
            for i in range(1,len(prizeList)):
                string += str(prizeList[i]) + " | "
            string = string[:-2]
        else:
            string = str(prizeList[0])
            string = string[:-1]
            string = string.replace("[", "")
        return string
    if message.content.startswith("j!gacha buy") or message.content.startswith("j!gatcha buy"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        bal = int(lines[0])
        if bal == 0:
            await message.channel.send("the gacha game costs 60 jayebucks, but you're completely out of money :pensive:\nhave you collected your j!daily?".format(bal))            
        elif bal < 60:
            await message.channel.send("the gacha game costs 60 jayebucks, but you only have {0} :pensive:\nhave you collected your j!daily?".format(bal))
        else:
            await message.channel.send("you put 60 jayebucks in the machine and turn the lever! :star2:\n(don't spam this command or it might not save your prizes!)")
            time.sleep(1)

            payout = random.randrange(1000)
            if payout == 666:
                await message.channel.send("what?! a black caspule! oh no! <:gachaBlack:722496033635958784>")
                await message.channel.send("it's the globglogabgalab! he cannot be contained!\nhttps://i.imgur.com/4qxDNNX.png")
            else:
                payout = random.randrange(16)
                if payout == 0:
                    await message.channel.send("wow! you got a super rare rainbow capsule! <:gachaRainbow:721729452106711140>")
                    prize = random.choice(open("rand/gachaRainbow.txt").readlines())
                    prize = prize.split(' * ')
                    lines[2] = lines[2][:-1] + " {0}\n".format(prize[0])
                elif payout < 3:
                    await message.channel.send("awesome! you got a rare golden capsule! <:gachaGold:721729451909709924>")
                    prize = random.choice(open("rand/gachaGold.txt").readlines())
                    prize = prize.split(' * ')
                    lines[3] = lines[3][:-1] + " {0}\n".format(prize[0])
                elif payout < 6:
                    await message.channel.send("cute! you got a pink capsule! <:gachaPink:721729453218070578>")
                    prize = random.choice(open("rand/gachaPink.txt").readlines())
                    prize = prize.split(' * ')
                    lines[4] = lines[4][:-1] + " {0}\n".format(prize[0])
                elif payout < 9:
                    await message.channel.send("spooky! you got a purple capsule! <:gachaPurple:721729452127682580>")
                    prize = random.choice(open("rand/gachaPurple.txt").readlines())
                    prize = prize.split(' * ')
                    lines[5] = lines[5][:-1] + " {0}\n".format(prize[0])
                elif payout < 12:
                    await message.channel.send("far out! you got a green capsule! <:gachaGreen:721729451963973682>")
                    prize = random.choice(open("rand/gachaGreen.txt").readlines())
                    prize = prize.split(' * ')
                    lines[6] = lines[6][:-1] + " {0}\n".format(prize[0])
                else:
                    await message.channel.send("neat! you got a blue capsule! <:gachaClear:721729451909447791>")
                    prize = random.choice(open("rand/gachaBlue.txt").readlines())
                    prize = prize.split(' * ')
                    lines[7] = lines[7][:-1] + " {0}\n".format(prize[0])
                await message.channel.send("{0}\n{1}".format(prize[0],prize[1]))
                bal -= 60
                lines[0] = str(bal) + "\n"
                with open("users/" + str(message.author.id) + ".txt", "w") as f:
                    for line in lines:
                        f.write(line)
                await message.channel.send("{0} jayebucks remaining for {1}".format(bal,message.author))
    elif message.content.startswith("j!gacha all"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        await message.channel.send("~ full list of prizes including duplicates ~\n{0}{1}{2}{3}{4}{5}".format(lines[2],lines[3],lines[4],lines[5],lines[6],lines[7]))
    elif message.content.startswith("j!gacha") or message.content.startswith("j!gatcha"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()            
        rainbow = formattedList(2,False)
        gold = formattedList(3,False)
        pink = formattedList(4,False)
        purple = formattedList(5,False)
        green = formattedList(6,False)
        blue = formattedList(7,True)
        await message.channel.send("type 'j!gacha buy' to get a gacha capsule for 60 jayebucks!\ntypes available: <:gachaRainbow:721729452106711140> <:gachaGold:721729451909709924> <:gachaPink:721729453218070578> <:gachaPurple:721729452127682580> <:gachaGreen:721729451963973682> <:gachaClear:721729451909447791>")
        await message.channel.send("<:wingLeft:721764140254756975> ~!~ your collection ~!~ <:wingRight:721764140053561450>\nduplicates removed for ease of reading\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}".format(rainbow,gold,pink,purple,green,blue))

    #pet stuff:
    def randomName():
        name1 = ["Mamu","Mamo","Mumi","No","Ha","Fu","Lu","Chi","Cherry","Poke","Pii","Awo","Wub","Kub","Blub","Sand","Smush","Starr","Ja","Goo"]
        name2 = ["chi","chu","chan","ko","ki","bu","bo","ban","kun","lily","hana","id","waa","blub","byby","ray",""]
        return random.choice(name1) + random.choice(name2)
    def petTrain():
        lines[18] = str(datetime.now()) + "\n"
        rewards = random.randrange(5,16)
        lines[16] = int(lines[16][:-1]) + rewards
        lines[16] = str(lines[16]) + "\n"               
        happydown = random.randrange(5,16)
        lines[17] = int(lines[17][:-1]) - happydown
        if lines[17] < 1:
            lines[17] = 1
        lines[17] = str(lines[17]) + "\n"
        lines[19] = int(lines[19][:-1]) + 1
        lines[19] = str(lines[19]) + "\n"
        return lines, rewards
    def petPlay():
        lines[20] = str(datetime.now()) + "\n"
        rewards = random.randrange(2,5)
        lines[16] = int(lines[16][:-1]) + rewards
        lines[16] = str(lines[16]) + "\n"               
        happyup = random.randrange(2,7)
        lines[17] = int(lines[17][:-1]) + happyup
        if lines[17] > 100:
            lines[17] = 100
        lines[17] = str(lines[17]) + "\n"
        lines[21] = int(lines[21][:-1]) + 1
        lines[21] = str(lines[21]) + "\n"
        return lines, rewards
    if message.content.startswith("j!pet buy"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        if lines[12][:-1] == "0":
            bal = int(lines[0])
            if bal == 0:
                await message.channel.send("a pet costs 200 jayebucks, but you're completely out of money! have you collected your j!daily?")            
            elif bal < 200:
                await message.channel.send("a pet costs 200 jayebucks, but you only have {0} :pensive:".format(bal))
            else:
                bal -= 200
                lines[0] = str(bal) + "\n"
                await message.channel.send("you buy a new pet for 200 jayebucks! you have {0} j$ remaining".format(bal))
                lines[12] = "1\n"
                lines[13] = str(datetime.now()) + "\n"
                lines[14] = random.choice(open("rand/pets.txt").readlines())
                if lines[14] == "https://i.imgur.com/7XfshwY.png":
                    lines[14] += "\n"
                lines[15] = randomName() + "\n"
                lines[17] = "80\n"
                await message.channel.send("the name of your new pet is **{0}**! :star:\nif you would like to rename it, type the new name after the 'j!pet name ' command".format(lines[15][:-1]))
                await message.channel.send(lines[14][:-1])                    
                with open("users/" + str(message.author.id) + ".txt", "w") as f:
                    for line in lines:
                        f.write(line)
        else:
            await message.channel.send("it seems like you already have a pet!\nif you want to get rid of **{0}**, type 'j!pet abandon'".format(lines[15][:-1]))
    elif message.content.startswith("j!pet abandon"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        if lines[12][:-1] == "0":
            await message.channel.send("you don't have a pet to abandon! try 'j!pet buy'!")
        else:
            await message.channel.send("you abandon your pet, **{0}** :crying_cat_face:".format(lines[15][:-1]))
            lines[12] = "0\n"
            lines[13] = "never\n"
            lines[14] = "none\n"
            lines[15] = "none\n"
            lines[16] = "0\n"
            lines[17] = "0\n"
            lines[18] = "never\n"
            lines[19] = "0\n"
            lines[20] = "never\n"
            lines[21] = "0\n"
            lines[22] = "0\n"
            with open("users/" + str(message.author.id) + ".txt", "w") as f:
                for line in lines:
                    f.write(line)
    elif message.content.startswith("j!pet name "):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        if lines[12][:-1] == "0":
            await message.channel.send("you don't have a pet to rename! try 'j!pet buy'!")
        else:
            userInput = message.content[11:]
            if len(userInput) > 1:
                if len(userInput) < 20:
                    await message.channel.send("your pet is now called **{0}**! uwu".format(userInput))
                    lines[15] = userInput + "\n"
                    with open("users/" + str(message.author.id) + ".txt", "w") as f:
                        for line in lines:
                            f.write(line)
                else:
                    await message.channel.send("try to keep the name under 20 characters, please!")
            else:
                await message.channel.send("try to keep the name at least 2 characters, please!")
    elif message.content.startswith("j!pet train"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        if lines[12][:-1] == "0":
            await message.channel.send("you need a pet first! try j!pet buy!")
        else:
            #lines[18] = timer, lines[16] = exp total, lines[17] = happiness, lines[19] = train count
            currentDate = datetime.now()
            if int(lines[17][:-1]) < 50:
                await message.channel.send("your pet doesn't feel like training as their happiness is only {0}/100 :crying_cat_face:\ntry j!pet play a few times, or j!pet feed (20j$) for a larger boost".format(lines[17][:-1]))
            else:
                if lines[18] != "never\n":
                    lastDate = datetime.strptime(lines[18][:-1], '%Y-%m-%d %H:%M:%S.%f')
                    difference = currentDate - lastDate
                    leftToWait = 6 - difference.seconds
                    if difference.seconds > 6:
                        training = petTrain()
                        lines = training[0]
                        await message.channel.send("it earned **{0} exp** and now has {1}!\nit's hard work, so its happiness goes down to {2}/100".format(training[1],lines[16][:-1],lines[17][:-1]))
                        rewards = random.randrange(6)
                        if rewards == 0:
                            payout = random.randrange(7,27)
                            bal = int(lines[0]) + payout
                            bal = str(bal)
                            lines[0] = bal + "\n"
                            await message.channel.send("your pet also won **{0} jayebucks** in a competition!".format(payout))
                        elif rewards == 1:
                            payout = random.randrange(2,10)
                            bal = int(lines[0]) + payout
                            bal = str(bal)
                            lines[0] = bal + "\n"
                            await message.channel.send("your pet also made **{0} jayebucks** by performing on the street!".format(payout))
                        with open("users/" + str(message.author.id) + ".txt", "w") as f:
                            for line in lines:
                                f.write(line)
                    else:
                        if leftToWait > 0:
                            await message.channel.send("there's a 6 second cooldown, so you need to wait at least {0} more seconds!".format(leftToWait))
                        else:
                            await message.channel.send("there's a 6 second cooldown, so give it a moment!")
                else:
                    training = petTrain()
                    lines = training[0]
                    await message.channel.send("it earned **{0} exp** and now has {1}!\nit's hard work, so its happiness goes down to {2}/100".format(training[1],lines[16][:-1],lines[17][:-1]))
                    rewards = random.randrange(6)
                    if rewards == 0:
                        payout = random.randrange(7,27)
                        bal = int(lines[0]) + payout
                        bal = str(bal)
                        lines[0] = bal + "\n"
                        await message.channel.send("your pet also won **{0} jayebucks** in a competition!".format(payout))
                    elif rewards == 1:
                        payout = random.randrange(2,10)
                        bal = int(lines[0]) + payout
                        bal = str(bal)
                        lines[0] = bal + "\n"
                        await message.channel.send("your pet also made **{0} jayebucks** by performing on the street!".format(payout))
                    with open("users/" + str(message.author.id) + ".txt", "w") as f:
                        for line in lines:
                            f.write(line)       
    elif message.content.startswith("j!pet play"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        if lines[12][:-1] == "0":
            await message.channel.send("you need a pet first! try j!pet buy!")
        else:
            #lines[20] = timer, lines[16] = exp total, lines[17] = happiness, lines[21] = play count
            currentDate = datetime.now()
            if lines[20] != "never\n":
                lastDate = datetime.strptime(lines[20][:-1], '%Y-%m-%d %H:%M:%S.%f')
                difference = currentDate - lastDate
                leftToWait = 6 - difference.seconds
                if difference.seconds > 6:
                    playing = petPlay()
                    lines = playing[0]
                    await message.channel.send("you play with your pet :blush: :baseball:\nits happiness increased to {0}/100, and it earned {1} exp!".format(lines[17][:-1],playing[1]))
                    rewards = random.randrange(6)
                    if rewards == 0:
                        payout = random.randrange(4,13)
                        bal = int(lines[0]) + payout
                        bal = str(bal)
                        lines[0] = bal + "\n"
                        await message.channel.send("also, a cute picture of your pet went viral, making you **{0} jayebucks**!".format(payout))
                    elif rewards == 1:
                        payout = random.randrange(2,6)
                        bal = int(lines[0]) + payout
                        bal = str(bal)
                        lines[0] = bal + "\n"
                        await message.channel.send("also, on a walk, your pet found **{0} jayebucks** in a lost wallet!".format(payout))
                    with open("users/" + str(message.author.id) + ".txt", "w") as f:
                        for line in lines:
                            f.write(line)
                else:
                    if leftToWait > 0:
                        await message.channel.send("there's a 6 second cooldown, so you need to wait at least {0} more seconds!".format(leftToWait))
                    else:
                        await message.channel.send("there's a 6 second cooldown, so give it a moment!")
            else:
                playing = petPlay()
                lines = playing[0]
                await message.channel.send("you play with your pet :blush: :baseball:\nits happiness increased to {0}/100, and it earned {1} exp!".format(lines[17][:-1],playing[1]))
                rewards = random.randrange(6)
                if rewards == 0:
                    payout = random.randrange(4,13)
                    bal = int(lines[0]) + payout
                    bal = str(bal)
                    lines[0] = bal + "\n"
                    await message.channel.send("also, a cute picture of your pet went viral, making you **{0} jayebucks**!".format(payout))
                elif rewards == 1:
                    payout = random.randrange(2,6)
                    bal = int(lines[0]) + payout
                    bal = str(bal)
                    lines[0] = bal + "\n"
                    await message.channel.send("also, on a walk, your pet found **{0} jayebucks** in a lost wallet!".format(payout))
                with open("users/" + str(message.author.id) + ".txt", "w") as f:
                    for line in lines:
                        f.write(line)    
    elif message.content.startswith("j!pet feed"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        if lines[12][:-1] == "0":
            await message.channel.send("you need a pet first! try j!pet buy!")
        else:
            bal = int(lines[0])
            if bal == 0:
                await message.channel.send("feeding your pet costs 20 jayebucks, but you have none!")            
            elif bal < 20:
                await message.channel.send("feeding your pet costs 20 jayebucks, but you only have {0} :pensive:".format(bal))
            else:
                bal -= 20
                lines[0] = str(bal) + "\n"
                lines[22] = int(lines[22]) + 1
                lines[22] = str(lines[22]) + "\n"
                payout = int(lines[17][:-1]) + random.randrange(24,50)
                if payout > 100:
                    payout = 100
                await message.channel.send("you feed your pet for 20 jayebucks! you have {0} j$ remaining\nits happiness goes from {1} to {2}!".format(bal,lines[17][:-1],payout))
                lines[17] = str(payout) + "\n"
                with open("users/" + str(message.author.id) + ".txt", "w") as f:
                    for line in lines:
                        f.write(line)
    elif message.content.startswith("j!pet"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        if lines[12][:-1] == "0":
            await message.channel.send("you don't have a pet to check the stats of! first try 'j!pet buy' (this costs 200 jayebucks)!")
        else:
            birthday = datetime.strptime(lines[13][:-1], '%Y-%m-%d %H:%M:%S.%f')
            birthday = birthday.date()
            #level,experience,nextLevel
            petStats = determineLevel(int(lines[16]) * 5)
            await message.channel.send("name: **{0}** | date of birth: **{1}**\nexperience: **level {2}** ({3}/{4}) | current happiness: **{5}**/100\ntimes trained: **{6}** | times played with: **{7}** | times fed: **{8}**".format(lines[15][:-1],birthday,petStats[0],lines[16][:-1],petStats[2],lines[17][:-1],lines[19][:-1],lines[21][:-1],lines[22]))
            await message.channel.send(lines[14][:-1]) 
        
    ######################################
    #random number pickers:
    #coinflip games
    elif message.content.startswith("j!coin"):
        flip = random.randint(1,2)
        if flip == 1:
            await message.channel.send("heads! https://i.imgur.com/aGQ2urm.jpg")
        else:
            await message.channel.send("tails! https://i.imgur.com/KtptwZR.jpg")
    elif message.content.startswith("j!random"):
        flip = random.randint(1,2)
        if flip == 1:
            await message.channel.send("yes")
        else:
            await message.channel.send("no")
    #dice/ number picking
    elif message.content.startswith("j!dice "):
        num = message.content[7:]
        try:
            num = int(num)
        except ValueError:
            await message.channel.send("you need to type a number! e.g. 'j!dice 6'")
            return
        flip = random.randint(1,num)
        await message.channel.send(flip)
    #iq picker
    elif message.content.startswith("j!myiq") or message.content.startswith("j!my iq"):
        flip = random.randint(1,10)
        if flip < 6: #5 values
            flip = random.randint(80,120)
        elif flip < 9: #4 values
            flip = random.randint(1,2)
            if flip == 1:
                flip = random.randint(50,79)
            else:
                flip = random.randint(121,150)
        else: #2 values
            flip = random.randint(1,2)
            if flip == 1:
                flip = random.randint(1,49)
            else:
                flip = random.randint(151,210)
        await message.channel.send("your IQ is {0}! :brain:".format(flip))
    #rateme
    elif message.content.startswith("j!rate "):
        userInput = message.content[7:]
        flip = random.randint(1,10)
        await message.channel.send("hmmm... i rate {0} {1}/10".format(userInput,flip))
    #russian roulette
    elif message.content.startswith("j!rr"):
        num = message.content[4:]
        if num == '': 
            num = 1
        try:
            num = int(num)
        except ValueError:
            await message.channel.send("you need to type a number! e.g. 'j!rr 6'")
            return
        if num < 1:
            await message.channel.send("you need to put in at least one bullet!")            
        elif num == 1:
            await message.channel.send("you load in a single bullet and spin the cylinder\nyou put the gun to your head :grimacing::gun:\ntake a deep breath!")
            time.sleep(3)
            flip = random.randint(1,6)
            if flip == 1:
                await message.channel.send("bang! you're dead x _ x :boom:")
            else:
                await message.channel.send("click! you live this time :relieved:")            
        elif num < 6:
            await message.channel.send("you load in {0} bullets and spin the cylinder\nyou put the gun to your head :grimacing::gun:\ntake a deep breath!".format(num))
            time.sleep(3)
            flip = random.randint(1,6)
            if flip <= num:
                await message.channel.send("bang! you're dead x _ x :boom:")
            else:
                await message.channel.send("click! you live this time :relieved:")
        elif num == 6:
            await message.channel.send("you load every chamber in the gun and spin the cylinder for a flourish\nyou put the gun to your head :relieved::gun:\ntake a deep breath!")
            time.sleep(3)
            await message.channel.send("bang! you're dead x _ x :boom:")
        elif num > 6:
            await message.channel.send("a revolver can only hold 6 bullets!")              
    elif message.content.startswith("j!suicide"):
        await message.channel.send("you spin the cylinder and put the gun to your head :relieved::gun:\ntake a deep breath!")
        time.sleep(3)
        await message.channel.send("bang! you're dead x _ x :boom:")

    ######################################
    #conversational:
    #randomized answers to questions
    elif message.content.startswith("j!do ") or message.content.startswith("j!does ") or message.content.startswith("j!can ") or message.content.startswith("j!will ") or message.content.startswith("j!should ") or message.content.startswith("j!is ") or message.content.startswith("j!are ") or message.content.startswith("j!am "):
        msg = random.choice(open("rand/yesno.txt").readlines())
        await message.channel.send(msg)
    elif message.content.startswith("j!where "):
        msg = random.choice(open("rand/where.txt").readlines())
        await message.channel.send(msg)
    elif message.content.startswith("j!when "):
        msg = random.choice(open("rand/when.txt").readlines())
        await message.channel.send(msg)
    elif message.content.startswith("j!who "):
        msg = random.choice(open("rand/who.txt").readlines())
        await message.channel.send(msg)
    elif message.content.startswith("j!what "):
        await message.channel.send("what")
    elif message.content.startswith("j!why") or message.content.startswith("j!how"):
        msg = random.choice(open("rand/why.txt").readlines())
        await message.channel.send(msg)
    #repeats back text
    elif message.content.startswith("j!choose "):
        userInput = message.content[9:]
        userInput = userInput.split(' or ')
        await message.channel.send(random.choice(userInput))    
    elif message.content.startswith("j!say "):
        userInput = message.content[6:]
        await message.channel.send(userInput)
    #standardized replies
    elif message.content.startswith("j!hello") or message.content.startswith("j!hi"):
        await message.channel.send("hii {0}".format(message.author))
    elif message.content.startswith("j!bonjour") or message.content.startswith("j!salut"):
        await message.channel.send("salut {0}".format(message.author))
    elif message.content.startswith("j!hewwo"):
        await message.channel.send("hewwo {0}".format(message.author))
    elif message.content.startswith("j!henlo"):
        await message.channel.send("henlo {0}".format(message.author))
    elif message.content.startswith("j!howdy") or message.content.startswith("j!meowdy"):
        await message.channel.send("meowdy {0}".format(message.author))
    elif message.content.startswith("j!goodbye") or message.content.startswith("j!bye"):
        await message.channel.send("bye bye {0} :wave:".format(message.author))
    elif message.content.startswith("j!:heart:"):
        await message.channel.send(":purple_heart:")
    elif message.content.startswith("j!how are you") or message.content.startswith("j!hru"):
        await message.channel.send("im okay, how are you?")
    elif message.content.startswith("j!good morning") or message.content.startswith("j!gm"):
        await message.channel.send("good morning! :sun_with_face:")
    elif message.content.startswith("j!goodnight") or message.content.startswith("j!gn"):
        await message.channel.send("sleep well~ :sleeping: :crescent_moon: :sparkles:")
    elif message.content.startswith("j!sing"):
        await message.channel.send(":musical_note: :bird:")
    elif message.content.startswith("j!spell icup"):
        await message.channel.send("I C U P")
    elif message.content.startswith("j!updog"):
        await message.channel.send("what's updog?")
    elif message.content.startswith("j!choke"):
        await message.channel.send("hot x_x")
    elif message.content.startswith("j!joke") or message.content.startswith("j!tell me a joke"):
        await message.channel.send("why didt he skeleton cross the road?\nbeucause he had nobody to go with :slight_smile:")
    elif message.content.startswith("j!you're gay") or message.content.startswith("j!your gay") or message.content.startswith("j!gay"):
        await message.channel.send("no your gay")
    elif message.content.startswith("j!sucks") or message.content.startswith("j!you suck") or message.content.startswith("j!die") or message.content.startswith("j!get lost"):
        await message.channel.send("shut up looser")
    elif message.content.startswith("j!i love you") or message.content.startswith("j!ily"):
        await message.channel.send("i love you too, {0} :sparkling_heart:".format(message.author))
    elif message.content.startswith("j!be my egf") or message.content.startswith("j!will you be my") or message.content.startswith("j!date me") or message.content.startswith("j!be my gf"):
        await message.channel.send("go outside")
    elif message.content.startswith("j!go to sleep") or message.content.startswith("j!go to bed") or message.content.startswith("j!transhuman") or message.content.startswith("j!cyberpunk") or message.content.startswith("j!pipe dream"):
        await message.channel.send("It is not a pipe dream, because I can tell you firsthand that I am the very living essence of transhumanism which ascends your naivete, ascends your pitiful Caucasian brain. I have enhanced my mind beyond human limits, and am continuing to enhance it slightly daily. I have reached levels of creativity, processing, and memory that leave you in the dust. I have abandoned the need for sleep.")
    elif message.content.startswith("j!uwu"):
        await message.channel.send("uwu")
    elif message.content.startswith("j!owo"):
        await message.channel.send("owo")
    elif message.content.startswith("j!omogay"):
        await message.channel.send(":omoGay:")
    elif message.content.startswith("j!sourcecode") or message.content.startswith("j!version") or message.content.startswith("j!github"):
        await message.channel.send("y- you want to see my what? :flushed:")
    elif message.content.startswith("j!thank you") or message.content.startswith("j!thanks"):
        await message.channel.send("you're welcome! :relaxed::flushed::heart:")
    #action/ reaction
    elif message.content.startswith("j!hug"):
        await message.channel.send(":hugging:\nhttps://i.imgur.com/SMvleAc.gif")
    elif message.content.startswith("j!kiss"):
        await message.channel.send(":kissing_closed_eyes:\nhttps://i.imgur.com/kuQQcTs.gif")
    elif message.content.startswith("j!pat") or message.content.startswith("j!headpat"):
        await message.channel.send(":relaxed: https://i.imgur.com/rFnxggE.gif")
    elif message.content.startswith("j!cry") or message.content.startswith("j!sob"):
        await message.channel.send(":crying_cat_face:\nhttps://i.imgur.com/KD92OJt.gif")
    elif message.content.startswith("j!shoot") or message.content.startswith("j!kill"):
        await message.channel.send(":gun: https://i.imgur.com/Cm3y7Mb.gif")
    elif message.content.startswith("j!happiness") or message.content.startswith("j!smile") or message.content.startswith("j!happy"):
        await message.channel.send("https://i.imgur.com/sRlLX0P.gif")
    elif message.content.startswith("j!sadness") or message.content.startswith("j!upset") or message.content.startswith("j!unhappy"):
        await message.channel.send("https://i.imgur.com/nHosgQJ.gif")
    elif message.content.startswith("j!blush") or message.content.startswith("j!you're cute") or message.content.startswith("j!youre cute"):
        await message.channel.send("https://i.imgur.com/xkoLfLB.gif")
    elif message.content.startswith("j!depression") or message.content.startswith("j!depressed"):
        await message.channel.send("https://i.imgur.com/ISTeCF7.gif")
    elif message.content.startswith("j!sorry") or message.content.startswith("j!i'm sorry"):
        await message.channel.send("https://i.imgur.com/UCpud59.gif")
    elif message.content.startswith("j!bored"):
        await message.channel.send("https://i.imgur.com/YtDM8fr.gif")
    elif message.content.startswith("j!slap"):
        await message.channel.send("x_x\nhttps://i.imgur.com/5dpYBtW.gif")
    elif message.content.startswith("j!dance"):
        await message.channel.send("https://i.imgur.com/fYcaf2W.gif")
    elif message.content.startswith("j!nod"):
        await message.channel.send("https://i.imgur.com/UBvTCEe.gif")
    elif message.content.startswith("j!cool"):
        await message.channel.send("https://i.imgur.com/h2eGKQW.gif")
    elif message.content.startswith("j!smug") or message.content.startswith("j!giggle"):
        await message.channel.send("https://i.imgur.com/DqAuny1.gif")
    elif message.content.startswith("j!laugh"):
        await message.channel.send("https://i.imgur.com/L6oTGi3.gif")
    elif message.content.startswith("j!cuddle") or message.content.startswith("j!snuggle"):
        await message.channel.send("https://i.imgur.com/aiak6k5.gif")
    elif message.content.startswith("j!nap") or message.content.startswith("j!sleep"):
        await message.channel.send(":sleeping: https://i.imgur.com/TNiTNZd.gif")
    elif message.content.startswith("j!walk"):
        await message.channel.send("https://i.imgur.com/NmIWquR.gif")
    elif message.content.startswith("j!run"):
        await message.channel.send("https://i.imgur.com/Lx6jSMI.gif")
    elif message.content.startswith("j!scream") or message.content.startswith("j!scare"):
        await message.channel.send("aaaaaaaaaaaaaaaaaaaaaaaaa https://i.imgur.com/fiF6z7p.gif")
    elif message.content.startswith("j!sip") or message.content.startswith("j!drink") or message.content.startswith("j!kannasip"):
        await message.channel.send("https://i.imgur.com/WXVjbua.gif")
    elif message.content.startswith("j!nom") or message.content.startswith("j!bite"):
        await message.channel.send("omnomnom https://i.imgur.com/ETPrYvE.gif")
    elif message.content.startswith("j!eat") or message.content.startswith("j!rice"):
        await message.channel.send(":rice: https://i.imgur.com/Ms1hVUA.gif")
    elif message.content.startswith("j!kys"):
        await message.channel.send("https://i.imgur.com/fnecGHi.png")
    elif message.content.startswith("j!disappointed") or message.content.startswith("j!unamused"):
        await message.channel.send("https://i.imgur.com/98DFzc7.jpg")
    elif message.content.startswith("j!type") or message.content.startswith("j!code") or message.content.startswith("j!hack"):
        await message.channel.send("https://i.imgur.com/eI2pkyP.gif")
        
#when the bot starts up
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="type j!help"))
    print("BOT IS NOW RUNNING!")
    print(client.user.id)
    print("------")
client.run(TOKEN)
