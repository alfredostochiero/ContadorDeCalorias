from django.shortcuts import render
from .models import Food, Consume

def index(request):
    user = request.user
    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed) # food object that has the name equal to the one pass with the post method
        # user who is logged in at the moment
        consume =  Consume(user=user, food_consumed=consume)
        consume.save() # save at the database the object consume
        foods = Food.objects.all()

    else :
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=user)
    context = {
        'foods': foods,
        'consumed_food': consumed_food,
        'user':user,
    }
    return render(request, 'calorias/index.html',context)





