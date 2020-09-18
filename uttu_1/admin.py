from django.contrib import admin
#from.models import Topping,Pizza,Person,Group,Membership,Ox,Person_1,Blog ,Type,Post#,Student,CommonInfo
from.models import Area,Place,Follow,Song,Playlist,Publisher,Author,Book,Apk_file,MyModel,Followers
# # Register your models here.


# admin.site.register(Topping)
# admin.site.register(Pizza)
#
# # THis is another
# admin.site.register(Person)
# admin.site.register(Group)
# admin.site.register(Membership)
#
# #
# admin.site.register(Ox)
#
# #
# admin.site.register(Person_1)
# #
# admin.site.register(Blog)
# #
#
#
# #admin.site.register(CommonInfo)  #this is abstract class so you can't register with the admin
# # #admin.site.register(Student)
#
# admin.site.register(Type)
# admin.site.register(Post)
#
#
# admin.site.register(Place)
# admin.site.register(Area)
#
# admin.site.register(Follow)
#
#
# admin.site.register(Song)
# admin.site.register(Playlist)


admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Author)


admin.site.register(Apk_file)

# tables
admin.site.register(MyModel)

#followers Following system

admin.site.register(Followers)