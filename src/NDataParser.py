import NObjects as nobjects

class NDataParser:
    def __init__(self, bs):
        self.bs = bs

    def _get_attr(self, tag, attr_name, required=True):
        if attr_name in tag.attrs:
            return tag[attr_name].strip()
        if (required):
            raise Exception('Не найден обязательный параметр {} для {}'.format(attr_name, type(tag)))
        return None

    def _get_tag_text(self, object, tag_name, required=True):
        if (object.find(tag_name) != None):
            return object.find(tag_name).text.strip()
        if (required):
            raise Exception('Не найден обязательный тэг {} для {}'.format(tag_name, type(object)))
        return None

    def _parse_categories(self):
        print('Parse Category')
        result = []
        categories = self.bs.findAll('category')
        for category in categories:
            result.append(nobjects.Category(
                self._get_attr(category, "id"),
                self._get_attr(category, "parentId", False),
                category.text)
            )
        print('Parsed')
        return categories

    def _parse_currencies(self):
        print('Parse Currencies')
        result = []
        currencies = self.bs.findAll('currency')
        for currency in currencies:
            result.append(nobjects.Currency(
                self._get_attr(currency, "id"),
                self._get_attr(currency, "rate")
            ))
        print('Parsed')
        return result

    def _parse_picture_urls(self, picture_urls):
        result = []
        for picture_url in picture_urls:
            result.append(picture_url.text)
        return result

    def _parse_offer_params(self, params):
        dict = {}
        for param in params:
            dict[self._get_attr(param, "name")] = param.text
        return dict

    def _parse_offers(self):
        print('Parse Offers')
        result = []
        offers = self.bs.findAll('offer')
        for offer in offers:
            try:
                result.append(nobjects.Offer(
                    self._get_attr(offer, "id"),
                    self._get_tag_text(offer, "categoryId"),
                    self._get_tag_text(offer, "name"),
                    self._get_tag_text(offer, "url"),
                    self._get_tag_text(offer, "price"),
                    self._get_tag_text(offer, "oldprice", False),
                    self._get_tag_text(offer, "currencyId"),
                    self._get_tag_text(offer, "vendor"),
                    self._get_tag_text(offer, "model"),
                    self._parse_picture_urls(offer.findAll("picture")),
                    self._parse_offer_params(offer.findAll("param")),
                    self._get_tag_text(offer, "quantity")
                ))
            except Exception as e:
                print('Проблема с оффером с id = ', offer.attrs["id"], ':\n', e)
        print('Parsed')
        return result

    def parse(self):
        categories = self._parse_categories()
        currencies = self._parse_currencies()
        offers = self._parse_offers()
        return nobjects.NData(categories, currencies, offers)
