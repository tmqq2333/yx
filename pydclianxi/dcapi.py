from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponse
import pymysql
import datetime
import os

conn=pymysql.connect(
    user='root',
    password='123456',
    port=3306,
    host='127.0.0.1',
    db='diancan',
    charset='utf8'
)
cursor=conn.cursor()
cursor.execute('set names utf8')
cursor.execute('set autocommit=1')


@xframe_options_exempt
def getfoodlist(request):
    print("接收到的参数typeid="+str(request.GET.get("typeid")))
    res='[{"author":"admin","contents":"1212","createtime":"1212","id":103,"source":"校内新闻","title":"“不忘初心，牢记使命”主题教育工作会议召开","typeid":"1"},{"author":"admin","contents":"2019年3月18日，由吉食道食品、申唐产业、翠宏食品、航佳食品、红灯笼食品、智琪食品六家公司共同发起，成都市食品工业协会联合主办的第四届“发现川味”中国餐饮高峰论坛及食材展在成都隆重举行。\r\n据悉，本届食材展汇聚了全国40 家餐饮业供应链企业。活动当天，全国知名餐饮品牌CEO、餐饮加盟门店企业主等上千名代表出席了餐饮高峰论坛，会上嘉宾从餐饮运营、营销、供应链等角度全方位的剖析餐饮行业当前的发展现状和行业前景。\r\n红餐作为战略合作媒体参与了本次活动，为大家进行详细的报道。","createtime":"2019-03-18","id":102,"source":"吃哪儿网","title":"在流量时代怎样做餐饮营销","typeid":"1"}]'
    response=HttpResponse(res)
    response["Access-Control-Allow-Origin"] ="*"
    response["Access-Control-Allow-Methods"] ="POST,GET,OPTIONS"
    #response["Access-Control-Max-Age"] ="1000"
    response["Access-Control-Allow-Headers"] ="*"
    return response

@xframe_options_exempt
def reg(request):
    print("接收到的参数typeid="+str(request.GET.get("typeid")))
    res='[{"author":"admin","contents":"1212","createtime":"1212","id":103,"source":"校内新闻","title":"“不忘初心，牢记使命”主题教育工作会议召开","typeid":"1"},{"author":"admin","contents":"2019年3月18日，由吉食道食品、申唐产业、翠宏食品、航佳食品、红灯笼食品、智琪食品六家公司共同发起，成都市食品工业协会联合主办的第四届“发现川味”中国餐饮高峰论坛及食材展在成都隆重举行。\r\n据悉，本届食材展汇聚了全国40 家餐饮业供应链企业。活动当天，全国知名餐饮品牌CEO、餐饮加盟门店企业主等上千名代表出席了餐饮高峰论坛，会上嘉宾从餐饮运营、营销、供应链等角度全方位的剖析餐饮行业当前的发展现状和行业前景。\r\n红餐作为战略合作媒体参与了本次活动，为大家进行详细的报道。","createtime":"2019-03-18","id":102,"source":"吃哪儿网","title":"在流量时代怎样做餐饮营销","typeid":"1"}]'
    response=HttpResponse(res)
    response["Access-Control-Allow-Origin"] ="*"
    response["Access-Control-Allow-Methods"] ="POST,GET,OPTIONS"
    response["Access-Control-Max-Age"] ="1000"
    response["Access-Control-Allow-Headers"] ="*"
    return response


def login(request):
    #print("接收到的参数typeid="+str(request.GET.get("typeid")))
    username=request.POST.get("username")
    password = request.POST.get("password")
    print(username)
    print(password)
    strsql="select id,username,password,truename,tel,address from tbusers where username='"+username+"' and password='"+password+"' "
    cursor.execute(strsql)
    conn.commit()
    row = cursor.fetchone()
    s=""
    if row:
        s=str({"id": row[0], "username": row[1], "password": row[2], "truename": row[3], "tel": row[4], "address": row[5]})
        s=s.replace("'","\"")
    res="["+s+"]"
    response=HttpResponse(res)
    response["Access-Control-Allow-Origin"] ="*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response   #返回到小程序端

@xframe_options_exempt
def getfoodlistbyrandom(request):
                                                            #order by  RAND() limit 4 表示随机拿4个数据
    strsql = "select id,proname,proprice,probrief,proaddress,imgurl from product order by  RAND() limit 2 "
    cursor.execute(strsql)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    while row:
        foodlist.append({"id": row[0], "proname": row[1], "proprice":str(row[2]), "probrief": row[3], "proaddress": row[4],"imgurl": row[5]})
        row = cursor.fetchone()
    sfood = str(foodlist)
    sfood =sfood.replace("'", "\"")
    strsql3= "select id,imgurl from uilunbo order by  RAND() limit 3 "
    cursor.execute(strsql3)
    conn.commit()
    pptlist = []
    row = cursor.fetchone()
    while row:
        pptlist.append({"id": row[0], "imgurl": row[1]})
        row = cursor.fetchone()
    sppt = str(pptlist)
    sppt= sppt.replace("'", "\"")
    strsql4 = "select id,tbname,imgurl from uichushi order by  RAND() limit 3 "
    cursor.execute(strsql4)
    conn.commit()
    chushilist = []
    row = cursor.fetchone()
    while row:
        chushilist.append({"id": row[0], "tbname": row[1], "imgurl": row[2]})
        row = cursor.fetchone()
    chushi = str(chushilist)
    chushi = chushi.replace("'", "\"")

    sresult="[{\"foodlist\":"+sfood+",\"pptlist\":"+sppt+", \"chushilist\":" + chushi + "}]"
    response = HttpResponse(sresult)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

