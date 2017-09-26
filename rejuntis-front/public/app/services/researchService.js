angular.module('researchServices',[])

.factory('Research',function($http){
    researchFactory = {};

    //User.create(regData)
    researchFactory.create = function(resData){
        return $http.post('api/users',resData);
    }
    return userFactory;
});