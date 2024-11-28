import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Affichage de l'uploader dans l'application Streamlit
file = st.file_uploader("Importer vos données ici", type=["csv"])

# Vérification si un fichier a été téléchargé
if file is not None:
    # Traitement du fichier téléchargé (par exemple, afficher les 5 premières lignes d'un DataFrame Pandas)
    df = pd.read_csv(file)
    st.dataframe(df)
    
    # Filtrage selon une catégorie donnée(setosa dans notre cas actuel)
    selected_value = st.selectbox("Filtrage par rapport à la colonne setosa :", df["setosa"].unique())
    filtered_data = df[df["setosa"] == selected_value]
    st.dataframe(filtered_data)

    # Ajout de colonnes 
    df["new_column"] = df["0.2"] * 2
    st.dataframe(df)

# Création d'un graphique avec Matplotlib
print("Ajout de la colonne 0.2 en multipliant ses éléments par deux")
x = np.linspace(- 2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)

# Affichage du graphique avec st.pyplot
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)


    
    