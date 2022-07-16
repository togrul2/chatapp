from user.models import EnhancedUser


def friends_list(request):
    friends = []
    if request.user.is_authenticated:
        friends = EnhancedUser.objects.get(pk=request.user.pk).get_friends_list()

    return {'friends': friends}
