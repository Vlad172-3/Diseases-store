from django.db import models


class Tag(models.Model):
    name = models.CharField(verbose_name='Тэг', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class BlogCategory(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория блога'
        verbose_name_plural = 'Категории блога'


class Article(models.Model):
    category = models.ForeignKey(to=BlogCategory,
                                 verbose_name='Категория',
                                 on_delete=models.SET_NULL,
                                 null=True
                                 )
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text_preview = models.TextField(verbose_name='Текст превью')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    publications = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
