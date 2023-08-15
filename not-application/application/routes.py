from application import app, db
from application.models import Customer,Order,Product,Order_detail
from flask import render_template, request

@app.route('/')
def home():
    return render_template ('index.html')

@app.route('/cart')
def cart():
    all_orders = Order_detail.query.all()
    order_string = ""
    for order in all_orders:
        order_string += "<br>"+ str(order.order_detail_id) + str(order.order_id) + str(order.quantity)  + str(order.price)
    return order_string