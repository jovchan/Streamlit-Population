import streamlit as st
import requests
import pandas as pd
import json as js

#from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode as AgGrid

url = "https://world-population3.p.rapidapi.com/continents/Europe"

querystring = {"rank":"1"}

headers = {
    'X-RapidAPI-Key': 'a5f5a9b506msh805e4bf54d3c310p162c0cjsn524d5e8e428f',
    'X-RapidAPI-Host': 'world-population3.p.rapidapi.com'
}



url2="https://world-population3.p.rapidapi.com/continents/"


option = st.selectbox("Continent",("Asia","Africa","North America", "South America", "Europe",  "Australia"))
if(option == "Asia"):
    url2+= "Asia"
if(option == "Africa"):
    url2+= "Africa"
if(option == "North America"):
    url2+= "North America"
if(option == "South America"):
    url2+= "South America"
if(option == "Europe"):
    url2+= "Europe"
if(option == "Australia"):
    url2+= "Australia"

Option_chart =[]   
response = requests.get(url2,headers=headers, params=querystring)
if(response):
    json = response.json()

    st.dataframe(json)

    for i in range(len(json)):
        Option_chart.append(json[i]["Country"])

    Option_chart.sort()
    data_Option = st.selectbox("Country",Option_chart)

    for v in range(len(json)):
        if json[v]["Country"] == data_Option:
            data_chart = json[v]
            break

    #st.dataframe(data_chart)

    my_iter = iter(data_chart)
    for i in range(0,5):
        col = next(my_iter)

    col = {}
    for i in range(0,8):
        temp = next(my_iter)
        col[i] = temp
    #st.write(data_chart[col[0]])
    ##final_chart = pd.DataFrame(data=[
    ##    [data_chart[col[0]],data_chart[col[1]], data_chart[col[2]], data_chart[col[3]], data_chart[col[4]],data_chart[col[5]],data_chart[col[6]],data_chart[col[7]]]
        
    ##    ],
    ##    columns=[
    ##       [col[0],col[1],col[2],col[3],col[4],col[5],col[6],col[7]]
            
    ##])

    ##st.dataframe(final_chart)


    final_chart_temp = {
        col[0]:data_chart[col[0]],
        col[1]:data_chart[col[1]],
        col[2]:data_chart[col[2]],
        col[3]:data_chart[col[3]],
        col[4]:data_chart[col[4]],
        col[5]:data_chart[col[5]],
        col[6]:data_chart[col[6]],
        col[7]:data_chart[col[7]],
    }
    y = js.dumps(final_chart_temp)

    #st.dataframe(final_chart_temp)
    st.line_chart(data=final_chart_temp)
else :
    st.write("Server Down")    

#response = requests.get(url,headers=headers, params=querystring)

#json_data = response.json()
#st.write(json_data[0]["2022 Population"])
#st.write(len(json_data))

#my_iter = iter(json_data[0])
#years = ""
#for i in range(0, 6):
    #years = next(my_iter)
#st.write(json_data[0][years])

#st.write(json_data)

