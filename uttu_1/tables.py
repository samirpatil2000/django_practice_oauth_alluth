import django_tables2 as tables

from .models import MyModel

class MyTable(tables.Table):

    class Meta:

        model = MyModel
        template_name = "django_tables2/bootstrap4.html"
        fields = ( "name", "email","ediNumber","status","fileField" )


#----------------------------> for sorting just click on the the fields < -----------------------------------

