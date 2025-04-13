from django.db import models



class Category(models.Model):
    name =models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Categories"
    
    
    def __str__(self):
       return self.name
   
    

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    author=models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)    
    
    def __str__(self):
        return f"{self.author} - {self.post.content}"
    