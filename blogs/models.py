from django.db import models

# Create your models here.
class Post(models.Model): 
    title = models.CharField(max_length = 120)
    body = models.TextField()
    author = models.ForeignKey(
        "auth.User", 
        on_delete = models.CASCADE #Comportamiento para borrar todo el contenido de ese autor
    )

    def __str__(self) -> str: #Este metodo sirve para mostrar el titulo de los post de la tabla
        return self.title