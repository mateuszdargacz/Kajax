Kajax.controller("mainCtrl", function ($scope, $cookies, $timeout, InitiateJS, sliderFactory, ServicesFactory,
                                       ProjectsFactory, ClientsFactory) {
    $scope.test = $cookies['csrftoken'];
    sliderFactory.then(function (data) {
        $scope.slider = data[0];
        ServicesFactory.then(function (data) {
            $scope.services = data;
            ProjectsFactory.then(function (data) {
                $scope.projects = data;
                ClientsFactory.then(function (data) {
                    $scope.clients = data;
                    console.log($scope.clients);
                    $timeout(InitiateJS.init, 2000)
                });
            });
        });

    });
}); 
