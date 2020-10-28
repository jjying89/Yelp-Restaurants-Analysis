
# NFL Stadiums: Restaurant density analysis.
Using the Yelp API we'll analyze the number of restaurants around the NFL team stadiums in:
>Two different timepoints: Saturday & Monday.
>Two different search terms :
	>1) General search term: “restaurants”
	>2) By category:  "sportsbars", "pubs", "wine_bars", "cocktailbars“ (considered as one for our analysis purposes).
>
>
> The data request using the Yelp API is done by the following notebooks:
> > By term:  [Request_Yelp_json_files.ipynb](https://github.com/CSwilliams88/project_1/blob/main/Request_Yelp_json_files.ipynb)
> 
> > By category:  [Request_Yelp_categories.ipynb](https://github.com/CSwilliams88/project_1/blob/main/Request_Yelp_categories.ipynb)
> 
>
>The data munging and data statistics is done by the notebooks:
>> By term:  [Analysis_Yelp_json_files.ipynb](https://github.com/CSwilliams88/project_1/blob/main/Analysis_Yelp_json_files.ipynb)
>
>> By category: [Analysis_Categories.ipynb](https://github.com/CSwilliams88/project_1/blob/main/Analysis_Categories.ipynb)
>  
>The plotting and analysis can be found in the following notebooks:
>
> [gmaps_Analysis.ipynb](https://github.com/CSwilliams88/project_1/blob/main/gmaps_Analysis.ipynb)
> 
> [Analysis_Avg_Plots.ipynb](https://github.com/CSwilliams88/project_1/blob/main/Analysis_Avg_Plots.ipynb)
> 
> [Categories Analysis Graphs.ipynb](https://github.com/CSwilliams88/project_1/blob/main/Categories%20Analysis%20Graphs.ipynb)
> 
> [Comparing Popular Teams.ipynb](https://github.com/CSwilliams88/project_1/blob/main/Comparing%20Popular%20Teams.ipynb)
> 
### Hypothesis. 
>Hypothesis: We believe the density of restaurants/bars around stadiums amount to a significant percentage of the total restaurants of the country.
### Questioning the data.
>
>**1**. How many restaurants in a 3000 meters radius (approx. 2 miles) are around the stadiums?
>
>**2**. How the restaurants (number, type, price, etc.) differ between cities?
>
>**3**. How the restaurants reviews compare before game day to the after game day?
>
>**4**. How do restaurants/bars score in cities with more popular franchises compare to less popular ones?
>
>>**a)** Compare restaurants’ ratings between most popular cities (NY, Chicago, Las Vegas, Seattle, San Francisco).
>
>> **b)** Compare restaurants’ ratings of cities with the most popular teams (Dallas Cowboys, New England Patriots, 	Pittsburgh Steelers, Green Bay Packers, Seattle Seahawks.
>
 >>**c)** Compare restaurants’ ratings of cities with the least popular teams (Jacksonville Jaguars, Tampa Bay Buccaneers, Tennessee Titans, Cincinnati Bengals, Buffalo Bills)

> The analysis of the  data and the answers to the questions above can be found in the project presentation file [Restaurant_density_analysis.](https://github.com/CSwilliams88/project_1/tree/main/Presentation)
> 
### Conclusions.
>According to statistica.com, there are 660,755 restaurants in the US as of spring 2018.

>From our analysis, we see that there are more than 12000 restaurants around the NFL Stadiums in a 3000 meters radius. That amounts to a **2%** of all restaurants in the USA.

