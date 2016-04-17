from django.contrib.auth.models import User

from artshop.shop.models import ShopUser


class ArtShopAuthBackend(object):
    def authenticate(self, username=None, password=None):
        shop_user = ShopUser.objects.filter(username__exact=username, password__exact=password).first()
        if shop_user is None:
            return None
        user = User.objects.filter(id=shop_user.id).first()
        if user is None:
            user = User(id=shop_user.id, username=str(shop_user.id) + '_' + shop_user.username)
            user.save()
        return user

    def get_user(self, user_id):
        return User.objects.get(id=user_id)
