Kajax = angular.module("Kajax", []);
var mainController = Kajax.controller('mainController', function ($scope, $rootScope, $location, GlobalService) {
    var failureCb = function () {
        console.log('YOLOOOO');
    };
    alert()
    $scope.globals = GlobalService;

    $scope.initialize = function (is_authenticated) {
        $scope.globals.is_authenticated = is_authenticated;
    };
})