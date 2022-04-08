const BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/static/'
    : 'http://localhost:8080/',
  outputDir: './dist/',
  transpileDependencies: ['vuetify'],

  // css: { extract: false },

  chainWebpack: config => {
    config.optimization
      .splitChunks(false)

    config
      .plugin('BundleTracker')
      .use(BundleTracker, [{ filename: '../frontend/webpack-stats.json' }])

    config
      .plugin('define')
      .tap(args => {
        let v = JSON.stringify(require('./package.json').version)
        args[0]['process.env']['VERSION'] = v
        return args
      })

    config.resolve.alias
      .set('__STATIC__', 'static')

    config.devServer
      .historyApiFallback(true)
      .public('http://localhost:8080')
      .host('localhost')
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .headers({ 'Access-Control-Allow-Origin': ['\*'] })
  }
}
