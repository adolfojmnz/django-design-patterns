from django.views import View
from django.http import JsonResponse

from .models import Post


class PublicPostJSONView(View):

    def get(self, request, *args, **kargs):
        data = Post.objects.public_posts().values(
            "posted_by_id", "message")[:5]
        return JsonResponse(list(data), safe=False)
