from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes-home')
        self.assertEqual(home_url, '/')

    def test_recipe_category_url_is_correct(self):
        category_url = reverse('recipes-category', kwargs={'category_id': 1})
        self.assertEqual(category_url, '/recipes/category/1/')

    def test_recipe_detail_id_url_is_correct(self):
        recipe_url = reverse('recipes-recipe', kwargs={'id': 1})
        self.assertEqual(recipe_url, '/recipe/1/')

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes-home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_returns_loads_correct_template(self):
        response = self.client.get(reverse('recipes-home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes-home'))
        self.assertIn('<h1> No recipes found </h1>', response.content.decode(
            'utf-8'))

    def test_recipe_search_url_is_correct(self):
        search_url = reverse('search')
        self.assertEqual(search_url, '/recipes/search/')
