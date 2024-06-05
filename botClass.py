import discord
from discord.ext import commands
from discord import app_commands
from typing import Type, Optional, Any

class DesiBhauClient(commands.Bot):
    def __init__(self, *, description: Optional[str] = None, **options: Any) -> None:
        command_prefix = "$"
        intents = discord.Intents.default()
        intents.message_content = True
        self.commandsSynced = False
        super().__init__(command_prefix=command_prefix, description=description, intents=intents, **options)

    async def on_ready(self):
        await self.wait_until_ready()
        # assert isinstance(self,commands.Bot)
        # self.commandTree = app_commands.CommandTree(self)
        # print(self.tree)
        if not self.commandsSynced:
            await self.tree.sync(guild=discord.Object(654590713333415937))
            print(self.tree)
            self.commandsSynced = True
        print("Logged in.")

    async def setup_hook(self) -> None:
        try:
            await self.load_extension("src.dev.shutdown")
            print("Loaded shutdown.")
            await self.load_extension("src.dev.sync")
            print("Loaded sync.")
            await self.load_extension("src.test")
            print("Loaded test.")

        except Exception as e:
            print(e)