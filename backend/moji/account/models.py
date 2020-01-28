from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.signals import post_save
from django.urls import reverse
import stripe
#from content.models import Feed
from django.contrib.auth.validators import UnicodeUsernameValidator
#from product.models import Product
from django.conf import settings
import uuid
from django.utils.translation import gettext_lazy as _
#NEW MODELS TO BE MADE
#POINTS
#BANK ACCOUNT
#add uid to profile
#product
#blocked users
"""
 @classmethod
    def normalize_username(cls, username):
        username = str(username)
        if username.isalnum():
            pass
        if len(username) < 2:
            raise ValueError('username needs to be more than 3 chars')


        return username.lower()
"""


class BannerManager(models.Manager):
    def get_queryset(self):
        return super(BannerManager, self).get_queryset().select_related('profile').values('username', 'uuid', bio=Lower('profile__bio'))
class MyUserManager(BaseUserManager):

    def create(self, email, username, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have an username address')

        user = self.model(
            email=self.normalize_email(email),
            username =User.normalize_username(username),
            date_of_birth=date_of_birth

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def exists(self):
        if self._result_cache is None:
            return self.query.has_results(using=self.db)
        return bool(self._result_cache)

    def create_superuser(self, email, username, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create(
            email,
            username,
            password=password,
            date_of_birth=date_of_birth,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True,editable=False)
    email = models.EmailField(unique=True)
    #username = models.CharField(max_length=40, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    date_joined = models.DateTimeField(auto_now_add=True)
    #password = models.CharField(_('password'), validators=settings.AUTH_PASSWORD_VALIDATORS,max_length=128)
    username = models.CharField(
        _('username'),
        max_length=60,
        unique=True,
        help_text=_('Required. 60 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    banner = BannerManager
    #_password = None

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','date_of_birth']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_short_name():
        return self.username

    def get_full_name():
        return f"active: {self.is_active} username: {self.username} uuid: {self.uuid}"

    def get_username():
        return self.username

    def __str__(self):
        return self.email + ' ' + self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class LastSeen(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ip_of_seen = models.GenericIPAddressField(editable=False, default=None)
    time_and_date = models.DateTimeField(auto_now_add=True, editable=False)
    #user_agent

class AccountRequest(models.Model):
    #user.requested.all() -> gives all the Requested invites and vise-versa
    userTo = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='af_requested')
    userFrom = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='af_requester')
    accept = models.BooleanField(default=False)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.userFrom.username

    def get_absolute_url(self):
        return reverse('account:detailAcceptance', kwargs={'name':self.userTo.username})

    def save(self, *args, **kwargs):
        try:
            a  = AccountRequest.objects.filter(userTo=self.userTo).get(userFrom=self.userFrom)
        except AccountRequest.DoesNotExist:
            if self.userFrom.profile in self.userTo.followed_by.all():
                return None
            elif self.accept == True: #or self.userTo in self.userFrom.profile.following: #and user saving it is the userTo:
                self.userFrom.profile.following.add(self.userTo)
                self.delete()
                return None
            else:
                super(AccountRequest, self).save(*args, **kwargs)
        return None



class Profile(models.Model):
    # user.profile.following -- users i follow
    # user.followed_by -- users that follow me -- reverse relationship
    #if block end subscription and add a exclude blocked_by.all() when user searches
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')
    blocked = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='blocked_by')
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    bio = models.CharField(max_length=255, null=True, blank=True)
    link1 = models.URLField(null=True,  blank=True)
    link2 = models.URLField(null=True,  blank=True)
    location = models.CharField(max_length=150, null=True,  blank=True)
    pic = models.FileField(null=True,  blank=True)
    banner = models.FileField(null=True, blank=True)
    strikes = models.IntegerField(default=0,  blank=True)
    suspended = models.BooleanField(default=False)
    private = models.BooleanField(default=True)
    celeb = models.BooleanField(default=False)
    active_notif = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followers_to_notif')
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    tier = models.PositiveIntegerField(default=1)
    content_requires_18 = models.BooleanField(default=False)
    #genre = models.CharField(max_length=25, choices=Genres)
    percentage = models.PositiveIntegerField(default=25)

    def __str__(self):
        return self.user.username



def createUserInfo(sender, **kwargs):
    if kwargs['created']:
        if kwargs['instance'].is_admin == False:
            profile = Profile.objects.create(user=kwargs['instance'])
            kwargs['instance'].profile.following.add(kwargs['instance'])


post_save.connect(createUserInfo, sender=User)

class AccountReport(models.Model):
    VIO = (())
    #user = models.ForeignKey(settings.AUTH_USER_MODEL)
    brief = models.TextField()
    violation = models.CharField(choices=VIO, max_length=25)
