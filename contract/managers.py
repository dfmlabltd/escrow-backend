from django.db import models
from django.db.models.signals import post_save

class EntityManager(models.Manager):

    def bulk_create(self, objs, **kwargs):
        
        objs = super(models.Manager,self).bulk_create(objs,**kwargs)
        
        for obj in objs:
            
            post_save.send(obj.__class__, instance=obj, created=True)
            
        return objs