from django.urls import path
from . import views # 同じディレクトリにある views.py をインポート

# アプリケーション内のURLパターンを定義するリスト
urlpatterns = [
    # path('URLパターン', ビュー関数, name='URL名')
    # '' はアプリケーションのルートパスを示す
    path('', views.index, name='index'),
]
