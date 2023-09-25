#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

data = {
    'title': ["Tasveer Mere Sanam", "Only You", "El pueblo del terror", "Machine", "MARY"],
    'year': ["1996", "1994", "1970", "2007", "2008"]
}

titles = pd.DataFrame(data)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'dataframe')


# In[4]:


num_movies = titles.shape[0]
print("Number of movies listed:", num_movies)




# In[ ]:


get_ipython().run_line_magic('pinfo', 'DataFrame')


# In[5]:


earliest_films = titles.sort_values(by='year').head(2)
print("The earliest two films listed:")
print(earliest_films)


# In[ ]:


3: How many movies have the title "Hamlet"?


# In[6]:


hamlet_movies = titles[titles['title'] == 'Hamlet']
num_hamlet_movies = hamlet_movies.shape[0]
print("Number of movies with the title 'Hamlet':", num_hamlet_movies)


# In[12]:


#4 How many movies are titled "North by Northwest"?
num_north_by_northwest = len(titles[titles['title'] == 'North by Northwest'])
print("Number of movies titled 'North by Northwest':", num_north_by_northwest)



# In[10]:


# 5When was the first movie titled "Hamlet" made?
hamlet_movies = titles[titles['title'] == 'Hamlet']
first_hamlet_movie_year = hamlet_movies['year'].min()
print("The first movie titled 'Hamlet' was made in:", first_hamlet_movie_year)



# In[11]:


# 6 List all of the "Treasure Island" movies from earliest to most recent.
treasure_island_movies = titles[titles['title'] == 'Treasure Island'].sort_values(by='year')
print("List of 'Treasure Island' movies from earliest to most recent:")
print(treasure_island_movies)


# In[13]:


# 7How many movies were made in the year 1950?
num_movies_1950 = len(titles[titles['year'] == '1950'])
print("Number of movies made in the year 1950:", num_movies_1950)



# In[9]:


# 8How many movies were made in the year 1960?
num_movies_1960 = len(titles[titles['year'] == '1960'])
print("Number of movies made in the year 1960:", num_movies_1960)


# In[8]:


# 9How many movies were made from 1950 through 1959?
num_movies_1950s = len(titles[(titles['year'] >= '1950') & (titles['year'] <= '1959')])
print("Number of movies made from 1950 through 1959:", num_movies_1950s)



# In[7]:


# 10In what years has a movie titled "Batman" been released?
batman_years = titles[titles['title'] == 'Batman']['year'].unique()
print("Years in which a movie titled 'Batman' has been released:", batman_years)


# # 11How many roles were there in the movie "Inception"?

# In[2]:


import pandas as pd


cast = pd.read_csv('cast.csv')


num_roles_in_inception = len(cast[(cast['title'] == 'Inception')])
print("Number of roles in the movie 'Inception':", num_roles_in_inception)


# # 12. How many roles in the movie "Inception" are NOT ranked by an "n" value?

# In[ ]:


import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

inception_roles = df[df['title'] == 'Inception']

num_unranked_roles = inception_roles['n'].isna().sum()

print(f'The number of roles in the movie "Inception" that are not ranked by an "n" value is: {num_unranked_roles}')


# # 13 But how many roles in the movie "Inception" did receive an "n" value?

# In[3]:


import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

inception_roles = df[df['title'] == 'Inception']

num_ranked_roles = inception_roles['n'].notna().sum()

print(f'The number of roles in the movie "Inception" that received an "n" value is: {num_ranked_roles}')


# # 14. Display the cast of "North by Northwest" in their correct "n"-value order, ignoring roles that did not earn a numeric "n" value.

# In[4]:


import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

north_by_northwest_cast = df[(df['title'] == 'North by Northwest') & df['n'].notna()]

north_by_northwest_cast['n'] = pd.to_numeric(north_by_northwest_cast['n'])

north_by_northwest_cast = north_by_northwest_cast.sort_values(by='n')

print(north_by_northwest_cast[['name', 'character', 'n']])


# In[5]:


#15. Display the entire cast, in "n"-order, of the 1972 film "Sleuth"
import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

sleuth_1972_cast = df[(df['title'] == 'Sleuth') & (df['year'] == 1972)]

sleuth_1972_cast = sleuth_1972_cast.sort_values(by='n')

print(sleuth_1972_cast[['name', 'character', 'n']])


# In[6]:


#16. Now display the entire cast, in "n"-order, of the 2007 version of "Sleuth".
import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

sleuth_2007_cast = df[(df['title'] == 'Sleuth') & (df['year'] == 2007)]

sleuth_2007_cast = sleuth_2007_cast.sort_values(by='n')

print(sleuth_2007_cast[['name', 'character', 'n']])


# In[7]:


# 17. How many roles were credited in the silent 1921 version of Hamlet?
import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

hamlet_1921_cast = df[(df['title'] == 'Hamlet') & (df['year'] == 1921)]

num_credited_roles = hamlet_1921_cast.shape[0]

print(f'The number of roles credited in the silent 1921 version of "Hamlet" is: {num_credited_roles}')


# In[8]:


#18. How many roles were credited in Branagh's 1996 Hamlet?
import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

branagh_hamlet_1996_cast = df[(df['title'] == 'Hamlet') & (df['year'] == 1996)]

