import datetime
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse  # 导入HttpResponse函数，主要是对response起作用
import pymysql     #导入连接数据库
from django.views.decorators.clickjacking import xframe_options_exempt

conn=pymysql.connect(    #配置数据库连接字符
    user='root',
    password='123456',
    port=3306,
    host='127.0.0.1',
    db='diancan',            #连接的相应的数据库名称
    charset='utf8'
)

cursor=conn.cursor()       #设置与数据库相关的参数
cursor.execute('set names utf8')
cursor.execute('set autocommit=1')



@xframe_options_exempt
def foodadd(request):               #菜品表单页面
    return render(request, 'foodadd.html')     #跳转到foodadd.html页面


#用来处理post提交的表单数据   因为框架里面有frame，在框架里面跨域要加@xframe_options_exempt
@xframe_options_exempt
def foodaddpost(request):   #接收templates里foodadd.html模块提交过来数据并处理
    tbname = request.POST.get('tbname')        #前面是以post方式提交的，就用poet方式接收
    tbprice = request.POST.get('tbprice')
    tbbrief = request.POST.get('tbbrief')
    tbaddress = request.POST.get('tbaddress')

    # 图片上传开始    如果这段代码引入进来有波浪线，把鼠标放上去选中引入包

    fullname = ""
    imgurl = request.FILES.get('tbpic')  # 接收前面以files提交的图片，放到imgurl里面
    # 有上传文件的情况   将图片 yxrs2.jpg 转为 20200226144630.jpg 格式并保持为 static/uploadimg/20200226144630.jpg
    if (str(imgurl) != "None"):  # str(imgurl)将imgurl对象转为字符串格式，判断是否有文件上传的情况
        t = datetime.datetime.today()  # 获取当前时间，放到t里面
        s = datetime.datetime.strftime(t, "%Y%m%d%H%M%S")  # 将时间格式化，s变量里面就是保存的当前时间格式化后的字符串
        oldname = imgurl.name  # 获取文件的旧的名称 yxrs2.jpg
        pos = oldname.rfind('.')  # 从文件的右边开始找点
        extname = ""  # 这个变量用来保存扩展名
        if pos > 0:  # 当找到点
            extname = oldname[pos:]  # .jpg 把扩展名取出来保存在变量extname中
        fullname = s + extname  # 用当前时间格式化后的字符串与扩展名拼接  得到一个新的文件名20200226144630.jpg
        file_path = os.path.join('static/uploadimg', fullname)  # 拼接出一个完整的路径static/uploadimg\20200226144630.jpg
        file_path = file_path.replace("\\", "/")  # 把路径中的反斜杠\替换为斜杠/ static/uploadimg/20200226144630.jpg
        with open(file_path, 'wb') as f:  # 在file_path下创建一个可写文件
            for chunk in imgurl.chunks():  # chunk表示文件可能是分块上传的
                f.write(chunk)  # 分块写入到文件中
    else:  # 没有上传文件的情况
        fullname = ""
    # 图片上传结束
    #上传的图片保存在static/uploadimg里面，在这个文件上右键--show in explorer可看到上传的图片，数据库里面保存的只是文件的名称，图片保存在static里面方便拿取
    #往表里面插数据
    strsql = "insert into product (proname,proprice,probrief,proaddress,imgurl) values ('" + tbname + "'," + tbprice + ",'" + tbbrief + "','" + tbaddress + "','" + fullname + "') "
    cursor.execute(strsql)   #执行SQL语句
    msg={}
    msg['xinxi']='保存成功'
    return render(request, 'foodadd.html',msg)    #提交成功后跳转到foodadd.html页面


#允许在框架下加载菜单
@xframe_options_exempt
def foodlist(request):
    strsql = "select id,proname,proprice,imgurl,probrief from product order by id desc"
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()    #fetchone表示每次只拿取一个值
    foodlist=[]
    while row:
        #print(row)
        foodlist.append({"id": row[0], "proname": row[1], "proprice": row[2],"imgurl": row[3],"probrief": row[4]})
        row = cursor.fetchone()
    return render(request, 'foodlist.html',{'foodlist': foodlist})
                          #渲染的页面         取的名称    这里面是数据
                       #将取的数据取一个名字去渲染页面

