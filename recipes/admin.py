from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import RecipeIngredient, Recipe, RecipeIngredientImage

User = get_user_model()

admin.site.register(RecipeIngredientImage)


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    readonly_fields = ['quantity_as_float', 'as_mks', 'as_imperial', 'timestamp', 'updated']
    fields = ['name', 'description', 'quantity', 'unit', 'directions', 'quantity_as_float',
              'active']  # Exclude 'timestamp' and 'updated'


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]  # Corrected the capitalization to 'inlines'
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']


admin.site.register(Recipe, RecipeAdmin)
