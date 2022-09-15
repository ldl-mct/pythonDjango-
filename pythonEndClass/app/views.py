from django.shortcuts import render
from .models import enteriModel
from django.http import  HttpResponse#引入http协议，响应函数

def zhuce(request):
    if request.method == "POST":
        xing = request.POST["xingming"]
        xue = request.POST["xuehao"]
        dian = request.POST["dianhua"]
        mi = request.POST["mima"]
        gen = request.POST["gender"]
        jian = request.POST["jianjie"]
        src = request.FILES["src"]
        m = enteriModel(xingming=xing,xuehao=xue,dianhua=dian,mima=mi,gender=gen,jianjie=jian,src=src)
        m.save()
        return HttpResponse("<script type ='text/javascript'>alert('注册成功');window.location.href='denglu'</script>")
    return render(request,"page.html")

def denglu(request):
    if request.method == "POST":
        enterXuehao = request.POST["xuehao"]
        enterMima = request.POST["mima"]
        orNo = enteriModel.objects.filter(xuehao=enterXuehao)
        if orNo:
            user = orNo[0]
            if user.mima == enterMima:
                return HttpResponse("<script type='text/javascript'>alert('登陆成功');window.location.href='private';</script>")
            else:
                return HttpResponse("<script type='text/javascript'>alert('密码有误');window.history.back();</script>")
        else:
            return HttpResponse("<script type='text/javascript'>alert('用户不存在，请注册');window.location.href='zhuce';</script>")

    return render(request,"home.html")

def private(request):
    allData = enteriModel.objects.all()
    return render(request,"newsList.html",{"allData":allData})
