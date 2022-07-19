import discord
from discord import app_commands
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot : commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="test")
    async def test(self, interaction : discord.Interaction):
        await interaction.response.send_message("Eagle has landed!", ephemeral=True)
    
    # @commands.command(name="test")
    # async def test(self,ctx,args):
    #     await ctx.reply(args)

async def setup(bot : commands.Bot):
    await bot.add_cog(Test(bot))

