from flask import render_template, request
import dao
from App import App


# phai đúng tên templates chua index thi no moi chiu chay nha
@App.route('/')
def index():
    kw = request.args.get('kw')
    categories = dao.load_categories()
    products = dao.load_products(kw)
    return render_template('index.html', categories=categories, products=products)


if __name__ == '__main__':
    from App import admin
    App.run(debug=True)
