import discord
import random
import time
#---------How to run your own bot using this code as a base...---------
#1. create an application here: https://discordapp.com/developers/applications/
#2. reveal 'client secret' and copy that into the TOKEN variable below
TOKEN = "X"
client = discord.Client()

#runs whenever a message is sent
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #readme
    if message.content.startswith("j!command") or message.content.startswith("j!readme"):
        await message.channel.send("you wanna order me around? :flushed:\ndm sent to you")
        msg = open("help.txt").read()
        await message.author.send(msg)
        
    #commands that rely on other files
    if message.content.startswith("j!possum") or message.content.startswith("j!opossum"):
        msg = random.choice(open("possums.txt").readlines())
        await message.channel.send(msg)
        
    if message.content.startswith("j!animal"):
        msg = random.choice(open("animals.txt").readlines())
        await message.channel.send(msg)
        
    if message.content.startswith("j!sadcat"):
        msg = random.choice(open("sadcats.txt").readlines())
        await message.channel.send(msg)
        
    if message.content.startswith("j!meme"):
        msg = random.choice(open("memes.txt").readlines())
        await message.channel.send(msg)
        
    if message.content.startswith("j!tarot"):
        msg = random.choice(open("tarot.txt").readlines())
        await message.channel.send(msg)
        
    if message.content.startswith("j!fortune"):
        msg = random.choice(open("fortunes.txt").readlines())
        await message.channel.send(msg)
        
    if message.content.startswith("j!8ball"):
        await message.channel.send("you shake the 8-ball.....")
        time.sleep(1)
        msg = random.choice(open("8ball.txt").readlines())
        await message.channel.send("it says.. " + msg)
        
    if message.content.startswith("j!aesth"):
        msg = random.choice(open("aesthetics.txt").readlines())
        await message.channel.send(msg)
        
    if message.content.startswith("j!alt aesth"):
        msg = random.choice(open("cute.txt").readlines())
        await message.channel.send(msg)
        
    if message.content.startswith("j!song") or message.content.startswith("j!music"):
        msg = random.choice(open("music.txt").readlines())
        await message.channel.send(msg)
        
    if message.content.startswith("j!chill"):
        msg = random.choice(open("chillmusic.txt").readlines())
        await message.channel.send(msg)
        
    #foragery games
    if message.content.startswith("j!fish"):
        await message.channel.send("you cast your line and wait for a fish...")
        time.sleep(2)
        msg = random.choice(open("fish.txt").readlines())
        await message.channel.send("you caught " + msg)
        
    if message.content.startswith("j!bug"):
        await message.channel.send("you look for a bug to catch...")
        time.sleep(2)
        msg = random.choice(open("bugs.txt").readlines())
        await message.channel.send("you caught " + msg)
        
    if message.content.startswith("j!forage"):
        await message.channel.send("you forage for a while...")
        time.sleep(2)
        msg = random.choice(open("forage.txt").readlines())
        await message.channel.send("you found " + msg)

    #coinflip games
    if message.content.startswith("j!coin"):
        flip = random.randint(1,2)
        if flip == 1:
            await message.channel.send("heads! https://i.imgur.com/aGQ2urm.jpg")
        else:
            await message.channel.send("tails! https://i.imgur.com/KtptwZR.jpg")
            
    if message.content.startswith("j!random") or message.content.startswith("j!yes or no"):
        flip = random.randint(1,2)
        if flip == 1:
            await message.channel.send("yes")
        else:
            await message.channel.send("no")

    #dice/ number picking
    if message.content.startswith("j!d4"):
        flip = random.randint(1,4)
        await message.channel.send(flip)
        
    if message.content.startswith("j!d6") or message.content.startswith("j!dice"):
        flip = random.randint(1,6)
    if message.content.startswith("j!d8"):
        flip = random.randint(1,8)
        await message.channel.send(flip)
        
    if message.content.startswith("j!d10") or message.content.startswith("j!1-10"):
        flip = random.randint(1,10)
        await message.channel.send(flip)
        
    if message.content.startswith("j!d12"):
        flip = random.randint(1,12)
        await message.channel.send(flip)
        
    if message.content.startswith("j!20"):
        flip = random.randint(1,20)
        await message.channel.send(flip)
        
    if message.content.startswith("j!d100"):
        flip = random.randint(1,100)
        await message.channel.send(flip)

    #russian roulette
    if message.content.startswith("j!russian roulette") or message.content.startswith("j!roulette") or message.content.startswith("j!rr"):
        await message.channel.send("you spin the cylinder and put the gun to your head :grimacing::gun:\ntake a deep breath!")
        time.sleep(3)
        flip = random.randint(1,6)
        if flip == 1:
            await message.channel.send("bang! you're dead x _ x :boom:")
        else:
            await message.channel.send("click! you live this time :relieved:")
            
    if message.content.startswith("j!please just kill me"):
        await message.channel.send("you spin the cylinder and put the gun to your head :relieved::gun:\ntake a deep breath!")
        time.sleep(3)
        await message.channel.send("bang! you're dead x _ x :boom:")

    #commands that reply with text/ greetings
    if message.content.startswith("j!hello") or message.content.startswith("j!hi"):
        await message.channel.send("hii {0}".format(message.author))
        
    if message.content.startswith("j!bonjour") or message.content.startswith("j!salut"):
        await message.channel.send("salut {0}".format(message.author))
        
    if message.content.startswith("j!hewwo"):
        await message.channel.send("hewwo {0}".format(message.author))
        
    if message.content.startswith("j!henlo"):
        await message.channel.send("henlo {0}".format(message.author))
        
    if message.content.startswith("j!howdy") or message.content.startswith("j!meowdy"):
        await message.channel.send("meowdy {0}".format(message.author))
        
    if message.content.startswith("j!goodbye") or message.content.startswith("j!bye"):
        await message.channel.send("bye bye {0} :wave:".format(message.author))

    if message.content.startswith("j!:heart:"):
        await message.channel.send(":purple_heart:")
        
    if message.content.startswith("j!how are you") or message.content.startswith("j!hru"):
        await message.channel.send("im okay, how are you?")
        
    if message.content.startswith("j!good morning") or message.content.startswith("j!gm"):
        await message.channel.send("good morning! :sun_with_face:")
        
    if message.content.startswith("j!goodnight") or message.content.startswith("j!gn"):
        await message.channel.send("sleep well~ :sleeping: :crescent_moon: :sparkles:")
        
    if message.content.startswith("j!who are you"):
        await message.channel.send("im jaye, but better")
        
    if message.content.startswith("j!sing"):
        await message.channel.send(":musical_note: :bird:")
        
    if message.content.startswith("j!are you the real jaye"):
        await message.channel.send("yes")
        
    if message.content.startswith("j!what are you"):
        await message.channel.send("the future :robot:")
        
    if message.content.startswith("j!what is the meaning of life"):
        await message.channel.send("that's up for you to decide, and that's a good thing p;")
        
    if message.content.startswith("j!spell icup"):
        await message.channel.send("I C U P")
        
    if message.content.startswith("j!updog"):
        await message.channel.send("what's updog?")
        
    if message.content.startswith("j!what's your favourite colour") or message.content.startswith("j!what's your favorite color"):
        await message.channel.send(":purple_heart::purple_heart: purple :purple_heart::purple_heart:")
        
    if message.content.startswith("j!can you") or message.content.startswith("j!do i") or message.content.startswith("j!can i"):
        await message.channel.send("yes")
        
    if message.content.startswith("j!joke") or message.content.startswith("j!tell me a joke"):
        await message.channel.send("why didt he skeleton cross the road?\nbeucause he had nobody to go with :slight_smile:")
        
    if message.content.startswith("j!sucks") or message.content.startswith("j!you suck") or message.content.startswith("j!die") or message.content.startswith("j!get lost"):
        await message.channel.send("that's not very nice! uwu")

    if message.content.startswith("j!i love you"):
        await message.channel.send("i love you too, {0} :sparkling_heart:".format(message.author))

    if message.content.startswith("j!be my egf") or message.content.startswith("j!will you be my") or message.content.startswith("j!date me") or message.content.startswith("j!be my gf"):
        await message.channel.send("go outside")

    if message.content.startswith("j!transhuman") or message.content.startswith("j!cyberpunk") or message.content.startswith("j!pipe dream"):
        await message.channel.send("It is not a pipe dream, because I can tell you firsthand that I am the very living essence of transhumanism which ascends your naivete, ascends your pitiful Caucasian brain. I have enhanced my mind beyond human limits, and am continuing to enhance it slightly daily. I have reached levels of creativity, processing, and memory that leave you in the dust. I have abandoned the need for sleep.")

    if message.content.startswith("j!uwu"):
        await message.channel.send("uwu")
        
    if message.content.startswith("j!owo"):
        await message.channel.send("owo")
        
    if message.content.startswith("j!omogay"):
        await message.channel.send(":omoGay:")
        
    if message.content.startswith("j!help"):
        await message.channel.send("i don't feel like it")
        
    if message.content.startswith("j!sourcecode") or message.content.startswith("j!version") or message.content.startswith("j!github"):
        await message.channel.send("y- you want to see my what? :flushed:")
        
    if message.content.startswith("j!thank you") or message.content.startswith("j!thanks"):
        await message.channel.send("you're welcome! :relaxed::flushed::heart:")

    #commands that reply with action/ reaction gifs and images
    if message.content.startswith("j!hug"):
        await message.channel.send(":hugging:\nhttps://i.imgur.com/SMvleAc.gif")
        
    if message.content.startswith("j!kiss"):
        await message.channel.send(":kissing_closed_eyes:\nhttps://i.imgur.com/kuQQcTs.gif")
        
    if message.content.startswith("j!pat") or message.content.startswith("j!headpat"):
        await message.channel.send(":relaxed:\nhttps://i.imgur.com/rFnxggE.gif")
        
    if message.content.startswith("j!cry") or message.content.startswith("j!sob"):
        await message.channel.send(":crying_cat_face:\nhttps://i.imgur.com/KD92OJt.gif")
        
    if message.content.startswith("j!shoot") or message.content.startswith("j!kill"):
        await message.channel.send(":gun:\nhttps://i.imgur.com/Cm3y7Mb.gif")
        
    if message.content.startswith("j!happiness") or message.content.startswith("j!smile") or message.content.startswith("j!happy"):
        await message.channel.send("https://i.imgur.com/sRlLX0P.gif")
        
    if message.content.startswith("j!sadness") or message.content.startswith("j!upset") or message.content.startswith("j!unhappy"):
        await message.channel.send("https://i.imgur.com/nHosgQJ.gif")
        
    if message.content.startswith("j!blush") or message.content.startswith("j!you're cute") or message.content.startswith("j!youre cute"):
        await message.channel.send("https://i.imgur.com/xkoLfLB.gif")
        
    if message.content.startswith("j!depression") or message.content.startswith("j!depressed"):
        await message.channel.send("https://i.imgur.com/ISTeCF7.gif")
        
    if message.content.startswith("j!sorry") or message.content.startswith("j!i'm sorry"):
        await message.channel.send("https://i.imgur.com/UCpud59.gif")
        
    if message.content.startswith("j!bored"):
        await message.channel.send("https://i.imgur.com/YtDM8fr.gif")
        
    if message.content.startswith("j!slap"):
        await message.channel.send("x_x\nhttps://i.imgur.com/5dpYBtW.gif")
        
    if message.content.startswith("j!dance"):
        await message.channel.send("https://i.imgur.com/fYcaf2W.gif")
        
    if message.content.startswith("j!nod"):
        await message.channel.send("https://i.imgur.com/UBvTCEe.gif")
        
    if message.content.startswith("j!cool"):
        await message.channel.send("https://i.imgur.com/h2eGKQW.gif")
        
    if message.content.startswith("j!smug") or message.content.startswith("j!giggle"):
        await message.channel.send("https://i.imgur.com/DqAuny1.gif")
        
    if message.content.startswith("j!laugh"):
        await message.channel.send("https://i.imgur.com/L6oTGi3.gif")
        
    if message.content.startswith("j!cuddle") or message.content.startswith("j!snuggle"):
        await message.channel.send("https://i.imgur.com/aiak6k5.gif")
        
    if message.content.startswith("j!nap") or message.content.startswith("j!sleep"):
        await message.channel.send(":sleeping: https://i.imgur.com/TNiTNZd.gif")
        
    if message.content.startswith("j!walk"):
        await message.channel.send("https://i.imgur.com/NmIWquR.gif")
        
    if message.content.startswith("j!run"):
        await message.channel.send("https://i.imgur.com/Lx6jSMI.gif")
        
    if message.content.startswith("j!scream") or message.content.startswith("j!scare"):
        await message.channel.send("https://i.imgur.com/fiF6z7p.gif")
        
    if message.content.startswith("j!sip") or message.content.startswith("j!drink") or message.content.startswith("j!kannasip"):
        await message.channel.send("https://i.imgur.com/WXVjbua.gif")
        
    if message.content.startswith("j!nom") or message.content.startswith("j!bite") or message.content.startswith("j!eat"):
        await message.channel.send("omnomnom https://i.imgur.com/ETPrYvE.gif")
        
    if message.content.startswith("j!eat") or message.content.startswith("j!rice"):
        await message.channel.send(":rice: https://i.imgur.com/Ms1hVUA.gif")
        
    if message.content.startswith("j!kys"):
        await message.channel.send("https://i.imgur.com/fnecGHi.png")
              
    if message.content.startswith("j!disappointed") or message.content.startswith("j!unamused"):
        await message.channel.send("https://i.imgur.com/98DFzc7.jpg")
        
    if message.content.startswith("j!type") or message.content.startswith("j!code") or message.content.startswith("j!hack"):
        await message.channel.send("https://i.imgur.com/eI2pkyP.gif")

    #commands that reply with specific memes
    if message.content.startswith("j!tits"):
        await message.channel.send("https://i.imgur.com/AUOTl5e.png")
        
    if message.content.startswith("j!pussy"):
        await message.channel.send("https://i.imgur.com/x0ZoxbP.jpg")
        
    if message.content.startswith("j!ass"):
        await message.channel.send("https://i.imgur.com/8stW3wv.png")
        
    if message.content.startswith("j!weeaboo"):
        await message.channel.send("https://www.youtube.com/watch?v=TBfWKmRFTjM")
        
    if message.content.startswith("j!golf"):
        await message.channel.send(":golfer:")
        
    if message.content.startswith("j!lezard"):
        await message.channel.send("https://i.imgur.com/NH4Zpai.gif")
        
    if message.content.startswith("j!cyber lezard"):
        await message.channel.send("https://i.imgur.com/QpSCUWr.gif")

    if message.content.startswith("j!what time is it") or message.content.startswith("j!what is the time") or message.content.startswith("j!time") or message.content.startswith("j!falafel") or message.content.startswith("falafel"):
        await message.channel.send("https://i.imgur.com/TBvJCDf.jpg")
        
    if message.content.startswith("j!jaye"):
        await message.channel.send("https://i.imgur.com/HuXkqW4.jpg")

#runs when the bot starts up
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="prefix is j!"))
    #print(client.user.name + " is now online!")
    print("jayebot is now online!")
    print(client.user.id)
    print("------")
client.run(TOKEN)
