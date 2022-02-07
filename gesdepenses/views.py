from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

from .models import treso, Main, Produit, Charge
from .forms import userForm, prod
# from frozen.models import Boss

# Create your views here.

def seed(request):
	som = treso()
	amount = int(request.GET['seed'])
	if amount:
		print("votre capital est : ", amount)
		treso.objects.create(amount = amount)
		print("amount created successfully")
	else:
		print("vos donnee ne sont pas ici")


	return render(request, "gespro.html", { 'seed': amount})


def home(request):
	dep = Main()
	amount = treso.objects.all()
	if request.user.is_authenticated:
		print("Welcome, you are connected: ", request.user)
	else:
		print("You must first connect")
		return redirect('/connect')

	if amount:
		print("la liste n'est pas vide")
		for element in amount:
			last = element
		dep.amount = last.amount

	else:
		print("la liste est videi")
		seed = False

		return render(request, "gespro.html", { 'seed': seed})

	return render(request, 'gespro.html', { 'dep': dep })

def minus(request):
	Tout = Main()
	seed = get_object_or_404(treso, id = 1)
	charge = int(request.GET['charge'])
	motif_ch = request.GET['motif_charge']

	seed.amount -= charge
	seed.save()

	Charge.objects.create(amount = charge, desc = motif_ch, \
		owner = request.user)

	charges = Charge.objects.all()
	produits = Produit.objects.all()

	Tout.amount = seed.amount
	Tout.depe = charges
	Tout.prod = produits
	Tout.owner = str(request.user)
	return render(request, 'gespro.html', { 'dep': Tout })

def plus(request):
	Tout = Main()
	seed = get_object_or_404(treso, id=1)
	produit = int(request.GET['produit'])
	motif_pr = request.GET['motif_produit']

	seed.amount += produit
	seed.save()

	Produit.objects.create(amount = produit, desc = motif_pr, \
		owner = request.user)

	charges = Charge.objects.all()
	produits = Produit.objects.all()

	Tout.amount = seed.amount
	Tout.depe = charges
	Tout.prod = produits
	Tout.owner = str(request.user)

	return render(request, 'gespro.html', { 'dep':Tout })

def dele(request):
	Tout = Main()
	seed = get_object_or_404(treso, id=1)
	charges = Charge.objects.all()
	produits = Produit.objects.all()
	Tout.amount = seed.amount
	Tout.depe = charges
	Tout.prod = produits

	val = {}
	val = request.GET
	try:
		dep = int(val['dep'])
		obj = get_object_or_404(Charge, id = dep)
		seed.amount += obj.amount
		seed.save()
		obj.delete()
		print("VOTRE charge est bien supprimer: ", obj)
	
	except Exception as e:
		pro = int(val['pro'])
		obj = get_object_or_404(Produit, id = pro) #object selected
		seed.amount -= obj.amount
		seed.save()
		# i can now delete it
		obj.delete()
		print("l'une des vos produits sont selectionnes: ", obj)
	charges = Charge.objects.all()
	produits = Produit.objects.all()
	Tout.amount = seed.amount
	Tout.depe = charges
	Tout.prod = produits

	return render(request, 'gespro.html', { 'dep':Tout })



def auto():
	Tout = Main()
	seed = get_object_or_404(treso, id=1)
	charges = Charge.objects.all()
	produits = Produit.objects.all()
	Tout.amount = seed.amount
	Tout.depe = charges
	Tout.prod = produits

def kwinj(request):
	name = request.GET['izina']
	password = request.GET['password']

	us = User.objects.get(username = name)
	us = authenticate(request, username= name, password= password)

	if us is not None:
		print("Winjiye neza : ", us.username)
		login(request, us)
		return redirect('/')
	else:
		print("Ntiwinjiye")
	return render(request, 'login.html')


def connect(request):
	return render(request, 'login.html')

def entrer(request):
	name = request.GET['izina']
	password = request.GET['password']

	ut = User.objects.get(username = name)
	login(request, ut)
	print("VOUS ETES BIEN CONNECTE : ", ut.username)

	return redirect('/')

def disconnect(request):
	logout(request)
	return redirect('/')

def register(request):
	if request.POST:
		print("Vous avez envoyé donnee")
		izina = request.POST['izina']
		email = request.POST['email']
		password = request.POST['password']

		if not authenticate(username = izina ,password = password):
			User.objects.create_user(username = izina, email= email,
			password = password)
			print("New user : ", izina )
			return redirect('/')
		else:

			print("Vous possediez deja un compte ")
	else:
		print("Vous n'avez pas envoyé donnee")
		return render(request, 'register.html')

	return render(request, 'register.html')