from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    CAR_BRANDS = (
        ('audi', 'Audi'),
        ('bmw', 'BMW'),
        ('ford', 'Ford'),
        ('jaguar', 'Jaguar'),
        ('land_rover', 'Land Rover'),
        ('mercedes_benz', 'Mercedes-Benz'),
        ('nissan', 'Nissan'),
        ('porsche', 'Porsche'),
        ('tesla', 'Tesla'),
        ('toyota', 'Toyota'),
    )

    CAR_MODELS = {
        'audi': (
            ('a3', 'A3'),
            ('a4_avant', 'A4 Avant'),
            ('q7', 'Q7'),
            ('a6', 'A6'),
            ('a5', 'A5'),
            ('e_tron', 'E-tron'),
        ),

        'bmw': (
            ('1_series', '1 Series'),
            ('3_series', '3 Series'),
            ('4_series', '4 Series'),
            ('5_series', '5 Series'),
            ('x5', 'X5'),
            ('ix3', 'IX3'),
        ),

        'ford': (
            ('focus', 'Focus'),
            ('puma', 'Puma'),
            ('monedo', 'Monedo'),
            ('mustang', 'Mustang'),
        ),

        'jaguar': (
            ('xf', 'Xf'),
            ('a3', 'A3'),
            ('f_pace', 'F-pace'),
            ('e_pace', 'I-pace'),
            ('xe', 'XE'),
            ('f_type', 'F-type'),
        ),

        'land_rover': (
            ('range_rover_evoque', 'Range Rover Evoque'),
            ('range_rover_velar', 'Range Rover Velar'),
            ('range_rover', 'Range Rover'),
            ('discovery', 'Discovery'),
        ),

        'mercedes_benz': (
            ('a_class', 'a Class'),
            ('c_class', 'c Class'),
            ('e_class', 'e Class'),
            ('g_class', 'G Class'),
            ('eqa', 'EQA'),
            ('eqs', 'EQS'),
        ),

        'nissan': (
            ('micra', 'Micra'),
            ('leaf', 'Leaf'),
            ('gtr', 'GT-R'),
            ('juke', 'Juke'),
            ('qashqai', 'Qashqai'),
        ),

        'porsche': (
            ('taycan', 'Taycan'),
            ('panamera', 'Panamera'),
            ('macan', 'Macan'),
            ('cayman', 'Cayman'),
            ('boxter', 'Boxter'),
        ),

        'tesla': (
            ('model_3', 'Model 3'),
            ('model_x', 'Model X'),
            ('model_y', 'Model Y'),
            ('model_s', 'Model S'),
        ),

        'toyota': (
            ('yaris', 'Yaris'),
            ('corolla', 'Corolla'),
            ('chr', 'CH-R'),
            ('camry', 'Camry'),
            ('supra', 'Supra'),
            ('a3', 'A3'),
        ),
    }

    BODY_TYPES = (
        ('saloon', 'Saloon'),
        ('estate', 'Estate'),
        ('coupe', 'Coupe'),
        ('hatchback', 'Hatchback'),
        ('suv', 'SUV'),
        ('convertible', 'Convertible'),
    )

    NUM_OF_SEATS = (
        (2, '2'),
        (4, '4'),
        (5, '5'),
        (7, '7'),
        (8, '8'),
    )

    CONDITION = (
        ('new', 'New'),
        ('used', 'Used'),
    )

    GEARBOX = (
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    )

    FUEL = (
        ('diesel', 'Diesel'),
        ('petrol', 'Petrol'),
        ('electric', 'Electric'),
    )

    MANUFACTURED_IN = (
        ('2023', '2023'),
        ('2022', '2022'),
        ('2021', '2021'),
        ('2020', '2020'),
        ('2019', '2019'),
        ('2018', '2018'),
    )

    COLOURS = (
        ('white', 'White'),
        ('black', 'Black'),
        ('silver', 'Silver'),
        ('yellow', 'Yellow'),
        ('red', 'Red'),
    )

    LOCATIONS = (
        ('london', 'London'),
        ('birmingham', 'Birmingham'),
        ('manchester', 'Manchester'),
        ('leeds', 'Leeds'),
        ('liverpool', 'Liverpool'),
        ('glasgow', 'Glasgow'),
        ('edinburgh', 'Edinburgh'),
        ('aberdeen', 'Aberdeen'),
    )

    MODEL_CHOICES = CAR_MODELS['audi'] + CAR_MODELS['bmw'] + CAR_MODELS['ford'] + CAR_MODELS['jaguar'] + CAR_MODELS[
        'land_rover'] + CAR_MODELS['mercedes_benz'] + CAR_MODELS['nissan'] + CAR_MODELS['porsche'] + CAR_MODELS[
        'tesla'] + CAR_MODELS['toyota']

    tuple(MODEL_CHOICES)

    unique_car_id = models.CharField(max_length=6, primary_key=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, verbose_name="Title")
    price = models.PositiveIntegerField(verbose_name="Price")
    brand = models.CharField(max_length=14, choices=CAR_BRANDS, verbose_name="Brand")
    model = models.CharField(max_length=18, choices=MODEL_CHOICES, verbose_name="Model")
    condition = models.CharField(max_length=4, choices=CONDITION, verbose_name="Condition")
    description = models.TextField(verbose_name="Description")
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='car_images/', blank=True, verbose_name="Photos / video")
    num_of_seats = models.PositiveIntegerField(choices=NUM_OF_SEATS, verbose_name="Number of seats")
    body_type = models.CharField(max_length=11, choices=BODY_TYPES, verbose_name="Body type")
    mileage = models.PositiveIntegerField(verbose_name="Mileage")
    transmission = models.CharField(max_length=9, choices=GEARBOX, verbose_name="Transmission")
    fuel_type = models.CharField(max_length=8, choices=FUEL, verbose_name="Fuel type")
    year = models.CharField(max_length=4, choices=MANUFACTURED_IN, verbose_name="Year")
    colour = models.CharField(max_length=6, choices=COLOURS, verbose_name="Colour")
    location = models.CharField(max_length=10, choices=LOCATIONS, verbose_name="Location")

    # field that sorting is based on
    # TODO: add cookies and stuff to count how many views a car listing gets
    #  maybe make it more advanced than just counting views
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.unique_car_id
