order_quantity = Column(Integer, nullable=False)
product_id = Column(Integer, ForeignKey('products.id')

                        