// pages/my/my.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    currentuserid:null,
    currentusertruename:'',
    currentusertruetel:'',
    currentusertrueaddress:'',
    memberid:''

  },
  fnmm:function(){
    wx.navigateTo({
      url: '/pages/message/message',
    
    })
  },
  fntc:function(){
    wx.redirectTo({
      url: '/pages/login/login',
     
    })
    }, 
    
    fndenglu:function(){
      wx.redirectTo({
        url: '/pages/login/login',
       
      })
      }, 

    fngr:function(){
    wx.redirectTo({
      url: '/pages/geren/geren',
     
    })
    }, 
  fnmytap:function(){
    wx.redirectTo({
      url: '/pages/login/login',
    });

  },
  fngotomyorder:function(){
    wx.redirectTo({
      url: '/pages/myorder/myorder',
    });

  },
  fnlianxi:function(){
    wx.redirectTo({
      url: '/pages/lxwm/lxwm',
    });

  },
  
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var currentuserid=wx.getStorageSync('currentuserid');
    var currentusertruename=wx.getStorageSync('currentusertruename');
    var currentusertruetel=wx.getStorageSync('currentusertruetel');
    var currentusertrueaddress=wx.getStorageSync('currentusertrueaddress');
    this.setData({
      currentuserid:currentuserid,
      currentusertruename:currentusertruename,
      currentusertruetel:currentusertruetel,
      currentusertrueaddress:currentusertrueaddress
    });
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