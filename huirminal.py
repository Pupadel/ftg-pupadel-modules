from .. import loader, utils
from asyncio import sleep

def register(cb):
	cb(хуирминалMod())
	
class хуирминалMod(loader.Module):
	"""пупадел топ"""
	strings = {'name': 'хуирминал'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
		
	async def terminаlcmd(self, message):
		"""ахвха это пранк броо"""
		args = utils.get_args_raw(message)
		await message.edit(f'<strong>Выполняемая cumанда:</strong>\n<code>{args}</code>\n\n<strong>Вывод:</strong>\n\n<strong>Ошибки/Предупреждения:</strong>')
		await sleep(0.2)
		await message.edit(f'<strong>Выполняемая cumанда:</strong>\n<code>{args}</code>\n\n<strong>Команда завершилась с кодом:</strong> <code>0</code>\n\n<strong>Вывод:</strong>\n\n\n<strong>Ошибки/Предупреждения:</strong>')
