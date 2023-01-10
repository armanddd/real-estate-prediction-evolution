# Predict'Immo

> Estimez la valeur de votre bien immobilier

L'application Predict'Immo permet d'estimer très simplement la valeur foncière
d'un bien immobilier en quelques clics !

## Améliorations

La version actuelle de l'application est un prototype initial ayant permis de
mettre en place le squelette général bout en bout:

- Entrainement d'un modèle d'apprentissage machine sur des données historiques
- Sérialisation du modèle
- Intégration du modèle dans une application web avec formulaire

Néanmoins, les premiers essais montrent les faiblesses suivantes :

- La véracité des prédictions est très aléatoire : les appartements semblent être très surévalués par rapport aux maisons, augmenter le nombre de pièces fait diminuer la valorisation
- Certaines prédictions renvoient des valeurs négatives, ce qui est impossible
- L'impossibilité d'obtenir une prédiction localisée : les prédictions se font sur les données globale 2021 du département de l'Isère, et ne sont donc pas assez précises. Idéalement, nous souhaiterions pouvoir saisir une adresse plus ou moins précise et obtenir une estimation ciblée.
