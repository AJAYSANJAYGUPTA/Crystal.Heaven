from flask import Flask, render_template, request, redirect, url_for
import os
from urllib.parse import quote


app = Flask(__name__)

# Dummy product data for testing
products = [
    {"name": "Crystal Band", "image": "crystal band.jpg", "description": "A beautiful crystal band", "price": "150rs"},
    {"name": "Crystal Bag", "image": "crystal bag2.jpg", "description": "A stunning crystal bag", "price": "750rs"},
    {"name": "Crystal Keychain", "image": "crystal keychain.jpg", "description": "Perfect for Your Keys", "price": "250rs"}

]

# Admin credentials
admin_username = "admin"
admin_password = "admin123"

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html', products=products)

# Route for ordering a product (redirects to WhatsApp)
@app.route('/order/<product_name>')
def order(product_name):
    # Find product based on name
    product = next((p for p in products if p['name'] == product_name), None)
    if product:
        message = f"Hi, I'd like to order the {product_name}. Price: {product['price']}. Description: {product['description']}"
        encoded_message = quote(message)
        whatsapp_url = f"https://wa.me/919172997568?text={encoded_message}"
        return redirect(whatsapp_url)
    return redirect(url_for('home'))

# Admin login page
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == admin_username and password == admin_password:
            return redirect(url_for('admin_dashboard'))
        else:
            return "Invalid credentials!"
    return render_template('admin.html')

# Admin dashboard to upload products
@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    if request.method == 'POST':
        product_name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        image = request.files['image']
        
        if image:
            image.save(os.path.join('static/images', image.filename))
        
        # Add new product to the products list
        products.append({
            'name': product_name,
            'description': description,
            'price': price,
            'image': image.filename
        })
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin_dashboard.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)