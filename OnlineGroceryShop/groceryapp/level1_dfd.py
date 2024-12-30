from graphviz import Digraph

# Create a new directed graph for Level 0 DFD
dfd = Digraph("DFD_Level_0", format="png")
dfd.attr(rankdir='RL', size='10,6',dpi='300')


# Add external entities
dfd.node('User', shape='rectangle', style='filled', color='lightblue', label='User', fontsize='14', width='1.5')
dfd.node('Website', shape='ellipse', label='Online Grocery Website', fontsize='14', width='2')
dfd.node('Admin', shape='rectangle', style='filled', color='lightgreen', label='Admin', fontsize='14', width='1.5')

# User interactions with the website
dfd.edge('User', 'Website', label='Request (Browse, Order, Register)', fontsize='12')
dfd.edge('Website', 'User', label='Response (Product Info, Order Confirmation)', fontsize='12')

# Admin interactions with the website
dfd.edge('Admin', 'Website', label='Manage Website (Update Products, View Orders)', fontsize='12')

# Render and view the diagram
dfd.render("level_0_dfd")
