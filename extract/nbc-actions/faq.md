# FAQ - GitHub Actions

Cette FAQ a pour but de répondre aux questions fréquentes afin d'aider les développeurs à mieux comprendre et utiliser GitHub Actions dans leurs projets.

---

## 1. Qu'est-ce que GitHub Actions ?

GitHub Actions est une plateforme d'intégration continue et de déploiement continu (CI/CD) intégrée à GitHub. Elle permet d'automatiser divers workflows tels que les tests, les builds et les déploiements directement depuis le dépôt.

---

## 2. Comment configurer un workflow avec GitHub Actions ?

Pour configurer un workflow, créez un fichier YAML dans le répertoire `.github/workflows` de votre dépôt. Par exemple :

```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout du code
        uses: actions/checkout@v2

      - name: Installer les dépendances
        run: npm install

      - name: Lancer les tests
        run: npm test
```

---

## 3. Comment utiliser des secrets dans mes workflows ?

Les secrets permettent de stocker des informations sensibles (comme des tokens ou clés API). Vous pouvez les configurer dans les paramètres de votre dépôt sur GitHub, puis y accéder dans votre workflow via `secrets.NOM_DU_SECRET` :

```yaml
- name: Utiliser un token secret
  run: echo "Le token est ${{ secrets.MY_SECRET_TOKEN }}"
```

---

## 4. Comment déboguer un workflow qui échoue ?

Pour déboguer un workflow, vous pouvez :
- Consulter les logs détaillés de l'exécution dans GitHub Actions.
- Ajouter des étapes de débogage (par exemple, des commandes `echo` pour afficher l'état de variables).
- Reproduire le workflow localement avec des outils comme [act](https://github.com/nektos/act).

---

## 5. Quelles sont les bonnes pratiques pour sécuriser mes workflows ?

Quelques bonnes pratiques incluent :
- **Limiter les permissions** : Utiliser le principe du moindre privilège pour le token GitHub.
- **Utiliser des secrets** : Stocker les informations sensibles dans les [secrets GitHub](https://docs.github.com/en/actions/security-guides/encrypted-secrets).
- **Vérifier les inputs** : Valider les entrées et le contexte des actions pour éviter toute exécution non souhaitée.
- **Mettre à jour régulièrement** : Garder les actions tierces à jour afin de bénéficier des dernières corrections de sécurité.

---

## 6. Puis-je utiliser GitHub Actions pour déployer mon application ?

Oui, GitHub Actions peut être utilisé pour automatiser le déploiement. Vous pouvez configurer des workflows spécifiques qui déploient votre application sur des environnements tels que AWS, Azure, ou GCP, en utilisant des actions dédiées ou vos propres scripts de déploiement.

---

## 7. Contact et support

Pour toute question ou assistance supplémentaire, veuillez contacter notre support technique :

- **Email** : support@example.com
- **Téléphone** : +33 1 23 45 67 89
- **Slack** : [Rejoignez notre canal Slack](https://example.slack.com)

---

## 8. Documentation complémentaire

Pour en savoir plus, consultez les ressources suivantes :

- [Documentation GitHub Actions officielle](https://docs.github.com/en/actions)
- [Guide de démarrage rapide](https://docs.github.com/en/actions/quickstart)
- [Blog GitHub Actions](https://github.blog/changelog/)

Cette FAQ est conçue pour être un point de départ. N'hésitez pas à l'enrichir au fil du temps selon l'évolution de vos besoins et des retours utilisateurs.