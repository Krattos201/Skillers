from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'pages'

class MyAppConfig(AppConfig):
	name ='myapp'

	def ready(self):
		from . import handlers