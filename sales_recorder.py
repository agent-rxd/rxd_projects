import csv
import datetime

sales_records = []
products = {}

def add_sales():
    customer_name = input("Enter customer name: ")
    mobile_number = input("Enter customer mobile number: ")
    
    purchased_products = []
    total_cost = 0
    
    while True:
        product_code = input("Enter product code (0 to exit): ")
        if product_code == '0':
            break
        if product_code not in products:
            print("Invalid product code. Please try again.")
            continue
        quantity = int(input("Enter quantity: "))
        
        product = products[product_code]
        purchased_products.append((product['name'], quantity, product['price']))
        total_cost += product['price'] * quantity
    
    sales_records.append({
        'date': datetime.datetime.now(),
        'customer_name': customer_name,
        'mobile_number': mobile_number,
        'purchased_products': purchased_products,
        'total_cost': total_cost
    })
    
    print("Sales recorded successfully!")
    print("Total cost:", total_cost)
    print()

def add_products():
    while True:
        product_code = input("Enter product code ('000' to exit): ")
        
        if product_code == '000':
            break
        
        product_name = input("Enter product name: ")
        product_price = float(input("Enter product price: "))
        
        products[product_code] = {
            'name': product_name,
            'price': product_price
        }
        
        print("Product added successfully!")
        print()

def view_sales_record():
    if not sales_records:
        print("No sales records found.")
        print()
        return
    
    sorted_sales = sorted(sales_records, key=lambda x: x['date'])
    
    for sale in sorted_sales:
        print("Date:", sale['date'])
        print("Customer Name:", sale['customer_name'])
        print("Mobile Number:", sale['mobile_number'])
        print("Purchased Products:")
        for product in sale['purchased_products']:
            print(" - Product:", product[0])
            print("   Quantity:", product[1])
            print("   Price:", product[2])
        print("Total Cost:", sale['total_cost'])
        print()

def save_sales_to_csv(filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Customer Name', 'Mobile Number', 'Product', 'Quantity', 'Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for sale in sales_records:
            date = sale['date'].strftime('%Y-%m-%d %H:%M:%S')
            customer_name = sale['customer_name']
            mobile_number = sale['mobile_number']
            
            for product in sale['purchased_products']:
                product_name = product[0]
                quantity = product[1]
                price = product[2]
                
                writer.writerow({
                    'Date': date,
                    'Customer Name': customer_name,
                    'Mobile Number': mobile_number,
                    'Product': product_name,
                    'Quantity': quantity,
                    'Price': price
                })
    
    print("Sales records saved to", filename)
    print()

def display_menu():
    print("Sales Logging Software")
    print("1. Add Sales")
    print("2. Add Products")
    print("3. View Sales Record")
    print("4. Save Sales Records to CSV")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        print()
        
        if choice == '1':
            add_sales()
        elif choice == '2':
            add_products()
        elif choice == '3':
            view_sales_record()
        elif choice == '4':
            filename = input("Enter the filename to save the sales records: ")
            save_sales_to_csv(filename)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            print()

if __name__ == "__main__":
    main()