@xframe_options_exempt
def foodedit(request):
    id = request.GET.get("id")    #这个id是通过get方式提交的，从foodlist获取要修改的id
    strsql1 = "select id,proname,proprice,imgurl,probrief,proaddress  from product where id="+id   #从数据库获取相关信息
    cursor.execute(strsql1)
    row = cursor.fetchone()    #取出这条信息
    view={"id": row[0], "proname": row[1], "proprice": row[2],"imgurl": row[3],"probrief": row[4],"proaddress": row[5]}
    return render(request, 'foodedit.html',{'foodview': view})    #将取出的数据放到foodedit.html页面
                         # 渲染的页面         取的名称    这里面是数据


@xframe_options_exempt
def foodeditpost(request):
    #接收参数
    proid = request.POST.get("proid")    #获取要修改项的id
    oldimgurl = request.POST.get("oldimgurl")   #获取旧的图片路径，以便若图片没有修改可继续使用这个路径

    tbname = request.POST.get("tbname")
    tbprice = request.POST.get("tbprice")
    tbbrief = request.POST.get("tbbrief")
    tbcontents = request.POST.get("tbcontents")

    imgurl = request.FILES.get('tbpic')

    fullname=""
    if(str(imgurl)!="None"):     #若图片被修改
        t = datetime.datetime.today()
        s = datetime.datetime.strftime(t, "%Y%m%d%H%M%S")
        oldname=imgurl.name
        pos = oldname.rfind('.')
        extname=""
        if pos > 0:
            extname= oldname[pos:]
        fullname=s+extname
        file_path = os.path.join('static/uploadimg', fullname)
        file_path=file_path.replace("\\","/")
        print(file_path)
        with open(file_path, 'wb') as f:
            for chunk in imgurl.chunks():
                f.write(chunk)
    else:
        fullname=oldimgurl     #图片没有被修改就要原来的图片路径

    sqlstr = "update product set proname='"+tbname+"',proprice="+tbprice+",probrief='"+tbbrief+"',proaddress='"+tbcontents+"',imgurl='"+fullname+"' where id="+proid
    cursor.execute(sqlstr)
    conn.commit()
    view = {"id": proid, "proname": tbname, "proprice": tbprice, "imgurl": fullname, "probrief": tbbrief, "proaddress": tbcontents,
            "msg":"保存成功"}
    return render(request, 'foodedit.html',{'foodview': view})


@xframe_options_exempt
def fooddelete(request):
    #删除数据
    id = request.GET.get("id")
    sqlstr1="delete from product where id="+id    #将对应的从数据库删除
    cursor.execute(sqlstr1)
    conn.commit()
                                                   #重新查询数据，渲染列表模板
    sqlstr2 = "select id,proname,proprice,imgurl,probrief from product order by id desc"
    cursor.execute(sqlstr2)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    foodlist = []
    while row:
        # print(row)
        foodlist.append({"id": row[0], "proname": row[1], "proprice": row[2], "imgurl": row[3], "probrief": row[4]})
        row = cursor.fetchone()
    return render(request, 'foodlist.html', {'foodlist': foodlist})


@xframe_options_exempt
def orderlist(request):
    strsql = "select id,orderid,sname,stel,saddress,sumprice,memberid,ctime,ptime,memo from tborderhead order by id desc "
    cursor.execute(strsql)
    conn.commit()
    list = []
    row = cursor.fetchone()
    while row:
        list.append({"id": row[0], "orderid": row[1], "sname": row[2], "stel": row[3], "saddress": row[4], "sumprice": row[5],"memberid": row[6], "ctime": row[7], "ptime": row[8], "memo": row[9]})
        row = cursor.fetchone()
    return render(request, 'orderlist.html', {'list': list})

