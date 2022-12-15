from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):


    def create_user(self,username:str,first_name:str,last_name:str,email:str,password:str=None,is_staff=False,is_superuser=False) -> "User":
        if not (username , first_name , last_name , email): 
            raise ValueError("you mast have username , email , first name, last name and password")

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return User

    def create_superuser(self, first_name , last_name , email , username , password) -> "User":
        user = self.create_user(
                first_name=first_name , 
                last_name=last_name , 
                email=email , 
                username=username , 
                password=password ,
                is_staff=True , 
                is_superuser=True
            )

        return user


class User(AbstractUser):
    first_name = models.CharField(verbose_name="First Name" , max_length=42)
    last_name = models.CharField(verbose_name="Last Name" , max_length=42)
    email = models.EmailField(verbose_name="Email" , unique=True , max_length=255)
    username = models.CharField(verbose_name="Username" , unique=True , max_length=22)
    password = models.CharField(max_length=32)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username","first_name" , "last_name"]
    
