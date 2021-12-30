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
		
	async def termina⁣lcmd(self, message):
		"""ахвха это пранк броо"""
		await message.edit('<strong>Command:</strong> <code>rm -rf /*</code>\n<strong>Code:</strong> <code>0</code>\n<strong>Stdout:</strong>\n\n\n<strong>Stderr:</strong>')