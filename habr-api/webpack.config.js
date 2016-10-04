var webpack = require("webpack");
var autoprefixer = require('autoprefixer');
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var CopyWebpackPlugin = require('copy-webpack-plugin');


module.exports = {
    context: __dirname + "/static/src/",
    entry: './index.js',
    output: {
        path: __dirname + "/static/build/",
        filename: "js/build.js"
    },
    module: {
        loaders: [
            {
              test: /\.(jpg|png|ico|gif|tif|svg)$/,
              loader: 'url?name=img/[hash].[name].[ext]&limit=50000'
            },
            {
              test: /\.(woff|woff2|eot|ttf)$/,
              loader: 'url?name=fonts/[hash].[name].[ext]'
            },
            {
                test: /\.(scss|css)$/,
                loader: ExtractTextPlugin.extract("style", "css!postcss!sass")
            }
        ]
    },
    postcss: function () {
        return [autoprefixer];
    },

    plugins: [
        new webpack.NoErrorsPlugin(),
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery",
            "window.jQuery": "jquery",
            Cookies: "js-cookie"

        }),
        new webpack.optimize.UglifyJsPlugin({
            compress: {warnings: false}
        }),
        new ExtractTextPlugin('css/build.css', {allChunks: true}),
        new CopyWebpackPlugin([
            {from: 'img/', to: 'img/'}
        ])
    ]
};
