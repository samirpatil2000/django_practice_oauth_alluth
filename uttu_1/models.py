from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


from django.utils import timezone
from django.contrib.auth.models import User
# from django.urls import reverse
# #from geography.models import ZipCode
# # Create your models here.
# class Topping(models.Model):
#     name=models.TextField(default="Topping",max_length=20)
#
#     def __str__(self):
#         return self.name
#
# class Pizza(models.Model):
#     name_of_pizza=models.TextField(default="Pizza")
#     topping=models.ManyToManyField(Topping)
#
#     def __str__(self):
#         return self.name_of_pizza
#
#
#
#
#
#
# class Person(models.Model):
#     name = models.CharField(max_length=128)
#
#     def __str__(self):
#         return self.name
#
# class Group(models.Model):
#    name = models.CharField(max_length=128)
#    members = models.ManyToManyField(Person, through='Membership')
#
#    def __str__(self):
#        return self.name
#
# class Membership(models.Model):
#    name = models.CharField(max_length=128)
#    person = models.ForeignKey(Person, on_delete=models.CASCADE)
#    group = models.ForeignKey(Group, on_delete=models.CASCADE)
#    date_joined = models.DateField()
#   # inviter = models.ForeignKey(Person,on_delete=models.CASCADE, related_name="membership_invites")
#    invite_reason = models.CharField(max_length=64)
#
#    def __str__(self):
#        return self.name
#
#
#
#
# class Ox(models.Model):
#     horn_length=models.IntegerField()
#
#     class Meta:
#         ordering=["horn_length"]
#         verbose_name_plural="oxen"
#
#
# class Person_1(models.Model):
#     first_name=models.CharField(max_length=50)
#     last_name=models.CharField(max_length=50)
#     birth_date=models.DateField()
#
#     def baby_boomer_status(self):
#         "Returns the person's baby boomer status"
#         import datetime
#         if self.birth_date<datetime.date(2000,10,10):
#             return "PRE-BOOMER"
#         elif self.birth_date<datetime.date(2005,10,10):
#             return "Baby boomer"
#         else:
#             return "Post-boomer"
#     @property
#     def full_name(self):
#         "Returns The full name of person"
#         return '%s %s' %(self.first_name,self.last_name)
#
#     def __str__(self):
#         return '%s %s' %(self.first_name,self.last_name)
#
#
#
#
#
# class Blog(models.Model):
#     name=models.CharField(max_length=100)
#     tagline=models.TextField()
#
#
#     def save(self,*args,**kwargs):
#         if self.name=="Samirpatil":
#             return "samirpatil can not have its own blog"
#         else:
#             super().save(*args,**kwargs)
#
#
# ##
# #
# # class CommonInfo(models.Model):
# #     name=models.CharField(max_length=100)
# #     age=models.PositiveIntegerField(default=0)
# #
# #     class Meta:
# #         abstract=True   #   do not register with the admin
# #
# #     # def __str__(self):1
# #     #     return self.name
# #
# #
# # class Student(CommonInfo):
# #     home_group=models.CharField(max_length=5)
# #
# #     def __str__(self):
# #         return self.name
# #
# #
# class Type(models.Model):
#     type=models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.type
#
# class Post(models.Model):
#
#     title = models.CharField(max_length=50)
#     content = models.TextField(max_length=4000)
#     date_posted = models.DateTimeField(default=timezone.now)
#     type=models.ForeignKey(Type,on_delete=models.CASCADE)
#
#
#     # blog_image_1=models.ImageField(upload_to='blog_pics')
#     author = models.ForeignKey(User,on_delete=models.CASCADE)  # this for if we delete the user the post will also deleted and not vice versa
#     def __str__(self):
#         return self.title


class Area(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    #
    # def __unicode__(self):
    #     return self.name
class Place(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    area = models.ManyToManyField(Area,related_name='area')


class Follow(models.Model):
    follower=models.ForeignKey(User,related_name='following' ,on_delete=models.CASCADE)
    following=models.ForeignKey(User,related_name='followers',on_delete=models.CASCADE)

    class Meta:
        unique_together=('follower','following')

    def __unicode__(self):
        return u'%s follows %s' % (self.follower,self.following)

    def __str__(self):
        return( "{} follows {}".format(self.follower,self.following))



#
# class Song(models.Model):
#     album = models.ForeignKey(Album, on_delete=models.CASCADE)
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#     song_title = models.CharField(max_length=200, null=False, blank=False)
#     audio_file = models.FileField(default='', upload_to='song')
#     is_favorite = models.BooleanField(default=False)
#     genre = models.CharField(max_length=250)
#     song_logo = models.CharField(max_length=1000, null=True)
#
#
#     @property
#     def filename(self):
#         return os.path.basename(self.audio_file.path)
#     def __str__(self):
#         return self.song_title

class Song(models.Model):
    name=models.TextField(default="mySong",max_length=200)
    def __str__(self):
        return self.name


class Playlist(models.Model):
    name=models.CharField(default="myPlaylist",max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
    def __str__(self):
        return self.name


#
#
#
# class Post(models.Model):
#     title=models.CharField(max_length=50)
#     sub_title=models.CharField(default="This is the subtitle of the post ",max_length=150)
#     content=models.TextField(max_length=4000)
#     date_posted=models.DateTimeField(default=timezone.now)
#     blog_image_1=models.ImageField(Blank=True,Null=True,upload_to='media')
#     blog_image_2=models.ImageField(Blank=True,Null=True,upload_to='media')
#     blog_image_3=models.ImageField(default='default.jpg',upload_to='media')
#     author =models.ForeignKey(User,on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
#

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    # address = models.CharField(max_length=50)
    # city = models.CharField(max_length=60)
    # state_province = models.CharField(max_length=30)
    # country = models.CharField(max_length=50)
    # website = models.URLField()

    class Meta:
       ordering = ["-name"]

    def __str__(self):
        return self.name


class Author(models.Model):
    # salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    last_accessed = models.DateTimeField()
    # email = models.EmailField()
    # headshot = models.ImageField(upload_to='author_headshots')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

class Apk_file(models.Model):
    file=models.FileField(upload_to='apk_files', blank=True)
    playStore_link=models.URLField(blank=True)
    title=models.CharField(max_length=40)

    def __str__(self):
        return self.title




# for table testing
class MyModel(models.Model):
    name=models.CharField(default="TableTesting",max_length=50,verbose_name="verboseName")
    email=models.EmailField(null=True)
    ediNumber=models.IntegerField(default=0)
    status=models.CharField(default="No",max_length=60)
    fileField=models.FileField(null=True)

    def __str__(self):
        return self.name


# followers following model TESTING..../...\
#

class Followers(models.Model):

    follower=models.ForeignKey(User,related_name='followinges',on_delete=models.DO_NOTHING)
    following=models.ForeignKey(User,related_name='followeres',on_delete=models.DO_NOTHING)

    class Meta:
        unique_together=('follower','following')

    def __unicode__(self):
        return u'%s follows %s' %(self.follower,self.following)

    def clean(self):
        if self.follower==self.following:
            raise ValidationError("One Cannot follow themselves")

    def __str__(self):
        return u'%s follows %s' %(self.follower,self.following)

















