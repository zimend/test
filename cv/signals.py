from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import UserProfile, Section



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		userprofile = UserProfile.objects.create(user=instance)
		
@receiver(post_save, sender=UserProfile)
def create_profile(sender, instance, created, **kwargs):
	if created:
		for i in [
				# ("hero","Bienvenue sur mon profile."),
				("main", "Cette section englobe toute les autres section mis à part l accueil"),
				("about","Dans cette section vous trouverez mes informations ainsi qu'une courte biographie."),
				("facts","Ici vous constatez des faits mesurés sur certains accoplissement!!"),
				("skills","Ci dessous je dénombre mes compétences techniques avec un score en pourcentage."),
				("resume","Ce qui suit est un curuculum vitae englobant mon éducation et mon parcours professionel chronologué."),
				("portfolio","Ici une galerie de mes réalisations achevées grouper en ce portfolio"),
				("certificats","Cette section présente mes Certificats et attestations de complétion de formation ou parcours"),
				("testimonials","Nous vous présentons ici quelques témoignages de nos clients , de nos collaborateurs et responsables avec qui, préalablement nous avons eu la chance de travailler"),
				("contact","Pour nous contacter veuillez remplir le formulaire suivant")
				# ("footer","Cette page est réalisée pour présenter des cv pour des profile utilisateurs")
			]:
			sections = Section.objects.create(profile=instance)
			sections.name = i[0]
			sections.description = i[1]
			sections.save()
