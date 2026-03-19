from django.shortcuts import render


def home(request):
	print('home')
	
	context = {
			'text': 'Olá home',
			'title': 'Essa é a uma página de exemplo - ',
		}
	return render(
		request,
		'home/index.html',
		context,
	)