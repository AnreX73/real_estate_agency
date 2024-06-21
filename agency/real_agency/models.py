from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=30, blank=True, verbose_name="телефон для связи"
    )
    is_estate_agent = models.BooleanField(
        db_default=False, verbose_name="Агент по недвижимости"
    )

    def get_absolute_url(self):
        return reverse("profile", kwargs={"user_id": self.pk})

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class AllObjectsCategories(models.Model):
    category = models.CharField(max_length=255, verbose_name="Категория объекта")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    is_out_city = models.BooleanField(db_default=False, verbose_name="За городом")
    category_icon = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Иконка категории"
    )

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_slug": self.slug})

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Категория объекта"
        verbose_name_plural = "Категории объектов"


class InCityRegion(models.Model):
    region = models.CharField(max_length=255, verbose_name="Район города")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )

    def get_absolute_url(self):
        return reverse("region", kwargs={"region_slug": self.slug})

    def __str__(self):
        return self.region

    class Meta:
        verbose_name = "Район города"
        verbose_name_plural = "Районы города"


class InCityMetro(models.Model):
    metro = models.CharField(max_length=255, verbose_name="Метро")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )

    def get_absolute_url(self):
        return reverse("metro", kwargs={"metro_slug": self.slug})

    def __str__(self):
        return self.metro

    class Meta:
        verbose_name = "Метро"
        verbose_name_plural = "Метро"


class InCityRoomAmount(models.Model):
    room_amount = models.CharField(max_length=255, verbose_name="Количество комнат")
    room_amount_int = models.IntegerField(verbose_name="Количество комнат цифрой")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )

    def get_absolute_url(self):
        return reverse("room_amount", kwargs={"room_amount_slug": self.slug})

    def __str__(self):
        return self.room_amount

    class Meta:
        verbose_name = "Количество комнат"
        verbose_name_plural = "Количество комнат"


class InCityRepairType(models.Model):
    repair_type = models.CharField(max_length=255, verbose_name="Тип ремонта")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )

    def get_absolute_url(self):
        return reverse("repair_type", kwargs={"repair_type_slug": self.slug})

    def __str__(self):
        return self.repair_type

    class Meta:
        verbose_name = "Тип ремонта"
        verbose_name_plural = "Типы ремонта"




class InCityBalconyType(models.Model):
    balcony = models.CharField(max_length=255, verbose_name="Балкон")


    def __str__(self):
        return self.balcony

    class Meta:
        verbose_name = "Балкон"
        verbose_name_plural = "Балконы"



# тип лифта
class InCityLiftType(models.Model):
    lift = models.CharField(max_length=255, verbose_name="Тип лифта")


    def __str__(self):
        return self.lift

    class Meta:
        verbose_name = "Тип лифта"
        verbose_name_plural = "Типы лифтов"

# тип стройматериалов
class InCityRoofType(models.Model):
    roof = models.CharField(max_length=255, verbose_name="Тип стройматериалов")


    def __str__(self):
        return self.roof

    class Meta:
        verbose_name = "Тип стройматериалов"
        verbose_name_plural = "Типы стройматериалов"

#загородная недвижимость

#расстояние до города
class OutCityDistanceToCity(models.Model):
    distance_to_city = models.CharField(max_length=255, verbose_name="Расстояние до города")
    distance_to_city_int = models.IntegerField(verbose_name="Расстояние до города цифрой")


    def __str__(self):
        return self.distance_to_city

    class Meta:
        verbose_name = "Расстояние до города"
        verbose_name_plural = "Расстояния до города"

# форма собственности
class OutCityOwnershipType(models.Model):
    ownership_type = models.CharField(max_length=255, verbose_name="Форма собственности")


    def __str__(self):
        return self.ownership_type

    class Meta:
        verbose_name = "Форма собственности"
        verbose_name_plural = "Формы собственности"

