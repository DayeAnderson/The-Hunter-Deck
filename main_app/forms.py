from django import forms
from .models import Weapon

WEAPON_CHOICES= (
    ('great_sword', 'Great Sword'),
    ('sword_&_shield', 'Sword & Shield'),
    ('dual_blades', 'Dual Blades'),
    ('long_sword', 'Long Sword'),
    ('hammer', 'Hammer'),
    ('hunting_horn', 'Hunting Horn'),
    ('lance', 'Lance'),
    ('gunlance', 'Gunlance'),
    ('switch_axe', 'Switch Axe'),
    ('charge_blade', 'Charge Blade'),
    ('insect_glaive', 'Insect Glaive'),
    ('bow', 'Bow'),
    ('light_bowgun', 'Light Bowgun'),
    ('heavy_bowgun', 'Heavy Bowgun')
)

class WeaponForm(forms.ModelForm):
    type = forms.ChoiceField(choices=WEAPON_CHOICES, required=True)
    class Meta:
        model = Weapon
