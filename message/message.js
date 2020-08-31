Page({



 
  /**
   * 页面的初始数据
   */
  data: {
    text:'',
    msg:''
  },
 
  fntext: function (e) {
    var that = this;
    var curvalue = e.detail.value;
    that.setData({
      text: curvalue
    });
  },
  fnccc:function(e){
    wx.navigateTo({
      url: '/pages/messagelist/messagelist',
    });
  },

  fntii:function(e){
    var that=this;
    var currentusertruename = wx.getStorageSync("currentusertruename");
    var currentuserid = wx.getStorageSync("currentuserid");
    console.log(currentusertruename);
    if(currentusertruename.length<1)
    {
        wx.showToast({
          title: '你还没有登录',
          icon:'none'
        });
        setTimeout(function(){
          wx.navigateTo({
            url: '/pages/login/login'
          });
        },2000);         
    }
    else
    {
      
      console.log(that.data.text)
      console.log(e)
      if (that.data.text==null||that.data.text == undefined || that.data.text=='')
      { 
        that.setData({
          msg: "提交失败"
        });
        
      }
      else{
        wx.request({
          url: getApp().globalData.urlhead+'/dcapi/message',
          method: 'POST',
          data: {
            userid: currentuserid,
            truename:currentusertruename,
            text: that.data.text
            
          },
          header: {
            'content-type': 'application/x-www-form-urlencoded' // 默认值
          },
          dataType: 'json',
          success(cc) {
  
            that.setData({
              msg: "提交成功"
            });
              
              setTimeout(function () {
                  wx.switchTab({
                    url: '/pages/my/my',
                  })
              }, 1000);
              
            
          
          
          }
        });
    }
  } 
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