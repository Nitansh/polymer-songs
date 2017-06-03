"use strict";

var gulp        = require( "gulp" ),
    polylint    = require( "gulp-polylint" ),
    jshint      = require( "gulp-jshint" ),
    exec        = require( "gulp-exec" ),
    argv        = require( "yargs" ).argv,
    vulcanize   = require("gulp-vulcanize"),
    crisper     = require("gulp-crisper"),
    clean       = require("gulp-clean"),
    uglify      = require("gulp-uglify"),
    pump        = require("pump"),
    viewName    = argv.view;  


gulp.task( "polylint", function () {
    return gulp.src( "./components/*/*.js" )
        .pipe( polylint() )
        .pipe( jshint.extract( "auto" ) )
        .pipe( jshint() )
        .pipe( polylint.combineWithJshintResults() )
        .pipe( jshint.reporter( "jshint-stylish" ) );
} );

/*
    clean the directory
*/

gulp.task("clean-build", function () {
    return gulp.src("build", {read: false})
        .pipe(clean());
});

gulp.task("clean-dist", function () {
    return gulp.src(viewName, {read: false})
        .pipe(clean());
});

gulp.task("clean",["clean-dist", "clean-build"]);

/*
    Vulcanize the main view
*/

gulp.task("vulcanize", ["clean"] , function() {
  
    return gulp.src(viewName+".html",{base: "./"})
        .pipe(vulcanize({
            inlineScripts: true,
            inlineCss: true,
            stripComments: true,
        }))
        .pipe(crisper({
            scriptInHead: true
        }))
        .pipe(gulp.dest("build"));
});

/*
    Compress the JS view
*/ 
gulp.task("compress",["vulcanize"], function (cb) {
  pump([
        gulp.src("build/*.js"),
        uglify(),
        gulp.dest(viewName)
    ],
    cb
  );
});

/*
    move the view file to dist folder
*/

gulp.task("move-html", ["vulcanize", "compress" ] ,function(cb) {
    gulp.src("./build/" + viewName + ".html")
        .pipe(gulp.dest(viewName));
});

gulp.task("move-images", ["vulcanize", "compress" ] ,function(cb) {
    gulp.src("src/images/*")
        .pipe(gulp.dest(viewName+"/src/images/"));
});

gulp.task("move", ["move-images", "move-html"]);

/*
    Build command
*/

gulp.task("build", ["clean","vulcanize", "compress"]);

/*
 Shortcut for using WebView Push command.
 Usage: gulp webViewPush --view <view to push to>
 */
gulp.task( "wvp", function () {
    var view          = argv.view,
        command       = "java -jar WebViewSync_3.5.2.jar push -v " + view,
        reportOptions = {
            err: true,    // default = true, false means don"t write err
            stderr: true, // default = true, false means don"t write stderr
            stdout: true  // default = true, false means don"t write stdout
        },
        commandOptions = {
            continueOnError: false,       // default = false, true means don"t emit error event
            pipeStdout: false            // default = false, true means stdout is written to file.contents
        };

    if ( view ) {
        return gulp.src( "./" + view + "/*" )
                   .pipe( exec( command ), commandOptions )
                   .pipe( exec.reporter( reportOptions ) );
    } else {
        console.log( "Please provide the view to push to using --view <view>" );
    }

} );
