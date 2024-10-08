import qrcode

def generate_qr_code(upi_id, app_name):
    # Define the payment URL based on the UPI ID and the payment app
    payment_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

    # Create QR code
    qr = qrcode.make(payment_url)

    # Save the QR code to a file
    qr.save(f'{app_name}_qr.png')

    # Display the QR code
    qr.show()

def main():
    upi_id = input("Enter your UPI ID: ")

    # Generate QR codes for different UPI apps
    generate_qr_code(upi_id, 'google_pay')
    # generate_qr_code(upi_id, 'phonepe')
    # generate_qr_code(upi_id, 'paytm')

if __name__ == "__main__":
    main()
