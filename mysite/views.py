from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request, num=None):
    # 无论是否有num参数，都返回相同的HTML页面
    # 页面内容的具体展示由前端JavaScript通过History API处理
    return render(request, "mysite/index.html")

# The texts are much longer in reality, but have
# been shortened here to save space
texts = ["Text 1", "Text 2", "Text 3"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")