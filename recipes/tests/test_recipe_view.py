from django.forms import CharField
from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Category, Recipe, User


class RecipeviewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        home_view = resolve(reverse('recipes-home'))
        self.assertIs(home_view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        category_view = resolve(reverse('recipes-category', kwargs={'category_id': 1}))
        self.assertIs(category_view.func, views.category)

    def test_recipe_detail_views_function_is_correct(self):
        detail_view = resolve(reverse('recipe-recipe', kwargs={'id': 1}))
        self.assertIs(detail_view.func, views.recipe)

    def test_recipe_home_tamplate_loads_recipes(self):
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='user@email.com',
        )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparantion_time=10, 
            preparantion_time_unit='Minutos',
            servings=5,
            servings_unit='Porcoes',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            is_published=True,
        )
        response = self.client.get(reverse('recipes-home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        self.assertIn('Recipe Title', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porcoes', content)
        self.assertEqual(len(response_context_recipes), 1)
        pass

    def test_recipe_category_view_returns_404_in_no_recipes_found(self):
        response = self.client.get(reverse('recipes-category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_returns_404_in_no_recipes_found(self):
        response = self.client.get(reverse('recipe-recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes-home'))
        self.assertIn(
            '<h1> No recipes found </h1>',
            response.content.decode('utf-8')
        )
