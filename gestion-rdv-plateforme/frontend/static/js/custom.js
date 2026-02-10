// Scripts personnalisés pour la Plateforme RDV

// Auto-hide alerts after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
});

// Confirmation avant suppression/annulation
function confirmAction(message) {
    return confirm(message || 'Êtes-vous sûr de vouloir effectuer cette action ?');
}

// Format date picker to French format
document.addEventListener('DOMContentLoaded', function() {
    const dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(function(input) {
        input.setAttribute('lang', 'fr');
    });
});

