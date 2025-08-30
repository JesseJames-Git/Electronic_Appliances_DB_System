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
    add_order, get_orders, delete_order,update_order_status,

    # --------------Order Items---------------
    add_order_item, get_order_items,delete_order_item
)

while True:
    click.secho("-------------Welcome to the Electrical Appliances Database System------------", bold=True, fg='green')
    click.secho("Select Option to Proceed", bold=True, fg='blue')
    click.secho("1. Suppliers")
    click.secho("2. Supply Orders")
    click.secho("3. Product Categories")
    click.secho("4. Products")
    click.secho("5. Customers")
    click.secho("6. Customer Orders")
    click.secho("7. Customer Order items")

    user_input = click.prompt("Option", type=int)

    if user_input == 1:
        click.secho("--------------  Suppliers' Options  -----------")
        click.secho("1. Add New Supplier")
        click.secho("2. View Company Suppliers")
        click.secho("3. Delete Supplier")

        supplier_option = click.prompt("Option", type=int)

        if supplier_option == 1:
            click.secho("Adding New Supplier......")
            name = click.prompt("Enter name")
            email = click.prompt("Enter email")
            phone = click.prompt("Enter phone")
            address = click.prompt("Enter Address")

            try:
                add_supplier(name, email, phone, address)
                click.secho(f"{name} has successfully been added as a Supplier")
            
            except:
                raise Exception(f"Error adding of {name} as a Supplier")

        if supplier_option == 2:
            click.secho("Showing Company Suppliers......")
            print( get_suppliers())

        if supplier_option == 3:
            click.secho("Deleting Supplier........")
            supplier_name = click.prompt("Enter the name of supplier: ")

            try:
                delete_supplier(supplier_name)
                click.secho(f"{supplier_name} has been deleted successfully")
            except:
                raise Exception(f"Error deleting {supplier_name}")

    if user_input == 2:
        click.secho("--------------  Supply Orders' Options  -----------")
        click.secho("1. Add New Supply Order")
        click.secho("2. View Supply Orders")
        click.secho("3. Delete Supply Order")

        if 