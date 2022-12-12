from django.db import models

# Create your models here.
class productMainModel(models.Model):
    SIZE=(
        ('10','10'),
        ('20','20'),
        ('30','30'),
    )
    Quality=(
        ('high','high'),
        ('low','low'),
        ('medium','medium')
    )

    title=models.CharField(max_length=20)
    description=models.TextField()
    price=models.IntegerField()
    unique_code=models.CharField(max_length=10,unique=True)
    Size=models.CharField(max_length=10,choices=SIZE)
    quality=models.CharField(max_length=10,choices=Quality)

    def __str__(self):
        return self.title 
 

class productColourModel(models.Model):
    COLOR=(
       ('red','red'),
        ('blue','blue'),
        ('green','green'),
        ('black','black')
    )

    product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    colour=models.CharField(max_length=10,choices=COLOR)

    def __str__(self):
        return self.colour 

class productImageModel(models.Model):
    product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='image')

    def __str__(self):
        return self.image 



