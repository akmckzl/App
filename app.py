import streamlit as st
import pandas as pd
import numpy as np
#df=pd.read_csv("file.csv")
st.title("blabla")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

df=pd.read_csv(r"C:\Users\agata\Desktop\Komunikacja wizualna\file.csv")
df = df[df['CustomerID'].notna()]
df2 = df.drop_duplicates(subset=["CustomerID"])
cities=df2["Location"].value_counts().index.tolist()
location=df2["Location"].value_counts()

miasto = df[df['Location']==cities[0]]
kob=miasto[miasto["Gender"]=="F"]
mez=miasto[miasto["Gender"]=="M"]
miasto2 = df[df['Location']==cities[1]]
kob2=miasto2[miasto2["Gender"]=="F"]
mez2=miasto2[miasto2["Gender"]=="M"]
miasto3= df[df['Location']==cities[2]]
kob3=miasto3[miasto3["Gender"]=="F"]
mez3=miasto3[miasto3["Gender"]=="M"]
miasto4 = df[df['Location']==cities[3]]
kob4=miasto4[miasto4["Gender"]=="F"]
mez4=miasto4[miasto4["Gender"]=="M"]
miasto5 = df[df['Location']==cities[4]]
kob5=miasto5[miasto5["Gender"]=="F"]
mez5=miasto5[miasto5["Gender"]=="M"]





# Przykładowe dane (możesz dostosować do swoich danych)
sredni_czas = [np.mean(kob["Tenure_Months"]),np.mean(mez["Tenure_Months"]),np.mean(kob2["Tenure_Months"]),np.mean(mez2["Tenure_Months"]),np.mean(kob3["Tenure_Months"]),np.mean(mez3["Tenure_Months"]),np.mean(kob4["Tenure_Months"]),np.mean(mez4["Tenure_Months"]),np.mean(kob5["Tenure_Months"]),np.mean(mez5["Tenure_Months"])]
srednia_kwota = [np.mean(kob["Online_Spend"]),np.mean(mez["Online_Spend"]),np.mean(kob2["Online_Spend"]),np.mean(mez2["Online_Spend"]),np.mean(kob3["Online_Spend"]),np.mean(mez3["Online_Spend"]),np.mean(kob4["Online_Spend"]),np.mean(mez4["Online_Spend"]),np.mean(kob5["Online_Spend"]),np.mean(mez5["Online_Spend"])]
plec = ["Female","Male","Female","Male","Female","Male","Female","Male","Female","Male"]
liczba_ludzi = [len(kob),len(mez),len(kob2),len(mez2),len(kob3),len(mez3),len(kob4),len(mez4),len(kob5),len(mez5)]
miasto = [cities[0],cities[0],cities[1],cities[1],cities[2],cities[2],cities[3],cities[3],cities[4],cities[4]]

# Mapowanie kolorów na płeć
colors_plec = {'Male': 'royalblue', 'Female': 'hotpink'}
plec_colors = [colors_plec[p] for p in plec]

# Mapowanie kolorów obramowania na miasto
colors_miasto = {cities[0]: 'red', cities[1]: 'limegreen', cities[2]: 'dimgray', cities[3]: 'orange', cities[4]: 'purple'}
miasto_colors = [colors_miasto[m] for m in miasto]

# Dostosowanie rozmiarów bąbelków do skali wykresu
rozmiary = [liczba/7 for liczba in liczba_ludzi]

# Stworzenie wykresu bąbelkowego
scatter = plt.scatter(sredni_czas, srednia_kwota, s=rozmiary, c=plec_colors, edgecolors=miasto_colors,  linewidths=3)

# Dodanie pustych okręgów przy płciach w legendzie
legenda_plec = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors_plec[p], markersize=10, label=p) for p in colors_plec]

# Dodanie pustych okręgów przy miastach w legendzie
legenda_miasto = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='white', markeredgecolor=colors_miasto[m], markersize=10, label=m) for m in colors_miasto]

plt.legend(handles=[*legenda_plec, *legenda_miasto], title='Legenda', loc='upper right')

# Dodanie etykiet osi
plt.xlabel('Average number of months the customers have been\nassociated with the platform [months]')
plt.ylabel('Average amount spent online by the customers [$]')
plt.title('Bubble Chart')

# Wyświetlenie wykresu
plt.show()

fig1, ax1 = plt.subplots()
ax1.scatter(sredni_czas, srednia_kwota, s=rozmiary, c=plec_colors, edgecolors=miasto_colors,  linewidths=3)
ax1.legend(handles=[*legenda_plec, *legenda_miasto], title='Legend', loc='upper right')
ax1.set_xlabel('Average number of months the customers have been\nassociated with the platform [months]',labelpad=10)
ax1.set_ylabel('Average amount spent online by the customers [$]',labelpad=10)

#ax1.axis('equal')  # wykres kołowy
#st.pyplot(fig1)
#cities[:0]=["Whole USA"]
options = st.multiselect(label='What are data are you interested in?',options=[cities[0],cities[1],cities[2],cities[3],cities[4],"Female","Male"],default=[cities[0],cities[1],cities[2],cities[3],cities[4],"Female","Male"])
st.write(options)  

if len(options) == 1:
    if cities[0] in options:
        st.pyplot(fig1)