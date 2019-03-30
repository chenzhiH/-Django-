const key='cookie'
function getSessionIDFromResponse(res){//获取cookie
  var cookie = res.header['Set-Cookie']
  console.log('get cookie:'+cookie)
  return cookie
}

function setCookieToStorage(cookie){
  try{  //存储cookie
    wx.setStorageSync(key, cookie)
  }catch(e){
    console.log(e)
  }
}

function getCookieFromStorage(){  //取出cookie
  var value=wx.getStorageSync(key)
  return value
}

module.exports = { //导出库
  setCookieToStorage: setCookieToStorage,
  getCookieFromStorage: getCookieFromStorage,
  getSessionIDFromResponse: getSessionIDFromResponse
}