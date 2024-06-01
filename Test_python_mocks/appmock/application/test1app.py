import time
"""Voici la fonctionrequest()
 qui fait des appels sur des API et qui retourne 10. 
 Dans notre cas, nous allons mettre une pause de 10 secondes 
 pour imiter le temps d’exécution des requêtes :
"""
def request():
    time.sleep(10)
    return 10

"""
Ensuite, nous allons implémenter la fonction qui appelle cette fameuse 
fonction, que nous nommeronsmain_function():
"""
def main_function():
    response = request()
    return response


"""
Voici le test unitaire 
(nous allons considérer que les deux fonctions 
précédentes sont contenues dans un même fichiermain.py) :
"""
def test_main_function(monkeypatch):
 
    def mockreturn():
        return 100
 
    monkeypatch.setattr('request', mockreturn)
 
    expected_value = 100
    assert main_function() == expected_value