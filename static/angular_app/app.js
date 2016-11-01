var Manitou = angular.module("Manitou", ['ngCookies'], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");


    }
);

Manitou.run(function () {
    
});

Manitou.config(['$httpProvider', '$cookiesProvider', function ($httpProvider, $cookieStore) {
    $httpProvider.defaults.headers.common['X-CSRFToken'] = $cookieStore.csrftoken;
    console.log($cookieStore)
}]);