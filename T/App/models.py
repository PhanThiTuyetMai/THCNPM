from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from App import db, App


class User(db.Model):
    get_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    avatar = Column(String(100),
                    default='https://cdn.tgdd.vn/Products/Images/42/305660/iphone-15-pro-max-tu-nhien-1.jpg')

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(250))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with App.app_context():
        db.create_all()

        import hashlib

        u = User(name='Admin2', username='admin2', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
                 is_active=1, get_id=1)
        db.session.add(u)
        db.session.commit()

# p1 = Product(name='iPhone 13', price=20000000, category_id=1,
#              image='https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg')
# p2 = Product(name='SamSung A23', price=15000000, category_id=1,
#              image='https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg')
# p3 = Product(name='Ipad 20', price=3000000, category_id=2,
#              image='https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg')
# p4 = Product(name='iPhone 15', price=900000000, category_id=1,
#              image='https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg')
# p5 = Product(name='Oppo S20', price=5990000, category_id=1,
#              image='https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg')
# p6 = Product(name='Ipad 8', price=80000000, category_id=2,
#              image='https://news.khangz.com/wp-content/uploads/2023/09/iphone-15-xanh-la-2-1.jpg')
# db.session.add_all([p1, p2, p3, p4, p5, p6])
# db.session.commit()

# c1 = Category(name='Mobile')
# c2 = Category(name='Tablet')
#
# db.session.add(c1)
# db.session.add(c2)
# db.session.commit()
# db.create_all()
