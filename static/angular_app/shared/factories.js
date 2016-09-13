/**
 __author__ = 'mateuszdargacz@gmail.com'
 __date__ = '6/11/16 / 12:13 PM'
 __git__ = 'https://github.com/mateuszdargacz'
 */

Kajax
    .factory('sliderFactory', ['$rootScope', '$http', '$q', function ($rootScope, $http, $q) {
        var deferred = $q.defer();

        $http.get('/api/slides/').success(function (data) {
            deferred.resolve(data);
        });

        return deferred.promise;
    }])
    .factory('ServicesFactory', ['$rootScope', '$http', '$q', function ($rootScope, $http, $q) {
        var deferred = $q.defer();

        $http.get('/api/services/').success(function (data) {
            deferred.resolve(data);
        });

        return deferred.promise;
    }])
    .factory('ProjectsFactory', ['$rootScope', '$http', '$q', function ($rootScope, $http, $q) {
        var deferred = $q.defer();

        $http.get('/api/projects/').success(function (data) {
            deferred.resolve(data);
        });

        return deferred.promise;
    }])
    .factory('ClientsFactory', ['$rootScope', '$http', '$q', function ($rootScope, $http, $q) {
        var deferred = $q.defer();

        $http.get('/api/clients/').success(function (data) {
            deferred.resolve(data);
        });

        return deferred.promise;
    }]);
