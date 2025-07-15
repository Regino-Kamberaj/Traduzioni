# 1^ Settimana

- **Martedì 25 febbraio (2h)**

	Organizzazione del corso. Introduzione. Concetti generali: explainability, interpretability, problema dell'allineamento. Rischi e pericoli nell'uso di modelli opachi di AI. Bias nei dati. Riferimenti legislativi a GDPR e AI Act.
	
	Materiale didattico: slides (00 e 01).

- **Giovedì 27 febbraio (2h)**

	Tassonomia dei modelli di XAI: modelli interpretable-by-design e modelli explainable post-hoc. Trade-off accuracy-explainability. Tipologie di spiegazioni per modelli black-box. Valutazione della explainability. Tecniche e metriche.

	Materiale didattico: slides (01), [sketchbook_20250207](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_02_27.png), sezione 3 articolo [Doshi-Velez & Kim (2017)](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/Doshi-Velez_Evaluation_2017.pdf).

# 2^ Settimana

- **Martedì 4 marzo (2h)**

	Approfondimento sulla valutazione della explainability: incremental feature deletion. Exploratory data analysis: statistiche descrittive, data visualization, tipologie di grafico. Esempi con il dataset Titanic Survival.

	Materiale didattico: slides (01), [sketchbook_20250304](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_03_04.png), [notebook_00_exploratory_data_analysis](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/00_Exploratory_Data_Analysis.ipynb).


- **Giovedì 6 marzo (2h)**

	Bias e fairness. Tipologie di bias: di campionamento, di raprresentazione, di aggregazione, di artifatto. Paradosso di Simpson. Esempi. Definizioni di fairness e metriche per misurarla.

	Materiale didattico: slides (01), [notebook_01_bias_and_fairness](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/01_Bias_and_Fairness.ipynb).
# 3^ Settimana

- **Martedì 11 marzo (2h)**

	Richiami su alberi di decisione: algoritmi greedy, entropia, Gini index. Sistemi basati su regole: decision sets (cenni) e decision lists. Algoritmi per apprendere decision lists: sequential covering.

	Materiale didattico: [MLNR24] sezioni 5.5 e 5.5.2 (sezione 5.5.1 su algoritmo OneR NO) [sketchbook_20250311_1](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_03_11_1.png), [sketchbook_20250311_2](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_03_11_2.png). NOTA: nella nuova versione [MLNR25] disponibile online si tratta della prima parte del capitolo 10.

- **Giovedì 13 marzo (2h)**

	Bayesian rule lists: apprendimento di liste di regole di decisione con statistica Bayesiana. Vantaggi e svantaggi nell'utilizzo di regole decisionali. Cenni all'algoritmo RuleFit.

	Materiale didattico: [MLNR24] sezione 5.5.2, [sketchbook_20250313_1](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_03_13_1.png), [sketchbook_20250313_2](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_03_13_2.png), script [rules_titanic.py](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/rules_titanic.py)e [rules_churn.py](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/rules_churn.py), dataset [bank_consumer_churn.csv](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/bank_customer_churn.csv). NOTA: nella nuova versione [MLNR25] disponibile online si tratta della seconda parte del capitolo 10.
# 4^ Settimana

- **Martedì 18 marzo (2h)**

	Algoritmo RuleFit: modello lineare combinato con regole decisionali. Alberi di decisione ottimali. Algoritmo GOSDT (cenni).

	Materiale didattico: [MLNR24] sezione 5.5.2, [RDN22] note di Cynthia Rudin su alberi di decisione ottimali, sketchbook [20250318_1](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_03_18_1.png), [20250318_2](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_03_18_2.png). Esempio di applicazione dell'algoritmo GOSDT per alberi di decisione ottimi: https://users.cs.duke.edu/~cynthia/CourseNotes/GOSDTComputationExampleWalkthrough.pdf

- **Giovedì 20 marzo (2h)**

	Algoritmo GOSDT per l'apprendimento di alberi ottimi. Introduzione a Generalized Additive Models e Explainable Boosting Machines.

	Materiale didattico: [RDN22] note di Cynthia Rudin su alberi di decisione ottimali, sketchbook [20250320_1](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_03_20_1.png), [20250320_2](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_03_20_2.png).
