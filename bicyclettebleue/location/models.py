from django.db import models

class Client(models.Model):
    cli_id = models.AutoField(db_column='CLI_ID', primary_key=True)  # Field name made lowercase.
    cli_nom = models.CharField(db_column='CLI_NOM', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_prenom = models.CharField(db_column='CLI_PRENOM', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_adresseposte = models.CharField(db_column='CLI_ADRESSEPOSTE', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_date_naissance = models.IntegerField(db_column='CLI_DATE_NAISSANCE', blank=True, null=True)  # Field name made lowercase.
    cli_mail = models.CharField(db_column='CLI_MAIL', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_tel = models.CharField(db_column='CLI_TEl', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_membre = models.CharField(db_column='CLI_MEMBRE', blank=True, null=True, max_length=100)  # Field name made lowercase.
    cli_date_debut = models.DateField()  # Field name made lowercase.
    cli_date_fin = models.DateField()  # Field name made lowercase.

    def __str__(self):
        return self.cli_nom

    class Meta:
        managed = False
        db_table = 'Client'




class Velo(models.Model):
    vel_id = models.AutoField(db_column='VEL_ID', primary_key = True)  # Field name made lowercase.
    vel_num_cadre = models.IntegerField(db_column='VEL_NUM_CADRE', blank=True, null=True)  # Field name made lowercase.
    vel_nom = models.TextField(db_column='VEL_NOM', blank=True, null=True)  # Field name made lowercase.
    vel_marque = models.TextField(db_column='VEL_MARQUE', blank=True, null=True)  # Field name made lowercase.
    vel_couleur = models.TextField(db_column='VEL_COULEUR', blank=True, null=True)  # Field name made lowercase.
    vel_type = models.TextField(db_column='VEL_TYPE', blank=True, null=True)  # Field name made lowercase.
    vel_photo = models.TextField(db_column='VEL_PHOTO', blank=True, null=True)  # Field name made lowercase.
    vel_statut = models.TextField(db_column='VEL_STATUT', blank=True, null=True)  # Field name made lowercase.
    vel_etat = models.TextField(db_column='VEL_ETAT', blank=True, null=True)  # Field name made lowercase.
    vel_remarque = models.TextField(db_column='VEL_REMARQUE', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.vel_nom


    class Meta:
        managed = False
        db_table = 'Velo'



class Location(models.Model):
    loc_id = models.AutoField(db_column='LOC_ID', primary_key = True)  # Field name made lowercase.
    loc_statut = models.CharField(db_column='LOC_STATUT', blank=True, null=True, max_length=30)  # Field name made lowercase.
    loc_client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'Location'


class Location_Velo(models.Model):
    date_debut = models.DateField()  # Field name made lowercase.
    date_fin   = models.DateField()  # Field name made lowercase.
    lv_loc_id = models.ForeignKey(Location, on_delete=models.CASCADE)  # Field name made lowercase.
    lv_vel_id = models.ForeignKey(Velo, on_delete=models.CASCADE)  # Field name made lowercase.



    class Meta:
        managed = False
        db_table = 'Location_Velo'


