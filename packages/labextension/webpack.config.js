var path = require('path');

module.exports = {
    entry: "./src/index.ts",
    output: {
        filename: "index.js",
        path: path.resolve(__dirname, 'dist'),
        libraryTarget: 'commonjs2'
    },
    devtool: 'source-map',
    resolve: {
        // Add '.ts' and '.tsx' as a resolvable extension.
        extensions: [".webpack.js", ".web.js", ".ts", ".tsx", ".js"]
    },
    module: {
        loaders: [
            // all files with a '.ts' or '.tsx' extension will be handled by 'ts-loader'
            { test: /\.tsx?$/, loader: "ts-loader" },
            { test: /\.css$/, use: ['style-loader', 'css-loader']}
        ]
    },
    externals: [
        '@jupyterlab/rendermime-interfaces',
        '@phosphor/coreutils',
        '@phosphor/widgets'
    ]
}