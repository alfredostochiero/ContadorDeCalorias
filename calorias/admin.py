from django.contrib import admin
from . models import Food, Consume,Goal
# Register your models here.

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name','carbs','protein','fats','calories')

@admin.register(Consume)
class ConsumeAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('user','calorie_goal')


