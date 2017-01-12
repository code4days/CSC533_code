var app = angular.module('myApp', ['ngMaterial']);

app.controller('alertController', function($scope, $mdDialog) {

    $scope.alert = '';
    $scope.showAlert = function(ev) {
        $mdDialog.show(
            $mdDialog.alert()
                .title('Cybroid')
                .content('Content served from Rasheed-Server v1.0.0')
                .ok('ok')
                .targetEvent(ev)
        );
    };
});