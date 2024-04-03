import pywikibot, time, argparse

def get_lombard_articles():
    site = pywikibot.Site("lmo", "wikipedia")
    print("Scaricando elenco pagine")
    if start_page:
        return [site.page(start_page)]
    else:
        return list(site.allpages(namespace=0, filterredir=False))
        
def check_links(article):
    if article.isRedirectPage() or article.isDisambig():
        return False
    
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
        except pywikibot.exceptions.Error:
            print("Errore, la pagina non può essere modificata")

def main():
    lombard_articles = get_lombard_articles(starting)
    print("Inizio della verifica")
    for article in lombard_articles:
        print(f"Verificando la pagina: {article}")
        time.sleep(3)
        if check_links(article):
            add_template(article)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script per aggiungere il template 'O' a Wikipedia in lombardo.")
    parser.add_argument("-start", nargs="?", help="Titolo della pagina da cui iniziare il controllo.", dest="start_page")
    args = parser.parse_args()

    main()

