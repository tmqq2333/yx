// pages/reg/reg.js
Page({



 
  /**
   * 页面的初始数据
   */
  data: {
    loginname: '',
    password: '',
    truename: '',
    tel: '',
    address: '',
    image: '',
    msg:''
    
  },
  fninputeditusername: function (e) {
    var that = this;
    var curvalue = e.detail.value;
    that.setData({
      loginname: curvalue
    });
    
  },
  fninputeditpassword: function (e) {
    var that = this;
    var curvalue = e.detail.value;
    that.setData({
      password: curvalue
    });
  },
  fninputedittruename: function (e) {
    var that = this;
    var curvalue = e.detail.value;
    that.setData({
      truename: curvalue
    });
  },
  fninputedittel: function (e) {
    var that = this;
    var curvalue = e.detail.value;
    that.setData({
      tel: curvalue
    });
  },
  fninputeditaddress: function (e) {
    var that = this;
    var curvalue = e.detail.value;
    that.setData({
      address: curvalue
    });
  },
  fninputeditimg: function (e) {
    var that = this;
    var curvalue = e.detail.value;
    that.setData({
      image: curvalue
    });
  },

  fnback:function(){
    wx.navigateTo({
      url: '/pages/login/login',
    });
  },

  uploadfn:function(e){
      // 选择图片
      wx.cloud.init()
      wx.chooseImage({
        count: 1,
        sizeType: ['compressed'],
        sourceType: ['album', 'camera'],
        success: function (res) {
  
          wx.showLoading({
            title: '上传中',
          })
  
          const filePath = res.tempFilePaths[0]
          
          // 上传图片
          const cloudPath = 'my-image' + filePath.match(/\.[^.]+?$/)[0]
          wx.cloud.uploadFile({
            cloudPath,
            filePath,
            success: res => {
              console.log('[上传文件] 成功：', res)
  
              app.globalData.fileID = res.fileID
              app.globalData.cloudPath = cloudPath
              app.globalData.imagePath = filePath
              
              wx.navigateTo({
                url: ''
              })
            },
            fail: e => {
              console.error('[上传文件] 失败：', e)
              wx.showToast({
                icon: 'none',
                title: '上传失败',
              })
            },
            complete: () => {
              wx.hideLoading()
            }
          })
  
        },
        fail: e => {
          console.error(e)
        }
      })
    
  },
  fnreg:function(e){
    var that = this;
    console.log(that.data.loginname)
    console.log(e)
    if (that.data.loginname==null||that.data.loginname == undefined || that.data.loginname==''||that.data.password==null||that.data.password == undefined || that.data.password=='')
    { 
      wx.showToast({
        title: '注册失败'
      });
      
    }
    else{
      wx.request({
        url: app.globalData.urlhead+'/dcapi/reg',
        method: 'POST',
        data: {
          loginname: that.data.loginname,
          password: that.data.password,
          truename:that.data.truename,
          tel: that.data.tel,
          address: that.data.address,
          image: that.data.image
          
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded' // 默认值
        },
        dataType: 'json',
        success(cc) {

            wx.showToast({
              title: '注册成功'
            });
            console.log(cc.data[0].truename)
            setTimeout(function () {
                wx.redirectTo({
                  url: '/pages/login/login',
                })
            }, 1000);
            that.setData({
              msg: ""
            });
          
        console.log(that.data.image)
        
        }
      });
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