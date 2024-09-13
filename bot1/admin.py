from django.contrib import admin

from .models import Contact, Management


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "tg_id",
        "phone_number",
        "first_name",
        "last_name",
        "reg_completed",
        "username",
        "grade",
        "stream",
        "is_admin",
    )
    list_filter = ("grade", "bot_number", "stream", "created_at", "updated_at")
    search_fields = ("phone_number", "first_name", "last_name", "username")

    def __str__(self) -> str:
        return f"Student: {self.id:02d}"


class MGTAdmin(admin.ModelAdmin):
    list_display = ("name", "registration_open", "id")


admin.site.register(Management, MGTAdmin)
admin.site.register(Contact, ContactAdmin)
