from django.http import HttpResponse

def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",  # Example rule, adjust as needed
        # Add more rules here as needed
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")