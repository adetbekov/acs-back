var utils = require('./utils')
var config = require('../config')
var isProduction = process.env.NODE_ENV === 'production'

module.exports = {
  loaders: Object.assign(
    {
      test: /\.sass$/,
      loaders: ["style", "css", "sass"]
    },
    {
      test: /\.jade$/,
      loaders: ["template", "jade", "html"]
    },
    {
      i18n: '@kazupon/vue-i18n-loader'
    },
    utils.cssLoaders({
      sourceMap: isProduction
        ? config.build.productionSourceMap
        : config.dev.cssSourceMap,
      extract: isProduction
    })
  ),
  transformToRequire: {
    video: 'src',
    source: 'src',
    img: 'src',
    image: 'xlink:href'
  }
}