# электроснабжение
class OutCityElectricity(models.Model):
    electricity = models.CharField(max_length=255, verbose_name="Электроснабжение")


    def __str__(self):
        return self.electricity

    class Meta:
        verbose_name = "Электроснабжение"
        verbose_name_plural = "Электроснабжение"

# водоснабжение
class OutCityWaterSupply(models.Model):
    water_supply = models.CharField(max_length=255, verbose_name="Водоснабжение")


    def __str__(self):
        return self.water_supply

    class Meta:
        verbose_name = "Водоснабжение"
        verbose_name_plural = "Водоснабжение"

# газоснабжение
class OutCityGasSupply(models.Model):
    gas_supply = models.CharField(max_length=255, verbose_name="Газоснабжение")


    def __str__(self):
        return self.gas_supply

    class Meta:
        verbose_name = "Газоснабжение"
        verbose_name_plural = "Газоснабжение"

# баня
class OutCityBathRoom(models.Model):
    bath_room = models.CharField(max_length=255, verbose_name="Баня")


    def __str__(self):
        return self.bath_room

    class Meta:
        verbose_name = "Баня"
        verbose_name_plural = "Баня"



# Асфальтовая дорога
class OutCityAsphaltRoad(models.Model):
    asphalt_road = models.CharField(max_length=255, verbose_name="Асфальтовая дорога")


    def __str__(self):
        return self.asphalt_road

    class Meta:
        verbose_name = "Асфальтовая дорога"
        verbose_name_plural = "Асфальтовая дорога"



# Магазин рядом
class OutCityShopNearly(models.Model):
    title = models.CharField(max_length=55, verbose_name='Магазин рядом')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Магазин рядом'
        verbose_name_plural = 'Магазин рядом'
        ordering = ['id']


# Водоем рядом
class OutCityWaterNearly(models.Model):
    title = models.CharField(max_length=55, verbose_name='Водоем рядом')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Водоем рядом'
        verbose_name_plural = 'Водоем рядом'
        ordering = ['id']


# Лес рядом
class OutCityForestNearly(models.Model):
    title = models.CharField(max_length=55, verbose_name='Лес рядом')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Лес рядом'
        verbose_name_plural = 'Лес рядом'
        ordering = ['id']


class BathroomType(models.Model):
    bathroom = models.CharField(max_length=255, verbose_name="Санузел")

    def __str__(self):
        return self.bathroom

    class Meta:
        verbose_name = "Санузел"
        verbose_name_plural = "Санузел"


class AllObjectsAbstract(models.Model):
    class SaleOrRent(models.TextChoices):
        SALE = "sale", "Продажа"
        RENT = "rent", "Аренда"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    object_category = models.ForeignKey(
        AllObjectsCategories,
        on_delete=models.CASCADE,
        verbose_name="Категория объекта",
    )
    address = models.CharField(max_length=255, verbose_name="Адрес")
    estate_agent = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Агент по недвижимости"
    )
    price = models.PositiveIntegerField(null=True, blank=True, verbose_name="Цена")
    is_hot = models.BooleanField(
        db_default=False,
        verbose_name="Горячие объявления",
        help_text="если хотите видеть на главной странице",
    )

    sale_or_rent = models.CharField(
        max_length=10,
        choices=SaleOrRent.choices,
        db_default=SaleOrRent.SALE,
        verbose_name="Тип объявления",
    )
    year = models.CharField(max_length=25, blank=True, verbose_name='Год постройки / Сдачи')
    content = RichTextField(blank=True, verbose_name='текстовое описание ')

    def get_absolute_url(self):
        return reverse("object", kwargs={"object_slug": self.slug})

    def format_price(self):
        price = self.price
        format_price =  '{0:,}'.format(price).replace(',', '`')
        return format_price
    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class InCityObject(AllObjectsAbstract):
    city_region = models.ForeignKey(
        InCityRegion, on_delete=models.CASCADE, verbose_name="Район города"
    )
    metro = models.ForeignKey(
        InCityMetro, on_delete=models.CASCADE, verbose_name="Метро"
    )
    metro_distance = models.CharField(max_length=255, blank=True, verbose_name='расстояние до метро')
    rooms_amount = models.ForeignKey(
        InCityRoomAmount, on_delete=models.CASCADE,related_name="rooms_amount", verbose_name="Количество комнат"
    )
    obj_square = models.PositiveIntegerField(blank=True, null=True, verbose_name="Площадь")
    live_square = models.PositiveIntegerField(blank=True, null=True, verbose_name="Жилая площадь")
    kitchen_square = models.PositiveIntegerField(blank=True, null=True, verbose_name="Площадь кухни")
    obj_repair = models.ForeignKey(
        InCityRepairType, on_delete=models.CASCADE, verbose_name="Ремонт"
    )
    obj_floor = models.PositiveIntegerField(blank=True, null=True, verbose_name="Этаж")
    all_floor = models.PositiveIntegerField(blank=True, null=True, verbose_name="Всего этажей")
    bathroom = models.ForeignKey(BathroomType, on_delete=models.CASCADE, verbose_name="Санузел")
    lift = models.ForeignKey(InCityLiftType, on_delete=models.CASCADE, verbose_name="Лифт")
    obj_roof = models.ForeignKey(InCityRoofType, on_delete=models.CASCADE, verbose_name="тип постройки")
    #floor


    class Meta:
        verbose_name = 'объект'
        verbose_name_plural = 'объект в городе'
        ordering = ['id']


