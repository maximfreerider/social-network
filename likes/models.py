from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Like(models.Model):
    """Модель Like основана на встроенном в Django фреймворке ContentType. Фреймворк ContentType предоставляет отношение
    GenericForeignKey, которое создает обобщенные (generic) отношения между моделями. Для сравнения, обычный ForeignKey
    создает отношение только с какой-то конкретной моделью.
    Процесс создания GenericForeignKey:
     1) Создаем поле с внешним ключом (ForeignKey) на модель ContentType.
     2) Создаем поле для хранения первичного ключа (primary key) объекта, который вы хотите связать с моделью Like.
     В этом поле мы будем хранить ID экземпляра модели Tweet. Но хранить можно ID любой модели (моделей),
     поэтому отношение и называется обобщенным.
     3) Создаем поле типа GenericForeignKey, передав в нее имена полей, которые мы создали в предыдущих двух пунктах."""
    user = models.ForeignKey(User,
                             related_name='likes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

