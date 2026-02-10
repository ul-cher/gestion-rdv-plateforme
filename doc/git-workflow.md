# 🔄 Git Workflow - Guide de l'Équipe

## 📋 Configuration Initiale (Une seule fois)

### 1. Cloner le repository
```bash
git clone <URL_GITHUB> plateforme-rdv-django
cd plateforme-rdv-django
```

### 2. Configurer Git en pull rebase par défaut
```bash
git config --global pull.rebase true
```

Cette commande évite les commits de merge inutiles et garde l'historique propre.

---

## 🚀 Workflow Quotidien

### Avant de commencer à travailler
```bash
# Récupérer les dernières modifications
git pull
```

### Pendant le développement
```bash
# Vérifier l'état de vos fichiers
git status

# Voir les modifications
git diff
```

### Après avoir terminé une feature
```bash
# Ajouter tous les fichiers modifiés
git add .

# Créer un commit avec référence JIRA
git commit -m "[JIRA-XXX] Description de la feature"

# Envoyer sur le serveur
git push
```

---

## ✅ Exemples de Commits

### Format recommandé
```
[JIRA-123] Ajout gestion des praticiens
[JIRA-124] Fix bug calendrier rendez-vous
[JIRA-125] Amélioration dashboard statistiques
[JIRA-126] Refactoring modèle Patient
[JIRA-127] Ajout export PDF pour les rapports
```

### Commande complète en une ligne
```bash
git pull && git add . && git commit -m "[JIRA-XXX] Description" && git push
```

---

## 📁 Fichiers à NE PAS commiter

Le `.gitignore` est déjà configuré pour ignorer :

- `target/` - Builds (Java/Maven)
- `node_modules/` - Dépendances npm
- `config/` - Configuration locale
- `__pycache__/` - Cache Python
- `venv/` - Environnement virtuel Python
- `db.sqlite3` - Base de données locale
- `.env` - Variables d'environnement

---

## 🔧 Commandes Utiles

### Voir l'historique
```bash
git log --oneline -10
```

### Annuler les modifications locales (avant commit)
```bash
git restore <fichier>
# ou pour tous les fichiers
git restore .
```

### Voir qui a modifié un fichier
```bash
git blame <fichier>
```

### Récupérer un fichier depuis le serveur
```bash
git checkout origin/main -- <fichier>
```

---

## ⚠️ En cas de conflit

Si `git pull` génère un conflit :

1. Git vous indiquera les fichiers en conflit
2. Ouvrez les fichiers et résolvez les conflits (cherchez `<<<<<<<`, `=======`, `>>>>>>>`)
3. Une fois résolu :
```bash
git add <fichiers_résolus>
git rebase --continue
```

4. Si vous voulez abandonner :
```bash
git rebase --abort
```

---

## 🎯 Bonnes Pratiques

✅ **À FAIRE**
- Commit fréquemment avec des messages clairs
- Référencer le ticket JIRA dans chaque commit
- Faire `git pull` avant chaque `git push`
- Vérifier avec `git status` avant de commit

❌ **À NE PAS FAIRE**
- Commiter directement dans `main` sans pull avant
- Utiliser `git push --force` (sauf urgence et accord équipe)
- Commiter des fichiers de configuration locale
- Faire des commits avec message vague ("fix", "update", etc.)

---

## 👥 Collaboration

### Inviter un collègue
1. Aller sur GitHub → Settings → Collaborators
2. Inviter par email ou username
3. Le collègue recevra une invitation par email

### Partager ses modifications
```bash
# Vérifier qu'on est à jour
git pull

# Partager
git push
```

---

## 📞 Support

En cas de problème :
1. Vérifier `git status` pour comprendre l'état
2. Lire le message d'erreur complet
3. Demander de l'aide à l'équipe
4. En dernier recours : créer une copie du dossier avant toute action destructive

---

## 🔗 Ressources

- [Documentation Git](https://git-scm.com/doc)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
- [GitHub Guides](https://guides.github.com/)
