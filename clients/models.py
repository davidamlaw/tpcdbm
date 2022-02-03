from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

class ClientEfs(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    nickname = models.CharField(max_length=64, blank=True)
    date_reviewed = models.DateField(default=timezone.now)
    current_address = models.CharField(max_length=64, blank=True)
    ca_city = models.CharField(max_length=64, blank=True)
    ca_state = models.CharField(max_length=2, blank=True)
    ca_zip = models.CharField(max_length=5, blank=True)
    phone1 = models.CharField(max_length=14, blank=True)
    ext1 = models.CharField(max_length=5, blank=True)
    phone2 = models.CharField(max_length=14, blank=True)
    ext2 = models.CharField(max_length=5, blank=True)
    previous_address = models.CharField(max_length=64, blank=True)
    pa_city = models.CharField(max_length=64, blank=True)
    pa_state = models.CharField(max_length=2, blank=True)
    pa_zip = models.CharField(max_length=5, blank=True)
    family_address = models.CharField(max_length=64, blank=True)
    fa_city = models.CharField(max_length=64, blank=True)
    fa_state = models.CharField(max_length=2, blank=True)
    fa_zip = models.CharField(max_length=5, blank=True)
    gender = models.CharField(max_length=32, blank=True)
    race = models.CharField(max_length=64, blank=True)
    dob = models.DateField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(999)])
    height_ft = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(12)])
    height_in = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(11)])
    weight = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(2000)])
    build = models.CharField(max_length=32, blank=True)
    hair = models.CharField(max_length=32, blank=True)
    eye_color = models.CharField(max_length=32, blank=True)
    resuscitation_status = models.CharField(max_length=32, blank=True)
    photo = models.ImageField(blank=True, upload_to='media')
    photo_date = models.DateField(blank=True, null=True)
    legal_competency_status = models.CharField(max_length=64, blank=True)
    language = models.CharField(max_length=64, blank=True)
    identifying_marks = models.CharField(max_length=128, blank=True)
    guardian1 = models.CharField(max_length=128, blank=True)
    g1_relationship = models.CharField(max_length=32, blank=True)
    g1_address = models.CharField(max_length=64, blank=True)
    g1_city = models.CharField(max_length=64, blank=True)
    g1_state = models.CharField(max_length=2, blank=True)
    g1_zip = models.CharField(max_length=5, blank=True)
    g1_home = models.CharField(max_length=14, blank=True)
    g1_work = models.CharField(max_length=14, blank=True)
    g1_ext = models.CharField(max_length=5, blank=True)
    g1_cell = models.CharField(max_length=14, blank=True)
    g1_email = models.EmailField(max_length=256, blank=True)
    guardian2 = models.CharField(max_length=128, blank=True)
    g2_relationship = models.CharField(max_length=32, blank=True)
    g2_address = models.CharField(max_length=64, blank=True)
    g2_city = models.CharField(max_length=64, blank=True)
    g2_state = models.CharField(max_length=2, blank=True)
    g2_zip = models.CharField(max_length=5, blank=True)
    g2_home = models.CharField(max_length=14, blank=True)
    g2_work = models.CharField(max_length=14, blank=True)
    g2_ext = models.CharField(max_length=5, blank=True)
    g2_cell = models.CharField(max_length=14, blank=True)
    g2_email = models.EmailField(max_length=256, blank=True)
    contact1 = models.CharField(max_length=128, blank=True)
    c1_relationship = models.CharField(max_length=32, blank=True)
    c1_home = models.CharField(max_length=14, blank=True)
    c1_work = models.CharField(max_length=14, blank=True)
    c1_ext = models.CharField(max_length=5, blank=True)
    c1_cell = models.CharField(max_length=14, blank=True)
    c1_email = models.EmailField(max_length=256, blank=True)
    contact2 = models.CharField(max_length=128, blank=True)
    c2_relationship = models.CharField(max_length=32, blank=True)
    c2_home = models.CharField(max_length=14, blank=True)
    c2_work = models.CharField(max_length=14, blank=True)
    c2_ext = models.CharField(max_length=5, blank=True)
    c2_cell = models.CharField(max_length=14, blank=True)
    c2_email = models.EmailField(max_length=256, blank=True)
    contact3 = models.CharField(max_length=128, blank=True)
    c3_relationship = models.CharField(max_length=32, blank=True)
    c3_home = models.CharField(max_length=14, blank=True)
    c3_work = models.CharField(max_length=14, blank=True)
    c3_ext = models.CharField(max_length=5, blank=True)
    c3_cell = models.CharField(max_length=14, blank=True)
    c3_email = models.EmailField(max_length=256, blank=True)
    agency_contact1 = models.CharField(max_length=128, blank=True)
    ac1_relationship = models.CharField(max_length=32, blank=True)
    ac1_address = models.CharField(max_length=64, blank=True)
    ac1_city = models.CharField(max_length=64, blank=True)
    ac1_state = models.CharField(max_length=2, blank=True)
    ac1_zip = models.CharField(max_length=5, blank=True)
    ac1_home = models.CharField(max_length=14, blank=True)
    ac1_work = models.CharField(max_length=14, blank=True)
    ac1_ext = models.CharField(max_length=5, blank=True)
    ac1_cell = models.CharField(max_length=14, blank=True)
    ac1_email = models.EmailField(max_length=256, blank=True)
    contact4 = models.CharField(max_length=128, blank=True)
    c4_relationship = models.CharField(max_length=32, blank=True)
    c4_home = models.CharField(max_length=14, blank=True)
    c4_work = models.CharField(max_length=14, blank=True)
    c4_ext = models.CharField(max_length=5, blank=True)
    c4_cell = models.CharField(max_length=14, blank=True)
    c4_email = models.EmailField(max_length=256, blank=True)
    agency_contact2 = models.CharField(max_length=128, blank=True)
    ac2_relationship = models.CharField(max_length=32, blank=True)
    ac2_address = models.CharField(max_length=64, blank=True)
    ac2_city = models.CharField(max_length=64, blank=True)
    ac2_state = models.CharField(max_length=2, blank=True)
    ac2_zip = models.CharField(max_length=5, blank=True)
    ac2_home = models.CharField(max_length=14, blank=True)
    ac2_work = models.CharField(max_length=14, blank=True)
    ac2_ext = models.CharField(max_length=5, blank=True)
    ac2_cell = models.CharField(max_length=14, blank=True)
    ac2_email = models.EmailField(max_length=256, blank=True)
    contact5 = models.CharField(max_length=128, blank=True)
    c5_relationship = models.CharField(max_length=32, blank=True)
    c5_home = models.CharField(max_length=14, blank=True)
    c5_work = models.CharField(max_length=14, blank=True)
    c5_ext = models.CharField(max_length=5, blank=True)
    c5_cell = models.CharField(max_length=14, blank=True)
    c5_email = models.EmailField(max_length=256, blank=True)
    record_location = models.CharField(max_length=64, blank=True)
    area = models.CharField(max_length=32, blank=True)
    physician_first_name = models.CharField(max_length=64, blank=True)
    physician_last_name = models.CharField(max_length=64, blank=True)
    p_address = models.CharField(max_length=64, blank=True)
    p_city = models.CharField(max_length=64, blank=True)
    p_state = models.CharField(max_length=2, blank=True)
    p_zip = models.CharField(max_length=5, blank=True)
    p_phone = models.CharField(max_length=14, blank=True)
    p_phone_ext = models.CharField(max_length=5, blank=True)
    p_fax = models.CharField(max_length=14, blank=True)
    p_fax_ext = models.CharField(max_length=5, blank=True)
    p_email = models.EmailField(max_length=256, blank=True)
    insurance = models.CharField(max_length=128, blank=True)
    can_protect_self = models.BooleanField(default=False)
    behavior_characteristics = models.CharField(max_length=256, blank=True)
    response_to_search = models.CharField(max_length=128, blank=True)
    pattern_of_movement = models.CharField(max_length=128, blank=True)
    places_frequented = models.CharField(max_length=256, blank=True)
    capabilities_limitations = models.CharField(max_length=256, blank=True)
    probable_dress = models.CharField(max_length=256, blank=True)
    last_seen = models.CharField(max_length=256, blank=True)
    last_seen_date = models.DateTimeField(blank=True, null=True)
    diagnosis = models.TextField(blank=True)
    allergies = models.CharField(max_length=256, blank=True)
    medications = models.TextField(blank=True)
    update_first_name = models.CharField(max_length=64, blank=True)
    update_last_name = models.CharField(max_length=64, blank=True)
