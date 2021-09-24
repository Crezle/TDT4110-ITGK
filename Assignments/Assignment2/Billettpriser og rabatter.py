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
#     <li><a href="Aarstider.ipynb">Årstider</a></li>
#         <li ><a href="Tekstbasert%20spill.ipynb">Tekstbasert spill</a></li>
#     <li><a href="Sjakkbrett.ipynb">Sjakkbrett</a></li>
#     <li class="active"><a href="Billettpriser%20og%20rabatter.ipynb">Billettpriser og rabatter</a></li>
#     <li><a href="Skatteetaten.ipynb">Skatteetaten</a></li>
#     <li><a href="Epletigging.ipynb">Datamaskinen som tigget epler</a></li>
#     <li><a href="Andregradsligning.ipynb">Andregradsligning</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Billettpriser og rabatter
# 
# **Læringsmål:**
# 
# * Betingelser
# 
# **Starting Out with Python:**
# 
# * Kap 3.1, 3.2, 3.4
# 
# I denne oppgaven skal du bruke betingelser (if-elif-else) til å bestemme billettprisen til en bruker basert på input fra brukeren. 
# 
# Transportselskapet «TravelevatoR» tilbyr reiser fra Trondheim til Pythonville. Ved bestilling minst 14 dager før man skal reise, kan man få minipris 199. Normal billett koster 440. 

# ### a)

# Skriv et program med to mulige oppførsler som vist under:
# 
#   
# ```python
# Dager til du skal reise? 15  
# Du kan få minipris: 199,-  
# >>>  
# Dager til du skal reise? 8  
# For sent for minipris; fullpris 440,-  
# ```
# ***Skriv koden din under***

# In[38]:


days=int(input("Dager til du skal reise? "))
minipris=199
fullpris=440
ungdomspris=fullpris*0.5
rabatt25=fullpris*0.75
if 0<=days<=14:
    print("Du kan få minipris:", minipris, ",-")
    print("Minipris", minipris, ",-", "kan ikke refunderes/endres")
    ans=input("Ønskes dette (J/N)? ")
    if ans.lower()=="j":
        print("Takk for pengene, god reise!")
    elif ans.lower()=="n":
        age=int(input("Skriv inn din alder: "))
        if 0<=age<=16:
            print("Prisen på billetten blir:", ungdomspris, ",-")
        elif age>=60:
            print("Prisen på billetten blir:", rabatt25, ",-")
        elif age>16:
            person=input("Er du student eller ansatt hos Forsvaret (J/N)? ")
            if person.lower()=="j":
                print("Prisen på billetten blir:", rabatt25, ",-")
            elif person.lower()=="n":
                print("Prisen på billetten blir:", fullpris, ",-")
            else:
                print("Ugyldig svar, prøv på nytt")
    else:
        print("Ugyldig svar, prøv på nytt")
elif 0>days:
    print("Ugyldig nummer, prøv på nytt")
else:
    print("For sent for minipris")
    age=int(input("Skriv inn din alder: "))
    if 0<=age<=16:
            print("Prisen på billetten blir:", ungdomspris, ",-")
    elif age>=60:
            print("Prisen på billetten blir:", rabatt25, ",-")
    elif age>16:
        person=input("Er du student eller ansatt hos Forsvaret (J/N)? ")
        if person.lower()=="j":
            print("Prisen på billetten blir:", rabatt25, ",-")
        elif person.lower()=="n":
            print("Prisen på billetten blir:", fullpris, ",-")
        else:
            print("Ugyldig svar, prøv på nytt")


# ### b)

# Det hender av og til at kunder ikke ønsker minipris, men heller vil ha fullprisbillett. Dette fordi minipris ikke kan refunderes / endres. Utvid derfor programmet så kunder spørres om de ønsker minipris – men kun der det er relevant. To eksempel på kjøring etter utvidelsen:
# 
#   
# ```python
# Dager til du skal reise? 17
# Minipris 199,- kan ikke refunderes/endres
# Ønskes dette (J/N)? J
# Takk for pengene, god reise!
# ```
#   
# ```python
# Dager til du skal reise? 17
# Minipris 199,- kan ikke refunderes/endres
# Ønskes dette (J/N)? N
# Da tilbyr vi fullpris: 440,-
# ```

# ### c)

# Det blir besluttet at barn under 16 gis 50% rabatt. Senior (60+), militær i uniform, og student gis 25% rabatt. Om man f.eks. både er 60+ og militær / student, får man likevel bare 25% rabatt. Alle disse rabattene gjelder kun i forhold til fullpris, for minipris gis ingen rabatter. Endre programmet så det spør kunden om alder, evt. også om student / militær, og regner ut riktig pris.
# 
# **NB:** De nye spørsmålene skal ***kun*** stilles når de er relevante, da det er et mål at kunden skal måtte svare på så få spørsmål som mulig.
# 
# Eksempel på kjøring av koden:
# 
#   
# ```python
# Dager til du skal reise? 17
# Minipris 199,- kan ikke refunderes/endres
# Ønskes dette (J/N)? N
# Skriv inn din alder: 15
# Prisen på biletten blir: 220,-
# ```

# ### d) Valgfri oppgave

# Du får godkjent oppgaven om du bare har klart a, b og delvis c, men prøv gjerne på denne litt vanskeligere d også.
# 
# Etter lobbyvirksomhet fra studentorganisasjoner endres reglene på følgende måte: Studenter får også litt rabatt på miniprisbilletter (10%),  samt at personer som både er studenter og militære  / 60+, eller studenter og barn, får to rabatter, og dermed bare betaler 0,75 * 0,75 eller 0.75 * 0.5 av fullpris. Merk at personer som er 60+ og militære, men ikke studenter, eller barn og militære, men ikke studenter, ikke får noen slik multiplisert rabatt, de må fortsatt nøye seg med den ene rabatten de hadde før, og de vanlige 199 for minipris. Endre programmet så det fungerer korrekt i forhold til de nye reglene.
