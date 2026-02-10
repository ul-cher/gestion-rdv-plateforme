"""
Commande de gestion Django pour créer des données de démonstration
Usage: python manage.py create_sample_data
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime, timedelta, time
from rdv_app.models import (
    Praticien, Patient, HorairePraticien, RendezVous, Rappel
)

User = get_user_model()


class Command(BaseCommand):
    help = 'Crée des données de démonstration pour l\'application'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Création des données de démonstration...'))
        
        # Créer un admin s'il n'existe pas
        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_superuser(
                username='admin',
                email='admin@plateforme-rdv.fr',
                password='admin123',
                first_name='Admin',
                last_name='Système',
                role='admin'
            )
            self.stdout.write(self.style.SUCCESS(f'✓ Admin créé: admin / admin123'))
        
        # Créer des praticiens
        praticiens_data = [
            {
                'username': 'dr_martin',
                'email': 'martin@plateforme-rdv.fr',
                'first_name': 'Jean',
                'last_name': 'Martin',
                'civilite': 'Dr',
                'specialite': 'Médecin généraliste',
                'telephone': '0123456789',
                'numero_rpps': '12345678901'
            },
            {
                'username': 'dr_dupont',
                'email': 'dupont@plateforme-rdv.fr',
                'first_name': 'Marie',
                'last_name': 'Dupont',
                'civilite': 'Dr',
                'specialite': 'Cardiologue',
                'telephone': '0123456790',
                'numero_rpps': '12345678902'
            },
            {
                'username': 'dr_bernard',
                'email': 'bernard@plateforme-rdv.fr',
                'first_name': 'Pierre',
                'last_name': 'Bernard',
                'civilite': 'Dr',
                'specialite': 'Dermatologue',
                'telephone': '0123456791',
                'numero_rpps': '12345678903'
            }
        ]
        
        for data in praticiens_data:
            if not User.objects.filter(username=data['username']).exists():
                user = User.objects.create_user(
                    username=data['username'],
                    email=data['email'],
                    password='praticien123',
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    role='praticien'
                )
                
                praticien = Praticien.objects.create(
                    user=user,
                    civilite=data['civilite'],
                    specialite=data['specialite'],
                    telephone=data['telephone'],
                    numero_rpps=data['numero_rpps'],
                    actif=True
                )
                
                # Créer des horaires (Lundi à Vendredi, 9h-12h et 14h-18h)
                for jour in range(1, 6):
                    HorairePraticien.objects.create(
                        praticien=praticien,
                        jour_semaine=jour,
                        heure_debut=time(9, 0),
                        heure_fin=time(12, 0)
                    )
                    HorairePraticien.objects.create(
                        praticien=praticien,
                        jour_semaine=jour,
                        heure_debut=time(14, 0),
                        heure_fin=time(18, 0)
                    )
                
                self.stdout.write(self.style.SUCCESS(f'✓ Praticien créé: {data["username"]} / praticien123'))
        
        # Créer des patients
        patients_data = [
            {
                'username': 'patient1',
                'email': 'jean.dupuis@email.fr',
                'first_name': 'Jean',
                'last_name': 'Dupuis',
                'civilite': 'M',
                'telephone': '0612345678',
                'adresse': '123 Rue de la Paix, 75001 Paris',
                'date_naissance': datetime(1980, 5, 15).date()
            },
            {
                'username': 'patient2',
                'email': 'sophie.martin@email.fr',
                'first_name': 'Sophie',
                'last_name': 'Martin',
                'civilite': 'Mme',
                'telephone': '0612345679',
                'adresse': '45 Avenue des Champs, 75008 Paris',
                'date_naissance': datetime(1992, 8, 22).date()
            },
            {
                'username': 'patient3',
                'email': 'paul.bernard@email.fr',
                'first_name': 'Paul',
                'last_name': 'Bernard',
                'civilite': 'M',
                'telephone': '0612345680',
                'adresse': '78 Boulevard Saint-Michel, 75006 Paris',
                'date_naissance': datetime(1975, 12, 3).date()
            }
        ]
        
        patients = []
        for data in patients_data:
            if not User.objects.filter(username=data['username']).exists():
                user = User.objects.create_user(
                    username=data['username'],
                    email=data['email'],
                    password='patient123',
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    role='patient'
                )
                
                patient = Patient.objects.create(
                    user=user,
                    civilite=data['civilite'],
                    telephone=data['telephone'],
                    adresse=data['adresse'],
                    date_naissance=data['date_naissance']
                )
                patients.append(patient)
                
                self.stdout.write(self.style.SUCCESS(f'✓ Patient créé: {data["username"]} / patient123'))
        
        # Créer quelques rendez-vous
        praticiens = Praticien.objects.all()
        if praticiens.exists() and patients:
            today = timezone.now()
            
            # RDV passé
            rdv1 = RendezVous.objects.create(
                patient=patients[0],
                praticien=praticiens[0],
                date_heure=today - timedelta(days=5, hours=2),
                motif='Consultation générale',
                statut='confirme'
            )
            
            # RDV futurs
            rdv2 = RendezVous.objects.create(
                patient=patients[1],
                praticien=praticiens[0],
                date_heure=today + timedelta(days=2, hours=3),
                motif='Contrôle annuel',
                statut='confirme'
            )
            
            # Créer les rappels pour le RDV futur
            Rappel.objects.create(
                rdv=rdv2,
                type_rappel='48h',
                date_envoi_prevue=rdv2.date_heure - timedelta(hours=48),
                envoye=False
            )
            Rappel.objects.create(
                rdv=rdv2,
                type_rappel='24h',
                date_envoi_prevue=rdv2.date_heure - timedelta(hours=24),
                envoye=False
            )
            
            rdv3 = RendezVous.objects.create(
                patient=patients[2],
                praticien=praticiens[1] if len(praticiens) > 1 else praticiens[0],
                date_heure=today + timedelta(days=7, hours=1),
                motif='Consultation cardiologie',
                statut='en_attente'
            )
            
            self.stdout.write(self.style.SUCCESS(f'✓ {3} rendez-vous créés'))
        
        self.stdout.write(self.style.SUCCESS('\n================================='))
        self.stdout.write(self.style.SUCCESS('✓ Données de démonstration créées!'))
        self.stdout.write(self.style.SUCCESS('=================================\n'))
        self.stdout.write('Comptes créés:')
        self.stdout.write('  Admin: admin / admin123')
        self.stdout.write('  Praticiens: dr_martin, dr_dupont, dr_bernard / praticien123')
        self.stdout.write('  Patients: patient1, patient2, patient3 / patient123')
        self.stdout.write('')

