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



# форма собственности
class OutCityOwnershipType(models.Model):
    ownership_type = models.CharField(max_length=255, verbose_name="Форма собственности")


    def __str__(self):
        return self.ownership_type

    class Meta:
        verbose_name = "Форма собственности"
        verbose_name_plural = "Формы собственности"




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
    distance_to_city_int = models.PositiveIntegerField(blank=True, null=True, verbose_name="Расстояние до города в км")
    land_square = models.PositiveIntegerField(blank=True,null=True, verbose_name='площадь участка в сотках', help_text='в сотках')
    type_of_ownership = models.ForeignKey(
        OutCityOwnershipType, on_delete=models.CASCADE, verbose_name="Вид собственности"
    )
    square = models.PositiveIntegerField(blank=True,null=True, verbose_name='площадь дома', help_text='в кв.м')
    obj_roof = models.ForeignKey(InCityRoofType, on_delete=models.CASCADE, verbose_name="тип постройки")
    bathroom = models.ForeignKey(BathroomType, on_delete=models.CASCADE, verbose_name="Санузел")
    electricity = models.BooleanField(default=False, verbose_name="Электроснабжение")
    water = models.BooleanField(default=False,verbose_name="Водоснабжение")
    gas = models.BooleanField(default=False, verbose_name="Газоснабжение")
    bath = models.BooleanField(default=False, verbose_name="Баня")
    shop_nearly = models.BooleanField(default=False,verbose_name="Магазин рядом")
    water_nearly = models.BooleanField(default=False, verbose_name="Водоем рядом")
    forest_nearly = models.BooleanField(default=False, verbose_name="Лес рядом")


    class Meta:
        verbose_name = 'объект'
        verbose_name_plural = 'объект за городом'
        ordering = ['id']

class CommercialObject(AllObjectsAbstract):
    class ComercObjectType(models.TextChoices):
        TRADEAREA = 'Торговая площадь', 'Торговая площадь'
        OFFICE = 'Офис', 'Офис'
        STOCK = 'Склад', 'Склад'
        FREEASSIGNMENT = 'Свободное назначение', 'Свободное назначение'
        MANUFACTURE = 'Производство', 'Производство'
        BUILDING = 'Здание', 'Здание'
        OTHER = 'Другое', 'Другое'
    obj_square = models.PositiveIntegerField(blank=True, null=True, verbose_name="Площадь")
    city_region = models.ForeignKey(
        InCityRegion, on_delete=models.CASCADE, verbose_name="Район города"
    )
    metro = models.ForeignKey(
        InCityMetro, on_delete=models.CASCADE, verbose_name="Метро"
    )
    commercу_object_type = models.CharField(
        max_length=255, choices=ComercObjectType.choices,default=ComercObjectType.OTHER, verbose_name="Тип объекта коммерческого недвижимости"
    ) 

    class Meta:
        verbose_name = 'коммерческий объект'
        verbose_name_plural = 'коммерческие объекты'
        ordering = ['id']


class SiteGraphicObjects(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(upload_to="help_objects/", verbose_name="Изображение")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")


    class Meta:
        verbose_name = 'графический объект'
        verbose_name_plural = 'графические объекты'
        ordering = ['id']


class Gallery(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(upload_to="gallery/", verbose_name="Изображение")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    


    class Meta:
        abstract = True

class InCityGallery(Gallery):
    obj = models.ForeignKey(InCityObject, on_delete=models.CASCADE, verbose_name="Объект")

    class Meta:
        verbose_name = 'галерея'
        verbose_name_plural = 'галереи'
        ordering = ['id']

class OutCityGallery(Gallery):
    obj = models.ForeignKey(OutCityObject, on_delete=models.CASCADE, verbose_name="Объект")

    class Meta:
        verbose_name = 'галерея'
        verbose_name_plural = 'галереи'
        ordering = ['id']


class CommercialGallery(Gallery):
    obj = models.ForeignKey(CommercialObject, on_delete=models.CASCADE, verbose_name="Объект")

    class Meta:
        verbose_name = 'галерея'
        verbose_name_plural = 'галереи'
        ordering = ['id']



