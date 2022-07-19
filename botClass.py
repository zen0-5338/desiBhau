import discord
from discord import app_commands
from discord.ext import commands
from typing import Type, Optional, Any


class DesiBhauClient(commands.Bot):
    def __init__(self, *, description: Optional[str] = None, **options: Any) -> None:
        command_prefix = "$"
        intents = discord.Intents.default()

        super().__init__(command_prefix=command_prefix, description=description, intents=intents, **options)

    async def on_ready(self):
        print("Logged in.")

    async def setup_hook(self) -> None:
        try:
            await self.load_extension("src.test")
            print("Loaded module test.")
        except Exception as e:
            print(e.__traceback__)
