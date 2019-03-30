//app.js
const cookieUtil = require('utils/cookie.js')
//app函数注册全局唯一的函数，智能调用一次，接收一个对象作为函数参数
App({
  //生命周期回调函数onLaunch
  onLaunch: function () {
    // 展示本地存储能力
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
      }
    })
    // 获取用户信息
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: res => {
              // 可以将 res 发送给后台解码出 unionId
              this.globalData.userInfo = res.userInfo

              // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
              // 所以此处加入 callback 以防止这种情况
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(res)
              }
            }
          })
        }
      }
    })
  },
  getAuthStatus: function () {
    return this.globalData.auth.isAuthorized
  },

  setAuthStatus: function (status) {
    console.log('set auth status: ' + status)
    if (status == true || status == false) {
      this.globalData.auth.isAuthorized = status
    } else {
      console.log('invalid status.')
    }

  },
  onShow: function () { },
  onHide: function () { },
  globalData: {
    userInfo: null, //全局数据，保存用户信息
    appId: 'wx813738013585e2d6',
    serverUrl: 'http://127.0.0.1:8000',
    apiVersion: '/api/v1.0',
    auth: {
      isAuthorized: false
    }
  }
})