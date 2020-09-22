from django.contrib.sessions.models import Session
from django.shortcuts import render
from django.contrib.auth import user_logged_in
from django.dispatch.dispatcher import receiver
# Create your views here.
from social_app.models import UserSession


def index(request):

    return render(request,'social_app/alluth.html')


#
@receiver(user_logged_in)
def remove_other_sessions(sender, user, request, **kwargs):
    # remove other sessions
    Session.objects.filter(usersession__user=user).delete()

    # save current session
    request.session.save()

    # create a link from the user to the current session (for later removal)
    UserSession.objects.get_or_create(
        user=user,
        session=Session.objects.get(pk=request.session.session_key)
    )


