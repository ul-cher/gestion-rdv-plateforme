# Frontend - Plateforme de Gestion des Rendez-vous

## 📁 Structure

```
frontend/
├── package.json          # Configuration npm (placeholder)
├── templates/            # Templates HTML Django
│   ├── base.html        # Template de base
│   └── rdv_app/         # Templates de l'application
│       ├── login.html
│       ├── register.html
│       ├── dashboard.html
│       ├── praticiens/   # Gestion des praticiens
│       ├── patients/     # Gestion des patients
│       ├── rendez_vous/  # Gestion des RDV
│       ├── annulations/  # Gestion des annulations
│       ├── rappels/      # Rappels automatiques
│       ├── statistiques/ # Dashboard statistiques
│       └── logs/         # Logs système
│
└── static/              # Fichiers statiques
    ├── css/
    │   └── custom.css   # Styles personnalisés
    └── js/
        └── custom.js    # JavaScript personnalisé
```

## 🎨 Stack Technique

- **Templates Engine:** Django Templates
- **CSS Framework:** Bootstrap 5 (CDN)
- **Icons:** Bootstrap Icons
- **JavaScript:** Vanilla JS + custom scripts

## 📝 Notes

- Les templates sont rendus côté serveur par Django
- Les fichiers statiques sont servis par Django en développement
- Bootstrap 5 est chargé via CDN pour simplifier le déploiement
