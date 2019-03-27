import requests

class API(object):

    def __init__(self):
        self.s = requests.session()
        self.base = 'https://selly.gg/api/v2/'
        self.key = 'Selly Secret Key'
        self.email = 'Your Email'

    def GetCoupons(self):
        url = self.base + 'coupons'
        r = self.s.get(url, auth=(self.email, self.key))
        coupon_num = 0
        try:
            for i in range(9999):
                print('Coupon ID: ' + str(r.json()[coupon_num]['id']) + '\n' + 'Product ID: ' + str(r.json()[coupon_num]['product_ids']) + '\n' + 'Coupon Code: ' + str(r.json()[coupon_num]['code']) + '\n' + 'Discount: ' + str(r.json()[coupon_num]['discount']) + '%' + '\n' + 'Maximum Uses: ' + str(r.json()[coupon_num]['max_use']) + '\n' + 'Total Uses: ' + str(r.json()[coupon_num]['uses']) + '\n' + '=====================================')
                coupon_num += 1
        except:
            print('All coupons have been listed.')

    def GetExactCoupon(self, coupon):
        url = self.base + 'coupons/' + str(coupon)
        r = self.s.get(url, auth=(self.email, self.key))
        print('Coupon ID: ' + str(r.json()['id']) + '\n' + 'Product ID: ' + str(r.json()['product_ids']) + '\n' + 'Coupon Code: ' + str(r.json()['code']) + '\n' + 'Discount: ' + str(r.json()['discount']) + '%' + '\n' + 'Maximum Uses: ' + str(r.json()['max_use']) + '\n' + 'Total Uses: ' + str(r.json()['uses']))

    def CreateCoupon(self, code, discount, product):
        url = self.base + 'coupons'
        coupon = {"coupon": {"code": code, "discount": int(discount), "product_ids": [product]}}
        r = self.s.post(url, json=coupon, auth=(self.email, self.key))
        print('Coupon ID: ' + str(r.json()['id']) + '\n' + 'Product ID: ' + str(r.json()['product_ids']) + '\n' + 'Coupon Code: ' + str(r.json()['code']) + '\n' + 'Discount: ' + str(r.json()['discount']) + '%' + '\n' + 'Maximum Uses: ' + str(r.json()['max_use']) + '\n' + 'Total Uses: ' + str(r.json()['uses']))

    def UpdateCoupon(self, coupon, code, discount, product):
        url = self.base + 'coupons/' + coupon
        coupon_data = {"coupon": {"code": code, "product_ids": [product],"discount": discount}}
        r = self.s.put(url, json=coupon_data, auth=(self.email, self.key))
        print('Coupon ID: ' + str(r.json()['id']) + '\n' + 'Product ID: ' + str(r.json()['product_ids']) + '\n' + 'Coupon Code: ' + str(r.json()['code']) + '\n' + 'Discount: ' + str(r.json()['discount']) + '%' + '\n' + 'Maximum Uses: ' + str(r.json()['max_use']) + '\n' + 'Total Uses: ' + str(r.json()['uses']) )

    def GetAllOrders(self):
        url = self.base + 'orders'
        r = self.s.get(url, auth=(self.email, self.key))
        try:
            num = 0
            for i in range(9999):
                print('Order ID: ' + str(r.json()[num]['id']) + '\n' + 'Product ID: ' + str(r.json()[num]['product_id']) + '\n' + 'Email: ' + str(r.json()[num]['email']) + '\n' + 'IP Address: ' + str(r.json()[num]['ip_address']) + '\n' + 'Country: ' + str(r.json()[num]['country_code']) + '\n' + 'Product: ' + str(r.json()[num]['product_title']) + '\n' + 'Price: ' + str(r.json()[num]['value']) + '\n' + 'Amount: ' + str(r.json()[num]['quantity']) + '\n' + 'Payment Type: ' + str(r.json()[num]['gateway']) + '\n' + 'Payment Status: ' + str(r.json()[num]['status']) + '\n' + 'Sent Item: ' + str(r.json()[num]['delivered']) + '\n' + 'Referral: ' + str(r.json()[num]['referral']) + '\n' + '=====================================')
                num += 1
        except:
            print('All orders have been listed.')

    def GetExactOrder(self, order):
        url = self.base + 'orders/' + order
        r = self.s.get(url, auth=(self.email, self.key))
        print('Order ID: ' + str(r.json()['id']) + '\n' + 'Product ID: ' + str(r.json()['product_id']) + '\n' + 'Email: ' + str(r.json()['email']) + '\n' + 'IP Address: ' + str(r.json()['ip_address']) + '\n' + 'Country: ' + str(r.json()['country_code']) + '\n' + 'Product: ' + str(r.json()['product_title']) + '\n' + 'Price: ' + str(r.json()['value']) + '\n' + 'Amount: ' + str(r.json()['quantity']) + '\n' + 'Payment Type: ' + str(r.json()['gateway']) + '\n' + 'Payment Status: ' + str(r.json()['status']) + '\n' + 'Sent Item: ' + str(r.json()['delivered']) + '\n' + 'Referral: ' + str(r.json()['referral']))

    def GetPageOrders(self, page):
        url = self.base + 'orders?page=' + str(page)
        r = self.s.get(url, auth=(self.email, self.key))
        try:
            num = 0
            for i in range(9999):
                print('Order ID: ' + str(r.json()[num]['id']) + '\n' + 'Product ID: ' + str(r.json()[num]['product_id']) + '\n' + 'Email: ' + str(r.json()[num]['email']) + '\n' + 'IP Address: ' + str(r.json()[num]['ip_address']) + '\n' + 'Country: ' + str(r.json()[num]['country_code']) + '\n' + 'Product: ' + str(r.json()[num]['product_title']) + '\n' + 'Price: ' + str(r.json()[num]['value']) + '\n' + 'Amount: ' + str(r.json()[num]['quantity']) + '\n' + 'Payment Type: ' + str(r.json()[num]['gateway']) + '\n' + 'Payment Status: ' + str(r.json()[num]['status']) + '\n' + 'Sent Item: ' + str(r.json()[num]['delivered']) + '\n' + 'Referral: ' + str(r.json()[num]['referral']) + '\n' + '=====================================')
                num += 1
        except:
            print('All orders have been listed.')

    def GetAllProducts(self):
        url = self.base + 'products'
        r = self.s.get(url, auth=(self.email, self.key))
        try:
            num = 0
            for i in range(9999):
                print('Product ID: ' + str(r.json()[num]['id']) + '\n' + 'Title: ' + str(r.json()[num]['title']) + '\n' + 'Description: ' + str(r.json()[num]['description']) + '\n' + 'Stock: ' + str(r.json()[num]['stock']) + '\n' + '=====================================')
                num += 1
        except:
            print('All products have been listed.')

    def GetExactProduct(self, product):
        url = self.base + 'products/' + product
        r = self.s.get(url, auth=(self.email, self.key))
        print('Product ID: ' + str(r.json()['id']) + '\n' + 'Title: ' + str(r.json()['title']) + '\n' + 'Description: ' + str(r.json()['description']) + '\n' + 'Stock: ' + str(r.json()['stock']))

    def CreateProduct(self, title, description, price, currency, product_type, product_keys):
        url = self.base + 'products'
        product = {"product": {"title": title, "description": description, "price": int(price), "currency": currency, "gateways": ['paypal'], "unlisted": True, "product_type": int(product_type), "info": product_keys}}
        r = self.s.post(url, json=product, auth=(self.email, self.key))
        print('Product ID: ' + str(r.json()['id']) + '\n' + 'Title: ' + str(r.json()['title']) + '\n' + 'Description: ' + str(r.json()['description']) + '\n' + 'Stock: ' + str(r.json()['stock']))

    def UpdateProduct(self, product, title, description, price, currency):
        url = self.base + 'products/' + product
        product_data = {"product": {"title": title, "description": description, "price": int(price), "currency": currency}}
        r = self.s.put(url, json=product_data, auth=(self.email, self.key))

    def DeleteProduct(self, product):
        url = self.base + 'products/' + product
        r = self.s.delete(url, auth=(self.email, self.key))

    def GetAllGroups(self):
        url = self.base + 'product_groups'
        r = self.s.get(url, auth=(self.email, self.key))
        try:
            num = 0
            for i in range(9999):
                print('Group ID: ' + str(r.json()[num]['id']) + '\n' + 'Title: ' + str(r.json()[num]['title']) + '\n' + 'Products: ' + str(r.json()[num]['product_ids']) + '\n' + '=====================================')
                num += 1
        except:
            print('All groups have been listed.')

    def GetExactGroup(self, product):
        url = self.base + 'product_groups/' + product
        r = self.s.get(url, auth=(self.email, self.key))
        print('Group ID: ' + str(r.json()['id']) + '\n' + 'Title: ' + str(r.json()['title']) + '\n' + 'Products: ' + str(r.json()['product_ids']))

    def GetAllMessages(self):
        url = self.base + 'queries'
        r = self.s.get(url, auth=(self.email, self.key))
        try:
            num = 0
            for i in range(9999):
                print('Message ID: ' + str(r.json()[num]['id']) + '\n' + 'Title: ' + str(r.json()[num]['title']) + '\n' + 'Email: ' + str(r.json()[num]['email']) + '\n' + 'Message: ' + str(r.json()[num]['message']) + '\n' + 'IP Address: ' + str(r.json()[num]['ip_address']) + '\n' + 'Message ID: ' + str(r.json()[num]['id']) + '\n' + '=====================================')
                num += 1
        except:
            print('All messages have been listed.')

    def GetExactMessage(self, message):
        url = self.base + 'queries/' + message
        r = self.s.get(url, auth=(self.email, self.key))
        print('Message ID: ' + str(r.json()['id']) + '\n' + 'Title: ' + str(r.json()['title']) + '\n' + 'Email: ' + str(r.json()['email']) + '\n' + 'Message: ' + str(r.json()['message']) + '\n' + 'IP Address: ' + str(r.json()['ip_address']) + '\n' + 'Message ID: ' + str(r.json()['id']))
