import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class User(BaseModel):
    name = models.CharField(max_length=80)
    email = models.EmailField(verbose_name="Email", unique=True, max_length=80)

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super(User, self).save(*args, **kwargs)
        return self

    class Meta:
        db_table = 'users'
        ordering = ['-created_at']


class Contact(BaseModel):
    name = models.CharField(verbose_name="Name", max_length=80)
    first_surname = models.CharField(verbose_name="First Surname", max_length=80)
    second_surname = models.CharField(verbose_name="Second Surname", max_length=80)
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=15)
    user = models.ForeignKey(User, verbose_name="User", related_name="contacts", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.first_surname = self.first_surname.title()
        self.second_surname = self.second_surname.title()
        super(Contact, self).save(*args, **kwargs)
        return self

    class Meta:
        db_table = 'contacts'
        ordering = ['-created_at']
