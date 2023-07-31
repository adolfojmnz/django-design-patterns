API_URL = "http://api.herocheck.com/?q={0}"


class SuperHeroWebAPI:

	@staticmethod
	def is_hero(username):
		url = API_URL.format(username)
		return webclient.get(url)
