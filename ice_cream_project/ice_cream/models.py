from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель, содержащая общие поля"""

    title = models.CharField(max_length=256)
    description = models.TextField()

    class Meta:
        abstract = True


class Category(PublishedModel):
    """Категория мороженного"""

    slug = models.SlugField(max_length=64, unique=True)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title


class Wrapper(PublishedModel):
    """Обёртка мороженного"""

    slug = models.SlugField(max_length=64, unique=True)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    """Мороженное"""

    price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name="ice_cream",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="ice_cream",
    )

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title
