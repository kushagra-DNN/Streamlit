import streamlit as st

# st.write('Hello world')
# a = st.text_input('Favourite movie')
# st.write(f'You favourite movie is {a}')
# is_clicked = st.button('Click me')

#st.write('## Hello Kushagra')

import pandas as pd

st.title('Global alignment')

seq1 = st.text_input('Type your first sequence')
seq2 = st.text_input('Type your second sequence')

#seq1 = 'ATGC'
#seq2 = 'TGC'



m = len(seq1)                                   #Seq1 will be the vertical sequence to the left
n = len(seq2)                                   #Seq2 will be the horizontal sequence on top
a = []                                          #Initialised matrix

#Scoring system for match, mismatch and gap:
match = 1
mismatch = -1
gap = -2

        
    
import numpy as np
a = np.zeros((m+1, n+1), dtype=int)

for j in range(n+1):
    a[0][j] = gap*j 

for i in range(m+1):
    a[i][0] = gap*i 
    
#print(a)

for i in range(1,m+1):
    for j in range(1, n+1):
        if seq1[i-1] == seq2[j-1]:
            a[i][j] = max(a[i][j-1]+gap, a[i-1][j]+gap, a[i-1][j-1]+match)
        else:
            a[i][j] = max(a[i][j-1]+gap, a[i-1][j]+gap, a[i-1][j-1]+mismatch)

st.write(a)

#background-color:#ff0000;

page_bg_img = '''
<style>
[data-testid='stAppViewContainer']{ 
background-image: url("https://www.unsw.edu.au/content/dam/images/science/general/research/2021-10-science/2021-10-a-microscopic-image-of-a-human-dna-strand.cropimg.width=1920.crop=square.png");
background-size:cover;
}
</style>
''' 
st.markdown(page_bg_img, unsafe_allow_html=True)