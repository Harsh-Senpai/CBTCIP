from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from datetime import datetime

def create_payment_receipt(customer_name, prod, TA, payment_method):
    # Create a unique filename using the current timestamp
    filename = f"Payment_Receipt_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"

    # Create a PDF document
    c = canvas.Canvas(filename, pagesize=letter)

    # Set font and size for the header
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(colors.darkblue)

    # Add header with company name
    c.drawCentredString(300, 750, "Inori's PC Store")

    # Set font and size for details
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)

    # Add receipt details
    c.drawString(50, 700, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(50, 680, f"Customer: {customer_name}")

    # Set font and color for Product details
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.darkgreen)

    # Add product details with pagination
    c.drawString(50, 650, "Product Details:")
    page_prod = 0
    current_y = 650

    for i, item in enumerate(prod, start=1):
        c.drawString(50, current_y - i * 20, f"{item['name']}: Rs. {item['price']:.2f}")
        page_prod += 1

        if page_prod >= 30:
            # Move to a new page if more than 30 products
            c.showPage()
            current_y = 750
            page_prod = 0

    # Add total amount
    c.drawString(50, current_y - (len(prod) + 1) * 20, f"Total Amount: Rs. {TA:.2f}")

    # Set font and color for payment method
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.darkblue)

    # Add payment method
    c.drawString(50, current_y - (len(prod) + 2) * 20, f"Payment Method: {payment_method}")

    # Add a line separator
    c.setStrokeColor(colors.grey)
    c.line(50, current_y - (len(prod) + 2.5) * 20, 550, current_y - (len(prod) + 2.5) * 20)

    # Set font and color for thank you message
    c.setFont("Helvetica-Oblique", 12)
    c.setFillColor(colors.darkblue)

    # Add thank you message
    c.drawString(50, current_y - (len(prod) + 3.5) * 20, "Thank you for shopping with Inori!")

    # Set font and color for footer
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.darkgrey)

    # Add contact information in the footer
    c.drawString(50, 30, "Contact us:")
    c.drawString(50, 15, "Email: support@inoriofficial.com | Phone: +91 9682208822")

    # Save the PDF file
    c.save()

    print(f"Payment Receipt Created Successfully: {filename}")

# Get user inputs
customer_name = input("Enter customer name: ")

# Get product details from the user
prod = []
while True:
    item_name = input("Enter the product name or type 'done' to submit: ")
    if item_name.lower() == 'done':
        break
    item_price = float(input("Enter the product price: "))
    prod.append({"name": item_name, "price": item_price})

# Calculate total amount
TA = sum(item['price'] for item in prod)

# List of payment methods
PM = ["Debit Card", "Credit Card", "Net Banking", "UPI", "Cash"]

# Display payment methods to the user
print("Available Payment Methods:")
for i, method in enumerate(PM, start=1):
    print(f"{i}. {method}")

# Get user's choice for payment method
selected_index = int(input("Input the value for selecting a payment method: "))
selected_method = PM[selected_index - 1]

# Create the payment receipt
create_payment_receipt(customer_name, prod, TA, selected_method)
