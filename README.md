# Project 5: Climate Change - A Global Analysis

### Problem Statement
Countries contribute to and are affected by climate change differently. In this project we seek to uncover specific global relationships between country inputs to climate change and their effects on a country. 

### Background
Global climate change is a widely known fact; green house gas emissions and co2 directly contribute to increased global temperatures. What is lesser known is how these changes affect yada yada

### Data Analyzed
* ['kahuna.csv'](./data/kahuna.csv): All data from [OurWorldInData](https://ourworldindata.org/charts): each feature taken from invidual csv files and merged into one. 

Link for Streamlit: https://share.streamlit.io/sara-zhou/project-5/main/code/sz/streamlit.py


### Data Dictionary
|Feature|Type|Dataset|Description|
|---|---|---|---|
|Entity|str|kahuna|The country name|
|Year|int|kahuna|The year per each country for the data|
|Death %|float|kahuna||
|CO2 Emmissions|int|kahuna||
|CO2 Emissions Per Cap|float|kahuna||
|Food Emissions|float|kahuna||
|Total GHG|float|kahuna|Description|
|Consumption of Ozone|float|kahuna|Description|
|Shared CO2 Emissions|float|kahuna|Description|
|Transport|float|kahuna|Description|
|Death_rate_ambient_ozone_pol|float|kahuna|Description|
|Death_rate_household_air_pol|float|kahuna|Description|
|Death_rate_all_causes|float|kahuna|Description|
|Death_actual_ozone|float|kahuna|Description|
|Death_actual_particulate|float|kahuna|Description|
|Death_actual_household|float|kahuna|Description|
|Death_under5|float|kahuna|Description|
|Death_5-14|float|kahuna|Description|
|Death_15-49|float|kahuna|Description|
|Death_50-69|float|kahuna|Description|
|Death_70+|float|kahuna|Description|
|Urban%|float|kahuna|Description|
|Child Mortality|float|kahuna|Description|
|Population|float|kahuna|Description|
|GDP|float|kahuna|Description|
|Forest area|float|kahuna|The area of |


### Analysis, Conclusions, and Recommendations

With a wide array of data that spanned climate metrics such as CO2 Emissions Per Cap, country demographics such as GDP (per cap), and outcome metrics such as share of deaths in a country attributed to air pollution risk factors (Deaths %), we set out to build a variety of cluster models that would enable us to investigate relationships across country, cluster, and year. We built agglomerative (hierarchical) models, DBSCAN models, and Kmeans models. We used a variety of techniques to visualize the performance of these models to choose which cluster model offered est insights into the data at hand. Some of these techniques like KElbowVisualizer abd SilhouetteVisualizer were drawn from an interesting library called yellowbrick. Other techniques were utilized from within scikit learn and scipy such as creating dendrograms with various linkage methods and comparing them based of cophonetic scores. Despite using various methods to identify the model that clustered 'optimally' accordring to various metrics (see 02_Modeling...nb), we placed the emphasis of our analysis on a Kmeans model of n_clusters=3 for clarity of inference.

For a closer look at some analysis of the other model methods see 07_End_Analysis.ipynb. 

Using our Kmeans model (n_clusters=3) we found that clusters were grouped very specifically at a country level. This was remarkable because none of the other models grouped the data in this way, namely, placing China and India in cluster 1, the United States in cluster 2, and the rest of the world (totalling 111 countries) in cluster 0. The body of our EDA thereafter focuses on uncovering the reason behind this model behavior. To do this we added the cluster label to the dataframe as a final feature and used groupby's to compare values at the cluster and country level across our metrics. From there we found visible disparities in mean behavior across cluster or country level data and we plotted out a variety of visualizations to provide an easier medium of inference into our cluster and country relationships. These included histograms to look at dispersions of country metrics across each cluster, bar charts to describe the difference in mean behavior for each cluster across all metrics, line graphs to make evident the change over time (1990-2014) of country level data and scatters and 3D plots to supplement our findings in a high level manner (see nb 04&05).


