from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib import messages
import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    db=0
)

@receiver(user_logged_in)
def login_success(sender, request, user, **kwargs):
    user_ip = request.META['REMOTE_ADDR']
    user = request.user.username
    user_last_ip = r.get(user)
    if user_last_ip is None:
        r.set(user, user_ip)
    elif user_last_ip.decode() != user_ip:
        print(f"Ip: {user_ip} - Ip_Precedente {user_last_ip}")
        r.set(user, user_ip)
        messages.warning(request,f'your ip has changed: current_ip {user_ip} | last_ip {user_last_ip}')



