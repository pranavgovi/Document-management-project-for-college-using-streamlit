
from datetime import date
from tkinter.ttk import Style

import numpy as np
import math
import pandas as pd
import plotly.express as px
import streamlit as st
from IPython.display import display
from PIL import Image
# importing the modules
from tabulate import tabulate
import re
from streamlit_option_menu import option_menu
from docx import Document
st.set_page_config(page_title='HEALTH CARE')
st.header('DASHBOARD FOR HEALTH CARE')
# st.subheader('Was the tutorial helpful?')
# importing openpyxl module
import openpyxl as xl
from openpyxl import Workbook
import datetime
data = pd.read_csv("train.csv") #path folder of the data file
st.write(data) #displays the table of data
dept=data['Department']
dic={}
for i in dept:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for key,val in dic.items():

    st.subheader('{} {}'.format(key, val))


