from django.views.generic import TemplateView
from .models import Homepage
from content.models import News_post
# Create your views here.


class HomepageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context

        context = super(HomepageView, self).get_context_data(**kwargs)

        context['news_list'] = News_post.objects.all()

        return context
