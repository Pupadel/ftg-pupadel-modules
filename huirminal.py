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
		await message.edit(f'<strong>Command:</strong> <code>{args}</code>\n<strong>Code:</strong> <code>0</code>\n<strong>Stdout:</strong>\n\n\n<strong>Stderr:</strong>')
