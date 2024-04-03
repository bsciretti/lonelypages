import pywikibot
import argparse
import time

def get_lombard_articles(start_page=None):
    """
    Ottiene un elenco di pagine in lingua lombarda su Wikipedia.
    Se specificato, inizia dalla pagina specificata, altrimenti recupera tutte le pagine.
    """
    site = pywikibot.Site("lmo", "wikipedia")
    print("Scaricando elenco pagine...")
    all_pages = list(site.allpages(namespace=0, filterredir=False))
    if start_page:
        # Trova l'indice della pagina specificata
        index = next((i for i, page in enumerate(all_pages) if page.title() == start_page), None)
        if index is not None:
            # Filtra l'elenco mantenendo solo le pagine successive
            all_pages = all_pages[index:]
    return all_pages

        
def check_links(article):
    if article.isRedirectPage() or article.isDisambig():
        return False
    time.sleep(3)
    references = article.getReferences()
    #print(references)
    for reference in references:
        #print(reference)
        if reference.namespace() == 0:
            return False
    return True

def add_template(article):
    text = article.text
    if '{{O' not in text:
        text = '{{O|date={{subst:CURRENTMONTHNAME}} {{subst:CURRENTYEAR}}}}\n'+text
        article.text = text
        try:
            article.save(summary='Sgiontad el template "O"')
            print(f"Aggiunto template 'O' alla pagina: {article.title()}")
        except pywikibot.exceptions.Error as e:
            print(f"Errore durante il salvataggio della pagina '{article.title()}': {e}")

def main():
    parser = argparse.ArgumentParser(description="Script per aggiungere il template 'O' a Wikipedia in lombardo.")
    parser.add_argument("-start", nargs="?", help="Titolo della pagina da cui iniziare il controllo.", dest="start_page")
    args = parser.parse_args()

    lombard_articles = get_lombard_articles(args.start_page)
    print("Inizio della verifica...")
    for article in lombard_articles:
        print(f"Verificando la pagina: {article.title()}")
        if check_links(article):
            add_template(article)

if __name__ == "__main__":
    main()
