# Architecture de la Plateforme RDV

## Vue d'ensemble

La plateforme de gestion de rendez-vous est construite sur une architecture moderne séparant le backend et le frontend.

## Backend - Django

### Stack Technique
- **Framework:** Django 5.0.1
- **Langage:** Python 3.8+
- **Base de données:** SQLite3 (dev) / PostgreSQL (prod recommandé)
- **ORM:** Django ORM

### Architecture MVC (MVT Django)

#### Models (Modèles de données)
- **User** - Gestion des utilisateurs avec rôles (admin, praticien, patient)
- **Praticien** - Informations sur les médecins
- **HorairePraticien** - Horaires de consultation par jour
- **Indisponibilite** - Gestion des congés
- **Patient** - Informations patients
- **RendezVous** - Gestion des RDV avec statuts
- **Annulation** - Demandes d'annulation
- **Rappel** - Système de rappels automatiques
- **Log** - Traçabilité des actions

#### Views (Vues/Contrôleurs)
- **Authentification:** Login, Register, Logout
- **Dashboard:** Vue d'ensemble personnalisée par rôle
- **CRUD:** Praticiens, Patients, RDV
- **Gestion:** Horaires, Indisponibilités, Annulations
- **Reporting:** Statistiques, Logs, Export CSV/PDF

#### Templates (Présentation)
- Base template avec Bootstrap 5
- Templates modulaires par fonctionnalité
- Responsive design (mobile-first)

### Sécurité
- **Authentification:** Django Auth System
- **Autorisation:** Décorateurs @login_required, permissions par rôle
- **CSRF Protection:** Activée par défaut
- **Logs:** Traçabilité complète avec IP et user agent
- **Validation:** Formulaires Django avec validations personnalisées

### API Design (Future)
Structure prête pour une API REST avec Django REST Framework:
- `/api/praticiens/` - Liste et détails des praticiens
- `/api/patients/` - Gestion des patients
- `/api/rendez-vous/` - CRUD des rendez-vous
- `/api/disponibilites/` - Créneaux disponibles

## Frontend

### Stack Actuelle
- **Bootstrap 5** - Framework CSS
- **Bootstrap Icons** - Iconographie
- **JavaScript Vanilla** - Interactions dynamiques

### Structure
```
frontend/
├── package.json
└── (Prêt pour Angular, React ou Vue.js)
```

### Évolutions possibles
- Migration vers Angular/React/Vue.js
- API REST pour découplage backend/frontend
- Progressive Web App (PWA)
- WebSockets pour notifications temps réel

## Base de Données

### Schéma relationnel

```
User (auth_user)
  └── Praticien (1:1)
       ├── HorairePraticien (1:N)
       ├── Indisponibilite (1:N)
       └── RendezVous (1:N)
  └── Patient (1:1)
       └── RendezVous (1:N)

RendezVous
  ├── Praticien (N:1)
  ├── Patient (N:1)
  ├── Annulation (1:1 optionnel)
  └── Rappel (1:N)

Log (traçabilité)
```

### Migrations
- Gérées par Django migrations
- Historique versionné
- Rollback possible

## Déploiement

### Développement
```bash
cd backend
python manage.py runserver
```

### Production (recommandé)
- **Web Server:** Nginx
- **WSGI Server:** Gunicorn
- **Database:** PostgreSQL
- **Cache:** Redis
- **Monitoring:** Sentry, ELK Stack
- **CI/CD:** GitHub Actions, GitLab CI

### Environnements
- `.env` pour configuration sensible
- `settings.py` modulaire (dev, staging, prod)

## Workflow Git

### Branches
- `main` - Production
- `develop` - Développement
- `feature/*` - Nouvelles fonctionnalités
- `hotfix/*` - Corrections urgentes

### Commits
Format: `[JIRA-XXX] Description`

Exemples:
- `[JIRA-123] Add patient appointment booking`
- `[JIRA-456] Fix calendar display bug`

### Workflow recommandé
```bash
git pull
git add .
git commit -m "[JIRA-XXX] feature description"
git push
```

## Performances

### Optimisations actuelles
- Requêtes optimisées avec `select_related` et `prefetch_related`
- Templates mis en cache
- Static files collectés et compressés

### Optimisations futures
- Redis pour cache et sessions
- CDN pour static files
- Database indexing
- Query optimization avec Django Debug Toolbar

## Tests

### Structure recommandée
```
backend/rdv_app/tests/
├── test_models.py
├── test_views.py
├── test_forms.py
└── test_utils.py
```

### Commandes
```bash
python manage.py test
python manage.py test rdv_app.tests.test_models
```

## Monitoring et Logs

### Logs système
- Fichier: `backend/*.log` (ignoré par git)
- Format: timestamp, level, message

### Logs applicatifs
- Table `Log` dans la base de données
- Capture: action, user, IP, timestamp
- Consultation: Interface admin

## Documentation

- `README.md` - Guide de démarrage
- `doc/architecture.md` - Ce document
- `doc/user-guide.md` - Guide utilisateur
- Docstrings dans le code Python
- Comments JSDoc dans le code JavaScript

---

**Version:** 1.0  
**Date:** Février 2026  
**Auteur:** Master ESILV - M1
