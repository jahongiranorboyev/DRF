import uuid
from django.db import models
from django.conf import settings



class BaseModel(models.Model):
    """
    Barcha moddellar uchun asosiy (base) model
    """

    guid = models.UUIDField(primary_key = True , default = uuid.uuid4, editable = True)
    create_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )



class BaseMeta(object):
    ordering = ('id',)