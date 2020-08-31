// pages/login/login.js

Page({
  /**
   * 页面的初始数据
   */
  data: {
    username: '',
    password: '',
    msg:''
  },
  fninputeditusername: function (e) {
    var that = this;
    var curvalue = e.detail.value;
    that.setData({
      username: curvalue
    });
  },
  fninputeditpassword: function (e) {
    var that = this;
    var curvalue = e.detail.value;
    that.setData({
      password: curvalue
    });
  },

  fngotoreg:function(){
    wx.navigateTo({
      url: '/pages/reg/reg',
    });
  },
  fnlogin:function(e){
    var that = this;
    wx.request({
      url: getApp().globalData.urlhead+'/dcapi/login',
      method: 'POST',
      data: {
        username: that.data.username,
        password: that.data.password
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded' // 默认值
      },
      dataType: 'json',
      success(cc) {
        console.log(cc.data);
        if(cc.data.length>0)
        {
          console.log(cc);
          // 返回的值，有返回表示数据库有值
          wx.setStorageSync("currentuserid", cc.data[0].id);
          wx.setStorageSync("currentusertruename", cc.data[0].truename);
          wx.setStorageSync("currentuserusername", cc.data[0].username);
          wx.setStorageSync("currentusertruetel", cc.data[0].tel);
          wx.setStorageSync("currentusertrueaddress", cc.data[0].address);
          wx.setStorageSync("currentuserimage", cc.data[0].image);
          wx.showToast({
            title: '登录成功'
          });
          console.log(cc.data[0].truename)
          setTimeout(function () {
              wx.switchTab({
                url: '/pages/index/index',
              })
          }, 1000);
          that.setData({
            msg: ""
          });
        }
        else
        {
          that.setData({
            msg:"用户名或密码错误",
        
          });
           
          setTimeout(function(){
            that.setData({
              msg:"",
          
            });
       
          },3000);
        }
       
      }
    });
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})