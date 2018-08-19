var viewModel;

var socket = io.connect('http://localhost:8888', { 'forceNew': true });

socket.on('teams', (teams) =>{
  console.log(teams);
  BuildViewModel(teams);
})

//-------------------Building--------------------
function BuildViewModel(teams)
{
  var teamsmodels = []
  teams.forEach(function(team) {
    if(team[0] == undefined) {return}
    var gpios = [];
    team.forEach(function(gpio) {
      var gpioViewModel = BuildGpio(gpio);
      if(gpioViewModel != null){
        gpios.push(gpioViewModel);
      }
    });
    teamsmodels.push(new TeamViewModel(team[0][0], gpios));
  });
  viewModel.Teams(teamsmodels);
}

function BuildGpio(gpio)
{
  var gpioNumber = gpio[1];
  if(gpioNumber == 6 || gpioNumber == 13 || gpioNumber == 19 || gpioNumber == 26 ) return null;

  var team = gpio[0];
  var gpioState = gpio[2];
  return new TeamGpioViewModel(team, gpioNumber, gpioState);
}

//--------------------ViewModels-----------------
var TeamGpioViewModel = function(teamId, gpioNumber, gpioValue){
  var self = this;
  self.TeamId = ko.observable(teamId);
  self.GpioNumber = ko.observable(gpioNumber);
  self.GpioValue = ko.observable(gpioValue);
  self.StyleClass = ko.computed(function(){
    var className = "";
    switch(gpioNumber){
      case 20: //RELAY 1
      case 21: //RELAY 2
        className = gpioValue == 0 ? 'fas fa-toggle-on' : 'fas fa-toggle-off';
      break;
      case 17: //MOVE
        className = gpioValue == 0 ?  'fas fa-male' : 'fas fa-walking';
      break;
      case 14: //LED
        className = gpioValue == 0 ?  'far fa-lightbulb' : 'fas fa-lightbulb';
        break;
      case 5:  //SERVO
        className = 'fab fa-hornbill';
      break;
    }
    return className;
    });
    self.ContainerClass = ko.computed(function(){
      var className = "";
      switch(gpioNumber){
        case 20: //RELAY 1
        case 21: //RELAY 2
          className = gpioValue == 0 ? 'greenContainer btn-outline-success' : 'redContainer btn-outline-danger';
        break;
        case 17: //MOVE
          className = gpioValue == 0 ?  'redContainer  btn-outline-danger' : 'greenContainer btn-outline-success';
        break;
        case 14: //LED
          className = gpioValue == 0 ?  'redContainer  btn-outline-danger' : 'greenContainer btn-outline-success';
        case 5: //SERVO
          className = gpioValue == 0 ?  'redContainer  btn-outline-danger' : 'greenContainer btn-outline-success';
        break;
      }
      return className;
      });
}

var TeamViewModel = function(teamId, gpios)
{
  var self = this;
  self.Id = ko.observable(teamId);
  self.Gpios = ko.observableArray(gpios);
}

var ViewModel = function(teams)
{
  var self = this;
  self.Teams = ko.observableArray(teams);
}

$(() => {
  
  //General Viewmodel
  viewModel = new ViewModel([]);
  ko.applyBindings(viewModel);
});