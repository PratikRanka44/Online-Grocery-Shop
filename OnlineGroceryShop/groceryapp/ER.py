import graphviz

def generate_er_diagram():
    # Create a new Digraph
    dot = graphviz.Digraph(comment='Online Shopping Management System or E-Commerce ER Diagram')

    # Entities
    dot.node('Admin', 'Admin', shape='box', style='filled', color='gold')
    dot.node('Supplier', 'Supplier', shape='box', style='filled', color='gold')
    dot.node('ShoppingWebsite', 'Shopping Website', shape='box', style='filled', color='gold')
    dot.node('ProductCategory', 'Product Category', shape='box', style='filled', color='gold')
    dot.node('Product', 'Product', shape='box', style='filled', color='gold')
    dot.node('Customer', 'Customer', shape='box', style='filled', color='gold')
    dot.node('Order', 'Order', shape='box', style='filled', color='gold')
    dot.node('Payment', 'Payment', shape='box', style='filled', color='gold')
    dot.node('Cart', 'Cart', shape='box', style='filled', color='gold')
    dot.node('TrackingDetail', 'Tracking Detail', shape='box', style='filled', color='gold')

    # Relationships (diamonds)
    dot.node('Manage', 'Manage', shape='diamond', style='filled', color='black', fontcolor='white')
    dot.node('Supplies', 'Supplies', shape='diamond', style='filled', color='black', fontcolor='white')
    dot.node('Has', 'Has', shape='diamond', style='filled', color='black', fontcolor='white')
    dot.node('Contains', 'Contains', shape='diamond', style='filled', color='black', fontcolor='white')
    dot.node('Make', 'Make', shape='diamond', style='filled', color='black', fontcolor='white')
    dot.node('AddedTo', 'Added To', shape='diamond', style='filled', color='black', fontcolor='white')

    # Admin attributes
    dot.node('AdminId', 'Admin_Id', shape='ellipse')
    dot.node('AdminName', 'Admin_name', shape='ellipse')
    dot.node('AdminRole', 'Admin_role', shape='ellipse')
    dot.edge('Admin', 'AdminId')
    dot.edge('Admin', 'AdminName')
    dot.edge('Admin', 'AdminRole')

    # Supplier attributes
    dot.node('SupplierId', 'Supplier_Id', shape='ellipse')
    dot.node('SupplierName', 'Supplier_name', shape='ellipse')
    dot.node('SupplierAddress', 'Supplier_Address', shape='ellipse')
    dot.edge('Supplier', 'SupplierId')
    dot.edge('Supplier', 'SupplierName')
    dot.edge('Supplier', 'SupplierAddress')

    # Shopping Website attributes
    dot.node('WebsiteId', 'Website_Id', shape='ellipse')
    dot.node('WebsiteName', 'Website_name', shape='ellipse')
    dot.node('WebsiteUrl', 'Website_url', shape='ellipse')
    dot.edge('ShoppingWebsite', 'WebsiteId')
    dot.edge('ShoppingWebsite', 'WebsiteName')
    dot.edge('ShoppingWebsite', 'WebsiteUrl')

    # Product Category attributes
    dot.node('CategoryId', 'Category_Id', shape='ellipse')
    dot.node('CategoryName', 'Category_name', shape='ellipse')
    dot.edge('ProductCategory', 'CategoryId')
    dot.edge('ProductCategory', 'CategoryName')

    # Product attributes
    dot.node('ProductId', 'Product_Id', shape='ellipse')
    dot.node('ProductName', 'Product_name', shape='ellipse')
    dot.node('ProductPrice', 'Product_price', shape='ellipse')
    dot.edge('Product', 'ProductId')
    dot.edge('Product', 'ProductName')
    dot.edge('Product', 'ProductPrice')

    # Customer attributes
    dot.node('CustId', 'Cust_Id', shape='ellipse')
    dot.node('FName', 'F_Name', shape='ellipse')
    dot.node('LName', 'L_Name', shape='ellipse')
    dot.node('ContactNo', 'Contact_no', shape='ellipse')
    dot.node('Address', 'Address', shape='ellipse')
    dot.node('City', 'City', shape='ellipse')
    dot.node('State', 'State', shape='ellipse')
    dot.node('PinCode', 'Pin_code', shape='ellipse')
    dot.edge('Customer', 'CustId')
    dot.edge('Customer', 'FName')
    dot.edge('Customer', 'LName')
    dot.edge('Customer', 'ContactNo')
    dot.edge('Customer', 'Address')
    dot.edge('Customer', 'City')
    dot.edge('Customer', 'State')
    dot.edge('Customer', 'PinCode')

    # Order attributes
    dot.node('OrderNo', 'Order_no', shape='ellipse')
    dot.node('OrderAmount', 'Order_Amount', shape='ellipse')
    dot.node('OrderDate', 'Order_date', shape='ellipse')
    dot.edge('Order', 'OrderNo')
    dot.edge('Order', 'OrderAmount')
    dot.edge('Order', 'OrderDate')

    # Payment attributes
    dot.node('PaymentNo', 'Payment_no', shape='ellipse')
    dot.node('PaymentDate', 'Payment_date', shape='ellipse')
    dot.node('PaymentAmount', 'Payment_amount', shape='ellipse')
    dot.edge('Payment', 'PaymentNo')
    dot.edge('Payment', 'PaymentDate')
    dot.edge('Payment', 'PaymentAmount')

    # Tracking Detail attributes
    dot.node('TrackingNo', 'Tracking_no', shape='ellipse')
    dot.node('CourierName', 'Courier_name', shape='ellipse')
    dot.edge('TrackingDetail', 'TrackingNo')
    dot.edge('TrackingDetail', 'CourierName')

    # Cart attributes
    dot.node('CartProductId', 'Product_Id', shape='ellipse')
    dot.node('Quantity', 'Quantity', shape='ellipse')
    dot.node('Size', 'Size', shape='ellipse')
    dot.edge('Cart', 'CartProductId')
    dot.edge('Cart', 'Quantity')
    dot.edge('Cart', 'Size')

    # Relationships between entities
    dot.edge('Admin', 'Manage')
    dot.edge('Manage', 'ShoppingWebsite')
    dot.edge('Supplier', 'Supplies')
    dot.edge('Supplies', 'Product')
    dot.edge('ShoppingWebsite', 'Has')
    dot.edge('Has', 'ProductCategory')
    dot.edge('ProductCategory', 'Has')
    dot.edge('Has', 'Product')
    dot.edge('Customer', 'Make')
    dot.edge('Make', 'Order')
    dot.edge('Make', 'Payment')
    dot.edge('Order', 'Contains')
    dot.edge('Contains', 'Product')
    dot.edge('Order', 'Has')
    dot.edge('Has', 'TrackingDetail')
    dot.edge('Product', 'AddedTo')
    dot.edge('AddedTo', 'Cart')

    # Render the graph to a file
    dot.render('er_diagram', format='png', cleanup=True)

# Call the function to generate the ER diagram
generate_er_diagram()
