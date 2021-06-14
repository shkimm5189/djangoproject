from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)
    rank = models.CharField(max_length=10)
    update_at = models.DateTimeField(auto_now=True)

    # restapi를 적용하지않고 바로 view와 연동할떄
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profiles.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_porfile(sender, instance, **kwargs):
    #     instance.profiles.save()

    class Meta:
        db_table = "cccr_user"


# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# #
# # class UserHelper(BaseUserManager):
# #     def create_user(self, email, nickname, name, password=None):
# #         if not email:
# #             raise ValueError("이메일 넣어라 뒤지기 싫으면")
# #         if not nickname:
# #             raise ValueError("이메일 넣어라 뒤지기 싫으면")
# #         if not nickname:
# #             raise ValueError("이메일 넣어라 뒤지기 싫으면")
# #
# #         user = self.model(
# #             email = self.normalize_email(email),
# #             nickname = nickname,
# #             name = name
# #         )
# #         user.set_password(password)
# #         user.save(using=self.db)
# #         return user
# #
# #
# #
# # class User(AbstractBaseUser):
# #     id = models.AutoField(primary_key=True)
# #     email = models.EmailField(max_length=50,null=False)
# #     nickname = models.CharField(max_length=30,null=False)
# #     name = models.CharField(max_length=30, null=False)
# #
# #     is_active = models.BooleanField(default=True)
# #     is_admin = models.BooleanField(default=False)
# #
# #     object = UserHelper()
# #
# #     USERNAME_FIELD = 'nickname'
# #     REQUIRED_FIELDS = ['email', 'name']
# #
# #     def __str__(self):
# #         return self.nickname