@xframe_options_exempt
def getfoodbyid(request):
    id= request.POST.get("id")
    strsql = "select id,proname,proprice,probrief,proaddress,imgurl from product where id="+id
    cursor.execute(strsql)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    if row:
        foodlist.append({"id": row[0], "proname": row[1], "proprice":str(row[2]), "probrief": row[3], "proaddress": row[4],"imgurl": row[5]})
    s = str(foodlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

@xframe_options_exempt
def getfoodlist(request):
    key= request.POST.get("key")
    strsql = "select id,proname,proprice,probrief,proaddress,imgurl from product order by id desc "
    if not key.strip()=="":
        strsql = "select id,proname,proprice,probrief,proaddress,imgurl from product where proname like '%"+key+"%'  order by id desc "
    cursor.execute(strsql)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    while row:
        foodlist.append({"id": row[0], "proname": row[1], "proprice":str(row[2]), "probrief": row[3], "proaddress": row[4],"imgurl": row[5]})
        row = cursor.fetchone()
    s = str(foodlist)
    s = s.replace("'", "\"")





    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

def addtocar(request):
    # 接收参数
    userid = request.POST.get('userid')
    proid = request.POST.get('proid')
    proname = request.POST.get('proname')
    procount = request.POST.get('procount')
    imgurl = request.POST.get('imgurl')
    price = request.POST.get('price')
    #获取最新时间并格式化
    ctime = datetime.datetime.now().strftime('%F %T')
    # 我们将一个菜品加入购物车的时候，首先要判断购物车里面是否已经存在这个菜品了，如果已经存在，就增加数量，如果不存在，就插入一条新的记录。
    strsql1 = "select id from tbshoppingcar where proid=" + proid + " and sessionid=" + userid
    cursor.execute(strsql1)
    conn.commit()
    row = cursor.fetchone()
    # 默认是往数据库插一条数据
    strsql2 = "insert into tbshoppingcar(sessionid,proname,proid,procount,ctime,imgurl,price) values (" + userid + ",'" + proname + "'," + proid + "," + procount + ",'" + ctime + "','" + imgurl + "'," + price + ") "
    #如果已经存在，就修改增加数量
    if row:
        strsql2 = "update tbshoppingcar set procount=procount+" + procount + " where proid=" + proid + " and sessionid=" + userid
    print(strsql2)
    cursor.execute(strsql2)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(res)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

@xframe_options_exempt
def getcarlist(request):
    userid= request.POST.get("userid")
    strsql = "select id,sessionid,proname,proid,procount,ctime,imgurl,price from tbshoppingcar where sessionid="+userid
    cursor.execute(strsql)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    while row:
        foodlist.append({"id": row[0], "sessionid": row[1], "proname":row[2], "proid": row[3], "procount": row[4],"ctime": row[5],"imgurl": row[6],"price":str(row[7])})
        row = cursor.fetchone()
    s = str(foodlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

def changecarnum(request):
    id= request.POST.get("id")
    typeid = request.POST.get("typeid")
    #默认是加一
    strsql = "update tbshoppingcar set procount=procount+1 where id=" + id
    #当是减的时候
    if typeid=="0":
        strsql = "update tbshoppingcar set procount = IF(procount > 1, procount - 1,1) where id=" + id
                                       #procount = IF(procount > 1, procount - 1,1)  表示如果procount>1 就procount-1
                                                                                        #如果procount<1 就procount=1
    cursor.execute(strsql)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

@xframe_options_exempt
def deleteitembyid(request):
    id= request.POST.get("id")
    strsql = "delete from tbshoppingcar where id="+id
    cursor.execute(strsql)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

#在线下单功能
@xframe_options_exempt
def saveorder(request):
    t = datetime.datetime.now()
    ctime = t.strftime('%Y-%m-%d %H:%M:%S')
    orderid = datetime.datetime.strftime(t, "%Y%m%d%H%M%S%f")
    userid= request.POST.get("userid")
    sumprice = request.POST.get("sumprice")
    sname = request.POST.get("sname")
    stel = request.POST.get("stel")
    saddress = request.POST.get("saddress")
    ptime = request.POST.get("ptime")
    memo = request.POST.get("memo")
    #插入表头信息
    cursor.execute("insert into tborderhead (orderid,sname,stel,saddress,sumprice,memberid,ctime,ptime,memo) values ('"+orderid+"','"+sname+"','"+stel+"','"+saddress+"',"+sumprice+","+userid+",'"+ctime+"','"+ptime+"','"+memo+"')")
    conn.commit()

    #把购物车里面的数据插入到订单明细表
    #先把购物车里当前这个人的菜品查询出来
    strsql = "select id,sessionid,proname,proid,procount,ctime,imgurl,price from tbshoppingcar where sessionid="+userid
    cursor.execute(strsql)
    conn.commit()
    #构造插入订单明细表的sql语句
    sqllists = []
    row = cursor.fetchone()
    while row:
        #{"id": row[0], "sessionid": row[1], "proname": row[2], "proid": row[3], "procount": row[4], "ctime": row[5],"imgurl": row[6], "price": str(row[7])}
        sqllists.append("insert into tborderitems (orderid,proid,proname,price,procount,imgurl) values ('"+orderid+"',"+str(row[3])+",'"+row[2]+"',"+str(row[7])+","+str(row[4])+",'"+row[6]+"')")
        row = cursor.fetchone()
    #遍历sql列表，执行插入订单明细表操作
    for sqlitem in sqllists:
        cursor.execute(sqlitem)
        conn.commit()
    #清空购物车
    cursor.execute("delete from tbshoppingcar where sessionid="+userid)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response


@xframe_options_exempt
def chushilist(request):
    strsql = "select id,tbname,probrief,imgurl from uichushi "
    cursor.execute(strsql)
    conn.commit()
    chushilist = []
    row = cursor.fetchone()
    while row:
        chushilist.append({"id": row[0], "tbname": row[1], "probrief": row[2], "imgurl": row[3]})
        row = cursor.fetchone()
    s = str(chushilist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

@xframe_options_exempt
def tiandianlist(request):
    strsql = "select id,proname,proprice,probrief,imgurl from uitiandian "
    cursor.execute(strsql)
    conn.commit()
    tiandianlist = []
    row = cursor.fetchone()
    while row:
        tiandianlist.append({"id": row[0], "proname": row[1], "proprice": row[2], "probrief": row[3],"imgurl": row[4]})
        row = cursor.fetchone()
    s = str(tiandianlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

@xframe_options_exempt
def getmyorderlist(request):
    memberid = request.POST.get("memberid")
    strsql = "select id,imgurl,orderid,price,procount,proname,sname,stel,saddress,sumprice,memberid,ctime,memo from dingdan where memberid=" + memberid+" order by id desc"
    cursor.execute(strsql)
    conn.commit()
    orderlist = []
    row = cursor.fetchone()
    while row:
        orderlist.append({"id": row[0], "imgurl": row[1], "orderid": row[2], "price": row[3],"procount": row[4],"proname": row[5], "sname": row[6], "stel": row[7], "saddress": row[8],"sumprice": row[9], "memberid": row[10], "ctime": row[11],"memo": row[12]})
        row = cursor.fetchone()
    s = str(orderlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response


@xframe_options_exempt
def reg(request):   #接收templates里foodadd.html模块提交过来数据并处理
    username = request.POST.get('loginname')        #前面是以post方式提交的，就用poet方式接收
    password = request.POST.get('password')
    truename = request.POST.get('truename')
    tel = request.POST.get('tel')
    address = request.POST.get('address')



    #上传的图片保存在static/uploadimg里面，在这个文件上右键--show in explorer可看到上传的图片，数据库里面保存的只是文件的名称，图片保存在static里面方便拿取
    #往表里面插数据
    strsql = "insert into tbusers (username,password,truename,tel,address) values ('" + username + "'," + password + ",'" + truename + "','" + tel + "','" + address + "') "
    cursor.execute(strsql)   #执行SQL语句
    s = "{\"msg\":\"注册成功\"}"
    res = "[" + s + "]"
    response = HttpResponse(res)

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response


@xframe_options_exempt
def gettiandianbyid(request):
    id= request.POST.get("id")
    strsql = "select id,proname,proprice,probrief,imgurl from uitiandian where id="+id
    cursor.execute(strsql)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    if row:
        foodlist.append({"id": row[0], "proname": row[1], "proprice":str(row[2]), "probrief": row[3], "imgurl": row[4]})
    s = str(foodlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

def message(request):
    userid = request.POST.get("userid")
    text = request.POST.get("text")
    truename = request.POST.get("truename")

    #strsql = "insert into tbusers (username,password,truename,tel,address) values ('"+username+"','"+password+"','"+truename+"','"+tel+"','"+address+"')";
    # cursor.execute(strsql)
    cursor.execute('insert into tbmessage (userid,truename,text) value (%s,%s,%s)',(userid,truename,text))
    conn.commit()
    s="{\"msg\":\"留言成功\"}"
    res="["+s+"]"
    response=HttpResponse(res)
    response["Access-Control-Allow-Origin"] ="*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response


@xframe_options_exempt
def messagelist(request):
    strsql = "select id,userid,truename,text,reply from tbmessage order by id desc"
    cursor.execute(strsql)
    conn.commit()
    messagelist = []
    row = cursor.fetchone()
    while row:
        if row[4] is None:
           messagelist.append({"id": row[0], "userid": row[1], "truename": row[2],"text": row[3]})

        else:
            messagelist.append({"id": row[0], "userid": row[1], "truename": row[2], "text": row[3],"reply": row[4]})
        row = cursor.fetchone()
    s = str(messagelist )
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response