@xframe_options_exempt
def orderdelete(request):
    #接收参数 参数就是用户订单号
    orderid = request.GET.get("orderid")
    #根据订单号删除订单抬头表和订单明细表的数据
    strsql1="delete from tborderhead where orderid="+orderid
    strsql2 = "delete from tborderitems where orderid=" + orderid
    #因为我们在数据库里面建立了外键约束，所以删除的时候必须先删除明细表，再删除抬头表里面的订单信息。
    cursor.execute(strsql2)
    cursor.execute(strsql1)

    # 查询删除后的数据，把删除后的数据重新渲染显示在列表中
    strsql = "select id,orderid,sname,stel,saddress,sumprice,memberid,ctime,ptime,memo from tborderhead order by id desc "
    cursor.execute(strsql)
    conn.commit()
    list = []
    row = cursor.fetchone()
    while row:
        list.append(
            {"id": row[0], "orderid": row[1], "sname": row[2], "stel": row[3], "saddress": row[4], "sumprice": row[5],
             "memberid": row[6], "ctime": row[7], "ptime": row[8], "memo": row[9]})
        row = cursor.fetchone()
    return render(request, 'orderlist.html', {'list': list})


@xframe_options_exempt
def orderview(request):
    #根据订单的id把订单的抬头和订单的明细全部查询出来，查询出来的结果只包含当前这个订单的信息
    orderid = request.GET.get("orderid")
    strsql1 = "select id,orderid,sname,stel,saddress,sumprice,memberid,ctime,ptime,memo from tborderhead where orderid=" + orderid
    strsql2 = "select id,orderid,proid,proname,price,procount,imgurl from tborderitems where orderid=" + orderid

    #查看订单明细信息
    cursor.execute(strsql2)
    rowitem = cursor.fetchone()
    list = []
    while rowitem:
        list.append({"id": rowitem[0], "orderid": rowitem[1], "proid": rowitem[2], "proname": rowitem[3], "price": rowitem[4],"procount": rowitem[5],"imgurl": rowitem[6]})
        rowitem = cursor.fetchone()

     #查看抬头信息
    cursor.execute(strsql1)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    head = {"id": row[0], "orderid": row[1], "sname": row[2], "stel": row[3], "saddress": row[4], "sumprice": row[5],
            "memberid": row[6], "ctime": row[7], "ptime": row[8], "memo": row[9], "items": list}
    return render(request, 'orderview.html', {'obj': head})
                            # 渲染的页面    取的名称  这里面是数据


@xframe_options_exempt
def login(request):
    return render(request, 'login.html')


