from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Customer, Order, Product, Order_detail

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                          SECRET_KEY='TEST_SECRET_KEY',
                          DEBUG=True,
                          WTF_CSRF_ENABLED=False
                          )
        return app

    def setUp(self):
        db.create_all()
        sample_product = Product(name="TestProduct", description="TestDescription", price=10.0, stock_level=10)
        db.session.add(sample_product)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestRoutes(TestBase):
    def test_home_route(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_products_route(self):
        response = self.client.get(url_for('products'))
        self.assertIn(b'TestProduct', response.data)

    def test_add_to_cart_route(self):
        response = self.client.post(url_for('add_to_cart'), data={'product_id': 1})        
        self.assertEqual(response.status_code, 302)
        self.assertIn(url_for('products'), response.location)

        order_detail = Order_detail.query.filter_by(product_id=1).first()
        self.assertIsNotNone(order_detail)
        self.assertEqual(order_detail.quantity, 1)