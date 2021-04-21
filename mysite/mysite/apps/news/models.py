import datetime
from django.db import models

from django.utils import timezone

class News(models.Model):
	news_title = models.CharField('название новости', max_length = 200)
	news_text = models.TextField('текст новости')
	pub_date = models.DateTimeField('дата публикации')
	
	def __str__(self):
		return self.news_title

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))	

	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'