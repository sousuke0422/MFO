import discord


class BaseWorker:
    def __init__(self, client: discord.Client):
        self.client = client
        ...

    async def loop(self, round_time: int, client: discord.Client):
        ...

    async def on_message(self, message: discord.Message):
        ...

    async def join(self, message: discord.Message):
        ...

    async def command(self, message: discord.Message, command: str, args: list):
        return True

    async def logout(self):
        ...
