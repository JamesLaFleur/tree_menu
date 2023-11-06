from django.db import models


class Menu(models.Model): 
    title = models.CharField(max_length=255, unique=True, verbose_name='menu_title')
    slug = models.CharField(max_length=255, verbose_name='menu_slug')


    def __str__(self) -> str:
        return self.title
    

class MenuItem(models.Model):
    """
    Пункт меню
    """
    title = models.CharField(max_length=255, verbose_name='menu_item_title')
    slug = models.CharField(max_length=255, verbose_name='menu_item_slug')
    menu = models.ForeignKey(Menu, blank=True, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='sub_items', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    