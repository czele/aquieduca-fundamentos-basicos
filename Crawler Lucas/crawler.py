from flask import Flask
import requests
from bs4 import BeautifulSoup
from flask import Flask
app = Flask(__name__)

@app.route("/get", methods=['GET'])
def get():

    url = 'https://webscraper.io/test-sites/tables'
    print('\n\n======================\n\n')
    response = requests.get(url)
    #print (response)

    html_string = response.text
    #print(html_string)

    soup = BeautifulSoup(html_string, "html.parser")
    #print(soup)

    tablerow = soup.find_all('tr')
    #print(tablerow[1])

    tabledata = tablerow[2].find_all('td')
    #print(tabledata)

    user ={
        "numero":"",
        "pnome":"",
        "snome":"",
        "user":""
    }
    #print(user)

    listafiltrado = []

    for elemento in tabledata:
        # filtrado = str(elemento).replace("<td>","")
        # filtrado = filtrado.replace("</td>","")
        # #print(filtrado)
        filtrado = elemento.text
        #print(filtrado)
        listafiltrado.append(filtrado)
    #print(listafiltrado)



    user["numero"]=listafiltrado[0]
    user["pnome"]=listafiltrado[1]
    user["snome"]=listafiltrado[2]
    user["user"]=listafiltrado[3]
    print(user)
