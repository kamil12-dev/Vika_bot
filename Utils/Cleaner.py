from typing import List
from discord.ext.commands import Context
from discord import Message, Embed
from Config.Singleton import Singleton
from Music.AyameBot import AyameBot


class Cleaner(Singleton):
    def __init__(self, bot: AyameBot = None) -> None:
        if not super().created:
            self.__bot = bot
            self.__clean_str = 'Загрузчик:'

    def set_bot(self, bot: AyameBot) -> None:
        self.__bot = bot

    async def clean_messages(self, ctx: Context, quant: int) -> None:
        if self.__bot is None:
            return

        last_messages: List[Message] = await ctx.channel.history(limit=quant).flatten()

        for message in last_messages:
            try:
                if message.author == self.__bot.user:
                    if len(message.embeds) > 0:
                        embed: Embed = message.embeds[0]
                        if len(embed.fields) > 0:
                            if embed.fields[0].name == self.__clean_str:
                                await message.delete()
            except Exception as e:
                print(f'ПРИМЕЧАНИЕ РАЗРАБОТЧИКА -> Сообщения об ошибках очистки {e}')
                continue
