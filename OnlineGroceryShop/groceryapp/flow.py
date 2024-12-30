from graphviz import Digraph

# Create a new Digraph object
flow_diagram = Digraph("SystemFlow", format='png')
flow_diagram.attr(rankdir='LR', size='8,5')

# Define the entities (User, Admin, Database)
flow_diagram.attr('node', shape='box', style='filled', color='lightblue')

# User Column
flow_diagram.node('U1', 'User: Open Website')
flow_diagram.node('U2', 'User: Browse Products')
flow_diagram.node('U3', 'User: Add to Cart')
flow_diagram.node('U4', 'User: Checkout')
flow_diagram.node('U5', 'User: Sign In/Register')
flow_diagram.node('U6', 'User: Add Address & Payment')
flow_diagram.node('U7', 'User: Place Order')
flow_diagram.node('U8', 'User: Track Order')
flow_diagram.node('U9', 'User: Receive Order Confirmation')

# Admin Column
flow_diagram.node('A1', 'Admin: Log In to Website')
flow_diagram.node('A2', 'Admin: Add/Edit Products')
flow_diagram.node('A3', 'Admin: Check Orders')
flow_diagram.node('A4', 'Admin: Update Order Status')

# Database Column
flow_diagram.node('D1', 'Database: Store Website Data')
flow_diagram.node('D2', 'Database: Retrieve Product Data')
flow_diagram.node('D3', 'Database: Store Cart Information')
flow_diagram.node('D4', 'Database: Validate User Details')
flow_diagram.node('D5', 'Database: Store Payment Details')
flow_diagram.node('D6', 'Database: Store Order Information')
flow_diagram.node('D7', 'Database: Retrieve Order Status')
flow_diagram.node('D8', 'Database: Admin Login Validation')
flow_diagram.node('D9', 'Database: Update Product Details')
flow_diagram.node('D10', 'Database: Retrieve Order Details')
flow_diagram.node('D11', 'Database: Store Transaction Details')

# Arrows from User actions to Database
flow_diagram.edge('U1', 'D1', label='Store Website Access')
flow_diagram.edge('U2', 'D2', label='Retrieve Products')
flow_diagram.edge('U3', 'D3', label='Store Cart Items')
flow_diagram.edge('U4', 'U5', label='Proceed to Sign In')
flow_diagram.edge('U5', 'D4', label='Validate User')
flow_diagram.edge('U6', 'D5', label='Store Payment Info')
flow_diagram.edge('U7', 'D6', label='Store Order Details')
flow_diagram.edge('U8', 'D7', label='Get Order Status')

# Arrows from Admin actions to Database
flow_diagram.edge('A1', 'D8', label='Admin Login')
flow_diagram.edge('A2', 'D9', label='Update Product Catalog')
flow_diagram.edge('A3', 'D10', label='Check Order Status')
flow_diagram.edge('A4', 'D6', label='Update Order Status')

# Flow between Database components
flow_diagram.edge('D1', 'D2', label='Fetch Data')
flow_diagram.edge('D6', 'D7', label='Update Order Progress')

# Save and render the diagram
flow_diagram.render('system_flow_diagram')
