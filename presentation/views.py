from django.shortcuts import render, redirect
from django.http import JsonResponse
import markdown
import re
import os
from django.conf import settings
import yfinance as yf

def home(request):
    return render(request, 'home.html')

def do_action(request):
    if request.method == "POST":
        return redirect('stocks')
    else:
        return redirect('home')

def stocks(request):
    tickers = {
        'Tesla': 'TSLA',
        'Volkswagen': 'VOW3.DE',
        'Netflix': 'NFLX',
        'Disney': 'DIS',
    }
    stock_data = {}
    for name, symbol in tickers.items():
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period='6mo')
        stock_data[name] = {
            'dates': hist.index.strftime('%Y-%m-%d').tolist(),
            'prices': hist['Close'].tolist(),
        }
    return render(request, 'stocks.html', {'stock_data': stock_data})

def readme(request):
    readme_path = os.path.join(settings.BASE_DIR, 'README.md')
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    html_content = markdown.markdown(content, extensions=['fenced_code'])
    html_content = re.sub(
        r'<pre><code class="language-mermaid">(.*?)</code></pre>',
        r'<div class="mermaid">\1</div>',
        html_content,
        flags=re.DOTALL
    )
    return render(request, 'readme.html', {'readme_html': html_content})