@xframe_options_exempt
def loginpost(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    strsql="select id,username,truename from manage where username='"+username+"' and password='"+password+"'"
    cursor.execute(strsql)
    row = cursor.fetchone()
    context = {}
    if row:
        #如果成功 就跳转到主页面
        return redirect("/static/myadmin/default.html")
    else:
        #重新渲染登录页面
        context['msg'] = '用户名或者密码错误!'
        return render(request, 'login.html', context)


@xframe_options_exempt
def uilunbo(request):               #菜品表单页面
    return render(request, 'uilunbo.html')     #跳转到uilunbo.html页面


#用来处理post提交的表单数据   因为框架里面有frame，在框架里面跨域要加@xframe_options_exempt
@xframe_options_exempt
def uilunbopost(request):   #接收templates里uilunbo.html模块提交过来数据并处理

    fullname = ""
    imgurl = request.FILES.get('tbpic')  # 接收前面以files提交的图片，放到imgurl里面
    # 有上传文件的情况   将图片 yxrs2.jpg 转为 20200226144630.jpg 格式并保持为 static/uploadimg/20200226144630.jpg
    if (str(imgurl) != "None"):  # str(imgurl)将imgurl对象转为字符串格式，判断是否有文件上传的情况
        t = datetime.datetime.today()  # 获取当前时间，放到t里面
        s = datetime.datetime.strftime(t, "%Y%m%d%H%M%S")  # 将时间格式化，s变量里面就是保存的当前时间格式化后的字符串
        oldname = imgurl.name  # 获取文件的旧的名称 yxrs2.jpg
        pos = oldname.rfind('.')  # 从文件的右边开始找点
        extname = ""  # 这个变量用来保存扩展名
        if pos > 0:  # 当找到点
            extname = oldname[pos:]  # .jpg 把扩展名取出来保存在变量extname中
        fullname = s + extname  # 用当前时间格式化后的字符串与扩展名拼接  得到一个新的文件名20200226144630.jpg
        file_path = os.path.join('static/uploadimg', fullname)  # 拼接出一个完整的路径static/uploadimg\20200226144630.jpg
        file_path = file_path.replace("\\", "/")  # 把路径中的反斜杠\替换为斜杠/ static/uploadimg/20200226144630.jpg
        with open(file_path, 'wb') as f:  # 在file_path下创建一个可写文件
            for chunk in imgurl.chunks():  # chunk表示文件可能是分块上传的
                f.write(chunk)  # 分块写入到文件中
    else:  # 没有上传文件的情况
        fullname = ""
    # 图片上传结束
    #上传的图片保存在static/uploadimg里面，在这个文件上右键--show in explorer可看到上传的图片，数据库里面保存的只是文件的名称，图片保存在static里面方便拿取
    #往表里面插数据
    strsql = "insert into uilunbo (imgurl) values ('" + fullname + "') "
    cursor.execute(strsql)   #执行SQL语句
    msg={}
    msg['xinxi']='保存成功'
    return render(request, 'uilunbo.html',msg)    #提交成功后跳转到foodadd.html页面


#允许在框架下加载菜单
@xframe_options_exempt
def uilunbolist(request):
    strsql = "select id,imgurl from uilunbo order by id desc"
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()    #fetchone表示每次只拿取一个值
    uilunbolist=[]
    while row:
        #print(row)
        uilunbolist.append({"id": row[0],"imgurl": row[1]})
        row = cursor.fetchone()
    return render(request, 'uilunbolist.html',{'uilunbolist': uilunbolist})

@xframe_options_exempt
def lunbodelete(request):
    #删除数据
    id = request.GET.get("id")
    sqlstr1="delete from uilunbo where id="+id    #将对应的从数据库删除
    cursor.execute(sqlstr1)
    conn.commit()
                                                   #重新查询数据，渲染列表模板
    sqlstr2 = "select id,imgurl from uilunbo order by id desc"
    cursor.execute(sqlstr2)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    uilunbolist = []
    while row:
        # print(row)
        uilunbolist.append({"id": row[0], "imgurl": row[1]})
        row = cursor.fetchone()
    return render(request, 'uilunbolist.html', {'uilunbolist': uilunbolist})


#三种传数据方式
def test(request):
    return render(request, 'test.html')      #templates里写了test.html模块

def testdata(request):
    context = {}
    context['hello'] = '夜鹰教程网测试!'       #templates里写了testdata.html模块
    return render(request, 'testdata.html',context)


def hello(request):
    s="<h1 style='color:red;'>welcome to rongzhi</h1>"
    response = HttpResponse(s)
    #允许跨域使用
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST,GET,OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


@xframe_options_exempt
def uichushi(request):               #菜品表单页面
    return render(request, 'uichushi.html')     #跳转到uichushi.html页面


#用来处理post提交的表单数据   因为框架里面有frame，在框架里面跨域要加@xframe_options_exempt
@xframe_options_exempt
def uichushipost(request):
    tbname = request.POST.get('tbname')        #前面是以post方式提交的，就用poet方式接收
    tbbrief = request.POST.get('tbbrief')


    # 图片上传开始    如果这段代码引入进来有波浪线，把鼠标放上去选中引入包

    fullname = ""
    imgurl = request.FILES.get('tbpic')  # 接收前面以files提交的图片，放到imgurl里面
    # 有上传文件的情况   将图片 yxrs2.jpg 转为 20200226144630.jpg 格式并保持为 static/uploadimg/20200226144630.jpg
    if (str(imgurl) != "None"):  # str(imgurl)将imgurl对象转为字符串格式，判断是否有文件上传的情况
        t = datetime.datetime.today()  # 获取当前时间，放到t里面
        s = datetime.datetime.strftime(t, "%Y%m%d%H%M%S")  # 将时间格式化，s变量里面就是保存的当前时间格式化后的字符串
        oldname = imgurl.name  # 获取文件的旧的名称 yxrs2.jpg
        pos = oldname.rfind('.')  # 从文件的右边开始找点
        extname = ""  # 这个变量用来保存扩展名
        if pos > 0:  # 当找到点
            extname = oldname[pos:]  # .jpg 把扩展名取出来保存在变量extname中
        fullname = s + extname  # 用当前时间格式化后的字符串与扩展名拼接  得到一个新的文件名20200226144630.jpg
        file_path = os.path.join('static/uploadimg', fullname)  # 拼接出一个完整的路径static/uploadimg\20200226144630.jpg
        file_path = file_path.replace("\\", "/")  # 把路径中的反斜杠\替换为斜杠/ static/uploadimg/20200226144630.jpg
        with open(file_path, 'wb') as f:  # 在file_path下创建一个可写文件
            for chunk in imgurl.chunks():  # chunk表示文件可能是分块上传的
                f.write(chunk)  # 分块写入到文件中
    else:  # 没有上传文件的情况
        fullname = ""
    # 图片上传结束
    #上传的图片保存在static/uploadimg里面，在这个文件上右键--show in explorer可看到上传的图片，数据库里面保存的只是文件的名称，图片保存在static里面方便拿取
    #往表里面插数据
    strsql = "insert into uichushi (tbname,probrief,imgurl) values ('" + tbname + "','" + tbbrief + "','" + fullname + "') "
    cursor.execute(strsql)   #执行SQL语句
    msg={}
    msg['xinxi']='保存成功'
    return render(request, 'uichushi.html',msg)    #提交成功后跳转到foodadd.html页面

@xframe_options_exempt
def uichushilist(request):
    strsql = "select id,tbname,probrief,imgurl from uichushi order by id desc"
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()    #fetchone表示每次只拿取一个值
    uichushilist=[]
    while row:
        #print(row)
        uichushilist.append({"id": row[0],"tbname": row[1],"probrief": row[2],"imgurl": row[3]})
        row = cursor.fetchone()
    return render(request, 'uichushilist.html',{'uichushilist': uichushilist})


@xframe_options_exempt
def chushidelete(request):
    #删除数据
    id = request.GET.get("id")
    sqlstr1="delete from uichushi where id="+id    #将对应的从数据库删除
    cursor.execute(sqlstr1)
    conn.commit()
                                                   #重新查询数据，渲染列表模板
    sqlstr2 = "select id,tbname,probrief,imgurl from uichushi order by id desc"
    cursor.execute(sqlstr2)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    uichushilist = []
    while row:
        # print(row)
        uichushilist.append({"id": row[0],"tbname": row[1],"probrief": row[2],"imgurl": row[3]})
        row = cursor.fetchone()
    return render(request, 'uichushilist.html', {'uichushilist': uichushilist})


@xframe_options_exempt
def uitiandian(request):               #菜品表单页面
    return render(request, 'uitiandian.html')     #跳转到foodadd.html页面


#用来处理post提交的表单数据   因为框架里面有frame，在框架里面跨域要加@xframe_options_exempt
@xframe_options_exempt
def uitiandianpost(request):   #接收templates里foodadd.html模块提交过来数据并处理
    tbname = request.POST.get('tbname')        #前面是以post方式提交的，就用poet方式接收
    tbprice = request.POST.get('tbprice')
    tbbrief = request.POST.get('tbbrief')

    # 图片上传开始    如果这段代码引入进来有波浪线，把鼠标放上去选中引入包

    fullname = ""
    imgurl = request.FILES.get('tbpic')  # 接收前面以files提交的图片，放到imgurl里面
    # 有上传文件的情况   将图片 yxrs2.jpg 转为 20200226144630.jpg 格式并保持为 static/uploadimg/20200226144630.jpg
    if (str(imgurl) != "None"):  # str(imgurl)将imgurl对象转为字符串格式，判断是否有文件上传的情况
        t = datetime.datetime.today()  # 获取当前时间，放到t里面
        s = datetime.datetime.strftime(t, "%Y%m%d%H%M%S")  # 将时间格式化，s变量里面就是保存的当前时间格式化后的字符串
        oldname = imgurl.name  # 获取文件的旧的名称 yxrs2.jpg
        pos = oldname.rfind('.')  # 从文件的右边开始找点
        extname = ""  # 这个变量用来保存扩展名
        if pos > 0:  # 当找到点
            extname = oldname[pos:]  # .jpg 把扩展名取出来保存在变量extname中
        fullname = s + extname  # 用当前时间格式化后的字符串与扩展名拼接  得到一个新的文件名20200226144630.jpg
        file_path = os.path.join('static/uploadimg', fullname)  # 拼接出一个完整的路径static/uploadimg\20200226144630.jpg
        file_path = file_path.replace("\\", "/")  # 把路径中的反斜杠\替换为斜杠/ static/uploadimg/20200226144630.jpg
        with open(file_path, 'wb') as f:  # 在file_path下创建一个可写文件
            for chunk in imgurl.chunks():  # chunk表示文件可能是分块上传的
                f.write(chunk)  # 分块写入到文件中
    else:  # 没有上传文件的情况
        fullname = ""
    # 图片上传结束
    #上传的图片保存在static/uploadimg里面，在这个文件上右键--show in explorer可看到上传的图片，数据库里面保存的只是文件的名称，图片保存在static里面方便拿取
    #往表里面插数据
    strsql = "insert into uitiandian (proname,proprice,probrief,imgurl) values ('" + tbname + "'," + tbprice + ",'" + tbbrief + "','" + fullname + "') "
    cursor.execute(strsql)   #执行SQL语句
    msg={}
    msg['xinxi']='保存成功'
    return render(request, 'uitiandian.html',msg)    #提交成功后跳转到foodadd.html页面

@xframe_options_exempt
def uitiandianlist(request):
    strsql = "select id,proname,proprice,probrief,imgurl from uitiandian order by id desc"
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()    # fetchone表示每次只拿取一个值
    uitiandianlist=[]
    while row:
        #print(row)
        uitiandianlist.append({"id": row[0], "proname": row[1], "proprice": row[2],"probrief": row[3],"imgurl": row[4]})
        row = cursor.fetchone()
    return render(request, 'uitiandianlist.html',{'uitiandianlist': uitiandianlist})



@xframe_options_exempt
def uitiandiandelete(request):
    #删除数据
    id = request.GET.get("id")
    sqlstr1="delete from uitiandian where id="+id    #将对应的从数据库删除
    cursor.execute(sqlstr1)
    conn.commit()
                                                   #重新查询数据，渲染列表模板
    sqlstr2 = "select id,proname,proprice,imgurl,probrief from uitiandian order by id desc"
    cursor.execute(sqlstr2)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    foodlist = []
    while row:
        # print(row)
        foodlist.append({"id": row[0], "proname": row[1], "proprice": row[2], "imgurl": row[3], "probrief": row[4]})
        row = cursor.fetchone()
    return render(request, 'uitiandianlist.html', {'uitiandianlist': foodlist})


@xframe_options_exempt
def messagelist(request):
    strsql = "select id,userid,truename,text,reply from tbmessage order by id desc"
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    messagelist=[]
    while row:
        #print(row)
        messagelist.append({"id": row[0], "userid": row[1], "truename": row[2],"text": row[3],"reply": row[4]})
        row = cursor.fetchone()
    return render(request, 'messagelist.html',{'messagelist': messagelist})

# @xframe_options_exempt
# def messagedelete(request):
#     id = request.GET.get("id")
#     sqlstr1 = "delete from tbmessage where id=" + id
#     cursor.execute(sqlstr1)
#     conn.commit()
#     # 重新查询数据，渲染列表模板
#     sqlstr2 = "select userid,truename,text,reply from tbmessage order by id desc"
#     cursor.execute(sqlstr2)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
#     row = cursor.fetchone()
#     messagelist = []
#     while row:
#         # print(row)
#         messagelist.append({"userid": row[0],  "truename": row[1],"text": row[2],"reply": row[3]})
#         row = cursor.fetchone()
#     return render(request, 'messagelist.html', {'messagelist': messagelist})

@xframe_options_exempt
def messagedelete(request):
    #删除数据
    id = request.GET.get("id")
    sqlstr1="delete from tbmessage where id="+id    #将对应的从数据库删除
    cursor.execute(sqlstr1)
    conn.commit()
                                                   #重新查询数据，渲染列表模板
    sqlstr2 = "select userid,truename,text,reply from tbmessage order by id desc"
    cursor.execute(sqlstr2)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    messagelist = []
    while row:
        # print(row)
        messagelist.append({"userid": row[0], "truename": row[1], "text": row[2], "reply": row[3]})
        row = cursor.fetchone()
    return render(request, 'messagelist.html', {'messagelist': messagelist})






@xframe_options_exempt
def messagereply(request):
    id = request.GET.get("id")
    strsql1 = "select id,truename,text from tbmessage  where id="+id
    cursor.execute(strsql1)
    row = cursor.fetchone()
    view={"id": row[0], "truename": row[1], "text": row[2]}
    return render(request, 'messagereply.html',{'view': view})


@xframe_options_exempt
def messagereplypost(request):
    #接收参数
    proid = request.POST.get("proid")
    tbcontents = request.POST.get("tbcontents")

    sqlstr = "update tbmessage set reply='"+tbcontents+"' where id="+proid
    cursor.execute(sqlstr)
    conn.commit()

    view = {"id": proid, "descriptions": tbcontents, "msg": "保存成功"}

    sqlstr2 = "select userid,truename,text,reply from tbmessage order by id desc"
    cursor.execute(sqlstr2)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    messagelist = []
    while row:
        # print(row)
        messagelist.append({"userid": row[0], "truename": row[1], "text": row[2], "reply": row[3]})
        row = cursor.fetchone()
    return render(request, 'messagelist.html', {'messagelist': messagelist})


@xframe_options_exempt
def memberlist(request):
    strsql = "select id,username,truename,tel,address from tbusers order by id desc"
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    memberlist=[]
    while row:
        #print(row)
        memberlist.append({"id": row[0], "username": row[1], "truename": row[2],"tel": row[3],"address": row[4]})
        row = cursor.fetchone()
    return render(request, 'memberlist.html',{'memberlist': memberlist})


@xframe_options_exempt
def memberdelete(request):
    id = request.GET.get("id")
    sqlstr1 = "delete from tbusers where id=" + id
    cursor.execute(sqlstr1)
    conn.commit()
    # 重新查询数据，渲染列表模板
    sqlstr2 = "select id,username,truename,tel,address from tbusers order by id desc"
    cursor.execute(sqlstr2)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    memberlist = []
    while row:
        # print(row)
        memberlist.append({"id": row[0], "username": row[1], "truename": row[2],"tel": row[3],"address": row[4]})
        row = cursor.fetchone()
    return render(request, 'memberlist.html', {'memberlist': memberlist})


@xframe_options_exempt
def uitiandianedit(request):
    id = request.GET.get("id")    #这个id是通过get方式提交的，从foodlist获取要修改的id
    strsql1 = "select id,proname,proprice,imgurl,probrief  from uitiandian where id="+id   #从数据库获取相关信息
    cursor.execute(strsql1)
    row = cursor.fetchone()    #取出这条信息
    view={"id": row[0], "proname": row[1], "proprice": row[2],"imgurl": row[3],"probrief": row[4]}
    return render(request, 'uitiandianedit.html',{'foodview': view})    #将取出的数据放到foodedit.html页面


@xframe_options_exempt
def uitiandianeditpost(request):
    #接收参数
    proid = request.POST.get("proid")    #获取要修改项的id
    oldimgurl = request.POST.get("oldimgurl")   #获取旧的图片路径，以便若图片没有修改可继续使用这个路径

    tbname = request.POST.get("tbname")
    tbprice = request.POST.get("tbprice")
    tbbrief = request.POST.get("tbbrief")


    imgurl = request.FILES.get('tbpic')

    fullname=""
    if(str(imgurl)!="None"):     #若图片被修改
        t = datetime.datetime.today()
        s = datetime.datetime.strftime(t, "%Y%m%d%H%M%S")
        oldname=imgurl.name
        pos = oldname.rfind('.')
        extname=""
        if pos > 0:
            extname= oldname[pos:]
        fullname=s+extname
        file_path = os.path.join('static/uploadimg', fullname)
        file_path=file_path.replace("\\","/")
        print(file_path)
        with open(file_path, 'wb') as f:
            for chunk in imgurl.chunks():
                f.write(chunk)
    else:
        fullname=oldimgurl     #图片没有被修改就要原来的图片路径

    sqlstr = "update uitiandian set proname='"+tbname+"',proprice="+tbprice+",probrief='"+tbbrief+"',imgurl='"+fullname+"' where id="+proid
    cursor.execute(sqlstr)
    conn.commit()
    view = {"id": proid, "proname": tbname, "proprice": tbprice, "imgurl": fullname, "probrief": tbbrief,
            "msg":"保存成功"}
    return render(request, 'uitiandianedit.html',{'foodview': view})