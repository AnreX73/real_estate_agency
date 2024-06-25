from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User, AllObjectsCategories, InCityRegion, InCityMetro, InCityRoomAmount, InCityRepairType, InCityBalconyType, InCityLiftType, InCityRoofType, OutCityDistanceToCity, OutCityOwnershipType, OutCityElectricity, OutCityWaterSupply, OutCityGasSupply, OutCityBathRoom, OutCityAsphaltRoad, OutCityShopNearly, OutCityWaterNearly, OutCityForestNearly, BathroomType, InCityObject, OutCityObject, CommercialObject


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
        'phone_number',
        'is_estate_agent',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'is_estate_agent',
    )
    raw_id_fields = ('groups', 'user_permissions')


@admin.register(AllObjectsCategories)
class AllObjectsCategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'is_out_city', 'gethtmlPhoto')
    list_filter = ('is_out_city',)
    search_fields = ('slug',)
    prepopulated_fields = {'slug': ('category',)}
    save_on_top = True

    def gethtmlPhoto(self, picture):
        if picture.category_icon:
            return mark_safe(f"<img src='{picture.category_icon.url}' width=50>")

    gethtmlPhoto.short_description = 'миниатюра'


@admin.register(InCityRegion)
class InCityRegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'region',)
    search_fields = ('region',)
    prepopulated_fields = {'slug': ('region',)}
    save_on_top = True


@admin.register(InCityMetro)
class InCityMetroAdmin(admin.ModelAdmin):
    list_display = ('id', 'metro',)
    search_fields = ('slug',)
    prepopulated_fields = {'slug': ('metro',)}
    save_on_top = True


@admin.register(InCityRoomAmount)
class InCityRoomAmountAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_amount', 'room_amount_int', 'slug')
    search_fields = ('slug',)


@admin.register(InCityRepairType)
class InCityRepairTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'repair_type', 'slug')
    search_fields = ('slug',)


@admin.register(InCityBalconyType)
class InCityBalconyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'balcony')


@admin.register(InCityLiftType)
class InCityLiftTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'lift')


@admin.register(InCityRoofType)
class InCityRoofTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'roof')


@admin.register(OutCityDistanceToCity)
class OutCityDistanceToCityAdmin(admin.ModelAdmin):
    list_display = ('id', 'distance_to_city', 'distance_to_city_int')


@admin.register(OutCityOwnershipType)
class OutCityOwnershipTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'ownership_type')


@admin.register(OutCityElectricity)
class OutCityElectricityAdmin(admin.ModelAdmin):
    list_display = ('id', 'electricity')


@admin.register(OutCityWaterSupply)
class OutCityWaterSupplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'water_supply')


@admin.register(OutCityGasSupply)
class OutCityGasSupplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'gas_supply')


@admin.register(OutCityBathRoom)
class OutCityBathRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'bath_room')


@admin.register(OutCityAsphaltRoad)
class OutCityAsphaltRoadAdmin(admin.ModelAdmin):
    list_display = ('id', 'asphalt_road')


@admin.register(OutCityShopNearly)
class OutCityShopNearlyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(OutCityWaterNearly)
class OutCityWaterNearlyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(OutCityForestNearly)
class OutCityForestNearlyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(BathroomType)
class BathroomTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'bathroom')


@admin.register(InCityObject)
class InCityObjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'is_published',
        'name',
        'slug',
        'object_category',
        'address',
        'estate_agent',
        'price',
        'is_hot',
        'sale_or_rent',
        'year',
        'content',
        'city_region',
        'metro',
        'metro_distance',
        'rooms_amount',
        'obj_square',
        'live_square',
        'kitchen_square',
        'obj_repair',
        'obj_floor',
        'all_floor',
        'bathroom',
        'lift',
        'obj_roof',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'is_published',
        'object_category',
        'estate_agent',
        'is_hot',
        'city_region',
        'metro',
        'rooms_amount',
        'obj_repair',
        'bathroom',
        'lift',
        'obj_roof',
    )
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}
    date_hierarchy = 'created_at'


@admin.register(OutCityObject)
class OutCityObjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'is_published',
        'name',
        'slug',
        'object_category',
        'address',
        'estate_agent',
        'price',
        'is_hot',
        'sale_or_rent',
        'year',
        'content',
        'distance_to_city',
        'land_square',
        'type_of_ownership',
        'square',
        'obj_roof',
        'bathroom',
        'electricity',
        'water',
        'gas',
        'bath',
        'asphalt_road',
        'shop_nearly',
        'water_nearly',
        'forest_nearly',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'is_published',
        'object_category',
        'estate_agent',
        'is_hot',
        'distance_to_city',
        'type_of_ownership',
        'obj_roof',
        'bathroom',
        'electricity',
        'water',
        'gas',
        'bath',
        'asphalt_road',
        'shop_nearly',
        'water_nearly',
        'forest_nearly',
    )
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}
    date_hierarchy = 'created_at'


@admin.register(CommercialObject)
class CommercialObjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'is_published',
        'name',
        'slug',
        'object_category',
        'address',
        'estate_agent',
        'price',
        'is_hot',
        'sale_or_rent',
        'year',
        'content',
        'obj_square',
        'city_region',
        'metro',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'is_published',
        'object_category',
        'estate_agent',
        'is_hot',
        'city_region',
        'metro',
    )
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}
    date_hierarchy = 'created_at'


admin.site.site_header = 'Real Agency'
admin.site.site_title = 'Real Agency'