# 5^ Settimana

- **Martedì 25 marzo (2h)**

	Generative Additive Models e Explainable Boosting Machines. Applicazioni ed esempi.

	Materiale didattico: sketchbook [2025_03_25.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_03_25.png), [presentazione](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/Rich_Caruana_EBMs.pdf) di Rich Caruana (esempi sul caso di polmonite). 

# 6^ Settimana

- **Martedì 1 aprile (2h)**

	Esercitazione su modelli interpretabili basati su alberi, liste e modelli additivi.

	Materiale didattico: notebook [02_RuleFit.ipynb](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/02_RuleFit.ipynb), [03_Explainable_Boosting_Machines.ipynb](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/03_Explainable_boosting_machines.ipynb), dataset [fico.csv](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/fico.csv), codice per alberi decisionali ottimi [run_gosdt.py](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/run_gosdt.py)


- **Giovedì 3 aprile (2h)**

	Neural additive models (cenni). Prototype-based networks. ProtoPNet.

	Materiale didattico: sketchbook [2025_04_03_1.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_04_03_1.png), [2025_04_03_2.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_04_03_2.png).

# 7^ Settimana

- **Martedì 8 aprile (2h)**

	Programmazione logica induttiva. Cenni alla programmazione logica. Definizioni, sintassi, semantica. Esempi: https://swish.swi-prolog.org/example/examples.swinb

	Materiale didattico: sketchbook [2025_04_08_1.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_04_08_1.png), [2025_04_08_2.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_04_08_2.png), [CD22] - Sezione 2 (fino alla sezione 2.2 inclusa).

- **Giovedì 10 aprile (2h)**

	Caratteristiche di un sistema di ILP. Metodologie di learning: learning from entailment, learning from interpretations. Il sistema Aleph. Il problema dei treni di Michalski.

	Materiale didattico: sketchbook [2025_04_10_1.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_04_10_1.png), [2025_04_10_2.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_04_10_2.png), [CD22] - Sezioni 3 (3.1 e 3.2 incluse), 4 (soltanto cenni) e 6.1 (Aleph).

	Esempi Aleph: https://cplint.ml.unife.it/example/aleph/aleph_examples.swinb

	Problema dei treni di Michalski: https://cplint.ml.unife.it/example/aleph/train.pl

# 8^ Settimana

- **Martedì 15 aprile (2h)**

	Neuro-symbolic Artificial Intelligence. Metodi ibridi per la combinazione di approcci simbolici e sub-simbolici. Knowledge-Based Artificial Neural Networks. Logica come regolarizzazione. Cenni alle Markov Logic Networks.

	Materiale didattico: lucidi del blocco 03 (slide da 38 a 46 soltanto come approfondimento).
# 9^ Settimana

- **Martedì 6 maggio (2h)**

	Introduzione ai metodi spiegabili a posteriori. Tassonomia di approcci: model explanation, outcome explanation, model inspection. Caratteristiche generali delle tecniche di model explanation. Cenni agli algoritmi Trepan e PALM.

	Materiale didattico: sketchbook [2025_05_06_1.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_05_06_1.png), [2025_05_06_2](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_05_06_2.png)[.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_04_10_2.png), survey [GMT18], in particolare sezioni 4-5-6-7-8, ma soltanto nelle parti trattate a lezione.


- **Giovedì 8 maggio (2h)**

	Metodi di spiegazione locali: esempi (local surrogate models, feature perturbation, saliency masks). Algoritmo LIME (Local Interpretable Model-agnositc Explanations).

	Materiale didattico: sketchbook [2025_05_08_1.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_05_08_1.png), [2025_05_08_2.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_05_08_2.png), [MLNR25] sezione 14.


# 10^ Settimana

