import click

from crud import (
    # --------------Suppliers---------------
    add_supplier, get_suppliers, delete_supplier,

    # --------------Suppy Orders---------------
    add_supply_order, get_all_supply_orders, update_supply_order_status, delete_supply_order,

    # --------------Product Categories---------------
    add_product_category, get_product_categories, delete_product_category,

    # --------------Product---------------
    add_product, get_all_products, delete_product,

    # --------------Customers---------------
    add_customer, get_customers, delete_customer,

    # --------------Customer Orders---------------
    add_order, get_orders, delete_order, update_order_status,

    # --------------Order Items---------------
    add_order_item, get_order_items,delete_order_item
)

while True:
    click.secho("-------------Welcome to the Electrical Appliances Database System------------", bold=True, fg='green')
    click.secho("Select Option  to Proceed", bold=True, fg='blue')
    click.secho("Select using the option's number", dim=True, fg='cyan')
    click.secho("1. Suppliers",fg='cyan')
    click.secho("2. Supply Orders",fg='cyan')
    click.secho("3. Product Categories",fg='cyan')
    click.secho("4. Products",fg='cyan')
    click.secho("5. Customers",fg='cyan')
    click.secho("6. Customer Orders",fg='cyan')
    click.secho("7. Customer Order items",fg='cyan')

    user_input = click.prompt("Option", type=int)

    if user_input == 1:
        click.secho("--------------  Suppliers' Options  -----------", fg='green')
        click.secho("Select an Option", dim=True, fg='blue')
        click.secho("1. Add New Supplier" ,fg='cyan')
        click.secho("2. View Company Suppliers",fg='cyan')
        click.secho("3. Delete Supplier",fg='cyan')

        supplier_option = click.prompt("Option", type=int)

        if supplier_option == 1:
            click.secho("Adding New Supplier......", dim='True',fg='cyan')
            name = click.prompt("Enter name")
            email = click.prompt("Enter email")
            phone = click.prompt("Enter phone")
            address = click.prompt("Enter Address")

            try:
                add_supplier(name, email, phone, address)
            except:
                raise Exception(f"Error adding of {name} as a Supplier")

        if supplier_option == 2:
            click.secho("Showing Company Suppliers......")
            suppliers = get_suppliers()

            if suppliers:
                for supplier in suppliers:
                    print(f"{supplier.id} | {supplier.name} | {supplier.email} | {supplier.phone} | {supplier.address}")
            else:
                click.secho("No suppliers found.")

        if supplier_option == 3:
            click.secho("Deleting Supplier........")
            supplier_name = click.prompt("Enter the name of supplier")

            try:
                delete_supplier(supplier_name) 
            except:
                raise Exception(f"Error deleting {supplier_name}")


    if user_input == 2:
        click.secho("--------------  Supply Orders' Options  -----------", fg='green')
        click.secho("Select an option", dim=True, fg='blue')
        click.secho("1. Add New Supply Order",fg='cyan')
        click.secho("2. View Supply Orders",fg='cyan')
        click.secho("3. Update Order Status",fg='cyan')
        click.secho("4. Delete Supply Order",fg='cyan')

        supply_order_option = click.prompt("Option", type=int)

        if supply_order_option == 1:
            click.secho("Adding New Supply Order.......")
            prod_id = click.prompt("Enter Product ID")
            quantity = click.prompt("Enter Quantity")
            supplier = click.prompt("Enter Supplier ID")
            status = click.prompt("Enter Order Status (Delivered or Not Delivered)", type=str)

            try:
                add_supply_order(prod_id, quantity, supplier, status="Not Delivered")
            except:
                raise Exception(f"Error adding New Supply Order")
        
        if supply_order_option == 2:
            click.secho("Showing Supply Orders")
            supply_orders = get_all_supply_orders()
            if supply_orders:
                for supply_order in supply_orders:
                    print(f"{supply_order.id} | {supply_order.quantity} | {supply_order.supplier_id} | {supply_order.status}")
            else:
                click.secho("Supply Order not found")

        if supply_order_option == 3:
            click.secho("Updating Supply Order Status........")
            supply_order_id = click.prompt("Enter Supply Order Id")

            try:
                update_supply_order_status(supply_order_id, "Delivered")
            except:
                raise Exception (f"Error updating order status")
        
        if supply_order_option == 4:
            click.secho("Deleting Supply Order........")
            supply_order_id = click.prompt("Enter Supply Order ID")

            try:
                delete_supply_order(supply_order_id)
                click.secho("Supply Order has been deleted successfully ")
            except:
                raise Exception ('Error deleting supply order')
            
            
    if user_input == 3:
        click.secho("----------------- Product Category ----------------")
        click.secho("Select an option:", dim=True, fg='blue')
        click.secho("1. Add Product Category",fg='cyan')
        click.secho("2. View all Product Categories",fg='cyan')
        click.secho("3. Delete Category Product",fg='cyan')

        category_option = click.prompt("Option", type=int)

        if category_option == 1:
            click.secho("Adding New Category......")
            name = click.prompt("Enter category name")
            quantity_in_stock = click.prompt("Enter Stock Quantity")
            description = click.prompt("Describe the Category")

            try:
                add_product_category(name, quantity_in_stock, description)
            except:
                raise Exception(f"{name} addition has failed.")
            
        if category_option == 2:
            click.secho("Viewing Product Categories.....")
            product_categories = get_product_categories()
            if product_categories:
                for product_category in product_categories:
                    print(f"{product_category.id} | {product_category.name} | {product_category.quantity_in_stock} | {product_category.description}")
            
        if category_option == 3:
            click.secho("Deleting a product category......")
            name = click.secho("Enter Existing Category Name")

            try:
                delete_product_category(name)
            except:
                raise Exception(f"{name} deletion has failed.")
            

    if user_input == 4:
        click.secho("------------------- Products -----------------")
        click.secho("Select an Option:", dim=True, fg='blue')
        click.secho("1. Add Product",fg='cyan')
        click.secho("2. View all Products",fg='cyan')
        click.secho("3. Delete Product",fg='cyan')

        product_option = click.prompt("Option", type=int)

        if product_option == 1:
            click.secho("Adding new product.......")
            name = click.prompt("Enter Product Name")
            brand = click.prompt("Enter Brand Name")
            price = click.prompt("Enter product price")
            availability = click.confirm("Is the product available?", default=True)
            category_id = click.prompt("Enter Categoty ID(Optional)")
            description = click.prompt("Enter Description(Optional)")

            add_product(name, brand, price, availability, category_id, description)
            
        if product_option == 2:
            click.secho("Viewing All Products.......")
            products = get_all_products()
            if products:
                for product in products:
                    print(f"{product.id}  | {product.name} | {product.brand} | {product.price} | {product.availability} | {product.category_id} | {product.description}")
        
        if product_option == 3:
            click.secho("Deleting Product.......")
            product_name = click.prompt("Enter Product Name")

            try:
                delete_product(product_name)
            except:
                raise Exception("Error during deletion")
            
            
    if user_input == 5:
        click.secho("--------------- Customers -----------------")
        click.secho("Select an Option:", dim=True, fg='blue')
        click.secho("1. Add Customer",fg='cyan')
        click.secho("2. View Customers",fg='cyan')
        click.secho("3. Delete Customer",fg='cyan')

        customer_option = click.prompt("Option", type=int)
            
        if customer_option == 1:
            click.secho("Adding Customer.......")
            first_name = click.prompt("Enter first name")
            last_name = click.prompt("Enter last name")
            email = click.prompt("Enter email")
            phone = click.prompt("Enter phone number(Optional)")
            address = click.prompt("Enter Address(Optional)")

            try:
                add_customer(first_name, last_name, email, phone, address)
            except:
                raise Exception("Error during addition")
        
        if customer_option == 2:
            click.secho("Viewing Customers.......")
            customers = get_customers()
            if customers:
                for customer in customers:
                    print(f"{customer.id} | {customer.first_name} | {customer.last_name} | {customer.email} | {customer.phone} | {customer.address}")

        if customer_option == 3:
            click.secho("Deleting Customer.......")
            customer_first_name = click.prompt("Enter Customer's First Name")

            try:
                delete_customer(customer_first_name)
            except:
                raise Exception ("Error during deletion")
            
            
    if user_input == 6:
        click.secho("--------------------- Orders ------------------")
        click.secho("Select an Option:", dim=True, fg='blue')
        click.secho("1. Add order",fg='cyan')
        click.secho("2. View orders",fg='cyan')
        click.secho("3. Delete order",fg='cyan')
        click.secho("4. Update order status",fg='cyan')

        order_option = click.prompt("Option", type=int)

        if order_option == 1:
            click.secho("Adding Order.......")
            customer_id = click.prompt("Enter Customer ID")
            order_datetime = click.prompt("Enter Order Date (YYYY-MM-DD)", type=click.DateTime(formats=['%Y-%m-%d']))
            order_date = order_datetime.date()
            order_status = click.prompt("Enter Order Status(Delivered or Not Delivered)")

            try:
                add_order(customer_id, order_date, order_status)
            except:
                raise Exception ("Failiure in placing new order")
            
        if order_option == 2:
            click.secho("View all placed Orders........")
            orders = get_orders()
            if orders:
                for order in orders:
                    print(f"{order.id} | {order.customer_id} | {order.order_date} | {order.order_status}")
        
        if order_option == 3:
            click.secho("Delete Order.......")
            order_id = click.prompt("Enter Order ID")

            try:
                delete_order(order_id)
            except:
                raise Exception("Failiure in deleting the Order")
            
        if order_option == 4:
            click.secho("Update Order Status.......")
            order_id = click.prompt("Enter Order ID")

            try:
                update_order_status(order_id)
            except:
                raise Exception ("Failiure in Updating Order Status")
            
        
    if user_input == 7:
        click.secho("--------------------Order Items----------------")
        click.secho("Select an Option:", dim=True, fg='blue')
        click.secho("1. Add Order Item",fg='cyan')
        click.secho("2. View Order items",fg='cyan')
        click.secho("3. Delete Order item",fg='cyan')

        item_option = click.prompt("Option", type=int)

        if item_option == 1:
            click.secho("Adding Order Item..........")
            order_id = click.prompt("Enter Order ID")
            product_id = click.prompt("Enter Product ID")
            quantity = click.prompt("Enter quantity")

            try:
                add_order_item(order_id, product_id, quantity)
            except:
                raise Exception ("Failiure in Adding Order Item")
            
        if item_option == 2:
            click.prompt("View Order Items.......")
            order_items = get_order_items()
            if order_items:
                for order_item in order_items:
                    print(f"{order_item.id} | {order_item.order_id} | {order_item.product_id} | {order_item.quantity}")

        if item_option == 3:
            click.prompt("Delete Order Item.......")
            item_id = click.prompt("Enter Order Item ID")

            try:
                delete_order_item(item_id)
            except:
                raise Exception ("Failiure in deleting Order Item")