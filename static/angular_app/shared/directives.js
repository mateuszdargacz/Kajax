Manitou
    .directive('timeAgo', function ($timeout) {
        return {
            restrict: 'A',
            scope: {
                title: '@'
            },
            link: function (scope, elem, attrs) {
                var updateTime = function () {
                    if (attrs.title) {
                        elem.text(moment(attrs.title).fromNow());
                        $timeout(updateTime, 15000);
                    }
                };
                scope.$watch(attrs.title, updateTime);
            }
        };
    })

    .directive('pendingbar', ['$rootScope',
        function ($rootScope) {
            return {
                link: function (scope, element, attrs) {
                    element.addClass('hide');
                    $rootScope.$on('$routeChangeStart', function () {
                        element.removeClass('hide');
                    });
                    $rootScope.$on('$routeChangeSuccess', function () {
                        element.addClass('hide');
                    });
                    $rootScope.$on('$routeChangeError', function () {
                        element.removeClass('hide');
                    });
                }
            };
        }])

    .directive('sliderD', ['$rootScope',
        function ($rootScope) {
            return {
                scope: {slider: '='},
                templateUrl: '/static/angular_app/views/slider.html',
                link: function (scope, element, attrs) {

                }
            };
        }])
    .directive('liftersD', ['$rootScope',
        function ($rootScope) {
            return {
                scope: {lifters: '='},
                templateUrl: '/static/angular_app/views/lifters.html',
                link: function (scope, element, attrs) {
                }
            };
        }])
