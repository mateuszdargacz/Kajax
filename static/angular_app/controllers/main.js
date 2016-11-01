Manitou.controller("mainCtrl", function ($scope, $cookies, $timeout, sliderFactory, LifterFactory) {
    $scope.test = $cookies['csrftoken'];
    sliderFactory.then(function (data) {
        $scope.slider = data[0];
        LifterFactory.then(function (data) {
            $scope.lifters = data;
            if (window.loading_screen !== undefined) window.loading_screen.finish();
            console.log($scope.lifters);
        });
    });
}); 
