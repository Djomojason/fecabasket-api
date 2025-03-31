from django.db import models

class Club(models.Model):
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    nom = models.CharField(max_length=100)
    nom_dirigeant = models.CharField(max_length=100, null=True, blank=True)
    date_creation = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    localite = models.CharField(max_length=100, null=True, blank=True)
    numero_telephone = models.CharField(max_length=20, null=True, blank=True)
    entraineur = models.CharField(max_length=100, null=True, blank=True)
    dossier = models.FileField(upload_to='dossiers/', null=True, blank=True)
    palmares = models.TextField(null=True, blank=True)
    couleurs_maillot = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

class Entraineur(models.Model):
    photo = models.ImageField(upload_to='entraineurs/', null=True, blank=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    lieu_residence = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    club = models.CharField(max_length=100)
    dossier = models.FileField(upload_to='dossiers_entraineurs/', null=True, blank=True)
    palmares = models.TextField(null=True, blank=True)
    notification = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Joueur(models.Model):
    SEXE_CHOICES = [('M', 'Masculin'), ('F', 'Féminin')]
    MAIN_CHOICES = [
        ('Droite', 'Droite'),
        ('Gauche', 'Gauche'),
        ('Ambidextre', 'Ambidextre')
    ]
    STATUT_CHOICES = [
        ('Actif', 'Actif'),  # Première lettre majuscule
        ('Inactif', 'Inactif'),
    ]
    
    photo = models.ImageField(upload_to='joueurs/', null=True, blank=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    date_naissance = models.DateField(null=True, blank=True)
    lieu_naissance = models.CharField(max_length=100, null=True, blank=True)
    residence = models.CharField(max_length=100, null=True, blank=True)
    main_forte = models.CharField(max_length=10, choices=MAIN_CHOICES, default='Droite')
    poids = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    taille = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    envergure = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    dossard = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    reseaux_sociaux = models.TextField(null=True, blank=True)
    annee_inscription = models.IntegerField(null=True, blank=True)
    nom_etablissement = models.CharField(max_length=150, null=True, blank=True)
    classe_frequentee = models.CharField(max_length=50, null=True, blank=True)
    nom_parent_1 = models.CharField(max_length=100, null=True, blank=True)
    telephone_parent_1 = models.CharField(max_length=15, null=True, blank=True)
    nom_parent_2 = models.CharField(max_length=100, null=True, blank=True)
    telephone_parent_2 = models.CharField(max_length=15, null=True, blank=True)
    passions = models.TextField(null=True, blank=True)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='Actif')
    dossier = models.FileField(upload_to='dossiers_joueurs/', null=True, blank=True)
    club = models.CharField(max_length=255, null=True, blank=True)
    ligue = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def imc(self):
        if self.taille and self.poids:
            return self.poids / ((self.taille/100) ** 2)
        return None

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Officiel(models.Model):
    noms = models.CharField(max_length=50)
    prenoms = models.CharField(max_length=50)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    lieu_residence = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    photo_profil = models.ImageField(upload_to='officiels/', null=True, blank=True)
    grade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.prenoms} {self.noms}"
    
#python manage.py runserver         