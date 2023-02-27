# future
This repository is for playing a little game of guessing the future. 

Predictions about the future sequence of events are made by each person participating in the game:

```
predictions:
  - 1 person on Mars (base, as in Antarctica)
  - 10 hours from Frankfurt to Sydney
  - Asteroid mining
  - Carbon capture
  - Cleaning robots (on human level with tidying up)
  - Diseases, cancer, Alzheimer's, Parkinson's (1 of them)
  - Diseases, cancer, Alzheimer's, Parkinson's (2 of them)
  - End of capitalism in Europe
  - End of the oil age
  - energy weapons on warships
  - First man turns 150
  - Fusion
  - Humanoid robots in everyday life
  - Majority of world population is atheist
  - Mini atomic power plants
  - Nano robots (self-replicating) for medicine
  - Net zero CO2
  - Permanent presence of at least 5000 people in space
  - Quantum computers
  - Revival of extinct species
  - Self-driving cars
  - Universal translation for some animals (orcas, elephants, monkeys) (1 of them)
  - Universities will be abolished
  - Work will no longer be necessary for the majority of the working-age (25 to 65) population
  - World government
  - World population reaches peak
```


Participants are encouraged to add timestamps to their predictions for anchoring. Currently the timestamps are not included in the evaluation. Scoring will not be possible until some of the events have occurred. 


Two Example predictions (by two imaginary People Felix and John) might look like this:
(the numbers (2,5,10, etc) mean Years from now  (Start of 2023) into the future)

```
John:
  # the numbers (2,5,10, etc) mean Years from now  (Start of 2023) into the future
  5:
    - Self-driving cars

  10:
    - Diseases, Cancer, Alzheimer's, Parkinson's (1 of them)
    - Revival of extinct species
    - Fusion
    - Diseases, Cancer, Alzheimer's, Parkinson's (2 of them)
    - Energy weapons on warships

  20:
    - 1 person on Mars (base, as in Antarctica)
    - Carbon capture
    - Nano robots (self-replicating) for medicine
    - 10 hours from Frankfurt to Sydney

  50:
    - Permanent presence of at least 5000 people in space
    - First man turns 150
    - World population reaches peak
    - End of the oil age

  100:
    - Work will no longer be necessary for the majority of the working-age (25 to 65) population
    - Asteroid mining
    - Net zero CO2
    - End of capitalism in Europe
    - Universal translation for some animals (orcas, elephants, monkeys) (1 of them)
    - Cleaning robots (on human level with tidying up)
    - Mini atomic power plants
    - Quantum computers
    - World government
    - Humanoid robots in everyday life
    - Majority of world population is atheist
    - Universities will be abolished
```

```
Felix:
   # the numbers (2,5,10, etc) mean Years from now  (Start of 2023) into the future
    2:
      - Self-driving cars

    5:
      - Quantum computers
      - Humanoid robots in everyday life
      - Majority of world population is atheist
      - Diseases, Cancer, Alzheimer's, Parkinson's (1 of them)
      - Universal translation for some animals (orcas, elephants, monkeys) (1 of them)
      - Revival of extinct species

    10:
      - Nano robots (self-replicating) for medicine
      - Diseases, Cancer, Alzheimer's, Parkinson's (2 of them)
      - First man turns 150
      - World population reaches peak
      - Fusion
      - 1 person on Mars (base, as in Antarctica)

    20:
      - Permanent presence of at least 5000 people in space
      - End of the oil age
      - Energy weapons on warships

    50:
      - Cleaning robots (on human level with tidying up)
      - 10 hours from Frankfurt to Sydney
      - Mini atomic power plants
      - Net zero CO2
      - Carbon capture
      - End of capitalism in Europe
      - Work will no longer be necessary for the majority of the working-age (25 to 65) population
      - Universities will be abolished

    100:
      - World government
      - Asteroid mining

```



An example score for the sequence of events ("realised"), i.e.

    - Carbon capture
    - First man turns 150
    - Fusion

is provided.


This configuration is found in 

```
myfuture-kedro/conf/base/parameters.yml 
```

To run the evalation run 

```
kedro run
```

inside the kedro folder (ie  my-future-kedro)