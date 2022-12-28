from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class SplashView(TemplateView):
    template_name = "theme/splash.html"


class QueueView(TemplateView):
    template_name = "theme/queue.html"

    def get_context_data(self, **kwargs):
        return {"items": ["a", "b", "c", "d"]}
