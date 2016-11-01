/**
 __author__ = 'mateuszdargacz@gmail.com'
 __date__ = '6/11/16 / 12:13 PM'
 __git__ = 'https://github.com/mateuszdargacz'
 */

Manitou
    .factory('sliderFactory', ['$rootScope', '$http', '$q', function ($rootScope, $http, $q) {
        var deferred = $q.defer();

        $http.get('/api/slides/').success(function (data) {
            deferred.resolve(data);
        });

        return deferred.promise;
    }])
    .factory('LifterFactory', ['$rootScope', '$http', '$q', function ($rootScope, $http, $q) {
        var deferred = $q.defer();

        $http.get('/api/lifters/').success(function (data) {
            deferred.resolve(data);
        });

        return deferred.promise;
    }]);
    