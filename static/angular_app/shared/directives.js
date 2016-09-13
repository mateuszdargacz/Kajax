Kajax
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
    .directive('servicesD', ['$rootScope',
        function ($rootScope) {
            return {
                scope: {services: '='},
                templateUrl: '/static/angular_app/views/services.html',
                link: function (scope, element, attrs) {

                }
            };
        }])
    .directive('projectsD', ['$rootScope',
        function ($rootScope) {
            return {
                scope: {projects: '='},
                templateUrl: '/static/angular_app/views/projects.html',
                link: function (scope, element, attrs) {

                }
            };
        }])
    .directive('clientsD', ['$rootScope',
        function ($rootScope) {
            return {
                scope: {clients: '='},
                templateUrl: '/static/angular_app/views/clients.html',
                link: function (scope, element, attrs) {

                }
            };
        }]);