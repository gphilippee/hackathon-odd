# Hackathon ODD

https://github.com/Garage-ISEP/hackathon-ia-developpement-durable

**Quelle méthode pour identifier les cibles ODD (Objectifs de Développement Durable) dans un texte?**

- ODD 12 : « Consommation et production responsables » (11 cibles)
https://sdgs.un.org/goals/goal12
- ODD 15 : « Vie terrestre » (12 cibles)
https://sdgs.un.org/goals/goal15
- ODD 16 : « Paix, justice et institutions efficaces » (12 cibles)
https://sdgs.un.org/goals/goal16

## OSDG data
https://github.com/osdg-ai/osdg-data

## Results

### ZS latent embedding with raw label

```shell
               precision    recall  f1-score   support
        12.1       0.00      0.00      0.00         0
        12.2       0.00      0.00      0.00         1
        12.3       0.20      0.50      0.29         2
        12.4       0.50      0.15      0.23        27
        12.5       0.00      0.00      0.00        11
        12.6       0.00      0.00      0.00         0
        12.7       0.00      0.00      0.00         1
        12.8       0.00      0.00      0.00         0
        12.a       0.00      0.00      0.00         2
        12.b       0.00      0.00      0.00         0
        12.c       0.00      0.00      0.00         0
        15.1       0.24      0.33      0.28        15
        15.2       0.17      0.17      0.17         6
        15.3       0.00      0.00      0.00         4
        15.4       0.00      0.00      0.00         0
        15.5       0.00      0.00      0.00         7
        15.6       0.00      0.00      0.00         4
        15.7       0.00      0.00      0.00         0
        15.8       0.00      0.00      0.00         0
        15.9       0.00      0.00      0.00         0
        15.a       0.00      0.00      0.00         0
        15.b       0.00      0.00      0.00         0
        15.c       0.00      0.00      0.00         0
        16.1       0.00      0.00      0.00         4
        16.2       0.00      0.00      0.00         0
        16.3       0.00      0.00      0.00         1
        16.4       0.00      0.00      0.00         0
        16.5       0.00      0.00      0.00        10
        16.6       1.00      0.10      0.18        10
        16.7       0.00      0.00      0.00         7
        16.8       0.00      0.00      0.00         0
        16.9       0.00      0.00      0.00         0
       16.10       0.00      0.00      0.00         1
        16.b       0.17      1.00      0.29         1
           0       0.00      0.00      0.00        31
   micro avg       0.09      0.09      0.09       145
   macro avg       0.06      0.06      0.04       145
weighted avg       0.20      0.09      0.10       145
```

![output](https://user-images.githubusercontent.com/55877031/168439899-e342f65b-5e1a-4aca-b3ff-0f91c809c1eb.png)


### ZS latent embedding with clean label

```shell
               precision    recall  f1-score   support

        12.1       0.00      0.00      0.00         0
        12.2       0.00      0.00      0.00         1
        12.3       0.00      0.00      0.00         2
        12.4       0.45      0.37      0.41        27
        12.5       0.00      0.00      0.00        11
        12.6       0.00      0.00      0.00         0
        12.7       0.00      0.00      0.00         1
        12.8       0.00      0.00      0.00         0
        12.a       0.25      0.50      0.33         2
        12.b       0.00      0.00      0.00         0
        12.c       0.00      0.00      0.00         0
        15.1       0.43      0.60      0.50        15
        15.2       0.43      0.50      0.46         6
        15.3       0.00      0.00      0.00         4
        15.4       0.00      0.00      0.00         0
        15.5       0.00      0.00      0.00         7
        15.6       0.00      0.00      0.00         4
        15.7       0.00      0.00      0.00         0
        15.8       0.00      0.00      0.00         0
        15.9       0.00      0.00      0.00         0
        15.a       0.00      0.00      0.00         0
        15.b       0.00      0.00      0.00         0
        15.c       0.00      0.00      0.00         0
        16.1       0.00      0.00      0.00         4
        16.2       0.00      0.00      0.00         0
        16.3       0.00      0.00      0.00         1
        16.4       0.00      0.00      0.00         0
        16.5       0.00      0.00      0.00        10
        16.6       0.00      0.00      0.00        10
        16.7       0.50      0.14      0.22         7
        16.8       0.00      0.00      0.00         0
        16.9       0.00      0.00      0.00         0
       16.10       0.00      0.00      0.00         1
        16.a       0.11      0.20      0.14         5
           0       0.00      0.00      0.00        31

   micro avg       0.17      0.17      0.17       149
   macro avg       0.06      0.07      0.06       149
weighted avg       0.17      0.17      0.16       149
```