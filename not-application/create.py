from application import db, app
from application.models import Customer,Order,Product,Order_detail
with app.app_context():
    db.drop_all()
    db.create_all()

    testuser = Order_detail(order_id=1, product_id=1, quantity=10, price=12.50)
    db.session.add(testuser)
    db.session.commit()

    testuser = Order_detail(order_id=2, product_id=2, quantity=20, price=100.50)
    db.session.add(testuser)
    db.session.commit()

    testuser = Order_detail(order_id=3, product_id=2, quantity=112, price=50.00)
    db.session.add(testuser)
    db.session.commit()

    bike_trail = Product(name="Bike Trail", description="Mountain Bike riding", price=50, stock_level=1)
    db.session.add(bike_trail)
    db.session.commit()

    zip_line = Product(name="Zip Line", description="Zip line x 5 goes", price=20, stock_level=1)
    db.session.add(zip_line)
    db.session.commit()

    flying = Product(name="flying", description="on a small fast plane", price=150, stock_level=1)
    db.session.add(flying)
    db.session.commit()

    gun_range = Product(name="Gun Range", description="Wild wild west style", price=75, stock_level=1)
    db.session.add(gun_range)
    db.session.commit()

