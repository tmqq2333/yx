// pages/geren/geren.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    currentuserid:null,
    currentusertruename:'',
    currentusertruetel:'',
    currentusertrueaddress:'',
    currentuserusername:'',
    mima:'******'

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
    var currentuserid=wx.getStorageSync('currentuserid');
    var currentusertruename=wx.getStorageSync('currentusertruename');
    var currentusertruetel=wx.getStorageSync('currentusertruetel');
    var currentusertrueaddress=wx.getStorageSync('currentusertrueaddress');
    var currentuserusername=wx.getStorageSync('currentuserusername');
    
    this.setData({
      currentuserid:currentuserid,
      currentusertruename:currentusertruename,
      currentusertruetel:currentusertruetel,
      currentusertrueaddress:currentusertrueaddress,
      currentuserusername:currentuserusername
    });

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