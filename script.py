import pywikibot, time

def get_lombard_articles():
    site = pywikibot.Site("lmo", "wikipedia")
    print("Scaricando elenco pagine")
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
    time.sleep(3)
    if '{{O' not in text:
        text = '{{O|date={{subst:CURRENTMONTHNAME}} {{subst:CURRENTYEAR}}}}\n'+text
        article.text = text
        article.save(summary='Sgiontad el template "O"')
        print(f"Aggiunto template 'O' alla pagina: {article.title()}")

def main():
    lombard_articles = get_lombard_articles()
    print("Inizio della verifica")
    for article in lombard_articles:
        print(f"Verificando la pagina: {article}")
        if check_links(article):
            add_template(article)

if __name__ == "__main__":
    main()
#################


