La data analysis utilizza metodi statistici e visuali per spiegare le correlazioni dei dati. I dati statistici se non usati insieme a quelli visuali potrebbero non fornire una soluzione corretta ed esatta; tramite la visualizzazione si possono osservare cose che le sole statistiche non ci dicono, come in [questo esempio](regio/File/data%20analysis%20example.pdf) (non da sapere).
# Plot
Solitamente i grafici sono utili per mostrare relazioni tra due variabili. Non è solitamente consigliato mostrare relazioni tra più di due variabili; se siamo molto bravi a fare grafici multidimensionali e interattivi allora si può fare, però è difficile.
Un modo per mettere in relazione tre variabili è usare i colori: sulle ascisse e orinate ho due variabili; la terza è espressa nello spazio definito dalle altre due tramite colori.
Le librerie più usate sono:
- Le classiche e quelle su cui si appoggiano le altre sono Pandas, numpy e matplotlib.
- Quelle più moderne sono seaborn, plotly (per grafici interattivi) e vega-altair (più avanzata).
- Le più specifiche per il ML e la XAI sono ydata-profling, FACETS e KNIME.
##### Scatter plot
È usato per mettere in relazione due variabili continue $x$ e $y$ ([grafico](regio/File/scatter%20plot.png)), dove ogni punto sul piano è dato dalla coppia $(x,y)$; se usato per variabili discrete allora vengono delle barre di samples.
Si possono mettere insieme più scatter plot in una [matrice](regio/File/scatter%20plot%20matrix.png) $n\times n$, in modo da avere a vista più coppie di variabili.
È usato per rappresentare pattern o outliers.
##### Bar plot
Mette in relazione la grandezza (quantità, media, varianza) di una variabile rispetto a un insieme di categorie discrete ([grafico](regio/File/bar%20plot.png)).
##### Istogramma
Rappresenta la distribuzione di una variabile continua: sulle ascisse abbiamo i valori delle variabili suddivise in bin, sulle ordinate la densità rispetto a ogni bin.
Usato per comprendere la distribuzione dei samples.
##### Box plot
Sulle ascisse ci sono le categorie discrete e sulle ordinate la distribuzione delle variabili. Il [box](regio/File/box%20plot.png) rappresenta il primo e terzo quartile, con la mediana nel mezzo; i baffi rapprensetano l'estensione della distribuzione; gli outliers sono rappresnetati da pallini esterni ai baffi.
Usato per capire la distribuzione dei samples e rappresentare gli outliers.