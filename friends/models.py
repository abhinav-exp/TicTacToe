from django.db import models

# Create your models here.
class room(models.Model):
	name = models.CharField(max_length = 3)
	last_t = models.DateTimeField()
	player1 = models.CharField(max_length = 32,blank=True)
	player2 = models.CharField(max_length = 32,blank=True)
	state = models.CharField(max_length = 9, blank=True)

	def __str__(self):
		return str(self.name)+" "+str(self.last_t)+" "\
			+" "+str(self.state)+" "+str(self.player1)+" "+str(self.player2)