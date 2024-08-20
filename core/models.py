from django.db import models
from multiselectfield import MultiSelectField
    
class Ctf(models.Model):

    DIFFICULTY_LEVELS = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
        ('Insane', 'Insane'),
    ]

    CATEGORY_CHOICES = [
        ('blue_team', 'Blue Team'),
        ('red_team', 'Red Team'),
        ('api_pentesting', 'API Pentesting'),
        ('web_security', 'Web Security'),
        ('android_security', 'Android Security'),
        ('open_source', 'Open Source'),
        ('source_code_review', 'Source Code Review'),
        ('sast', 'SAST'),
        ('dast', 'DAST'),
        ('owasp_top_10', 'OWASP Top 10'),
    ]

    TECH_USAGE = [
        ('linux', 'Linux'),
        ('burp_suite', 'Burp Suite'),
        ('nmap', 'Nmap'),
        ('nessus', 'Nessus'),
        ('web_app', 'Web App'),
        ('windows', 'Window'),
        
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    creator_name = models.CharField(max_length=100, null=True, blank=True)
    short_description = models.TextField(max_length=50)
    creation_date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=500)
    category = MultiSelectField(choices=CATEGORY_CHOICES, null=True, blank=True) 
    Tech_usage = MultiSelectField(choices=TECH_USAGE, null=True, blank=True) # Linked to Category
    image = models.ImageField(upload_to='ctf_images/')
    official_writeup = models.URLField(max_length=200, null=True, blank=True)  # URLField for writeup link
    users_joined = models.PositiveIntegerField(default=0)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVELS, default='Easy')
    install_instructions = models.TextField(max_length=700, null=True, blank=True)
    more_info = models.URLField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name
    

class PublicWriteUp(models.Model):
    ctf = models.ForeignKey(Ctf, related_name='writeups', on_delete=models.CASCADE)
    link = models.URLField(max_length=150)

    def __str__(self):
        return f"WriteUp for {self.ctf.name}"
