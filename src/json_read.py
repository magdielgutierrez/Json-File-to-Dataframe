import json
import pandas as pd

# DECLARAMOS UN DICCIONARIO PARA LOS VALORES DEL DATAFRAME 
list_data={"GRUPO":[],"ID":[],"NAME":[]}

#------------------------------------------------------------------------------
# LECTURA DE ARCHIVO JSON --> HACIA DICCIONARIO  
with open("extension.json", encoding='utf-8-sig', errors='ignore') as json_data:
     data_json = json.load(json_data, strict=False)
     
#------------------------------------------------------------------------------
# ACCESO A LOS KEY DEL NIVEL 1 Y 2 DEL DICCIONARIO
access_nivel_1_de_json= data_json['data']
access_nivel_2_de_json= access_nivel_1_de_json['items']

#------------------------------------------------------------------------------
# ITERAMOS CON EL NIVEL 2 QUE ES UNA LISTA DE DICCIONARIO
for i in access_nivel_2_de_json:
    # EXTRAEMOS CADA POSICION EN FORMATO LISTA QUE LUEGO ITERAMOS
    items_data=i['extensionUserPropertyListEntries']
    for x_set in items_data:
        # AÑADIMOS CADA KEY AL DICCIONARIO PARA DATAFRAME
        list_data['GRUPO'].append(i["id"])
        list_data['ID'].append(x_set["id"])
        list_data['NAME'].append(x_set["name"])
 
#------------------------------------------------------------------------------
# PASAMOS DEL DICCIONARIO A DATAFRAME           
df_random_values = pd.DataFrame.from_dict(list_data,orient='index')
# TRASPONER COLUMNAS A FILAS 
df_random_values = df_random_values.T

#------------------------------------------------------------------------------
# SALIDA DE DATAFRAME 
print("Tamaño de dataframe: ", df_random_values.shape[0],end="\n")
print(df_random_values.sample(20))