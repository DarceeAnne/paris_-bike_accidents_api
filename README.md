# Paris Bike Accidents API

View API documentation [here](http://localhost:8080/docs/#/default/get_accidents_velo)

This API exposes a dataset of bike accidents in France. It is a mix of four data sources:
  - The [Accidents de Vélo dataset](https://opendata.koumoul.com/datasets/accidents-velos) (primary dataset) compiled by Koumoul 
  - Three dimension tables created manually from the [guide of official labels published by l’autorité de la statistique publique](https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2022/#/resources/8ef4c2a3-91a0-4d98-ae3a-989bde87b62a)
    
The primary dataset contains approximately 75,000 accident records covering the time period of 2005-2021. 
The dimension tables cover the categorization of sex (male, female), position (road, bike path, side walk, etc.), and route (home to work & vice versa, home to school and vice versa, shopping, etc.). 

    
View data prepared by Koumoul [here](https://opendata.koumoul.com/datasets/accidents-velos)
    
View original source data from data.gouv.fr [here](https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2022/)
