from django.db import models
# need to install the package below to use it. 
# from django_s3_storage.storage import S3Storage

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    image = models.ManyToManyField(Photo, on_delete=models.CASCADE, related_name='photos')
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # decided to add a likes field here with a Many to Many relationship
    likes = models.ManyToManyField(CustomUser, related_name='liked_posts', blank=True)

    def __str__(self) -> str:
        return self.caption

# if using AWS S3 to store your photos, you'll need to install the 'boto3' library, which is a Python SDK for interacting with AWS services, including S3.
# need to include from django.core.files.storage import default_storage up top to use storage= below. 

# I think this is going to need to live in a different app so it can interact with Post class. 
class Photo(models.Model):
    image = models.ImageField(storage=S3Storage(), upload_to='path_to_be_determined')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    on_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    # dont think i need a relationship to user because there is one on Post already. 

    def __str__(self) -> str:
        return super().__str__()