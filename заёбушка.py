from asyncio import sleep
from .. import loader, utils

def register(cb):
	cb(ЗаёбушкаMod())
	
class ЗаёбушкаMod(loader.Module):
	"""Заебет любого"""
	strings = {'name': 'NIGGER ALARM'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
		
	async def niggercmd(self, message):
		""".nigger <колличество> <реплай на того, кого заебать>"""
		reply = await message.get_reply_message()
		if not reply:
			await message.edit("<b>А кого заёбывать-то?</b>")
			return
		id = reply.from_id
		args = utils.get_args(message)
		count = 50
		if args:
			if args[0].isdigit():
				if int(args[0]) < 0:
					count = 50
				else:
					count = int(args[0])
		txt = '<a href="tg://user?id={}">!!!NIGGER ALARM!!!</a>'.format(id)
		await message.delete()
		for _ in range(count):
			await sleep(0.3)
			msg = await message.client.send_message(message.to_id, txt)
			await sleep(0.3)
			await msg.delete()
			
