from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    parent = models.ForeignKey('self',
            on_delete=models.CASCADE,
            blank=True,
            null=True,
            related_name='children')

    def parents(self):
        obj = self
        res = []
        while obj.parent != None:
            obj = obj.parent
            res.append(obj)
        return res

    def siblings(self):
        return Category.objects.filter(parent=self.parent).exclude(id=self.id)