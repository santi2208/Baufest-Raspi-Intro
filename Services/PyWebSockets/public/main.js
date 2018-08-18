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
      gpios.push(new TeamGpioViewModel(gpio[0],gpio[1],gpio[2]));
    });
    teamsmodels.push(new TeamViewModel(team[0][0], gpios));
  });
  viewModel.Teams(teamsmodels);
}

//--------------------ViewModels-----------------
var TeamGpioViewModel=function(teamId, gpioNumber, gpioValue){
  var self = this;
  self.TeamId = ko.observable(teamId);
  self.GpioNumber = ko.observable(gpioNumber);
  self.GpioValue = ko.observable(gpioValue);
  self.StyleClass = ko.computed(function(){
    var className = "";
    switch(gpioNumber){
      case 20:
      case 21:
        className = gpioValue == 0 ? 'fas fa-toggle-on' : 'fas fa-toggle-off';
      break;
      case 17:
        className = gpioValue == 0 ?  'fas fa-male' : 'fas fa-walking';
      break;
      case 14:
        className = gpioValue == 0 ?  'far fa-lightbulb' : 'fas fa-lightbulb';
      break;
    }
    return className;
    });
    self.ContainerClass = ko.computed(function(){
      var className = "";
      switch(gpioNumber){
        case 20:
        case 21:
          className = gpioValue == 0 ? 'greenContainer btn-outline-success' : 'redContainer btn-outline-danger';
        break;
        case 17:
          className = gpioValue == 0 ?  'redContainer  btn-outline-danger' : 'greenContainer btn-outline-success';
        break;
        case 14:
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