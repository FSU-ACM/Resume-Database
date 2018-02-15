const gulp = require('gulp');
const sass = require('gulp-sass');

gulp.task('styles', function () {

    return gulp.src('./webapp/public/sass/*.sass')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('./webapp/public/css'));

});

gulp.task('default', ['styles'])
