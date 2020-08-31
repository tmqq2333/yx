//index.js
//获取应用实例


Page({
  data: {
    motto: 'Hello World',
    foodlist:[],
    pptlist:[],
    chushilist:[],
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    urlhead:""
  },
  fnedit:function(e){
    var that = this;
    var curvalue = e.detail.value;
    getApp().globalData.key=curvalue;
  },
  fnsearch:function(){
    wx.switchTab({
      url: '/pages/foodlist/food',
    });
  },
  
  fntuijian:function(){
    wx.switchTab({
      url: '/pages/foodlist/food',
    });

  },
  fntiandain:function(){
    wx.redirectTo({
      url: '/pages/tiandian/tiandian',
    });

  },
  fnmingchu:function(){
    wx.redirectTo({
      url: '/pages/cooker/cooker',
    });
  },
  fncanyan:function(){
    wx.redirectTo({
      url: '/pages/canyan/canyan',
    });
  },
  
  onShow:function(){
    var that=this;
    console.log(getApp().globalData.urlhead);
    that.setData({
      urlhead:getApp().globalData.urlhead
    });
      //在此处编写请求首页菜品数据的逻辑代码
    wx.request({
      url: getApp().globalData.urlhead+'/dcapi/getfoodlistbyrandom',
      method: 'POST',
      data: {
        
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded' // 默认值
      },
      dataType: 'json',
      success(cc) {
        console.log(cc.data[0].foodlist);
        that.setData({
          foodlist:cc.data[0].foodlist ,//把后端查询出来的菜品列表信息存放到foodlist数组中
          pptlist:cc.data[0].pptlist,
          chushilist:cc.data[0].chushilist
        });
      }
    });
  },
  
  fngotofoodview5:function(e){
    console.log(e.currentTarget.dataset.foodname);
    var id=23
      wx.navigateTo({
        url: '/pages/foodview/foodview?id='+id,
      });
  },

  fngotofoodview4:function(e){
    console.log(e.currentTarget.dataset.foodname);
    var id=24
      wx.navigateTo({
        url: '/pages/foodview/foodview?id='+id,
      });
  },
  fngotofoodview3:function(e){
    console.log(e.currentTarget.dataset.foodname);
    var id=22
      wx.navigateTo({
        url: '/pages/foodview/foodview?id='+id,
      });
  },
  fngotofoodview2:function(e){
    console.log(e.currentTarget.dataset.foodname);
    var id=15
      wx.navigateTo({
        url: '/pages/foodview/foodview?id='+id,
      });
  },
  fngotofoodview:function(e){
    console.log(e.currentTarget.dataset.foodname);
    
      wx.navigateTo({
        url: '/pages/foodview/foodview?id='+e.currentTarget.dataset.id,
      });
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function () {
    if (getApp().globalData.userInfo) {
      this.setData({
        userInfo: getApp().globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse){
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      getApp().userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          getApp().globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },
  getUserInfo: function(e) {
    console.log(e)
    getApp().globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  }
})
