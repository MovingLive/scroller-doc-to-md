import os
from collections import deque
from urllib.parse import urldefrag, urljoin, urlparse

import html2text
import requests
from bs4 import BeautifulSoup


def normalize_url(url):
    """
    Normalise l'URL en supprimant le fragment et la barre oblique finale.
    """
    url, frag = urldefrag(url)
    if url.endswith("/"):
        url = url[:-1]
    return url


def crawl_and_collect(start_url, file_name_output):
    """
    Parcourt la documentation à partir de l'URL de départ et collecte le contenu Markdown de chaque page.
    """
    visited = set()
    queue = deque()
    queue.append(start_url)
    base_netloc = urlparse(start_url).netloc
    base_path = urlparse(start_url).path

    markdown_contents = []

    while queue:
        url = queue.popleft()
        url = normalize_url(url)
        if url in visited:
            continue
        visited.add(url)
        print(f"Traitement de : {url}")

        try:
            response = requests.get(url)
            if response.status_code != 200:
                continue
            html_content = response.text
            soup = BeautifulSoup(html_content, "html.parser")

            # Extraire le contenu principal
            main_content = soup.find("main", {"id": "article-contents"})
            if main_content is None:
                # Si la structure est différente, utiliser le corps principal
                main_content = soup.find("div", {"class": "markdown-body"})
                if main_content is None:
                    main_content = soup

            # Convertir le contenu principal en Markdown
            html_main_content = str(main_content)
            converter = html2text.HTML2Text()
            converter.ignore_links = False
            markdown = converter.handle(html_main_content)

            # Supprimer tout avant le premier titre de niveau 1
            lines = markdown.split("\n")
            start_index = None
            for i, line in enumerate(lines):
                if line.startswith("# "):
                    start_index = i
                    break
            if start_index is not None:
                markdown = "\n".join(lines[start_index:])
            else:
                # Aucun titre de niveau 1 trouvé, ignorer cette page
                continue

            # Ajouter le contenu Markdown à la liste
            markdown_contents.append(markdown)

            # Trouver tous les liens et les ajouter à la file d'attente
            for link in main_content.find_all("a", href=True):
                href = link["href"]
                next_url = urljoin(url, href)
                parsed_next_url = urlparse(next_url)
                if parsed_next_url.netloc != base_netloc:
                    continue
                next_url = normalize_url(next_url)
                if not parsed_next_url.path.startswith(base_path):
                    continue
                if next_url not in visited:
                    queue.append(next_url)

        except Exception as e:
            print(f"Échec du traitement de {url}: {e}")

    # Écrire tout le contenu Markdown dans un seul fichier
    all_markdown = "\n\n".join(markdown_contents)
    with open(file_name_output, "w", encoding="utf-8") as f:
        f.write(all_markdown)


if __name__ == "__main__":
    # URL de départ (par exemple, la documentation GitHub Copilot)
    START_URL = "https://docs.github.com/fr/copilot"
    FILE_NAME_OUTPUT = "extract/documentation_github_copilot.md"
    crawl_and_collect(START_URL, FILE_NAME_OUTPUT)
