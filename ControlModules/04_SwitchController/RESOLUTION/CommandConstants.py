import json

def GetActionName(key):
	with open('ActionsConfig.json') as json_data_file:
		data = json.load(json_data_file)
		if key in data:
			return data[key]['functionName']
		return None
		
def GetGpioPort(key):
	with open('GpioConfigs.json') as json_data_file:
		data = json.load(json_data_file)
		if key in data:
			return data[key]['gpioPort']		
		return None