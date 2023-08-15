from application import app, db
from application.models import Customer,Order,Product,Order_detail
from flask import render_template, request, redirect,url_for

@app.route('/cart')
def cart():
    all_product = Product.query.all()
    all_orders = Order_detail.query.all()
    total_amount = sum([order.quantity * order.price for order in all_orders])
    return render_template('cart.html', all_orders=all_orders, total_amount=total_amount, all_product=all_product) 

@app.route('/update_quantity/<int:order_detail_id>', methods=['POST'])
def update_quantity(order_detail_id):
    new_quantity = request.form.get('new_quantity')
    order_detail = Order_detail.query.get(order_detail_id)    
    if order_detail:
        order_detail.quantity = int(new_quantity)
        db.session.commit()    
    return redirect(url_for('cart'))

@app.route('/delete_item/<int:order_detail_id>', methods=['POST'])
def delete_item(order_detail_id):
    order_detail = Order_detail.query.get(order_detail_id)    
    if order_detail:
        db.session.delete(order_detail)
        db.session.commit()    
    return redirect(url_for('cart'))  # Removed the form object from the redirect

@app.route('/payment')
def payment():
    return render_template('payment.html')
