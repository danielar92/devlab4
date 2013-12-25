from django.db import models

class Pagina(models.Model):
	url = models.URLField('URL',max_length=500,primary_key=True)
	nombre = models.CharField('Nombre',max_length=200)
	likes = models.PositiveIntegerField('Likes',default=0)
	dislikes = models.PositiveIntegerField('Dislikes',default=0)
	ranking = models.PositiveIntegerField('Ranking',default=0)

	def __unicode__(self):
		return self.nombre + " (" + self.url + ")"

class Usuario(models.Model):
	correo = models.EmailField('Correo',max_length=200,primary_key=True)
	username = models.CharField('Username',max_length=200)
	password = models.CharField('Password',max_length=200)
	paginas = models.ManyToManyField(Pagina,blank=True)

	def __unicode__(self):
		return self.username 
   
class Categoria(models.Model):
	nombre = models.CharField('Nombre',max_length=200,primary_key=True)
	paginas = models.ManyToManyField(Pagina,blank=True)
	usuarios = models.ManyToManyField(Usuario,blank=True)

	def __unicode__(self):
		return self.nombre
