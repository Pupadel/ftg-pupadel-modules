from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError


def register(cb):
    cb(WhatAnimeMod())
    
class WhatAnimeMod(loader.Module):
    """Поиск аниме по фото by @WhatAnimeBot """
    strings = {'name': 'WhatAnime'}

    async def animecmd(self, message):
        """Используй: .anime <реплай>."""
        chat = "@WhatAnimeBot"
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if text:
         reply = text
        await message.edit("<b>Минуточку...</b>")
        async with message.client.conversation(chat) as conv:
            try:
                user = await utils.get_user(reply)
                response = conv.wait_event(events.MessageEdited(incoming=True, from_users=chat))
                video = conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
                await message.client.send_message(chat, reply)
                response = await response
                video = await video
            except YouBlockedUserError:
                await message.edit("<b>Разблокируй @WhatAnimeBot</b>")
                return
            await message.client.send_message(message.to_id, response.message)
            await message.client.send_message(message.to_id, video.message)
            await message.delete()