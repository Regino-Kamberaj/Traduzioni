È un modello derivato dall'unione di [approcci statistici e simbolici](regio/Approcci%20neuro-simbolici/Approcci%20neuro-simbolici.md#StarAI).
# Definzione
Una Markov Logic Network è definita da un insieme di regole e dei pesi, uno associato a ogni regola; più il peso di una regola è alto più voglio che la regola sia vera.
# Applicazioni
- Inferenza
	Siccome ogni regola ha un peso, posso voler dedurre la probabilità che qualcosa di non noto sia vero. Non ho una certezza (come nella logica pura), ma una probabilità associata a un evento.
- Learning
	Se ho un dataset posso imparare i pesi. Più complesso è imparare le regole.