num_credited_roles = branagh_hamlet_1996_cast.shape[0]

print(f'The number of credited roles in Kenneth Branagh\'s 1996 version of "Hamlet" is: {num_credited_roles}')


# In[9]:


#19. How many "Hamlet" roles have been listed in all film credits through history?
import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

hamlet_roles = df[df['title'] == 'Hamlet']

num_hamlet_roles = hamlet_roles['character'].nunique()

print(f'The number of "Hamlet" roles listed in all film credits through history is: {num_hamlet_roles}')


# In[10]:


#20. How many people have played an "Ophelia"?
import pandas as pd
csv_file = "cast.csv"

df = pd.read_csv(csv_file)

ophelia_roles = df[df['character'] == 'Ophelia']

num_ophelia_actors = ophelia_roles['name'].nunique()

print(f'The number of people who have played the role of "Ophelia" is: {num_ophelia_actors}')


# In[11]:


#21. How many people have played a role called "The Dude"?
import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

the_dude_roles = df[df['character'] == 'The Dude']

num_the_dude_actors = the_dude_roles['name'].nunique()

print(f'The number of people who have played a role called "The Dude" is: {num_the_dude_actors}')


# In[12]:


#22 How many people have played a role called "The Stranger"?
import pandas as pd
csv_file = "cast.csv"

df = pd.read_csv(csv_file)

the_stranger_roles = df[df['character'] == 'The Stranger']

num_the_stranger_actors = the_stranger_roles['name'].nunique()

print(f'The number of people who have played a role called "The Stranger" is: {num_the_stranger_actors}')


# In[13]:


#23 How many roles has Sidney Poitier played throughout his career?
import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

sidney_poitier_roles = df[df['name'] == 'Sidney Poitier']

num_sidney_poitier_roles = sidney_poitier_roles['character'].nunique()

print(f'Sidney Poitier has played {num_sidney_poitier_roles} roles throughout his career.')


# In[14]:


#24 How many roles has Judi Dench played?
import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

judi_dench_roles = df[df['name'] == 'Judi Dench']

num_judi_dench_roles = judi_dench_roles['character'].nunique()

print(f'Judi Dench has played {num_judi_dench_roles} roles throughout her career.')


# In[15]:


#25 List the supporting roles (having n=2) played by Cary Grant in the 1940s, in order by year.
import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

cary_grant_supporting_roles_1940s = df[(df['name'] == 'Cary Grant') & (df['n'] == 2) & (df['year'] >= 1940) & (df['year'] <= 1949)]

cary_grant_supporting_roles_1940s = cary_grant_supporting_roles_1940s.sort_values(by='year')

print(cary_grant_supporting_roles_1940s[['year', 'character']])


# In[16]:


#26 List the leading roles that Cary Grant played in the 1940s in order by year
import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

cary_grant_leading_roles_1940s = df[(df['name'] == 'Cary Grant') & (df['n'] == 1) & (df['year'] >= 1940) & (df['year'] <= 1949)]

cary_grant_leading_roles_1940s = cary_grant_leading_roles_1940s.sort_values(by='year')

print(cary_grant_leading_roles_1940s[['year', 'character']])


# In[17]:


#27 How many roles were available for actors in the 1950s?
import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

roles_1950s = df[(df['year'] >= 1950) & (df['year'] <= 1959)]

num_roles_1950s = roles_1950s.shape[0]

print(f'The number of roles available for actors in the 1950s is: {num_roles_1950s}')


# In[18]:


#28 How many roles were available for actresses in the 1950s?
import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

actress_roles_1950s = df[(df['year'] >= 1950) & (df['year'] <= 1959) & (df['type'] == 'actress')]

num_actress_roles_1950s = actress_roles_1950s.shape[0]

print(f'The number of roles available for actresses in the 1950s is: {num_actress_roles_1950s}')


# In[20]:


#29 How many leading roles (n=1) were available from the beginning of film history through 1980?
import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

leading_roles_until_1980 = df[(df['year'] <= 1980) & (df['n'] == 1)]

num_leading_roles_until_1980 = leading_roles_until_1980.shape[0]

print(f'The number of leading roles (n=1) available from the beginning of film history through 1980 is: {num_leading_roles_until_1980}')


# In[21]:


#30  How many non-leading roles were available through from the beginning of film history through 1980?
import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

non_leading_roles_until_1980 = df[(df['year'] <= 1980) & (df['n'] != 1)]

num_non_leading_roles_until_1980 = non_leading_roles_until_1980.shape[0]

print(f'The number of non-leading roles (n values other than 1) available from the beginning of film history through 1980 is: {num_non_leading_roles_until_1980}')


# In[22]:


#31  How many roles through 1980 were minor enough that they did not warrant a numeric "n" rank?
import pandas as pd

csv_file = "cast.csv"

df = pd.read_csv(csv_file)

roles_without_n_rank_until_1980 = df[(df['year'] <= 1980) & df['n'].isna()]

num_roles_without_n_rank_until_1980 = roles_without_n_rank_until_1980.shape[0]

print(f'The number of roles through 1980 that did not warrant a numeric "n" rank is: {num_roles_without_n_rank_until_1980}')

