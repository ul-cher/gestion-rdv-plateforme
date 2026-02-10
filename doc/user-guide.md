# Guide Utilisateur - Plateforme de Gestion des Rendez-vous

## Table des matières

1. [Connexion et Inscription](#connexion-et-inscription)
2. [Interface Patient](#interface-patient)
3. [Interface Praticien](#interface-praticien)
4. [Interface Administrateur](#interface-administrateur)
5. [FAQ](#faq)

---

## Connexion et Inscription

### Première connexion

1. Accédez à l'application : `http://127.0.0.1:8000/`
2. Cliquez sur **"S'inscrire"** si vous êtes un nouveau patient
3. Remplissez le formulaire d'inscription :
   - Nom d'utilisateur
   - Email
   - Mot de passe
   - Informations personnelles (nom, prénom, date de naissance, etc.)
4. Cliquez sur **"Créer mon compte"**

### Connexion

1. Entrez votre **nom d'utilisateur**
2. Entrez votre **mot de passe**
3. Cliquez sur **"Se connecter"**

### Comptes de test

Pour tester l'application, utilisez les comptes suivants :

| Rôle | Username | Password |
|------|----------|----------|
| Administrateur | `admin` | `admin123` |
| Praticien | `dr_martin` | `praticien123` |
| Patient | `patient1` | `patient123` |

---

## Interface Patient

### Dashboard Patient

Après connexion, vous accédez à votre tableau de bord qui affiche :
- Vos **prochains rendez-vous**
- Votre **historique** de rendez-vous
- Accès rapide aux fonctionnalités

### Prendre un rendez-vous

1. Cliquez sur **"Prendre un rendez-vous"**
2. Sélectionnez un **praticien** dans la liste
3. Choisissez une **date** disponible
4. Sélectionnez un **créneau horaire** libre
5. Ajoutez un **motif** (optionnel)
6. Cliquez sur **"Réserver"**
7. Votre rendez-vous est créé avec le statut "En attente de confirmation"

### Consulter mes rendez-vous

1. Allez dans **"Mes rendez-vous"**
2. Visualisez tous vos RDV passés et à venir
3. Filtrez par statut :
   - 🟡 **En attente** : En attente de confirmation
   - 🟢 **Confirmé** : Validé par le praticien
   - 🔴 **Annulé** : Rendez-vous annulé
   - ⚪ **Absence** : Vous ne vous êtes pas présenté

### Annuler un rendez-vous

1. Dans votre liste de rendez-vous, cliquez sur un RDV
2. Cliquez sur **"Demander une annulation"**
3. Indiquez le **motif** de l'annulation
4. Cliquez sur **"Envoyer la demande"**
5. La demande sera traitée par le praticien ou l'administrateur

### Modifier mon profil

1. Cliquez sur votre nom en haut à droite
2. Sélectionnez **"Mon profil"**
3. Modifiez vos informations
4. Cliquez sur **"Enregistrer"**

---

## Interface Praticien

### Dashboard Praticien

Votre tableau de bord affiche :
- **Planning de la journée**
- **Rendez-vous à confirmer**
- **Statistiques** rapides (nombre de patients, taux d'occupation)

### Gérer mon planning

#### Voir mon planning

1. Cliquez sur **"Mon planning"**
2. Visualisez vos rendez-vous par :
   - **Jour**
   - **Semaine**
   - **Mois**
3. Cliquez sur un rendez-vous pour voir les détails

#### Définir mes horaires de consultation

1. Allez dans **"Mes horaires"**
2. Pour chaque jour de la semaine :
   - Cochez si vous travaillez ce jour-là
   - Indiquez l'heure de **début** (ex: 09:00)
   - Indiquez l'heure de **fin** (ex: 18:00)
3. Cliquez sur **"Enregistrer"**

#### Ajouter une indisponibilité (congés)

1. Cliquez sur **"Mes indisponibilités"**
2. Cliquez sur **"Ajouter une indisponibilité"**
3. Renseignez :
   - **Date de début**
   - **Date de fin**
   - **Motif** (congés, formation, etc.)
4. Cliquez sur **"Enregistrer"**
5. Les créneaux seront automatiquement bloqués

### Confirmer des rendez-vous

1. Allez dans **"Rendez-vous en attente"**
2. Consultez la liste des RDV non confirmés
3. Pour chaque rendez-vous :
   - Cliquez sur **"Confirmer"** ✅
   - Ou cliquez sur **"Refuser"** ❌ (avec motif)

### Gérer mes patients

1. Cliquez sur **"Mes patients"**
2. Consultez la liste de tous vos patients
3. Cliquez sur un patient pour voir :
   - Ses informations personnelles
   - Son historique de rendez-vous
   - Ses annulations

### Traiter les demandes d'annulation

1. Allez dans **"Annulations"**
2. Consultez les demandes en attente
3. Pour chaque demande :
   - **Accepter** l'annulation
   - **Refuser** l'annulation (avec motif)

---

## Interface Administrateur

### Dashboard Administrateur

Le tableau de bord admin affiche :
- **Vue d'ensemble globale** de l'activité
- **Statistiques en temps réel**
- **Dernières actions** dans le système

### Gérer les praticiens

#### Ajouter un praticien

1. Cliquez sur **"Praticiens"** > **"Ajouter un praticien"**
2. Remplissez le formulaire :
   - Informations personnelles
   - **Spécialité** (généraliste, cardiologue, etc.)
   - **Durée de consultation** (en minutes)
   - Créer le compte utilisateur associé
3. Cliquez sur **"Enregistrer"**

#### Modifier/Supprimer un praticien

1. Dans la liste des praticiens
2. Cliquez sur **"Modifier"** ✏️ ou **"Supprimer"** 🗑️
3. Faites vos modifications
4. Cliquez sur **"Enregistrer"**

### Gérer les patients

1. Cliquez sur **"Patients"**
2. Actions disponibles :
   - **Voir** les détails
   - **Modifier** les informations
   - **Supprimer** un patient (attention, supprime aussi ses RDV)

### Gérer tous les rendez-vous

1. Cliquez sur **"Tous les rendez-vous"**
2. Visualisez tous les RDV du système
3. Filtrez par :
   - **Praticien**
   - **Statut**
   - **Date**
4. Actions possibles :
   - Modifier un rendez-vous
   - Changer le statut
   - Supprimer un rendez-vous

### Statistiques et rapports

#### Tableau de bord statistiques

1. Cliquez sur **"Statistiques"**
2. Consultez :
   - **Taux d'occupation** par praticien
   - **Taux d'annulation**
   - **Répartition** par spécialité
   - **Évolution** des rendez-vous dans le temps

#### Export de données

1. Dans la page statistiques
2. Cliquez sur **"Exporter CSV"** ou **"Exporter PDF"**
3. Le fichier se télécharge automatiquement

### Consulter les logs

1. Cliquez sur **"Logs"**
2. Consultez toutes les actions importantes :
   - Qui a fait quoi et quand
   - Adresse IP
   - Type d'action (création, modification, suppression)
3. Filtrez par :
   - **Utilisateur**
   - **Type d'action**
   - **Date**

### Gérer les rappels automatiques

Les rappels sont générés automatiquement :
- **48h avant** le rendez-vous
- **24h avant** le rendez-vous

Pour consulter les rappels envoyés :
1. Cliquez sur **"Rappels"**
2. Visualisez l'historique des rappels
3. Vérifiez le statut d'envoi

---

## FAQ

### Comment réinitialiser mon mot de passe ?

Contactez un administrateur qui pourra réinitialiser votre mot de passe via l'interface Django Admin.

### Puis-je prendre plusieurs rendez-vous en même temps ?

Oui, vous pouvez prendre plusieurs rendez-vous avec différents praticiens ou aux différentes dates.

### Combien de temps à l'avance puis-je prendre un rendez-vous ?

Il n'y a pas de limite. Vous pouvez réserver tant que le praticien a défini ses horaires.

### Puis-je annuler un rendez-vous confirmé ?

Oui, mais vous devez faire une **demande d'annulation** qui sera validée par le praticien ou l'administrateur.

### Que signifie "En attente de confirmation" ?

Cela signifie que vous avez réservé un créneau mais que le praticien doit encore valider votre rendez-vous.

### Comment savoir si mon rendez-vous est confirmé ?

Vous recevrez une notification dans votre dashboard et le statut passera à **"Confirmé"** 🟢.

### Puis-je modifier un rendez-vous déjà pris ?

Non directement. Vous devez d'abord annuler le rendez-vous existant, puis en créer un nouveau.

### Les rappels sont-ils automatiques ?

Oui, le système génère automatiquement des rappels 48h et 24h avant chaque rendez-vous confirmé.

### Que se passe-t-il si je ne me présente pas à un rendez-vous ?

Le praticien ou l'administrateur peut marquer votre rendez-vous comme **"Absence"**. Cela apparaîtra dans votre historique.

### Comment contacter le support technique ?

Contactez l'administrateur système à l'adresse : support@plateforme-rdv.com

---

## Raccourcis clavier (Futurs)

| Raccourci | Action |
|-----------|--------|
| `Ctrl + N` | Nouveau rendez-vous |
| `Ctrl + P` | Voir le planning |
| `Ctrl + S` | Sauvegarder |
| `Esc` | Fermer la modale |

---

## Support

Pour toute question ou problème technique :
- 📧 Email : support@plateforme-rdv.com
- 📞 Téléphone : 01 23 45 67 89
- 💬 Chat : Disponible dans l'application (coin inférieur droit)

---

**Version:** 1.0  
**Dernière mise à jour:** Février 2026
