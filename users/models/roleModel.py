
from django.db import models
from django.utils.text import slugify


class Role(models.Model):
    name = models.CharField(verbose_name="Nombre del rol", null=False, max_length=50,
                            help_text="Solo ADMIN y CLiente")
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        db_table = "roles"
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            cont = 1

            while Role.objects.filter(slug=slug.exists()):
                slug = f"{slug}-{cont}"
                cont += 1

        super().save(*args, **kwargs)