
var Kajax = angular.module("Kajax", ["ngCookies", 'ui.state'], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    alert()

    }
);

Kajax.run(function ($http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
    alert()

});

Kajax.config(function ($routeProvider) {
        alert()
    $routeProvider
        .when("/", {
            templateUrl: "angular_app/views/main.js",
            controller: "mainController"
        })
        .otherwise({
            redirectTo: '/'
        })
});