import discord
from discord import app_commands
from discord.ext import commands

class test(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="test2")
    async def test2(self, interaction : discord.Interaction):
        await interaction.response.send_message("Eagle has landed!", ephemeral=True)
    
    @commands.command(name="test")
    async def test(self,ctx,*args):
        print(args)
        if args is not None:
            await ctx.reply(" ".join(args))
        else:
            ctx.reply("The Eagle has landed!")

async def setup(bot : commands.Bot):
    await bot.add_cog(test(bot))

