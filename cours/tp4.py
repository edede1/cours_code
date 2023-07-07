from datetime import datetime, timedelta, timezone

# Décalage horaire pour Africa/Douala
delta_douala = timedelta(hours=1)  # Décalage de +1 heure par rapport à UTC

# Décalage horaire pour Europe/Paris
delta_paris = timedelta(hours=2)  # Décalage de +2 heures par rapport à UTC

# Obtention de l'heure actuelle en UTC
heure_utc = datetime.now(timezone.utc)

# Calcul de l'heure pour Africa/Douala
heure_douala = heure_utc + delta_douala

# Calcul de l'heure pour Europe/Paris
heure_paris = heure_utc + delta_paris

# Conversion des heures au format local
heure_douala_local = heure_douala.strftime("%H:%M:%S")
heure_paris_local = heure_paris.strftime("%H:%M:%S")

# Affichage des heures correspondantes
print("Heure à Douala (Africa/Douala) :", heure_douala_local)
print("Heure à Paris (Europe/Paris) :", heure_paris_local)
