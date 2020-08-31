// pages/foodview/foodview.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    foodprice:'',//菜品的单价
    buynum:1,//订购的数量
    sumprice:'',//总价
    proname:'',
    brief:'',
    descriptions:'',
    imgurl:'',
    tiandianid:''

  },
  fnaddtocar:function(){
    var that=this;
    var userid=wx.getStorageSync('currentuserid');//currentuserid是login.js页面保存的
    if(userid>0)   //判断用户是否登录
    {
      var tiandianid=that.data.tiandianid;
      var proname=that.data.proname;
      var procount=that.data.buynum;
      var imgurl=that.data.imgurl;
      var price=that.data.foodprice;
      wx.request({
        url: getApp().globalData.urlhead+'/dcapi/addtocar',
        method: 'POST',
        data: {
          userid: userid,
          proid:tiandianid,
          proname:proname,
          procount:procount,
          imgurl:imgurl,
          price:price
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded' // 默认值
        },
        dataType: 'json',
        success(cc) {
          console.log(cc.data);
          wx.switchTab({
            url: '/pages/shopcar/shopcar'
          });
        }
      });
    }
    else
    {
      wx.redirectTo({
        url: '/pages/login/login'
      })
    }

  },

  fnjia:function(){
    console.log("1");
    //点击加号按钮的时候，要将购买数量增加1
    var price=this.data.foodprice;/*从当前页面的data对象中把单价取出来*/
    var oldnum=this.data.buynum;/*获取购买的数量*/
    oldnum++; //把原来的数量加1
    var sum = oldnum * price;/*计算总价  总价虽然计算好了，但是并没有应用到data对象上*/
    this.setData({
      buynum: oldnum,
      sumprice:sum
    });
    console.log("2");
},
fnjian:function(){
  var price = this.data.foodprice;
  var oldnum = this.data.buynum;
  if (oldnum>1)
  {
    oldnum--; //把原来的数量减1
    var sum = oldnum * price;
    this.setData({
      buynum: oldnum,
      sumprice: sum
    });
  }    
},

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that=this;
    var id = options.id;   //获取地址上传过来的id
    console.log(id);
    that.setData({
      tiandianid:id
    });
    wx.request({
      url: getApp().globalData.urlhead+'/dcapi/gettiandianbyid',
      method: 'POST',
      data: {
        id: id
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded' // 默认值
      },
      dataType: 'json',
      success(cc) {
        console.log(cc.data);
        that.setData({
          foodprice:cc.data[0].proprice,
          sumprice:cc.data[0].proprice,
          proname: cc.data[0].proname,
          brief: cc.data[0].probrief,
          descriptions: cc.data[0].proaddress,
          imgurl:getApp().globalData.urlhead+"/static/uploadimg/"+cc.data[0].imgurl
        });
      }
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