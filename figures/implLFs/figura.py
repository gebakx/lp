import streamlit as st

s = '''
graph g {
n1 [label="@"]
n2 [label="@"]
n1 -- n2
n3 [label="e3"]
n1 -- n3
n4 [label="@"]
n2 -- n4
n5 [label="e2"]
n2 -- n5
n6 [label="f"]
n4 -- n6
n7 [label="e1"]
n4 -- n7
}

'''

st.graphviz_chart(s)
