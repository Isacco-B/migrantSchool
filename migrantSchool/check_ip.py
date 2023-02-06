import redis

def check_user_ip(request,args,**kwarsg):
    redis_client = redis.Redis(
        host="localhost",
        port=6379,
        db=0
        )
    ip = request.META.get('REMOTE_ADDR')
    print(ip)
    print(request.user.username)
    return ip
