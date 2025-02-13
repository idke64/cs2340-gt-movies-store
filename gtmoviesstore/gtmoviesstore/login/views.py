from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "login/index.html"  # Make sure this template exists