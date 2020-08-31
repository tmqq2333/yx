// pages/test/test.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    tbname:'风雨欲来风满楼，食客云来香满楼',
    msg:''
  },
  // 当点击test.wxml页面的 点击我 按钮的时候，就触发这个函数执行,在控制台输出123，并将上面的tbname的值改为wangming
  fnclick:function(){
    var that=this;//this在不同的函数中代表不同的含义，我们要想在其他函数中使用此处的this,我们可以定义一个变量that，把当前的this保存起来，然后在其他地方使用。
    console.log("123");
    this.setData({
      tbname:'wangming'
    })

    //用延迟函数去改变data中的值，主要掌握that的使用，延迟5秒
    // setTimeout(function(){
    //   that.setData({
    //     tbname:"王敏"
    //   });
    // },5000);

  },

  fnclick3:function(){

    //1、专门跳转到tabbar定义的页面,tabbar页面就是在app.json里面tabbar对象下写的页面
    // wx.switchTab({
    //   url: '/pages/index/index',
    // });

    //2、关闭原来的页面，打开新的页面
    // wx.redirectTo({
    //   url: '/pages/foodview/foodview',
    // })

     //3、打开新的页面，但是原来的页面并没有关闭
    // wx.navigateTo({
    //   url: '/pages/foodview/foodview',
    // });

     //4、返回上一个页面，通过指定delta的值，可以返回指定的步数。
     wx.navigateBack({
      delta: 1
    });
  },

  fnchange:function(e){
    //通过给input元素添加bindinput事件（文本框里面的值发生改变的时候就会触发），

    //通过事件对象e就能获取到当前文本框里面的值。
    console.log(e);

    //把文本框中的值设置到data对象上。可以供页面上其他地方使用。
    this.setData({
      msg:e.detail.value
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    const appInstance = getApp()
    console.log(appInstance.globalData.username)

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