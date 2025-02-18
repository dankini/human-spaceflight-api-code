# apps/missions/admin.py

# deviates from standard admin.py layout so that we can incorporate data import/export functionality in admin interface using django-import-export library

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from apps.missions.models import Mission, Crew
from apps.astronauts.models import Astronaut


# Inline for Crew Members in the Mission Admin
class CrewInline(admin.TabularInline):
    model = Crew
    extra = 0  # Number of empty forms to display
    fields = ('astronaut', 'role', 'age_at_launch_ymd')
    autocomplete_fields = ['astronaut']  # Allows searching for astronauts in the admin
    readonly_fields = ('age_at_launch_ymd',)  # Can make these fields readonly


# Mission Admin
#class MissionAdmin(admin.ModelAdmin):
@admin.register(Mission)
class MissionAdmin(ImportExportModelAdmin):
    list_display = ('name', 'launch_date_time', 'agency', 'crew_size', 'get_crew_names')
    search_fields = ('name', 'agency__name',)
    list_filter = ('launch_date_time', 'agency')
    inlines = [CrewInline]
    readonly_fields = ('get_crew_names',)  # To make sure crew names are visible, but non-editable
    
    # Optional method to display crew members as a comma-separated list
    def get_crew_names(self, obj):
        return ", ".join(astronaut.get_full_astronaut_name for astronaut in obj.crew_members.all())
    get_crew_names.short_description = 'Crew Members'


# Crew Admin
#class CrewAdmin(admin.ModelAdmin):
@admin.register(Crew)
class CrewAdmin(ImportExportModelAdmin):
    list_display = ('astronaut', 'mission', 'role', 'age_at_launch_ymd')
    search_fields = ('astronaut__first_name', 'astronaut__last_name', 'mission__name', 'role')
    list_filter = ('mission', 'astronaut', 'role')
    autocomplete_fields = ['astronaut', 'mission']  # Allows searching through the admin
    readonly_fields = ('age_at_launch_ymd',)  # Make this field readonly since it is dynamically calculated

    # Optionally you can add a method to calculate the astronaut's age at mission launch
    def age_at_launch(self, obj):
        return obj.age_at_launch
    age_at_launch.short_description = 'Age at Launch'

    # Order dropdown lists alphabetically
    #def formfield_for_foreignkey(self, db_field, request, **kwargs):
        #if db_field.name == "astronaut":
            #kwargs["queryset"] = Astronaut.objects.order_by("astronaut")
            #kwargs["queryset"] = Astronaut.objects.filter(anyfilters=anyfilters).order_by#('astronaut')
        #elif db_field.name == "mission":
            #kwargs["queryset"] = Mission.objects.order_by("name")
        #return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    
   # def formfield_for_foreignkey(self, db_field, request, **kwargs):
       # if db_field.name == "author":
            #kwargs["queryset"] = Author.objects.filter(anyfilters=anyfilters).order_by('name')
        #return super(MyModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)



# Register the models with the admin site
#admin.site.register(Mission, MissionAdmin)
#admin.site.register(Crew, CrewAdmin)




#from import_export.admin import ImportExportModelAdmin
#from django.contrib import admin
#from apps.missions.models import Mission, Crew


# class MissionAdmin(admin.ModelAdmin):
#@admin.register(Mission)
#class MissionAdmin(ImportExportModelAdmin):
    #list_display = [
        #"name",
        #"agency",
        #"launch_date_time",
        #"duration_secs",
    #]


# admin.site.register(Mission, MissionAdmin)


#@admin.register(Crew)
#class CrewAdmin(ImportExportModelAdmin):
    #list_display = [
        #"astronaut",
        #"mission",
        #"role",
        #"age_at_launch_ymd",
    #]


# admin.site.register(Crew, CrewAdmin)
