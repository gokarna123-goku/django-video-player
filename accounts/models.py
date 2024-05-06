from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import UserManager



class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    email and password are required. Other fields are optional.
    """

    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    phone = models.CharField(null=True, blank=True, unique=True, max_length =10)
    profile_picture = models.ImageField(upload_to='userprofile', blank=True, null=True)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [ ]


    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_profile_pic(self):
        if not self.profile_picture:
            return "https://sp-ao.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_232,h_232/https://loanscanada.ca/wp-content/uploads/2018/04/Is-Bankruptcy-The-Answer-to-Student-Loan-Debt.png"
        else:
            return self.profile_picture.url
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from PIL import Image
        if self.profile_picture:
            img = Image.open(self.profile_picture.path)
            reduced_resolution = (200, 200)
            img.thumbnail(reduced_resolution)
            img.save(self.profile_picture.path)
        


