import discord
from botCredentials import ADMIN_ID, OWNER_ID
# from random import randint,seed


class DesiBhauClient(discord.Client):

    curseKeyWords = ["topa", "gandu", 'randi',
                     "chu", "mc", "bc", "bsdk", "lod", "muh"]
    requireNSFWPermissions = True
    backfire = True
    tagUserFormatStringPC = "<@!{0}>"
    tagUserFormatStringMobile = "<@{0}>"

    async def on_ready(self):
        # seed()
        print('Logged on as {0}!'.format(self.user))

    ######## MESSAGE PARSING ########
    async def on_message(self, message):
        try:
            messageContent = message.content.lower()
            messageAuthorID = message.author.id

            print(messageContent)

            botMentioned = bool(
                message.content.find(
                    self.tagUserFormatStringPC.format(self.user.id)) != -1
                or
                message.content.find(
                    self.tagUserFormatStringMobile.format(self.user.id)) != -1
            )

            if message.author == self.user or message.author.bot or not botMentioned:
                return

            if str(messageAuthorID) in ADMIN_ID:
                if messageContent.find("shutdown") != -1:
                    await message.channel.send("Shutting down...")
                    await self.close()

                elif messageContent.find("nsfw") != -1:
                    self.requireNSFWPermissions = not self.requireNSFWPermissions
                    await message.channel.send("NSFW Channel Required : {}".format(self.requireNSFWPermissions))
            else:
                if messageContent.find("shutdown") != -1 or messageContent.find("nsfw") != -1:
                    await message.channel.send("Nikal laude, pehli fursat me nikal,nahi milne wala tujhe kuch <a:youtried:803206113935753237>")
                

            ###### BOT MENTION PROCESSING #######
            if not message.channel.nsfw and self.requireNSFWPermissions:
                await message.channel.send("I can't curse you back dammit. Enable NSFW permissions in this channel.")
                return

            # messageContent += self.curseKeyWords[randint(0,len(self.curseKeyWords)-1)]
            if self.backfire:

                if messageContent.find("gand") != -1:
                    # print('Message from {0.author}: {0.content}'.format(message))
                    await message.channel.send("<@{0}> , do chapaat marunga to akal aayegi.".format(messageAuthorID))

                elif messageContent.find("topa") != -1:
                    await message.channel.send("<@{0}>, chup re ne nahitar tara ghare aaine maaris.".format(messageAuthorID))

                elif messageContent.find("randi") != -1:
                    await message.channel.send("<@{0}>, teri maa randi saale.".format(messageAuthorID))

                # elif messageContent.find("chutiya") != -1 or messageContent.find("chutiye") != -1:
                elif messageContent.find("chu") != -1:
                    await message.channel.send("<@{0}>, muh me le mera 9 inch ka.".format(messageAuthorID))

                elif messageContent.find("mc") != -1 or messageContent.find("madar") != -1:
                    await message.channel.send("<@{0}>, tabhi to tu is duniya me aaya.".format(messageAuthorID))

                elif messageContent.find("bc") != -1 or messageContent.find("bhen") != -1:
                    await message.channel.send("<@{0}>, sidhe teri gaand me danda daalunga.".format(messageAuthorID))

                elif messageContent.find("bsdk") != -1 or messageContent.find("bosd") != -1:
                    await message.channel.send("<@{0}>, loduchand teri gaand faad dunga.".format(messageAuthorID))

                elif messageContent.find("lod") != -1 or messageContent.find("lund") != -1 or messageContent.find("laud") != -1 or messageContent.find("land") != -1 or messageContent.find("lawd") != -1:
                    await message.channel.send("<@{0}>, Lauda faink ke marunga puri khandan chud jayegi.".format(messageAuthorID))

                elif messageContent.find("muh") != -1 or messageContent.find("mooh") != -1:
                    await message.channel.send("<@{0}>".format(messageAuthorID))

                else:
                    print("None of above")

        except Exception as onMessageException:
            print("onMessageException, Type - {} : {}".format(
                onMessageException.__class__.__name__, onMessageException))

    async def on_disconnect(self):
        print("Successfully disconnected {0} !".format(self.user))
