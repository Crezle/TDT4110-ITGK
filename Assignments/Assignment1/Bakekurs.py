#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving1.ipynb">Øving 1</a>
#     </div>
#     <ul class="nav navbar-nav">
#         <li><a href="Intro%20til%20jupyter.ipynb">Intro til Jupyter</a></li>
#       <li ><a href="Jeg%20elsker%20ITGK!.ipynb">Jeg elsker ITGK!</a></li>
#     <li ><a href="Kalkulasjoner.ipynb">Kalkulasjoner</a></li>
#     <li><a href="Input%20og%20variable.ipynb">Input og variable</a></li>
#     <li><a href="Tallkonvertering.ipynb">Tallkonvertering</a></li>
#     <li ><a href="Peppes%20Pizza.ipynb">Peppes Pizza</a></li>
#     <li ><a href="Geometri.ipynb">Geometri</a></li>
#     <li ><a href="Vitenskapelig%20notasjon.ipynb">Vitenskapelig notasjon</a></li>
#     <li ><a href="Tetraeder.ipynb">Tetraeder</a></li>
#     <li class="active"><a href="Bakekurs.ipynb">Bakekurs</a></li>
#     <li ><a href="James%20Bond%20and%20Operation%20round().ipynb">James Bond and Operation Round</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Bakekurs
# 
# **Læringsmål:**
# 
# * Printe ut tekst til skjerm på en fin måte
# 
# * Kalkulasjoner i Python
# 
# **Starting Out with Python:**
# 
# * Kap. 2.3
# 
# * Kap. 2.8
# 
# * Kap. 8
# 
# I denne oppgaven skal du beregne mengden ingredienser som trengs for å lage cookies og printe resultatet på et fint format. 
# 
# Du skal lage cookies og har en oppskrift som gir 48 cookies. Den oppskriften krever følgende ingredienser:
# 
# * 400 g sukker 
# * 320 g smør
# * 500 g sjokolade
# * 2 egg 
# * 460 g hvetemel 

# ## a)

# Spør brukeren om hvor mange cookies han eller hun ønsker å bake og skriv ut hvor mange ingredienser som trengs for å lage så mange cookies.
# 
# Eksempel på kjøring:
# 
#   
# ```python
# Hvor mange cookies ønsker du å bake? 24
# Antall cookies: 24 
# sukker(g): 200.0
# smør(g): 160.0
# sjokolade(g): 250.0
# egg: 1.0
# hvetemel(g): 230.0
# ```
#     
# ***Skriv koden din i blokka under.***

# In[1]:


cookies=int(input("Hvor mange cookies ønsker du å bake? "))
print("Antall cookies:", cookies)
sukker=(400/48)*cookies
smør=(320/48)*cookies
sjoko=(500/48)*cookies
egg=(2/48)*cookies
mel=(460/48)*cookies
print("sukker(g):", sukker)
print("smør(g):", smør)
print("sjokolade(g):", sjoko)
print("egg:", egg)
print("mel:", mel)


# #### Tips til oppgave a: Escape Character

# `\n` er nyttig å bruke her for å få en ny linje! Eks. `print(“hei\npå\ndeg”)` gir
# 
# **Utskrift**
#   
# ```
# hei  
# på  
# deg
# ```

# ## b)

# Be brukeren om hvor mange cookies han eller hun ønsker å lage tre ganger og skriv ut ingrediensene på en fin og elegant måte. Du trenger kun å skrive ut antall cookies, og hvor mye sjokolade og sukker som trengs i gram.
# 
# Eksempel på kjøring:
# 
#   
# ```python
# Hvor mange cookies vil du lage? 24
# og hvor mange cookies vil du lage nå? 48
# og hvor mange cookies vil du lage til slutt? 72
# Antall cookies:        sukker(g)    sjokolade(g)
# 24                         200.0           250.0
# 48                         400.0           500.0
# 72                         600.0           750.0
# ```
# 
# `rjust()` og `ljust()` er nyttige funksjoner her, men for å bruke dem må man først konvertere antall cookies til en streng vha. `str()`. Andre ting som kan være nyttig er `\t` som lager et innrykk i teksten.
# 
# ***Skriv koden din i blokka under.***

# In[13]:


cookies1=int(input("Hvor mange cookies vil du lage? "))
cookies2=int(input("og hvor mange cookies vil du lage nå? "))
cookies3=int(input("og hvor mange cookies vil du lage til slutt? "))
sukker1=str((400/48)*cookies1).rjust(20)
sukker2=str((400/48)*cookies2).rjust(20)
sukker3=str((400/48)*cookies3).rjust(20)
sjoko1=str((500/48)*cookies1).rjust(20)
sjoko2=str((500/48)*cookies2).rjust(20)
sjoko3=str((500/48)*cookies3).rjust(20)
cookie1=str(cookies1).ljust(20)
cookie2=str(cookies2).ljust(20)
cookie3=str(cookies3).ljust(20)
cookie="Antall cookies:"
sukker='sukker(g)'
sjoko="sjokolade(g)"
lcookie=cookie.ljust(20)
rsukker=sukker.rjust(25)
rsjoko=sjoko.rjust(20)

print("Antall cookies:", rsukker, rsjoko)
print(cookie1, sukker1, sjoko1)
print(cookie2, sukker2, sjoko2)
print(cookie3, sukker3, sjoko3)


# #### ljust() og rjust()

# `streng.ljust(width)` returnerer strengen "left justified" i en streng av lengde `width`. `streng.rjust(width)` gjør det sammen bare at strengen blir "right justified". For eksempel blir `print('hei'.rjust(15))` til:
# 
#   
# ```python
#            hei      #teksten printes altså ut etter 12 white spaces, ettersom strengen har lengde 3
# ```
#     
# Du kan lese mer om `rjust()` og `ljust()` [her](https://docs.python.org/2/library/stdtypes.html?highlight=rjust#str.rjust). 
