from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# シンプルなビュー関数を定義
# リクエストオブジェクトを受け取り、HttpResponseオブジェクトを返す
def index(request):
    # HTTPレスポンスとして文字列を返す
    return HttpResponse("Hello, World!")

# HTMLテンプレートを返すビューの例 (後で詳しく扱います)
# def index(request):
#     # templates/myapp/index.html をレンダリングして返す
#     return render(request, 'myapp/index.html', {})

