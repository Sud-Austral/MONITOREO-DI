import pandas as pd
import pyodbc

df = pd.read_excel("https://github.com/Sud-Austral/MONITOREO-DI/blob/main/000%20AGENCIA%20INFORMACION%20DI/agencia_informacion.xlsx?raw=true")

conection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=sud-austral.database.windows.net;Database=agencia;uid=sudaustral;pwd=Sud123456789")
cursor = conection.cursor()

def registro():
    c = ""
    print(df)
    for i, index in df.iterrows():

        _id = df["id"][i]

        # print(_id)

        query = "SELECT id FROM agencia_informacion WHERE id = " + str(_id)
        dfC = pd.read_sql(query, conection)

        if (len(dfC) >= 1):
            print("Actualizando id: " + str(_id))

            # index = df["id"].max();
            # index = index + 1;

            query = "UPDATE agencia_informacion SET "
            for j in df.columns[1:]:
                c += j  + "='" + str(df[j][i]).replace("'"," ") +"', "
            query = query + c + "WHERE id='" + str(_id) +"'"
            query = query.replace(", WHERE", " WHERE")
            cursor.execute(query)
            print(query)

            c = "" 
            conection.commit()

        else:
            print("Guardando id: " + str(_id))
            # index = df["id"].max()

            # index = index + 1
            query = "INSERT INTO agencia_informacion VALUES (" + str(_id) + ",'"
            for j in df.columns[1:]:
                query = query + str(df[j][i]).replace("'"," ") +  "','"
            query = query[:-2] + ");"
            print(query)
            cursor.execute(query)
            
        
        conection.commit()

if __name__ == "__main__":
    
    registro()