# lonelypages
Script per l'inserimento del template {{O}}, attualmente utilizzato su lmo.wikipedia, che non utilizza la pagina speciale LonelyPages.

## Cosa serve...
- PyWikiBot
- Account con permesso di bot

## Come funziona...
- Prelevamento della lista  di tutte le voci in NS0
- Verifica su ogni voce in NS0 dei link entranti
- Apposizione del template O su tutte le voci che:
- - Non hanno link entranti o hanno link entranti solo da NS diversi da zero
  - Non hanno già il template O
  - Non sono protette (in tal caso il bot non può modificarle)
 
## Parametri
- start: voce da cui iniziare

## Da aggiungere
- [ ] Selettore del sito da controllare e configurazione multiedizione (come su lonelypages.py integrato in PWB)
- [ ] Possibilità di scaricare e usare una lista di voci, per ridurre l'onere sul server
- [ ] Utilizzo di espressioni regolari per identificare la presenza del template O
- [ ] Riconoscimento delle voci con link che provengono solo da anni, giorni o template disambiguanti
