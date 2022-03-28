# Databases-advanced
Opdracht Databases Advanced

Voor deze opdracht moesten we een bitcoin data scraper maken. We moesten alle data halen van (https://www.blockchain.com/btc/unconfirmed-transactions) hiervan moesten we de Time, Hash, USD value, BTC value scrapen. Deze data moesten we doorsturen naar redis. In redis moesten we de hoogste 5 eruit halen en deze doorsturen naar mongoDB en daar opslaan.  

Bij mij werkte de code niet die ik schreef voor redis. Ondanks ik de code juist had geschreven kreeg ik de hele tijd onverklaarbare errors. Daarom is het deel van redis er bij mij uitgevallen.

Wat ik heb gedaan is alles gescraped dan de data in een dataframe gestoken, deze gesorteerd op BTC value om dan alleen de 5 grootste door te sturen naar MongoDB. 

Wat heb ik gebruikt om deze opdracht te maken:

- python3 
- beautifulsoup4
- pandas
- regex
- requests
- time
- pymongo

mongoDB runt via docker op localhost:27017
