import requests
from django.shortcuts import render

def index(request):
	url = 'https://openexchangerates.org/api/latest.json?app_id=08282bcf2e894509a5a4faa5a46b4838'

	r = requests.get(url.format()).json()

	conversion = {
		'mkd': r['rates']['MKD'],
		'rsd': r['rates']['RSD'],
	}
	# Optional: This line prints the value in the terminal console
	# print(conversion) 
	
	data = {'conversion': conversion}
	return render(request, 'currency/index.html', data)
