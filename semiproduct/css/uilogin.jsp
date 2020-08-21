<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page language="java" import="java.util.*" %>
<%@ page language="java" import="java.sql.*" %>
<%@ page language="java" import="java.util.regex.*" %>
<%
String msg = (String)request.getAttribute("msg");
if(msg==null)
{
	msg="";
}
%>   
    
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<!--引入公共样式表-->
		<link rel="stylesheet" type="text/css" href="css/common.css"/>
		<!--引入私有样式表-->
		<link rel="stylesheet" type="text/css" href="css/login.css"/>
	</head>
	<body>
		
		<!--头部开始-->
		<div id="loginheader">
			<div class="innerclass"><img src="img/regLogo.png"/></div>
		</div>
		<!--头部结束-->
		
		<!--主体开始-->
		<div id="main">
			<div class="innerclass" style="position: relative;">
				<div id="loginform">
					<form action="uilogin" method="post">
						<p class="title"><span>账号登陆</span> | <span id="saocode">扫码登陆</span></p>
						<p class="ff"><input type="text" name="username" placeholder="邮箱/手机/小米ID" /></p>
						<p class="ff" style="margin-top: 14px;"><input type="password" name="password" placeholder="密码"/></p>
						<p class="btn"><input type="submit" value="登录" id="btnlogin"></p>
						<p class="forgetpassword"><span style="color:red;"><%=msg%></span>   <a href="reg.jsp">立即注册</a> | <a href="###">忘记密码</a></p>
					</form>
				</div>
			</div>
		</div>
		
		<!--主体结束-->
		
		<!--底部开始-->
		<div id="footer">
			<div id="service" class="innerclass">
				<a href="###" style="background-image: url(img/icon1.png);">预约维修服务</a> | <a href="###" style="background-image: url(img/icon2.png);">7天无理由退货</a> | <a href="###" style="background-image: url(img/icon3.png);">15天免费换货</a> | <a href="###" style="background-image: url(img/icon4.png);">满150元包邮</a> |<a href="###" style="background-image: url(img/icon5.png);">520余家售后 </a> 
			</div>
			<div id="bottomwrapper" class="innerclass">
				<div id="bottomleft">
					<dl>
						<dt>帮助中心</dt>
						<dd>账户管理</dd>
						<dd>购物指南</dd>
						<dd>订单操作</dd>
					</dl>
					<dl>
						<dt>帮助中心</dt>
						<dd>账户管理</dd>
						<dd>购物指南</dd>
						<dd>订单操作</dd>
					</dl>
					<dl>
						<dt>帮助中心</dt>
						<dd>账户管理</dd>
						<dd>购物指南</dd>
						<dd>订单操作</dd>
					</dl>
					<dl>
						<dt>帮助中心</dt>
						<dd>账户管理</dd>
						<dd>购物指南</dd>
						<dd>订单操作</dd>
					</dl>
					<dl>
						<dt>帮助中心</dt>
						<dd>账户管理</dd>
						<dd>购物指南</dd>
						<dd>订单操作</dd>
					</dl>
					<dl>
						<dt>帮助中心</dt>
						<dd>账户管理</dd>
						<dd>购物指南</dd>
						<dd>订单操作</dd>
					</dl>
				</div>
				<div id="bottomright">
				</div>
			</div>
			
			<div id="copyright" class="innerclass">
				<p class="first">
					<a href="###">小米商城</a> |
					<a href="###">miui</a> |
					<a href="###">米聊</a> |
					<a href="###">游戏</a> |
					<a href="###">多看阅读</a> |
					<a href="###">小城</a> |
					<a href="###">游戏</a> |
					<a href="###">小米商城</a> |
					<a href="###">游戏</a> |
					<a href="###">小米</a> 
				</p>
				<p> ICP备案号 数 蜀 ICB 55234441212 京公安备案 ：sssss223222</p>
				<p>违法和不良信息举报电话：12315 </p>
			</div>
			
		</div>
		<!--底部结束-->
		
	</body>
</html>
    