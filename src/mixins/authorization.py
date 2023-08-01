from django.core.exceptions import PermissionDenied


class LoginRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CheckOwnerMixin:

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj
