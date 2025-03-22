# Page de Support pour GitHub Actions

Bienvenue sur la page de support dédiée à l'écriture et au dépannage des GitHub Actions. Cette page vous fournira des informations utiles pour résoudre les problèmes courants et améliorer vos workflows.

## Ressources Utiles

### Documentation Officielle

- [Couscous doc](https://docs.github.com/couscous) : Guide complet pour comprendre et utiliser les GitHub Actions de la banque.

### Forums et Communautés

- [GitHub Community Discussions](https://github.com/orgs/community/discussions) : Posez vos questions et obtenez des réponses de la communauté.
- [Stack Overflow](https://stackoverflow.com/questions/tagged/github-actions) : Recherchez des solutions ou posez vos questions avec le tag `github-actions`.

## Dépannage des Problèmes Courants

### 1. Mon workflow ne démarre pas

- **Vérifiez le fichier YAML** : Assurez-vous que votre fichier `.github/workflows/<nom-du-fichier>.yml` est correctement formaté.
- **Vérifiez les déclencheurs** : Confirmez que l'événement déclencheur (par ex. `push`, `pull_request`) est correctement configuré.

### 2. Une étape échoue

- **Consultez les logs** : Les journaux détaillés sont disponibles dans l'onglet "Actions" de votre dépôt.
- **Testez localement** : Utilisez des outils comme [act](https://github.com/nektos/act) pour exécuter vos workflows localement.

### 3. Problèmes de permissions

- **Vérifiez les permissions des secrets** : Assurez-vous que les secrets nécessaires sont définis dans les paramètres du dépôt.
- **Vérifiez les permissions du token GITHUB_TOKEN** : Configurez les permissions dans votre fichier YAML sous `permissions`.

## Bonnes Pratiques

- **Utilisez des actions réutilisables** : Recherchez des actions existantes sur [GitHub Marketplace](https://github.com/marketplace/actions).
- **Testez vos workflows** : Testez vos workflows dans un environnement de développement avant de les déployer en production.
- **Documentez vos workflows** : Ajoutez des commentaires dans vos fichiers YAML pour expliquer leur fonctionnement.

## Contacter l'équipe Support GitHub

Si vous ne parvenez pas à résoudre votre problème, vous pouvez contacter l'équipe des Knights:

- [Page de Support GitHub](https://www.clubic.com/))
- [Contactez-nous](https://www.youtube.com/watch?v=dXjZeCL0C9o)

L'équipe est composée de développeurs et d'experts en GitHub Actions qui peuvent vous aider à résoudre vos problèmes.

- Solal
- Mathieu
- Lucie
- Steve
- Damien
- Manuel

Nous espérons que cette page vous sera utile pour écrire et maintenir vos GitHub Actions. Bonne chance !