- **Martedì 13 maggio (2h)**

	Approfondimento su LIME: costo del calcolo di una spiegazione, cenni alla tecnica Submodular Pick. Algoritmo PredDiff per la stima dell'impatto di una feature sull'uscita di un modello. Introduzione alla teoria dei giochi non-cooperativi (cenni alla teoria dell'equilibrio di Nash) e cooperativi (Shapley values).

	Materiale didattico: sketchbook [2025_05_13_1.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_05_13_1.png), [2025_05_13_2.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_05_13_2.png), [2025_05_13_3.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_05_13_3.png).

- **Giovedì 15 maggio (2h)**

	Metodo SHAP (SHapley Additive exPlanations) per produrre spiegazioni sulla base del calcolo degli Shapley values. Assiomi di equità. Esempi di coalizioni. Cenni all'approssimazione degli Shapley values. Tecnica KernelSHAP e legame con LIME.

	Materiale didattico: sketchbook [2025_05_15_1.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_05_15_1.png), [2025_05_15_2.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_05_15_2.png), [MLNR25] sezioni 17-18.


# 11^ Settimana

- **Martedì 20 maggio (2h)**

	KernelSHAP. Legame tra SHAP e LIME. Esempi di applicazioni ed utilizzo di librerie Python.

	Materiale didattico: sketchbook [2025_05_20.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_05_20.png), notebook [05_LIME.ipynb](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/05_LIME.ipynb?time=1747747066739), [06_SHAP.ipynb](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/06_SHAP.ipynb?time=1747747078467), [run_shap.ipynb](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/run_shap.ipynb).

- **Giovedì 22 maggio (2h)**

	Metodi di spiegazione basati su gradiente: Vanilla Gradient, SmoothGrad, GradCam. Mappe di salienza.

	Materiale didattico: [MLNR25] capitolo 25, lavagne [20250522_1.jpg](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/20250522_1.jpg), [20250522_2.jpg](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/20250522_2.jpg), [20250522_3.jpg](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/20250522_3.jpg), [20250522_4.jpg](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/20250522_4.jpg), [20250522_5.jpg](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/20250522_5.jpg), [20250522_6.jpg](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/20250522_6.jpg), [20250522_7.jpg](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/20250522_7.jpg), [20250522_8.jpg](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/20250522_8.jpg).

# 12^ Settimana
- **Martedì 27 maggio (2h)**

	Metodi di spiegazione basati su gradiente: GradCam, Guided GradCam. Problematiche relative alle salency maps, test di robustezza. Introduzione ai metodi di explanation basati su attention.

	Materiale didattico: [MLNR25] capitolo 25, sketchbook [2025_05_27_1.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_05_27_1.png), [2025_05_27_2.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_05_27_2.png), notebook [07_Gradient_based_approaches.ipynb](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/07_Gradient_based_approaches.ipynb).


- **Giovedì 29 maggio (2h)**

	Attention: definizione generale (ad alto livello), utilizzo di query (Q), keys (K), values (V) per il calcolo dell'attention. Relazione tra attention ed explanation. Ceteris paribus plots come tecnica model-agnostic per la valutazione dell'importanza di singole feature.

	Materiale didattico: sketchbook [2025_05_29_1.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_05_29_1.png), [2025_05_29_2.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_05_29_2.png), [2025_05_29_3.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_05_29_3.png).

# 13^ Settimana
- **Martedì 3 giugno (2h)**

	Individual Conditional Expectation (ICE) e Partial Dependence Plot (PDP) come grafici per la spiegazione delle feature. Permutation feature importance. Introduzione ai concept bottleneck models.

	Materiale didattico: sketchbook [2025_06_03_1.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_06_03_1.png), [2025_06_03_2.png](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/2025_06_03_2.png), notebook [08_Dependence_plots.ipynb](https://e-l.unifi.it/pluginfile.php/3289993/course/section/427330/08_Dependence_Plots.ipynb), [MLNR25] capitoli 12-13-19-23.

- **Giovedì 5 giugno (2h)**

	Applicazioni di XAI: astronomia, biologia marina, safety-critical systems, documenti legali, musica, visual reasoning.

	Materiale didattico: lucidi del blocco 05.
