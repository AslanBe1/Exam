import psycopg2

class Product:
    def __init__(self, name, price, color,image):
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save(self):
        try:
            conn = psycopg2.connect(
                host="localhost",
                user="postgres",
                password="123",
                port="5432",
                database="exam")
            cur = conn.cursor()
            query = "INSERT INTO product (name, price, color, image) VALUES (%s, %s, %s, %s)"
            cur.execute(query, (self.name, self.price, self.color, self.image))
            conn.commit()
            cur.close()
            conn.close()
            print(f'Product: {self.name}\nPrice: {self.price}\nColor: {self.color}\nImage: {self.image} ')
            print("Product has been saved")

        except Exception as e:
            print(e)


product = Product("BMW",35689.23,"BLACK","hhtps:gefdckkfdkagdy")
product.save()