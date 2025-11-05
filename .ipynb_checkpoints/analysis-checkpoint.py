# 🎨 LEVEL 4 – Visualization (Matplotlib + Seaborn)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("netflix_data.csv")

#clean which don't have rating
rating_df = df.dropna(subset=['rating'])

#rating with counts
rating_counts = rating_df.groupby('rating')['rating'].count()

#Most common rating
highest_rating = rating_counts[rating_counts==rating_counts.max()].index


df.info()
print(df.head())
df.tail()
#Movies released in 2015
movies_release_in_2015 = len(df[df['release_year']==2015])


#Movies or tv shows released in india
df.dropna(subset=['country'], inplace=True)
items_release_in_india = df[df['country'].str.lower()=='india'].pivot_table(index='release_year', columns='type', values='title', aggfunc='count')
items_release_in_india =items_release_in_india.fillna(0).astype('int')
items_release_in_india['Total Releasd'] = items_release_in_india['Movie']+items_release_in_india['TV Show']

#Top 5 countries of producing netflix content
top_countries = df.groupby('country')['title'].count().sort_values(ascending=False).head()
top_countries

# For each rating, show how many movies and how many TV shows exist.
rating_wise_count = rating_df.pivot_table(index='rating', columns='type', values='title', aggfunc='count')
rating_wise_count = rating_wise_count.fillna(0).astype('int')
rating_wise_count.reset_index(inplace=True)

# Find which year had the most releases overall.
year_of_highest_release = df.groupby('release_year')['title'].count().sort_values(ascending=False).reset_index()
year_of_highest_release.iloc[0,0]


# Plot a bar chart showing how many titles exist per rating.
ratings = rating_wise_count['rating']
x = np.arange(len(ratings))
width=0.30
plt.bar(x, rating_wise_count['Movie'], width=width,label="Movies")
plt.bar(x+width, rating_wise_count['TV Show'], width=width,label="TV Show")
plt.xlabel('Ratings')
plt.ylabel('Total numbers')
plt.title('Total movies or show vs ratings')
plt.tight_layout()
plt.grid()
plt.xticks(x, ratings)
plt.legend()
plt.show()
