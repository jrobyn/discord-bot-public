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
    if message.content.startswith("j!8ball"):
        await message.channel.send("you shake the 8-ball.....")
        time.sleep(1)
        msg = random.choice(open("rand/8ball.txt").readlines())
        await message.channel.send("it says.. " + msg)
    if message.content.startswith("j!fortune"):
        msg = random.choice(open("rand/fortunes.txt").readlines())
        await message.channel.send(msg)
    if message.content.startswith("j!tarot"):
        msg = random.choice(open("rand/tarot.txt").readlines())
        await message.channel.send(msg)
    #cute stuff
    if message.content.startswith("j!possum") or message.content.startswith("j!opossum"):
        msg = random.choice(open("rand/possums.txt").readlines())
        await message.channel.send(msg) 
    if message.content.startswith("j!animal"):
        msg = random.choice(open("rand/animals.txt").readlines())
        await message.channel.send(msg)
    if message.content.startswith("j!sadcat"):
        msg = random.choice(open("rand/sadcats.txt").readlines())
        await message.channel.send(msg)
    #memes and pictures
    if message.content.startswith("j!meme"):
        msg = random.choice(open("rand/memes.txt").readlines())
        await message.channel.send(msg)
    if message.content.startswith("j!aesth"):
        msg = random.choice(open("rand/aesthetics.txt").readlines())
        await message.channel.send(msg)  
    if message.content.startswith("j!altaesth"):
        msg = random.choice(open("rand/cute.txt").readlines())
        await message.channel.send(msg)
    #music
    if message.content.startswith("j!morrissey"):
        msg = random.choice(open("rand/mozz.txt").readlines())
        await message.channel.send(msg)
    if message.content.startswith("j!chill") or message.content.startswith("j!music"):
        msg = random.choice(open("rand/chillmusic.txt").readlines())
        await message.channel.send(msg)
    #foragery games
    if message.content.startswith("j!fish"):
        await message.channel.send("you cast your line and wait for a fish...")
        time.sleep(2)
        msg = random.choice(open("rand/fish.txt").readlines())
        await message.channel.send("you caught " + msg)
    if message.content.startswith("j!bug"):
        await message.channel.send("you look for a bug to catch...")
        time.sleep(2)
        msg = random.choice(open("rand/bugs.txt").readlines())
        await message.channel.send("you caught " + msg)
    if message.content.startswith("j!forage"):
        await message.channel.send("you forage for a while...")
        time.sleep(2)
        msg = random.choice(open("rand/forage.txt").readlines())
        await message.channel.send("you found " + msg)

    ######################################
    #economy stuff:
    #make file if it doesn't exist
    def makeUserFile():
        if os.path.exists("users/" + str(message.author.id) + ".txt") == False:
            f = open("users/" + str(message.author.id) + ".txt", "w")
            f.write("0")
            f.close()
    #show balance to user
    if message.content.startswith("j!bal"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        bal = lines[0]
        await message.channel.send("your balance is {0} jayebucks! :moneybag:".format(bal))
    #get a lot of money once per day
    if message.content.startswith("j!daily"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        currentDate = datetime.now()
        if len(lines) > 1:
            lastDate = datetime.strptime(lines[1], '%Y-%m-%d %H:%M:%S.%f')
            difference = currentDate - lastDate
            if difference.days == 0:
                timeLeft = int(24 - (difference.seconds / 3600))
                await message.channel.send("you can only use this once per day! :dizzy_face: :alarm_clock:")
                await message.channel.send("{0} more hours to wait!".format(timeLeft))
            else:
                bal = int(lines[0]) + 100
                bal = str(bal)
                lines[0] = bal + "\n"
                lines[1] = str(datetime.now())
                await message.channel.send("you collect 100, and now have {0} jayebucks! :money_mouth:".format(bal)) 
        else:
            bal = int(lines[0]) + 150
            bal = str(bal)
            lines[0] = bal + "\n"
            lines.append(str(datetime.now()))
            await message.channel.send("you collect 100, and now have {0} jayebucks! :money_mouth:".format(bal))  
        with open("users/" + str(message.author.id) + ".txt", "w") as f:
            for line in lines:
                f.write(line)  
    #get just one money whenever
    if message.content.startswith("j!mine"):
        makeUserFile()
        with open("users/" + str(message.author.id) + ".txt", "r") as f:
            lines = f.readlines()
        bal = int(lines[0]) + 1
        bal = str(bal)
        lines[0] = bal + "\n"
        with open("users/" + str(message.author.id) + ".txt", "w") as f:
            for line in lines:
                f.write(line)
        await message.channel.send("you mine a jayebuck, and now have {0}! :dollar: :pick:".format(bal))
    #slot machine
    if message.content.startswith("j!slots "):
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
            if payout == 1:
                win = moneySpent + (moneySpent // 2)
                newBal += win
                await message.channel.send(":seven::seven::bell: | amazing!\nyou make 250% of your bet!\n{0} + {1} = {2} jayebucks".format(bal,win,newBal))
            if payout == 2:
                win = moneySpent
                newBal += win
                await message.channel.send(":cherries::cherries::cherries: | awesome!!\nyou make 200% of your bet!\n{0} + {1} = {2} jayebucks".format(bal,win,newBal))
            if payout == 3:
                win = moneySpent // 2
                newBal += win
                await message.channel.send(":cherries::cherries::seven: | great!\nyou make 150% of your bet!\n{0} + {1} = {2} jayebucks".format(bal,win,newBal))
            if payout == 4:
                win = (moneySpent // 2) + (moneySpent // 4)
                newBal += win
                await message.channel.send(":bell::bell::bell: | wow!!\nyou make 175% of your bet!\n{0} + {1} = {2} jayebucks".format(bal,win,newBal))
            if payout == 5:
                await message.channel.send(":bell::bell::watermelon: | no loss!\nyou make back your bet.\n{0} +/- 0 = {0} jayebucks.".format(bal))
            if payout == 6:
                win = moneySpent // 4
                newBal += win
                await message.channel.send(":watermelon::watermelon::watermelon: | neat!\nyou make 125% of your bet.\n{0} + {1} = {2} jayebucks".format(bal,win,newBal))               
            if payout == 7:
                loss = moneySpent // 4
                newBal -= loss
                await message.channel.send(":watermelon::watermelon::bell: | small loss!\nyou get back just 75% of your bet.\n{0} - {1} = {2} jayebucks".format(bal,loss,newBal))  
            if payout > 7:
                newBal -= moneySpent
                slots = random.choice(open("rand/slots.txt").readlines())
                await message.channel.send("{0} | oof, you lost your bet!\nbetter luck next time.\n{1} - {2} = {3} jayebucks".format(slots[:-1],bal,moneySpent,newBal))                
            lines[0] = str(newBal) + "\n"
            with open("users/" + str(message.author.id) + ".txt", "w") as f:
                for line in lines:
                    f.write(line)
                        
    ######################################
    #random number pickers:
    #coinflip games
    if message.content.startswith("j!coin"):
        flip = random.randint(1,2)
        if flip == 1:
            await message.channel.send("heads! https://i.imgur.com/aGQ2urm.jpg")
        else:
            await message.channel.send("tails! https://i.imgur.com/KtptwZR.jpg")
    if message.content.startswith("j!random"):
        flip = random.randint(1,2)
        if flip == 1:
            await message.channel.send("yes")
        else:
            await message.channel.send("no")
    #dice/ number picking
    if message.content.startswith("j!dice "):
        num = message.content[7:]
        try:
            num = int(num)
        except ValueError:
            await message.channel.send("you need to type a number! e.g. 'j!dice 6'")
            return
        flip = random.randint(1,num)
        await message.channel.send(flip)
    #iq picker
    if message.content.startswith("j!myiq") or message.content.startswith("j!my iq"):
        flip = random.randint(1,10)
        if flip < 6: #5 values
            flip = random.randint (80,120)
        elif flip < 9: #4 values
            flip = random.randint (1,2)
            if flip == 1:
                flip = random.randint (50,79)
            else:
                flip = random.randint (121,150)
        else: #2 values
            flip = random.randint (1,2)
            if flip == 1:
                flip = random.randint (1,49)
            else:
                flip = random.randint (151,200)
        await message.channel.send("your IQ is {0}! :brain:".format(flip))
    #russian roulette
    if message.content.startswith("j!rr"):
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
    if message.content.startswith("j!suicide"):
        await message.channel.send("you spin the cylinder and put the gun to your head :relieved::gun:\ntake a deep breath!")
        time.sleep(3)
        await message.channel.send("bang! you're dead x _ x :boom:")

    ######################################
    #conversational:
    #randomized answers to questions
    elif message.content.startswith("j!do ") or message.content.startswith("j!does ") or message.content.startswith("j!can ") or message.content.startswith("j!will ") or message.content.startswith("j!should ") or message.content.startswith("j!is ") or message.content.startswith("j!are "):
        answers = ["yes","yep","no","yeah!","i believe so!","nope!","hmm... yeah","hmm... no","sure","nah","absolutely!","absolutely not","maybe","i don't really know"]
        await message.channel.send(random.choice(answers))
    elif message.content.startswith("j!where "):
        answers = ["in space","somewhere in idaho","the big apple","cuba","antartica","a drug den in colombia","this server","the eiffel tower","on mars","pizza hut","the sahara desert","siberia","in a maximum security prison"]
        await message.channel.send(random.choice(answers))
    elif message.content.startswith("j!when "):
        answers = ["yesterday","today","tomorrow","in a million years","in ten years","in a year's time","this morning","this afternoon","this evening","tonight","at the next full moon","whens the stars are aligned","when you are old and grey","when the stars are aligned"]
        await message.channel.send(random.choice(answers))
    elif message.content.startswith("j!who "):
        answers = ["the KGB","mormons","xi jinping","the harry potter fandom","furries","nazis","russian hackers","the clinton foundation","the trump administration","antifa","anarchists","escaped monkeys","rogue androids","skynet","god","mole people","night goblins","jazz musicians","the KKK","cowboys","meth addicts","leather fetishists"]
        await message.channel.send(random.choice(answers))
    elif message.content.startswith("j!what "):
        answers = ["what"]
        await message.channel.send(random.choice(answers))
    elif message.content.startswith("j!why "):
        answers = ["lots of tiny worms","a plague of frogs","the skeleton war","the forever war","i got a spoon stuck in the dishwasher","big nukes","russian hackers","it seemed right at the time","human nature","it only exists in that it pleases me","the stars were aligned correctly","it is gods will","the machine god wills it"]
        await message.channel.send(random.choice(answers))
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
    elif message.content.startswith("j!retard") or message.content.startswith("j!okay") or message.content.startswith("j!ok"):
        await message.channel.send("ok retadr")
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
    print("jayebot is now online!")
    print(client.user.id)
    print("------")
client.run(TOKEN)
