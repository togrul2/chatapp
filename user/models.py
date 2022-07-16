from django.contrib.auth.models import User
from django.db.models import QuerySet, Q

from chat.models import Friendship


class EnhancedUser(User):
    class Meta:
        proxy = True

    def get_friends_list(self) -> QuerySet[User]:
        sent = User.objects.filter(friends_sent__in=self.friends_received.all())
        received = User.objects.filter(friends_received__in=self.friends_sent.all())
        return sent.union(received)
