import unittest
import sys
import os

sys.path.append(os.path.dirname(__file__))

from app import app

class TestCounterApp(unittest.TestCase):

    def setUp(self):
        """Préparation de l'application Flask en mode Test"""
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_page_accueil_statut_200(self):
        """Vérifie que le site web répond correctement (Code HTTP 200 = Succès)"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_page_accueil_contenu(self):
        """Vérifie que le texte obligatoire 'Bonjour !' est bien affiché sur la page"""
        response = self.client.get('/')
        self.assertIn(b"Bonjour !", response.data)

if __name__ == '__main__':
    unittest.main()