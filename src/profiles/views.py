from django.views.generic.base import TemplateView


class ProfileListView(TemplateView):
    template_name = "profiles/index.html"

