# Utilisation des exécuteurs hébergés par la banque (NBC runners)

Il est fortement conseillé d'utiliser les runners hébergés par la banque (nbc-runners)

Vous pouvez utiliser les exécuteurs de la banque pour exécuter vos workflows GitHub Actions.

```yaml
jobs:
  build-and-test:
    runs-on: nbc-runners
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Run tests
        run: |
          python -m unittest discover -s tests
```