class OutCityObject(AllObjectsAbstract):
    distance_to_city = models.ForeignKey(
        OutCityDistanceToCity, on_delete=models.CASCADE, verbose_name="Расстояние до города"
    )
    land_square = models.PositiveIntegerField(blank=True, verbose_name='площадь участка')
    type_of_ownership = models.ForeignKey(
        OutCityOwnershipType, on_delete=models.CASCADE, verbose_name="Вид собственности"
    )
    square = models.PositiveIntegerField(blank=True, verbose_name='площадь дома', help_text='в кв.м')
    obj_roof = models.ForeignKey(InCityRoofType, on_delete=models.CASCADE, verbose_name="тип постройки")
    bathroom = models.ForeignKey(BathroomType, on_delete=models.CASCADE, verbose_name="Санузел")
    electricity = models.ForeignKey(OutCityElectricity, on_delete=models.CASCADE, verbose_name="Электроснабжение")
    water = models.ForeignKey(OutCityWaterSupply, on_delete=models.CASCADE, verbose_name="Водоснабжение")
    gas = models.ForeignKey(OutCityGasSupply, on_delete=models.CASCADE, verbose_name="Газоснабжение")
    bath = models.ForeignKey(OutCityBathRoom, on_delete=models.CASCADE, verbose_name="Баня")
    asphalt_road = models.ForeignKey(OutCityAsphaltRoad, on_delete=models.CASCADE, verbose_name="Асфальтовая дорога")
    shop_nearly = models.ForeignKey(OutCityShopNearly, on_delete=models.CASCADE, verbose_name="Магазин рядом")
    water_nearly = models.ForeignKey(OutCityWaterNearly, on_delete=models.CASCADE, verbose_name="Водоем рядом")
    forest_nearly = models.ForeignKey(OutCityForestNearly, on_delete=models.CASCADE, verbose_name="Лес рядом")


    class Meta:
        verbose_name = 'объект'
        verbose_name_plural = 'объект за городом'
        ordering = ['id']

class CommercialObject(AllObjectsAbstract):
    obj_square = models.PositiveIntegerField(blank=True, null=True, verbose_name="Площадь")
    city_region = models.ForeignKey(
        InCityRegion, on_delete=models.CASCADE, verbose_name="Район города"
    )
    metro = models.ForeignKey(
        InCityMetro, on_delete=models.CASCADE, verbose_name="Метро"
    )

    class Meta:
        verbose_name = 'коммерческий объект'
        verbose_name_plural = 'коммерческие объекты'
        ordering = ['id']






