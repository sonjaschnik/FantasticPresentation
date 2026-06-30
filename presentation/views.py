# myapp/views.py
from django.shortcuts import render, redirect
import markdown
import os
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def do_action(request):
    if request.method == "POST":
        readme_path = os.path.join(settings.BASE_DIR, 'README.md')
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        html_content = markdown.markdown(content)
        return render(request, 'readme.html', {'readme_html': html_content})
    else:
        return redirect('home')

