from django.shortcuts import render,redirect
from .models import Food, Consume,Goal

def index(request):
    user = request.user

    if request.method == 'POST' and request.POST.get('food_consumed'):
        food_consumed = request.POST.get('food_consumed')
        consume = Food.objects.get(name=food_consumed) # food object that has the name equal to the one pass with the post method
        # user who is logged in at the moment
        consume =  Consume(user=user, food_consumed=consume)
        consume.save() # save at the database the object consume
        foods = Food.objects.all()




    else :
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=user)


    if request.method == 'POST' and request.POST.get('meta_calorica'):
        meta = request.POST.get('meta_calorica')
        meta_calorica = Goal.objects.get(user=user)
        #meta_calorica = Goal(user=user, calorie_goal=meta)
        meta_calorica.calorie_goal = int(meta)
        meta_calorica.save()
        metaCalorica = meta_calorica.calorie_goal

    try :
        meta_calorica = Goal.objects.get(user=user)
        metaCalorica = meta_calorica.calorie_goal
    except Exception :
        metaCalorica = 3000


    # loop itera sobre cada alimento do adicionado pelo usuário e faz um somatorio de cada macronutriente
    calorias,proteinas,gorduras,carboidratos = (0,0,0,0)
    for item in consumed_food:
        calorias += item.food_consumed.calories
        proteinas += item.food_consumed.protein
        gorduras += item.food_consumed.fats
        carboidratos += item.food_consumed.carbs

    #meta_calorias = 2000 # depois ir no model e criar um campo para meta_calorias
    porcentagem_calorias = (calorias/metaCalorica)*100
    if porcentagem_calorias > 100:
        porcentagem_calorias = 100

    macro = proteinas + gorduras + carboidratos
    porce_proteinas = round((proteinas/macro),3) * 100
    porce_gorduras = round((gorduras/macro),3) *100
    porce_carboidratos = round((carboidratos/macro),3) *100



    context = {
        'foods': foods,
        'consumed_food': consumed_food,
        'user':user,
        'calorias': calorias,
        'metaCalorica': metaCalorica,
        'proteinas' :round(proteinas,3),
        'gorduras' : round(gorduras,3),
        'carboidratos' : round(carboidratos,3),
        'porcentagem_calorias':porcentagem_calorias,
        'porce_proteinas' : porce_proteinas,
        'porce_gorduras' : porce_gorduras,
        'porce_carboidratos' : porce_carboidratos,
    }
    return render(request, 'calorias/index.html',context)

def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request,'calorias/delete.html')




