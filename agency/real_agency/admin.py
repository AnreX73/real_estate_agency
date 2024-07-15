from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (
    User,
    AllObjectsCategories,
    InCityRegion,
    InCityMetro,
    InCityRoomAmount,
    InCityRepairType,
    InCityBalconyType,
    InCityLiftType,
    InCityRoofType,
    OutCityOwnershipType,
    BathroomType,
    InCityObject,
    OutCityObject,
    CommercialObject,
    SiteGraphicObjects,
    InCityGallery,
    OutCityGallery,
    CommercialGallery
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "last_login",
        "is_superuser",
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
        "date_joined",
        "phone_number",
        "is_estate_agent",
    )
    list_filter = (
        "is_superuser",
        "is_staff",
        "is_active",
        "date_joined",
        "is_estate_agent",
    )
    raw_id_fields = ("groups", "user_permissions")


@admin.register(AllObjectsCategories)
class AllObjectsCategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "is_out_city", "gethtmlPhoto")
    list_filter = ("is_out_city",)
    search_fields = ("slug",)
    prepopulated_fields = {"slug": ("category",)}
    save_on_top = True

    def gethtmlPhoto(self, picture):
        if picture.category_icon:
            return mark_safe(f"<img src='{picture.category_icon.url}' width=50>")

    gethtmlPhoto.short_description = "миниатюра"


@admin.register(InCityRegion)
class InCityRegionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "region",
    )
    search_fields = ("region",)
    prepopulated_fields = {"slug": ("region",)}
    save_on_top = True


@admin.register(InCityMetro)
class InCityMetroAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "metro",
    )
    search_fields = ("slug",)
    prepopulated_fields = {"slug": ("metro",)}
    save_on_top = True


@admin.register(InCityRoomAmount)
class InCityRoomAmountAdmin(admin.ModelAdmin):
    list_display = ("id", "room_amount", "room_amount_int", "slug")
    search_fields = ("slug",)


@admin.register(InCityRepairType)
class InCityRepairTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "repair_type", "slug")
    search_fields = ("slug",)


@admin.register(InCityBalconyType)
class InCityBalconyTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "balcony")


@admin.register(InCityLiftType)
class InCityLiftTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "lift")


@admin.register(InCityRoofType)
class InCityRoofTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "roof")


@admin.register(OutCityOwnershipType)
class OutCityOwnershipTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "ownership_type")


@admin.register(BathroomType)
class BathroomTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "bathroom")


class InCityGalleryAdmin(admin.TabularInline):
    model = InCityGallery
    fields = ("gethtmlPhoto", "name", "is_published")
    readonly_fields = ("gethtmlPhoto",)

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=75>")

    gethtmlPhoto.short_description = "миниатюра"



class InCityObjectAdmin(admin.ModelAdmin):
    inlines = [InCityGalleryAdmin]
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "is_published",
        "name",
        "slug",
        "object_category",
        "address",
        "estate_agent",
        "price",
        "is_hot",
        "sale_or_rent",
        "year",
        "content",
        "city_region",
        "metro",
        "metro_distance",
        "rooms_amount",
        "obj_square",
        "live_square",
        "kitchen_square",
        "obj_repair",
        "obj_floor",
        "all_floor",
        "bathroom",
        "lift",
        "obj_roof",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "is_published",
        "object_category",
        "estate_agent",
        "is_hot",
        "city_region",
        "metro",
        "rooms_amount",
        "obj_repair",
        "bathroom",
        "lift",
        "obj_roof",
    )
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ["name"]}
    date_hierarchy = "created_at"

class OutCityGalleryAdmin(admin.TabularInline):
    model = OutCityGallery
    fields = ("gethtmlPhoto", "name", "is_published")
    readonly_fields = ("gethtmlPhoto",)

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=75>")

    gethtmlPhoto.short_description = "миниатюра"

class OutCityObjectAdmin(admin.ModelAdmin):
    inlines = [OutCityGalleryAdmin]
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "is_published",
        "name",
        "slug",
        "object_category",
        "address",
        "estate_agent",
        "price",
        "is_hot",
        "sale_or_rent",
        "year",
        "content",
        "distance_to_city_int",
        "land_square",
        "type_of_ownership",
        "square",
        "obj_roof",
        "bathroom",
        "electricity",
        "water",
        "gas",
        "bath",
        "shop_nearly",
        "water_nearly",
        "forest_nearly",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "is_published",
        "object_category",
        "estate_agent",
        "is_hot",
        "distance_to_city_int",
        "type_of_ownership",
        "obj_roof",
        "bathroom",
        "electricity",
        "water",
        "gas",
        "bath",
        "shop_nearly",
        "water_nearly",
        "forest_nearly",
    )
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ["name"]}
    date_hierarchy = "created_at"

class CommercialGalleryAdmin(admin.TabularInline):
    model = CommercialGallery
    fields = ("gethtmlPhoto", "name", "is_published")
    readonly_fields = ("gethtmlPhoto",)

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=75>")

    gethtmlPhoto.short_description = "миниатюра"

class CommercialObjectAdmin(admin.ModelAdmin):
    inlines = [CommercialGalleryAdmin]
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "is_published",
        "name",
        "slug",
        "object_category",
        "address",
        "estate_agent",
        "price",
        "is_hot",
        "sale_or_rent",
        "year",
        "content",
        "obj_square",
        "city_region",
        "metro",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "is_published",
        "object_category",
        "estate_agent",
        "is_hot",
        "city_region",
        "metro",
    )
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ["name"]}
    date_hierarchy = "created_at"


@admin.register(SiteGraphicObjects)
class SiteGraphicObjectsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "gethtmlPhoto")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ["name"]}

    def gethtmlPhoto(self, picture):
        if picture.image:
            return mark_safe(f"<img src='{picture.image.url}' width=50>")
    gethtmlPhoto.short_description = "миниатюра"

admin.site.register(InCityObject, InCityObjectAdmin)
admin.site.register(OutCityObject, OutCityObjectAdmin)
admin.site.register(CommercialObject, CommercialObjectAdmin)
admin.site.site_header = "Real Agency"
admin.site.site_title = "Real Agency"
