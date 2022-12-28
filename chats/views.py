
from django.views.generic import TemplateView
# Create your views here.


class ChatView(TemplateView):
    template_name = "chats/chat.html"
