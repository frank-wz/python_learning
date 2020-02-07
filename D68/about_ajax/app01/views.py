from django.shortcuts import render,redirect,HttpResponse
from django import views
from app01.models import Publisher,UserInfo
from django.http import JsonResponse
from functools import wraps

# Create your views here.

# 使用装饰器做Cookie版登录验证
def check_login(func):
    @wraps(func)
    def inner(request,*args,**kwargs):
        # 先做Cookie验证
        # cookie_value = request.COOKIES.get('hl')
        cookie_value = request.get_signed_cookie(key='hl',salt='qsjhjsnb!',default=None)
        if cookie_value == 'dsb':
            rep = func(request,*args,**kwargs)
            return rep
        else:
            return_url = request.path_info  # /home/
            return redirect('/login/?returnUrl={}'.format(return_url))
    return inner

# 登录
class LoginView(views.View):

    def get(self,request):
        rep = render(request,'login.html')
        return rep

    def post(self,request):
        name = request.POST.get('name')
        pwd = request.POST.get('password')
        remember_7 = request.POST.get('remember',None)
        is_ok = UserInfo.objects.filter(name=name,password=pwd)
        if is_ok:
            # 登陆成功
            # 求return_url
            print(request.get_full_path())
            return_url = request.GET.get('returnUrl','/index/')
            print(return_url)
            print('-'*120)
            rep = redirect(return_url) # 拿到要返回的响应对象
            # 如果勾选了7天免登录
            if remember_7:
                rep.set_signed_cookie('hl','dsb',salt='qsjhjsnb!', max_age=7*24*60*60)  # 告诉浏览器在自己本地保存一个键值对hl:dsb
            else:
                rep.set_signed_cookie('hl','dsb',salt='qsjhjsnb!')
            # 否则就是用默认的浏览器关闭就失效
            return rep
        else:
            return render(request,'login.html', {'error_msg':'用户名或密码错误！'})

# 首页
@check_login
def index(request):
    # cookie_value = request.COOKIES.get('hl')
    # if cookie_value == 'dsb':
        data = Publisher.objects.all()
        return render(request,'index.html',{'publisher_list':data})
    # else:
    #     # 没有登陆过，默认跳转到登陆页面
    #     return redirect('/login/')

# 删除出版社
def delete_publisher(request):
    # 先取到删除的id
    delete_id = request.POST.get('id')
    res = {'code':0}
    try:
        Publisher.objects.filter(id=delete_id).delete()
    except Exception as e:
        res['code'] = 1
        res['err_msg'] = str(e)
    return JsonResponse(res)

# home页面
@check_login
def home(request):
    return HttpResponse('home!')

# 注销
def logout(request):
    rep = redirect('/login/')
    rep.delete_cookie('hl')
    return rep