from blog.models import Post
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        title=['python','Rasberry','arduino','money','psychology','new things','bad things']
        name=['santhosh','kishore','gopi','varun','jeeva','akshaay','retna kumar']
        content=['this is very import news about the things all around','hi','hello','bye','sorry','good bye','good afternoon']

        for t,n,c in zip(title,name,content):
            Post.objects.create(title=t,name=n,content=c)
