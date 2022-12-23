from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where cpf is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, cpf, password, **extra_fields):
        """
        Create and save a User with the given cpf and password.
        """
        if not cpf:
            raise ValueError('The CPF must be set')
        user = self.model(cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, cpf, password, **extra_fields):
        """
        Create and save a SuperUser with the given cpf and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(cpf, password, **extra_fields)
