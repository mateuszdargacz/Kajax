
var Kajax = angular.module("Kajax", [], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");


    }
);

Kajax.run(function () {
window.loading_screen.finish();
});