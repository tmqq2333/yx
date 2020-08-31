// pages/tiandian/tiandian.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    tiandianlist:[]

  },

  fngotofoodview:function(e){
    console.log(e.currentTarget.dataset.foodname);
    
      wx.navigateTo({
        url: '/pages/tiandianview/tiandianview?id='+e.currentTarget.dataset.id,
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
    var that=this;
    that.setData({
      urlhead:getApp().globalData.urlhead
    });
        //在此处编写请求首页菜品数据的逻辑代码
      wx.request({
        url: getApp().globalData.urlhead+'/dcapi/tiandianlist',
        method: 'POST',
        data: {
          
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded' // 默认值
        },
        dataType: 'json',
        success(cc) {
          console.log(cc);
          that.setData({
            tiandianlist:cc.data
          });
        }
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