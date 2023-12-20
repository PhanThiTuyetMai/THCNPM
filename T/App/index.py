import math
import utils
from flask import render_template, request, redirect, jsonify, session  # chuyen trang
import dao
from App import App, login
from flask_login import login_user


# phai đúng tên templates chua index thi no moi chiu chay nha
@App.route('/')
def index():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')

    categories = dao.load_categories()
    products = dao.load_products(kw, cate_id, page)

    num = dao.count_product()
    return render_template('index.html', products=products,
                           pages=math.ceil(num / App.config['PAGE_SIZE']))


@App.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')


@App.route("/api/cart", methods=['post'])
def add_to_cart():
    data = request.json

    cart = session.get('cart')
    if cart is None:
        cart = {}

    id = str(data.get("id"))
    if id in cart:
        cart[id]['quantity'] += 1
    else:
        cart[id] = {
            "id": id,
            "name": data.get("name"),
            "price": data.get("price"),
            "quantity": 1
        }

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


@App.route('api/cart/<product_id>', methods=['put'])
def update_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        quantity = request.json.get('quantity')
        cart[product_id]['quantity'] = int(quantity)

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


@App.route('api/cart/<product_id>', methods=['delete'])
def delete_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        del cart[product_id]

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


@App.route('/cart')
def cart():
    return render_template('cart.html')


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id=user_id)


@App.context_processor
def common_response():
    return {
        'categories': dao.load_categories(),
        'cart': utils.count_cart(session.get('cart'))
    }


if __name__ == '__main__':
    from App import admin

    App.run(debug=True)
