from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from .models import Like

# User = get_user_model()


def add_like(obj, user):
    """лайкаю obj"""
    obj_type = ContentType.objects.get_for_model(obj)
    like, is_created = Like.objects.get_or_create(
        content_type=obj_type,
        object_id=obj.id,
        user=user
    )


def remove_like(obj, user):
    obj_type = ContentType.objects.get_for_model(obj)
    Like.objects.filter(
        content_type=obj_type,
        object_id=obj.id,
        user=user
    ).delete()


def is_fan(obj, user) -> bool:
    """проверяю лайкнул ли пользователь(user) -> obj"""
    if not user.is_authenticated:
        return False
    obj_type = ContentType.objects.get_for_model(obj)
    likes = Like.objects.filter(
        content_type=obj_type,
        object_id=obj.id,
        user=user
    )
    return likes.exists()


def get_fans(obj):
    """Поучаем все пользователей которые лайкнули 'obj' """
    obj_type = ContentType.objects.get_for_model(obj)
    return User.objects.filter(
        likes__content_type=obj_type,
        likes__object_id=obj.id
    )
