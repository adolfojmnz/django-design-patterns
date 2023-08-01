from posts.models import Post


class FeedMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["feed"] = Post.objects.public_posts(self.request.user)
        return context
