import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

st.title("Online Shopping Data")

df = pd.read_csv(r"C:\Users\agata\Desktop\Komunikacja wizualna\file.csv")
df = df.replace("F","Female")
df = df.replace("M","Male")
df = df[df['CustomerID'].notna()]
df2 = df.drop_duplicates(subset=["CustomerID"])
cities = df2["Location"].value_counts().index.tolist()
location = df2["Location"].value_counts()

data_by_gender_and_city = []

for city in cities:
    miasto = df[df['Location'] == city]
    data_by_gender = []

    for gender in ["Female", "Male"]:
        gender_data = miasto[miasto["Gender"] == gender]
        data_by_gender.append({
            "Gender": gender,
            "Average_Tenure_Months": np.mean(gender_data["Tenure_Months"]),
            "Average_Online_Spend": np.mean(gender_data["Online_Spend"]),
            "Count": len(gender_data),
            "City": city
        })

    data_by_gender_and_city.extend(data_by_gender)



# Opcje dla płci
selected_gender = st.multiselect(label='Select gender', options=["Female", "Male"], default=["Female", "Male"])

# Opcje dla miast
selected_city = st.multiselect(label='Select city', options=cities, default=cities)

# Dodaj slidery do interakcji
x_axis_limit = st.slider('Set x-axis limit', min_value=14, max_value=40, value=(23,31))
y_axis_limit = st.slider('Set y-axis limit', min_value=1350, max_value=2500, value=(1700,2150))
# Filtruj dane na podstawie wybranych opcji
filtered_data = [entry for entry in data_by_gender_and_city if entry["Gender"] in selected_gender and entry["City"] in selected_city]

# Mapowanie kolorów na płeć
colors_plec = {'Male': 'royalblue', 'Female': 'hotpink'}
plec_colors = [colors_plec[p] for p in [entry["Gender"] for entry in filtered_data]]

# Mapowanie kolorów obramowania na miasto
colors_miasto = {cities[0]: 'red', cities[1]: 'limegreen', cities[2]: 'dimgray', cities[3]: 'orange', cities[4]: 'purple'}
miasto_colors = [colors_miasto[m] for m in [entry["City"] for entry in filtered_data]]

# Dostosowanie rozmiarów bąbelków do skali wykresu
rozmiary = [entry["Count"] / 7 for entry in filtered_data]

# Tworzenie interaktywnego wykresu
fig, ax = plt.subplots()
scatter = ax.scatter([entry["Average_Tenure_Months"] for entry in filtered_data],
                    [entry["Average_Online_Spend"] for entry in filtered_data],
                    s=rozmiary, c=plec_colors, edgecolors=miasto_colors, linewidths=3)

# Dodanie pustych okręgów przy płciach w legendzie
legend_elements_plec = [Line2D([0], [0], marker='o', color='w', markerfacecolor=colors_plec[p], markersize=10, label=p) for p in set(colors_plec)]

# Dodanie pustych okręgów przy miastach w legendzie
legend_elements_miasto = [Line2D([0], [0], marker='o', color='w', markerfacecolor='white', markeredgecolor=colors_miasto[m], markersize=10, label=m) for m in set(colors_miasto)]

# Umieszczenie legendy w jednym miejscu
ax.legend(handles=legend_elements_plec + legend_elements_miasto, title='Legend', loc='upper right')

ax.set_xlabel('Average number of months the customers have been\nassociated with the platform [months]', labelpad=10)
ax.set_ylabel('Average amount spent online by the customers [$]', labelpad=10)

# Dodaj interaktywność do wykresu


# Zaktualizuj limity osi
ax.set_xlim([x_axis_limit[0], x_axis_limit[1]])
ax.set_ylim([y_axis_limit[0], y_axis_limit[1]])


st.pyplot(fig)
