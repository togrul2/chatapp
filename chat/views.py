from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.models import User

from chat.models import Friendship, Chat
from user.models import EnhancedUser


@require_GET
@login_required
def chat_view(request, receiver_id):
    receiver = get_object_or_404(EnhancedUser, id=receiver_id)
    chat, _ = Chat.objects.get_or_create(friendship=Friendship.get_friendship(request.user, receiver))
    messages = chat.messages.all()
    context = {'receiver': receiver, 'messages': messages}
    return render(request, 'chat/chat.html', context=context)


@require_GET
@login_required(login_url='login')
def friends_view(request):
    context = {}
    return render(request, 'chat/friends.html', context=context)


@require_GET
def friend_requests(request):
    requests = Friendship.objects.filter(accepted=False, receiver=request.user)
    context = {'requests': requests}
    return render(request, 'chat/friendship-requests.html', context=context)


@require_POST
def accept_request(request, request_id):
    Friendship.objects.filter(id=request_id).update(accepted=True)
    return redirect('friend-requests')


@require_POST
def decline_request(request, request_id):
    Friendship.objects.filter(id=request_id).delete()
    return redirect('friend-requests')


@require_GET
@login_required(login_url='login')
def find_friends(request):
    context = {'users': []}

    if (query := request.GET.get('query', '')) != '':
        users = User.objects.filter(~Q(username=request.user.username) &
                                    ~Q(friends_sent__in=request.user.friends_received.all()) &
                                    ~Q(friends_received__in=request.user.friends_sent.all()) &
                                    Q(username__icontains=query) |
                                    Q(first_name__icontains=query) |
                                    Q(last_name__icontains=query) |
                                    Q(email__icontains=query))

        # Doesn't work in sqlite3
        # user = EnhancedUser.objects.get(id=request.user.id)
        #
        # users = User.objects.filter(Q(username__icontains=query) |
        #                             Q(first_name__icontains=query) |
        #                             Q(last_name__icontains=query) |
        #                             Q(email__icontains=query)).difference(user.get_friends_list())

        context['users'] = users

    return render(request, 'chat/find-friends.html', context=context)


@require_POST
def send_friendship_request(request, pk):
    receiver = get_object_or_404(User, pk=pk)
    Friendship.objects.create(sender=request.user, receiver=receiver)
    return redirect('find-friends')
