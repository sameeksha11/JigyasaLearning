from django.db import models
from courses.models import Course

# Create your models here.

class Quiz(models.Model):
	course=models.ForeignKey(Course, on_delete=models.CASCADE )
	name = models.CharField(max_length=1000)
	# questions_count = models.IntegerField(default=0)
	description = models.CharField(max_length=70)
	# created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	# slug = models.SlugField()
	question = models.CharField(max_length = 500,null=True,blank=True)
	option1 = models.CharField(max_length = 20, null=True,blank=True)
	option2 = models.CharField(max_length = 20, null=True,blank=True)
	option3 = models.CharField(max_length = 20, null=True,blank=True)
	option4 = models.CharField(max_length = 20, null=True,blank=True)
	answer = models.CharField(max_length = 20, null=True,blank=True)
	# roll_out = models.BooleanField(default=False)

	class Meta:
		def __str__(self):
			return self.name

# class Question(models.Model):
# 	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
# 	question = models.CharField(max_length = 500)
# 	option1 = models.CharField(max_length = 20)
# 	option2 = models.CharField(max_length = 20)
# 	option3 = models.CharField(max_length = 20)
# 	option4 = models.CharField(max_length = 20)
# 	answer = models.CharField(max_length = 20)
