from django.db import models

# Create your models here.
class room_model(models.Model):
	name = models.CharField(max_length = 3)
	last_t = models.DateTimeField()
	state = models.CharField(max_length = 9, blank=True)
	no_people = models.IntegerField(default=0)
	re = models.IntegerField(default = 0)
	def __str__(self):
		return str(self.name)+" "+str(self.last_t)+" "+str(self.no_people)+" "+str(self.state)