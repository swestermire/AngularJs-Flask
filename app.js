// NEED TO LEARN
// need to learn custom filer fields
// Creating AngularJS Service Facotories (or just Factories)
// Routing through AngularJS
// Provider function.... seems kindof similar to Factor Services?
//.constant for defining constants in angular js
// directive isolates (scope params) so that directives are not dependent on controller '=' and '@' binding
// goal is make directive less coupled/more independent from the controller
// Bundling behavior on a directive by specifying controller: 

// Partially Implemented
// ng-show, ng-hide (button doesn't work to change show to hide), ng-if
// custom directives (Directive Definition Object or DDO property) (couldn't get url templates, ex: template.html, to work)

// ALREADY IMPLEMENTED
// AngularJS Services
// AngularJS Provided Filters
// 2-way and 1-way binding
// implementing multiple controllers
// integrating some css into webapp
// Asynchronous Function - Promises
// $http services - gathering data from Heroku released app/database
console.log("app.js file initiated...")
(function(){
  var angJSAppMod = angular.module("AngJSApp-Learning", []);
  
  angJSAppMod.controller('ngrepeatctrl', ngrepeatctrl);
  angJSAppMod.controller('searchBarCtrl', searchBarCtrl);
  angJSAppMod.controller('ngHideShowCtrl' , ngHideShowCtrl);
  angJSAppMod.controller('userShoppingListCtrl' , userShoppingListCtrl);
  angJSAppMod.controller('masterListCtrl' , masterListCtrl).service('customService' , customService);
  angJSAppMod.controller('asyncCtrl' , asyncCtrl).service('menuItemsService' , menuItemsService).service('healthyService', healthyService)
  angJSAppMod.controller('menuCategoriesCtrl' , menuCategoriesCtrl).service('menuCategoryService', menuCategoryService)
  angJSAppMod.controller('customDirectiveCtrl' , customDirectiveCtrl).directive('customDirective', customDirective).directive('templateUrlDirective' , templateUrlDirective)         
  
  angJSAppMod.controller('codepenAngJSctrl', function($scope){
    $scope.title = "AngularJS Demo"
    $scope.outputTitle = "Simple 2-way Binding using ng-model"
    $scope.name = "AngularJS $scope.name default";
    $scope.outputDescrip = "Simple usage of 2-way binding involves ng-model" + "that hooks up DOM functionality according to AngularJS's framework. An on-blur eventhandler was also added through angularJS by "
    $scope.clear = function(){
      $scope.name = "Clear Function was Executed!"
    };
    
  })
  
  ngrepeatctrl.$inject = [$scope, $filter];
  function ngrepeatctrl($scope, $filter){
    $scope.title = "ng-repeat Using angularJS";
    $scope.outputDescrip = "Simple usage of ng-repeat to traverse and output" + " elements from an $scope defined array in angularJS.  Also includes basic filtering."
    $scope.array = ['hello' , 'my' , 'name' , 'is', 'Blah'];
  }

  searchBarCtrl.$inject($scope, $filter);
  function searchBarCtrl($scope, $filter){
    $scope.title = "ng-repeat and 2-way binding for serach functionality through an array with display";
    // $scope.search = " ";
    $scope.array = ['fruit rollups', 
                    'fruit cupcake' , 
                    'cheesecake cupcake', 
                    'New York Cheesecake', 
                    'Cheese Whiz'];
  }
  
  $("#ex-btn").click(function(){
    console.log("jquery button is being clicked")
    $("#ex-btn-output").text = "Button was clicked";
  })

  customServiceCtrl.$inject($scope, "customService");
  function masterListCtrl($scope, customService){
    $scope.title = "Experimenting with AngJS Services - Master List"

    $scope.shoppingList = customService.getItems();
    
    $scope.addItem = function(){
      customService.addItem($scope.newItemName, 
                            $scope.newItemPrice, 
                            $scope.newItemQuantAvail);

      $scope.clearFields(["newItemName", "newItemPrice", "newItemQuantAvail"])
    }

    $scope.clearFields = function(attr_array){
      for (attr in attr_array){
        $scope.attr = "";
      }
    }
  };

  userShoppingListCtrl.$inject($scope, 'customService');
  function userShoppingListCtrl($scope, customService){
    $scope.title = "Experimenting with AngJS Services - Master List"
    $scope.shoppingList = customService.getItems();
  };
  
  // services are singletons meaning that each dependent component gets a reference
  // to the same instance.  Multiple controllers injected with a Service will all 
  // have access to the service instance (i.e. same data)
  function customService(){
      var service = this;
      var items = [];

      service.addItem = function(itemName, price, quantity){
        var item = {
          name: itemName,
          price: price,
          qtyAvail: quantity
        }

        items.push(item);
      }

      service.getItems = function(){
        return items;
      }
  };


ngHideShowCtrl.$inject($scope);
function ngHideShowCtrl($scope){
  $scope.title = "ng-Hide and ng-Show Demonstration";
  $scope.boolVal = false;

  $scope.changeBool = function(){
    if ($scope.boolVal){
      $scope.boolVal = false;
      console.log("Boolean Value is False")
    } else {
      $scope.boolVal = true;
      console.log("Boolean Value True")
    }
  };
}

asyncCtrl.$inject($scope, "menuItemsService")
function asyncCtrl($scope, menuItemsService){
  $scope.title = "Examples of Asynchronous Functions"

  $scope.addItems = function(){
    menuItemsService.addItem($scope.itemName, 
                             $scope.itemPrice,
                             $scope.itemCal,
                             $scope.itemFat)
  }

  $scope.menuItems = menuItemsService.getItems();
  
}

menuItemService('$q' , 'healthyService')
function menuItemsService($q, healthyService){
  var service = this;
  var menuItems = [];

  service.addItem = function(name, price, calories, fat){
    // cleanest approach for using promise services... a way to
    // implement asycnhronous functions
    var promiseCal = healthyService.checkCal(calories);
    var promiseFat = healthyService.checkFat(fat);

    // $q resolves all the promises into one statement..
    // only if all promises are execture successfully... aka not defer.reject are returned
    // then the function executes
    $q.all([promiseCal, promiseFat]).then(function(reponse){
      var item = {
        name: name,
        price: price,
        cal: calories,
        fat: fat
      }

      menuItems.push(item)
    
    })

      .catch(function(response){
        var item = {
          name: name + " - Unhealthy",
          price: price,
          cal: calories,
          fat: fat
        }

      menuItems.push(item)
      
      })
    }
  

  service.getItems = function(){
    console.log('Menu Items provided by service updated')
    return menuItems
  }
}

healthyService.$inject('$q' , '$timeout')
function healthyService($q, $timeout){
  var service = this;

  service.checkCal = function(input){
    var deferred = $q.defer();
    var result = {
      message:""
    }
    
    $timeout(function(){

      if (input <= 1000){
      deferred.resolve(result)
    } else {
      result.message = "High Calorie Menu Item";
      deferred.reject(result)
    }

    }, 2000);

    return deferred.promise 
  }

  service.checkFat = function(input){
    var deferred = $q.defer();
    var result = {
      message: ""
    }

    $timeout(function(){
      if (input <= 50){
        deferred.resolve(result)
      } else {
        result.message = "High Fat Menu Item"
        deferred.reject(result)
      }
    }, 1000);

    return deferred.promise
  }
}

menuCategoriesCtrl.$inject = [$scope, "menuCategoryService"];
function menuCategoriesCtrl($scope, menuCategoryService){
  $scope.title = "Calling Data from Heroku-Based Database using AngularJS HttpGet Requests"
  
  var menu = this;
  var promise = menuCategoryService.getMenuCategories();

  promise.then(function(response) {
    $scope.categories = response.data;
  })
  .catch(function(error){
    console.log("Something went wrong!")
  })
}

// menuCategoryService.$inject = ['$http'] ????
menuCategoryService.$inject = ['$http']
function menuCategoryService($http){
  var service = this;

  service.getMenuCategories = function(){
    console.log('http "get" request sent using AngJS Service')
    var response = $http({
      method: "GET",
      url: ("http://davids-restaurant.herokuapp.com/categories.json")
    })

    return response
  }
};

customDirective.$inject = [$scope, "customDirective", 'templateUrlDirective']
function customDirectiveCtrl($scope, customDirective, templateUrlDirective){

}


function customDirective(){
  var ddo = {
    // template is a built-in attribute for custom directives
    template: "This is a DDO output using custom directives and attribute restrictions",
    // A - attribute, E - Element, AE - Both Element and Attribute
    restrict: 'A' 
  };

  return ddo;
}

function templateUrlDirective(){
  return {
    // Trying to pull html data from a saved template... not able to find html file?
    templateUrl: 'Users/randomTemplate.html',
    restrict: 'E'
  };

}

})()
