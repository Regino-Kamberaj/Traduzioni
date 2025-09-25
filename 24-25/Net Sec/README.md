# Capture the Contrabbandiero 
---

## Introduction
---
Capture the Contrabbandiero is our ctf challenge!

Inside our container we builded a simple website where there is a database of workers.

Inside this site we have put two flags. 
The difficulties of those flags are respectively easy and medium where:
- The first one is a simple ascii art.
- The second one is an invitation to join in our crew. :) 

So try to capture them all!

## Instructions
---
- Firstly pull the container
```
docker pull alonzobazaar/unsafe
```

- Then to run the container, put the following command (on mac try on port 5001:5000)
```
docker run -d -p 5000:5000 alonzobazaar/unsafe
```

- Open your browser and go to
```
http://localhost:5000/
```

- From there, you're on your own!

## Hints
---
- To find the first flag, the most basic one, is not necessary to log in.
	- So think about any file that is present in almost all sites...

- Meanwhile for the second flag, after you reached to get in... you have to discover a not very obvious table in SQLite.
	- Then from this, try to find out where the secret infomation is!


# Bullet Points Relazione 

## Abstract

Mini introduzione sul CTF e sulla divisione dei compiti da fare ovvero:
	1. Creare un "capture the flag" per i nostri colleghi
	2. Catturare una o più bandiere create dai nostri colleghi
## Prima parte Relazione

In questa prima parte si discute about il container creato
### La scelta delle vulnerabilità

(Qui Deste)
Perchè abbiamo scelto questa vulnerabilità: In quanto la più interessante a nostro avviso fra le vulnerabilità a livello applicazione, inoltre interessante capire come sanitizzare e quali sono le cause di questa vulnerabilità, ovvero come nel caso dell'uso di certe query non riesci a sanitizzare, strumento postgres (?)
e per allungare il brodo si parla di SQL - Injection
### La preparazione del container + metodo che abbiamo visto per la cattura

(Qui Kiro)
In questa parte si discute un attimo della realizzazione del sito, dovuta alla grande idea del maestro Kirollos, in particolare per la scelta dell'uso di flask e la creazione del database tramite python. 

(Qui Kiro+Deste)
Successivamente l'aggiunta delle due flag, con tutta la spiegazione per la prima con la trovata di sql_master e l'idea di aggiungere una tabella nascosta -> sqlinjection per cercare di raggiungere questa.
Mentre per la seconda l'idea di aggiungere qualcosa che avrebbe un pensiero outside of the box.

(Qui Kiro, ma non la vuole mettere dicci te Deste)
Infine tutta la parte del caricamento del container docker su docker hub e in comandi necessari per lanciare il container.

Fine prima parte
## Seconda parte relazione

Nella seconda invece si riparte dal secondo punto dell'abstract ovvero della cattura delle flag. +tentativi mal riusciti

### Cattura prima flag: container di alex white?

### Cattura seconda flag: container spagnolo?

### Cattura terza flag: altri container ??

