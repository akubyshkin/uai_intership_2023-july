class Category:
    def __init__(self, id, parent_id, name):
        self.id = id
        self.parent_id = parent_id  # nullable
        self.name = name

class Currency:
    def __init__(self, id, rate):
        self.id = id
        self.rate = rate

class Offer:
    def __init__(self, id, category_id, name, url, price, old_price, currency_id, vendor, model, picture_urls, params, quantity):
        self.id = id
        self.category_id = category_id
        self.name = name
        self.url = url
        self.price = price
        self.old_price = old_price  # nullable
        self.currency_id = currency_id
        self.vendor = vendor
        self.model = model
        self.picture_urls = picture_urls
        self.params = params
        self.quantity = quantity

class NData:
    def __init__(self, categories, currencies, offers):
        self.categories = categories
        self.currencies = currencies
        self.offers = offers
