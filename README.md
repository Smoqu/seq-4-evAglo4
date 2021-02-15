# seq-4-evAglo4

|          | Tri par sélection durée | Tri par insertion durée | vainqueur | écart relatif |
| -------- | ----------------------- | ----------------------- | --------- | ------------- |
| 50 str   | 2,00E-03                | 1,00E-03                | Insertion | 50,01%        |
| 50 tuple | 2,00E-03                | 1,00E-03                | Insertion | 50,03%        |
| 50 int   | 1,00E-03                | 2,00E-03                | Sélection | 49,99%        |
| 50 float | 1,00E-03                | 2,00E-03                | Sélection | 50,01%        |
| 50 bool  | 2,00E-03                | 1,00E-03                | Insertion | 50,01%        |
| 1000 int | 5,78E-01                | 5,39E-01                | Insertion | 6,75%         |


On remarque que le tri par insertion est plus performant que le tri par sélection sur les types comme les string, les tuples, et les boolléens.
Le tri par sélection est plus performant sur jeux de données de ptites tailles commes les int et les float, seulement pour les jeux de données plus importants le tri par insertion remporte.
