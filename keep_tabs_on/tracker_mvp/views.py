from django.shortcuts import render


def main(request):
    return render(request, template_name="tracker_mvp/index.html")
