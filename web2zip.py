from .. import loader, utils
from asyncio import sleep
import subprocess as sp

def register(cb):
	cb(Web2zipMod())
	
class Web2zipMod(loader.Module):
	"""пупадел топ"""
	strings = {'name': 'Web2zip'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
		
	async def web2zipcmd(self, message):
		""".web2zip <ссылка на сайт>/nExemple: https://pupadel.ml"""
		website = utils.get_args_raw(message)
		if website.startswith("https://"):
			website = website[8:]
		if website.startswith("http://"):
			website = website[7:]
		if not website:
			await message.edit("Используйте <code>.help Web2zip</code>")
			return
		await message.edit("<code>Загрузка.</code>")
		await sleep(0.5)
		await message.edit("<code>Загрузка..</code>")
		await sleep(0.5)
		await message.edit("<code>Загрузка...</code>")
		sp.getoutput('apt install wget -y && apt install zip -y')
		path = sp.getoutput('pwd')
		output = sp.getoutput(f'wget -r -k -l 30 -p -E -nc {website} -P {path}')
		if f'wget: unable to resolve host address ‘{website}’' in output:
			await message.edit("<code>Сайт не найден</code>")
			return
		sp.getoutput(f'zip -r {website}.zip {website}/')
		await message.respond(file=f'{path}/{website}.zip')
		sp.getoutput(f'rm -rf {path}/{website}.zip')
		sp.getoutput(f'rm -rf {path}/{website}')
		await message.delete()
