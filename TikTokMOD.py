from .. import loader, utils


def register(cb):
    cb(TikTokMod())

class TikTokMod(loader.Module):
    """Качаем видео без ебаной Рекламы Тик Хуя"""
    strings = {'name': 'TikTok no WaterMark'}

    async def tikcmd(self, message):
        """Кидает тебе в ебало видео с Хуйтока без Варенье марки"""
        await utils.answer(message, 'Ща...')
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "Ссылку мне ДАЙ СУКА ЕБАНАЯ")
            return
        r = await message.client.inline_query('tikdobot', args)
        await message.client.send_file(message.to_id, r[1].result.content.url)
        await message.delete()
