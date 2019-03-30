// pages/service/service.js

const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    isConstellationView: false,
    isJokeView: false,
    constellationData: null,
    jokeData: null
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var isConstellationViewTmp = false
    var isJokeViewTmp = false
    if (options.type == 'constellation') {
      isConstellationViewTmp = true
      this.updateConstellationData()
    } else if (options.type == 'joke') {
      isJokeViewTmp = true
      this.updateJokeData()
    }
    this.setData({
      isConstellationView: isConstellationViewTmp,
      isJokeView: isJokeViewTmp
    })

  },

  updateConstellationData: function () {
    var that = this
    wx.showLoading({
      title: '加载中',
    })
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/constellation',
      success: function (res) {
        that.setData({
          constellationData: res.data.data
        })
        wx.hideLoading()
      }
    })
  },

  updateJokeData: function () {
    var that = this
    wx.showLoading({
      title: '加载中',
    })
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/joke',
      success: function (res) {
        that.setData({
          jokeData: res.data.data
        })
        wx.hideLoading()
      }
    })
  },
})