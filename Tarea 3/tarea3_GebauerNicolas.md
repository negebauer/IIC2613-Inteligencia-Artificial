## IIC2613 Inteligencia Articial - Tarea 3

| Rut | UC | Nombre |
|:---:|:--:|:------:|
| 18501880-6 | 13634941 | Nicolás Gebauer Martínez

***

#### Información general

Primero se debe leer el [readme](readme.txt)

***

#### Experimentos con Descenso de Gradiente

Primero se executó el programa `DescGrdt1` con los valores por defecto `old_min = 10` y `learningRate = 0.1`. Luego se modificó la tasa de aprendizaje a valores menores, en particula se probó con `0.08, 0.05, 0.04, 0.01, 0.005, 0.001`.  
Se observa que al disminuir la tasa de aprendizaje la velocidad con la que se desciende hacia el mínimo de la función es cada vez menor. En particular, con una tasa de aprendizaje de `0.001` se demora minutos, mientras que con `0.1` se hace en unos pocos segundos. También es de destacar que la disminución de la tasa de aprendizaje se hace mucho más evidente al estar evaluando valores cercanos al mínimo (`x<1`).  
Luego se aumento el valor de la tasa de aprendizaje. Se probaron los valores `0.2, 0.4, 0.6, 0.8, 1`. Se observa que la velocidad de descenso es mayor al aumentar la tasa de aprendizaje. Se destaca que para los valores `0.6` y `0.8` se observa que el descenso se "pasa de largo". Dado que se aumentó tanto la tasa de aprendizaje se logró dar un salto que pasó de `x=10` a un `x~-5`. Luego volvió a converger hacia `x=0`.  
De aqui se puede concluir ventajas y desventajas de el valor de la tasa de aprendizaje. Con un mayor valor se tiende más rápido al mínimo pero se pueden dar saltos muy grandes, pasandose del mínimo. En cambio, si la tasa de aprendizaje es pequeña se evita pasar de largo pero la convergencia es mucho más lenta.

Luego se executó el programa `DescGrdt2` con los valores por defecto `old_min = 1` y `learningRate = 0.1`. Se observa que efectivamente se tiende al mínimo local
Se executó con distintas combinaciones de punto inicial y tasas de aprendizaje, de las cuales se destacan las siguientes:

|`old_min`|`learningRate`|mínimo|
|:-:|:-:|:-:|
|1|0.1|-2.09|
|2.2|0.1|4.19|
|1|4|-6938.73|
|2.2|3.6|-34119.7|
|2.2|4|-820265.65|

Se puede observar que el punto inicial y la tasa de aprendizaje tienen un efecto muy importante en el resultado final, no solo en que tan rápido se calcula. Si se cambia el punto inicial se termina obteniendo un mínimo local. Además, si la tasa de aprendizaje es muy grande se puede terminar en un mínimo local al que se quería en un principio.

#### Análisis de Sentimientos en Críticas de Películas

##### Word2Vec

Se ejecutaron las comparaciones pedidas, más las extras `car + water - wheels` con la intención de obtener `boat` y ver la similitud de `man` con `men`. Los resultados son los siguientes:

> Comparing most similar to positives ['woman', 'king'] and negatives ['man']  
(u'queen', 0.7118192315101624)  
(u'monarch', 0.6189674139022827)  
(u'princess', 0.5902431011199951)  
(u'crown_prince', 0.5499460697174072)  
(u'prince', 0.5377321839332581)  
(u'kings', 0.5236844420433044)  
(u'Queen_Consort', 0.5235946178436279)  
(u'queens', 0.5181134343147278)  
(u'sultan', 0.5098593235015869)  
(u'monarchy', 0.5087412595748901)  

> Comparing most similar to positives ['paris', 'italy'] and negatives ['france']  
(u'lohan', 0.5069675445556641)  
(u'madrid', 0.48184293508529663)  
(u'heidi', 0.4799900949001312)  
(u'real_madrid', 0.4753322899341583)  
(u'florence', 0.4682057499885559)  
(u'diego', 0.467273086309433)  
(u'ronnie', 0.4672326445579529)  
(u'juventus', 0.4672061502933502)  
(u'joel', 0.46537238359451294)  
(u'huntelaar', 0.46358999609947205)  

> Comparing most similar to positives ['car', 'water'] and negatives ['wheels']  
(u'sewage', 0.5073274374008179)  
(u'groundwater', 0.48820173740386963)  
(u'Floridan_aquifer', 0.4697296917438507)  
(u'aquifers', 0.4586605429649353)  
(u'Water', 0.4582120180130005)  
(u'underground_aquifer', 0.4578779935836792)  
(u'tapwater', 0.453736811876297)  
(u'freshwater', 0.4533122479915619)  
(u'shallow_aquifer', 0.44539833068847656)  
(u'Elephant_Butte_Reservoir', 0.44529250264167786)  

> Comparing similarity of breakfast with cereal  
0.365095440625  

> Comparing similarity of class with course  
0.22938951003  

> Comparing similarity of man with men  
0.548976303226  

Se puede observar que efectivamente se cumplen algunas de las relaciones mencionadas en el informe. `rey-hombre+mujer` se parece a `reina` con un `71%` de similitud, lo cual es un número muy elevado. Otra similitud alta fue la de `men` con `man`. Llama la atención que estos resultados son distintos. Se tenía la intención de que auto - ruedas + agua diera bote, pero los resultados no fueron favorables.

##### PolarityExamples.txt y MovieReviewExamples.txt

Al observar las reseñas de películas se destaca que estas tienden a ser un conjunto de comentarios cortos, a diferencia de por ejemplo frases más largas y estructuradas. Sin embargo, siguen siendo comentarios con un orden más formal que los del archivo _polarity_. Este otro tiene mensajes informales y desordenados que incluyen, por ejemplo, comentarios sarcásticos que podrían ser más difíciles de entender para una inteligencia artificial, dado que el sentido del mensaje es el contrario del significado que se extrae de las palabras usadas.

##### SVM

##### Matriz confusión

##### Mejoras

##### Críticas inventadas
