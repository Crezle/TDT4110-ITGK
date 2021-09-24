#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving2.ipynb">Øving 2</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li><a href="Ulike%20typer%20if-setninger.ipynb">Ulike typer if-setninger</a></li>
#     <li><a href="Sammenligning%20av%20strenger.ipynb">Sammenligning av strenger</a></li>
#     <li><a href="Logiske%20operatorer%20og%20logiske%20uttrykk.ipynb">Logiske operatorer og logiske uttrykk</a></li>
#     <li><a href="Forbrytelse%20og%20straff.ipynb">Forbrytelse og straff</a></li>
#     <li class="active"><a href="Aarstider.ipynb">Årstider</a></li>
#         <li ><a href="Tekstbasert%20spill.ipynb">Tekstbasert spill</a></li>
#     <li><a href="Sjakkbrett.ipynb">Sjakkbrett</a></li>
#     <li><a href="Billettpriser%20og%20rabatter.ipynb">Billettpriser og rabatter</a></li>
#     <li><a href="Skatteetaten.ipynb">Skatteetaten</a></li>
#     <li><a href="Epletigging.ipynb">Datamaskinen som tigget epler</a></li>
#     <li><a href="Andregradsligning.ipynb">Andregradsligning</a></li>
#     </ul>
#   </div>
# </nav>
# 
# 
# # Årstider
# 
# **Læringsmål:**
# - Betingelser
# - Logiske uttrykk
# 
# **Starting Out with Python:**
# - Kap. 3.3-3.5
# 
# I denne oppgaven skal en bruker skrive inn dag og måned og få ut hvilken årstid datoen tilhører.
# 
# Et år har (offisielt) fire årstider, og i denne oppgaven tar vi utgangspunkt i at årstidsskiftene følger tabellen nedenfor. **(Merk deg datoene)**
# 
# 
# Årstid | Første dag
# --- | ---
# Vår | 20. mars
# Sommer | 21. juni
# Høst | 22. september
# Vinter | 21. desember

# **Oppgave:** Lag et program som tar inn en måned som en streng og en dag i denne måneden som et tall fra brukeren. Programmet skal så skrive ut årstiden assosiert med denne datoen.
# 
# Du kan anta at inputen er en gyldig dato.
# 
# **Eksempel på kjøring:**
# ```
# Måned: mars
# Dag: 20
# Vår
# ```  
#   
# ```
# Måned: mars
# Dag: 19
# Vinter
# ```  
#   
# ```
# Måned: november
# Dag: 20
# Høst
# ```
# 
# ___Skriv din kode her:___

# In[20]:


mnd=str(input("Oppgi en måned: "))
dag=int(input("Oppgi en dag (nr): "))
if mnd.lower() == "februar" and (0<dag<=28):
    ses="Vinter"
    print("Måned:", mnd)
    print("Dag:", dag)
    print(ses)
elif (mnd.lower() == "april" or mnd.lower() == "juni" or mnd.lower() == "september" or mnd.lower() == "november") and (0<dag<=30):
    if mnd.lower() == "april":
        ses="Vår"
        print("Måned:", mnd)
        print("Dag:", dag)
        print(ses)
    elif mnd.lower() == "juni":
        ses="Sommer"
        print("Måned:", mnd)
        print("Dag:", dag)
        print(ses)
    elif mnd.lower() == "september" or mnd.lower() == "november":
        ses="Høst"
        print("Måned:", mnd)
        print("Dag:", dag)
        print(ses)
elif (mnd.lower() == "januar" or mnd.lower() == "mars" or mnd.lower() == "mai" or mnd.lower() == "juli" or mnd.lower() == "august" or mnd.lower() == "oktober" or mnd.lower() == "desember") and (0<dag or dag<=31):
    if mnd.lower() == "desember" or mnd.lower() == "januar":
        ses="Vinter"
        print("Måned:", mnd)
        print("Dag:", dag)
        print(ses)
    elif mnd.lower() == "mars" or mnd.lower() == "mai":
        ses="Vår"
        print("Måned:", mnd)
        print("Dag:", dag)
        print(ses)
    elif mnd.lower() == "juli" or mnd.lower() == "august":
        ses="Sommer"
        print("Måned:", mnd)
        print("Dag:", dag)
        print(ses)
    elif mnd.lower() == "oktober":
        ses="Høst"
        print("Måned:", mnd)
        print("Dag:", dag)
        print(ses)
else:
        print("Oppgitte datoen er ugyldig")

