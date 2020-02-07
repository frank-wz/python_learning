from django.shortcuts import render,redirect,HttpResponse
from app01.models import UserInfo, Publisher,Book
from django.http import JsonResponse


# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        # 去数据库中以email和pwd去检索
        ret = UserInfo.objects.filter(email=email,password=pwd)
        if ret:
            # 登陆成功
            return redirect('https://www.luffycity.com')
        else:
            # 登陆失败
            return render(request,'login.html',{'error_msg':'用户名或密码错误'})
    return render(request,'login.html')

# 出版社列表页面的处理函数
def publisher_list(request):
    # 去数据库中把所有的出版社数据取出来
    ret = Publisher.objects.all()
    # print(ret)
    # print(ret[0],type(ret[0]))
    # print(ret[0].id)
    # print(ret[0].name)
    # 在页面上把出版社数据展示出来
    # return HttpResponse('ok')
    return render(request,'publisher_list.html', {'publisher_list':ret})

# 添加出版社
def add_publisher(request):
    #判断请求的方法是不是POST
    if request.method == 'POST' :
        # 表示用户填写了信息，提交过来
        # 1 获取用户填写的信息
        new_name = request.POST.get('publisher_name')
        # 添加到数据库中
        Publisher.objects.create(name=new_name)
        # 给用户返回提示
        # return HttpResponse('添加成功')
        return redirect('/publisher_list/')
    # 返回一个页面，有form表单让用户填写新出版社信息
    return render(request,'add_publisher.html')

# 删除出版社
def delete_publisher(request):
    # 获取要删除的出版社id   --> 获取URL中的id参数
    # print(request.GET) #<QueryDict: {'id': ['6']}>
    delete_id = request.GET.get('id')
    # 去数据库根据id删除对应的数据
    Publisher.objects.filter(id=delete_id).delete()
    # 告诉用户删除成功
    # return HttpResponse('要删除啦！')
    return redirect('/publisher_list/')

# 编辑出版社
def edit_publisher(request):
    # # 获取要编辑的出版社ID
    # edit_id = request.GET.get('id')
    # # 2 根据id去数据库那到要编辑的出版社数据
    # edit_obj = Publisher.objects.get(id=edit_id)

    # 如果是POST请求
    if request.method == 'POST':
        # 表示用户修改完了出版社信息，给我提交数据了
        # 取到用户编辑之后的信息
        edit_id = request.POST.get('id')
        new_name = request.POST.get('new_name')
        # 去数据库更新一下
        Publisher.objects.filter(id=edit_id).update(name=new_name)
        # 给用户展示编辑之后的效果
        res = {'code':0,'next_url':'/publisher_list/'}
        return JsonResponse(res)


# day58  ----  ↓  -----
def book_list(request):
    #  找到数据库中所有的书籍
    data = Book.objects.all()
    print(data) # <QuerySet [<Book: Book object>, <Book: Book object>, <Book: Book object>]>
                # <QuerySet [<Book: <时间简史>>, <Book: <未来简史>>, <Book: <人类简史>>]>
    first_book_obj = data[0]
    print(first_book_obj, type(first_book_obj)) # 拿到第一本书，是一个书籍对象
    print(first_book_obj.publisher,type(first_book_obj.publisher))  # --> 面向对象之组合
    print(first_book_obj.publisher_id)    # 和书关联的出版社的id
    #获取和书关联的出版社的名称
    print(first_book_obj.publisher.name)

    # 在页面上展示出来
    return render(request,'book_list.html',{'book_list':data})
    # return HttpResponse('查书籍')


# 删除书籍
def delete_book(request):
    # 获取要删除的书籍的id
    delete_id = request.GET.get('id')
    # 去数据库找到要删除的书籍，删除掉
    Book.objects.filter(id=delete_id).delete()
    # 跳转到
    return redirect('/book_list/')

#添加书籍
def add_book(request):
    publisher_list = Publisher.objects.all()
    if request.method == 'POST':
        # 获取书籍名称
        new_title = request.POST.get('title')
        # 获取关联的出版社的id值
        publisher_id = request.POST.get('publisher')
        # 用获取到的数据创建新的书籍
        Book.objects.create(title=new_title,publisher_id=publisher_id)
        # Book.objects.create(title=new_title,publisher=Publisher.objects.get(id=publisher_id))
        # 跳转到书籍
        return redirect('/book_list/')
    return render(request,'add_book.html',{'publisher_list':publisher_list})


# 编辑书籍
def edit_book(request):
    # 先获取要编辑的书籍的id
    edit_book_id = request.GET.get('id')
    # 获取要编辑的书籍对象
    edit_book_obj = Book.objects.get(id=edit_book_id)
    #如果是post请求
    if request.method == 'POST':
        new_title = request.POST.get('title')
        # 获取修改之后的出版社
        new_publisher_id = request.POST.get('publisher')
        # 修改数据库中对应的数据
        edit_book_obj.title = new_title
        edit_book_obj.publisher_id = new_publisher_id
        edit_book_obj.save()
        # 改完之后跳转会书籍列表页面
        return redirect('/book_list/')

    # 难道所有的出版社数据，用来展示页面上的select标签
    all_publisher = Publisher.objects.all()
    
    return render(request,'edit_book.html',{'book':edit_book_obj,'publisher_list':all_publisher})
