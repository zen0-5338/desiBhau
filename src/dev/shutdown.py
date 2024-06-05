import discord
from discord.ext import commands
from typing import Optional,Literal

class shutdown(commands.Cog):
    def __init__(self,bot : commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="shutdown")
    async def shutdown(self,ctx):
        await ctx.bot.close()
    
async def setup(bot : commands.Bot):
    await bot.add_cog(shutdown(bot))


