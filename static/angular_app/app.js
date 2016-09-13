var Kajax = angular.module("Kajax", ['ngCookies'], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");


    }
);

Kajax.run(function () {
    
});
Kajax.config(['$httpProvider', '$cookiesProvider', function ($httpProvider, $cookieStore) {
    $httpProvider.defaults.headers.common['X-CSRFToken'] = $cookieStore.csrftoken;
    console.log($cookieStore)
}]);