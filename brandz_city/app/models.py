from typing import Text
from django.db import models
from django.contrib.auth.models import User


#Creating a customer model to save customer information.
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    shoe_size = models.IntegerField()
    house_number = models.CharField(max_length=50)
    locality = models.CharField(max_length=500)
    landmark = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

    def __str__(self):
        name = str(self.name)
        phone_number = str(self.phone_number)
        shoe_size = str(self.shoe_size)
        house_number = str(self.house_number)
        locality = str(self.locality)
        id = str(self.id)
        return (f"({id}) {name}/{phone_number},Size: {shoe_size} H.No: {house_number}, {locality}")


#Category set where all the shoes will be categorised as per requirements.
CATEGORY_CHOICES = (
    ('S', 'Shoes'),
    ('C', 'Crocs'),
    ('F', 'Flips'),
)



#Contact model can be used as a form so that a user can contact the admin.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    contact_for = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        id = str(self.id)
        name = str(self.name)
        email = str(self.email)
        contact_for = str(self.contact_for)

        return(f"{name}({email}): {contact_for}")


#Product model saves the product information.
class Product(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    size_available = models.CharField(max_length=150)
    original_price = models.FloatField()
    price = models.FloatField()
    # unit = models.CharField(choices=UNIT, max_length=7)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_img = models.ImageField(upload_to='productimg')
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        title = str(self.title)
        price = str(self.price)
        id = str(self.id)
        return (f"ID: {id} -  {title} - Rs{price}")


#Cart model saves the product to cart classified by user, product and quantitiy.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.price


#Shows package delivery status to customer when a product is ordered.
STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Canceled', 'Canceled'),
)



#This model is used to store the order info in the admin dashboard so that the admin can verify the order.
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              default='Pending', max_length=50)
    

    # def save(self, *args, **kwargs):
    #     product = self.product
    #     if product.quantity >= self.quantity:
    #         product.quantity -= self.quantity
    #         product.save()
    #         super(OrderPlaced, self).save(*args, **kwargs)
    #     else:
    #         raise ValueError('Ordered quantity is greater than available quantity.')
            

    @property
    def total_cost(self):
        return self.quantity * self.product.price
