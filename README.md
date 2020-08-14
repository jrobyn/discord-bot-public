# jayebot-public

--Overview:
This is a public version of a Discord bot that I created just for fun, and added to servers I talk in. It has had some server specific commands removed, but is otherwise pretty much the same, and now has a lot of features. Anyone is welcome to use the code to help get their own bot working, and to adapt any games and commands for their own purposes.
Many commands are just for fun, like fortune telling, tarot, cute animal pictures, dice rolling, random number games, etc. There are also some conversational commands, like letting the bot rate items, choose between two options, answer questions, or send specific reaction gifs.
One major feature is a working economy. Users can collect daily rewards, mine or scavenge, and gift money to other users. The money can be spent either on a slot machine game or on a gacha 'monster girl' game.
Each user can also buy a pet, which is randomized. They can then train the pet, levelling it up, or play with it and feed it to keep it happy.
A non-exhaustive list of commands can be found in help.txt.

--Guide:
To run your own bot you will need to go to create an application on https://discordapp.com/developers/applications/, click to reveal 'client secret', and copy that into the TOKEN variable near the top of the code. If you then run the code in Python, with discord.py installed, the bot will come online and you can invite it to your servers. You can look at how I've written commands here and copy and change whatever you want to. Some examples of how user data is laid out are in the 'users' file, with one blank file, and one with sample data and descriptions.
Note that the emojis in the gacha section won't show up if you use that code as-is, and you may want to remove them, or replace them with emojis in a server that you are running the bot in.

thank you
