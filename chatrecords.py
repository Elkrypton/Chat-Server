

class ChatRecord(object):

	def __init__(self):
		self.data = []

	def add(self,s):
		return self.data.append(s)

	def __str__(self):

		if len(self.data) == 0:
			return "no message yet !"
		else:
			_data = '\n'.join(self.data)
			self.save_data(_data)
			return '\n'.join(self.data)

	def save_data(self,data):

		File = open('log.txt','a')
		File.write(str(data))
		File.close()