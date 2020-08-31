// pages/myorder/myorder.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    messagelist:[],
    msg:'',
    mss:'回复：'
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
    wx.request({
      url: getApp().globalData.urlhead+'/dcapi/messagelist',
      method: 'POST',
      data: {
        
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded' // 默认值
      },
      dataType: 'json',
      success(cc) {
        console.log(cc.data.reply);
       
        that.setData({
          messagelist:cc.data//把后端查询出来的菜品列表信息存放到foodlist数组中
        });
      //   var i=0;
      //   for(i=0;i<cc.data.length;i++){
      //   if (cc.data[i].reply==null||cc.data[i].reply == undefined ||cc.data[i].reply==''){
      //     that.setData({
      //       mss:''
      //     });
      //     console.log(cc.data)
      //   }
      //   }
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