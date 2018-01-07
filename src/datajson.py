#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib, json
url = "https://download.data.grandlyon.com/ws/rdata/sit_sitra.sittourisme/all.json"
reponse = urllib.urlopen(url)
data = json.loads(reponse.read())

donnee = data.get("values")

# Création des listes vides pour les items voulus
tab_hotel = []
tab_resto = []
tab_patri = []
tab_com   = []
tab_coll  = []
tab_loc   = []

# Récupère les adresses dans le fichier JSON.
for z in donnee:
	liste_commune = z["commune"]
	# Modification du champ commune car les arrondissements ne sont pas reconnus par le geocoding.
	if liste_commune[-3] == "1" or liste_commune[-4] == "2" or liste_commune[-4] == "3" or liste_commune[-4] == "4" or liste_commune[-4] == "5" or liste_commune[-4] == "6" or liste_commune[-4] == "7" or liste_commune[-4] == "8" or liste_commune[-4] == "9":
		commune = "Lyon"
	else: commune = liste_commune

	# Informations importantes
	nom            = z["nom"]
	nb_etoile      = z["classement"]		# Hôtels, hébergements.
	site           = z["siteweb"]
	tel            = z["telephone"]
	adresse        = z["adresse"] + ", " + commune + ", " + z["codepostal"]
	prix_min       = z["tarifsmin"]			# Hôtels, hébergements et restaurants.
	prix_max       = z["tarifsmax"]
	type_resto_com = z["type_detail"]		# Restaurants et commerces.

	# Remplissage des tableaux
	if z["type"] == "HOTELLERIE":
		tab_hotel.append(adresse + "?" + nom + "?" + nb_etoile + "?" + site + "?" + tel + "?" + prix_min + "?" + prix_max)
	elif z["type"] == "RESTAURATION":
		tab_resto.append(adresse + "?" + nom + "?" + site + "?" + tel + "?" + prix_min +"?" + prix_max + "?"+ type_resto_com)
	elif z["type"] == "PATRIMOINE_CULTUREL":
		tab_patri.append(adresse + "?" + nom + "?" + site + "?" + tel)
	elif z["type"] == "COMMERCE_ET_SERVICE":
		tab_com.append(adresse + "?" + nom + "?" + site + "?" + tel + "?" + type_resto_com)
	elif z["type"] == "HEBERGEMENT_COLLECTIF":
		tab_coll.append(adresse + "?" + nom + "?" + nb_etoile + "?" + site + "?" + tel + "?" + prix_min + "?" + prix_max)
	elif z["type"] == "HEBERGEMENT_LOCATIF":
		tab_loc.append(adresse + "?" + nom + "?" + nb_etoile + "?" + site + "?" + tel + "?" + prix_min + "?" + prix_max)

# Conversion des adresses en latitude et longitude
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='ENTREZ LA CLE ICI!')

#Découpage des chaînes de caractères de chaque ligne du tableau puis conversion en str grâce à .encpde("utf-8") et placement dans le fichier.js

####################### HOTELS ########################
fichier = open("data_hotel.js", "a")
fichier.write("{\"type\": \"hotel\",\n\"features\": [")

indice_i = 0
for i in tab_hotel:
	j = i.split("?")

	adr_j      = j[0].encode("utf-8")
	nom_j      = j[1].encode("utf-8")
	etoile_j   = j[2].encode("utf-8")
	site_j     = j[3].encode("utf-8")
	tel_j      = j[4].encode("utf-8")
	prix_min_j = j[5].encode("utf-8")
	prix_max_j = j[6].encode("utf-8")

	geocode_result_hotel = gmaps.geocode(adr_j)
	if geocode_result_hotel != []:
		latitude  = str(geocode_result_hotel[0]["geometry"]["location"]["lat"])
		longitude = str(geocode_result_hotel[0]["geometry"]["location"]["lng"])

		virgule = "{\"geometry\": {\"type\": \"Point\", \"coordinates\": [" + longitude + "," + latitude + "]}, \"properties\": {\"nom\":\"" + nom_j + "\", \"adresse\": \"" + adr_j +"\"}, \"other_information\": {\"etoile\": \"" + etoile_j + "\", \"siteweb\": \"" + site_j + "\", \"tel\": \"" + tel_j + "\", \"prixMini\": \"" + prix_min_j + "\", \"prixMaxi\": \"" + prix_max_j + "\"}},"

		if indice_i != len(tab_hotel) - 1:
			fichier.write(virgule + "\n")
		else:
			fichier.write(virgule[:-1] + "\n")
	indice_i += 1

fichier.write("]}")
fichier.close()



##################### RESTAURANTS ######################
fichier = open("data_resto.js", "a")
fichier.write("{\"type\": \"resto\",\n\"features\": [")

indice_i = 0
for i in tab_resto:
	j = i.split("?")

	adr_j            = j[0].encode("utf-8")
	nom_j            = j[1].encode("utf-8")
	site_j           = j[2].encode("utf-8")
	tel_j            = j[3].encode("utf-8")
	prix_min_j       = j[4].encode("utf-8")
	prix_max_j       = j[5].encode("utf-8")
	type_resto_com_j = j[6].encode("utf-8")

	geocode_result_resto = gmaps.geocode(adr_j)
	if geocode_result_resto != []:
		latitude  = str(geocode_result_resto[0]["geometry"]["location"]["lat"])
		longitude = str(geocode_result_resto[0]["geometry"]["location"]["lng"])

		virgule = "{\"geometry\": {\"type\": \"Point\", \"coordinates\": [" + longitude + "," + latitude + "]}, \"properties\": {\"nom\": \"" + nom_j + "\", \"adresse\": \"" + adr_j + "\"}, \"other_information\": {\"siteweb\": \"" + site_j + "\", \"tel\": \"" + tel_j + "\", \"prixMini\": \""+ prix_min_j + "\", \"prixMaxi\": \"" + prix_max_j + "\", \"typeResto\": \"" + type_resto_com_j + "\"}},"

		if indice_i != len(tab_resto) - 1:
			fichier.write(virgule + "\n")
		else:
			fichier.write(virgule[:-1] + "\n")
	indice_i += 1

fichier.write("]}")
fichier.close()



################# PATRIMOINE CULTUREL ##################
fichier = open("data_patri.js", "a")
fichier.write("{\"type\": \"patrimoine\",\n\"features\": [")

indice_i = 0
for i in tab_patri:
	j = i.split("?")

	adr_j            = j[0].encode("utf-8")
	nom_j            = j[1].encode("utf-8")
	site_j           = j[2].encode("utf-8")
	tel_j            = j[3].encode("utf-8")

	geocode_result_patri = gmaps.geocode(adr_j)
	if geocode_result_patri != []:
		latitude  = str(geocode_result_patri[0]["geometry"]["location"]["lat"])
		longitude = str(geocode_result_patri[0]["geometry"]["location"]["lng"])

		virgule = "{\"geometry\": {\"type\": \"Point\", \"coordinates\": [" + longitude + "," + latitude + "]}, \"properties\": {\"nom\": \"" + nom_j + "\", \"adresse\": \"" + adr_j + "\"}, \"other_information\": {\"siteweb\": \"" + site_j + "\", \"tel\": \"" + tel_j + "\"}},"

		if indice_i != len(tab_patri) - 1:
			fichier.write(virgule + "\n")
		else:
			fichier.write(virgule[:-1] + "\n")
	indice_i += 1

fichier.write("]}")
fichier.close()



################# COMMERCE ET SERVICE #################
fichier = open("data_commerce.js", "a")
fichier.write("{\"type\": \"commerce\",\n\"features\": [")

indice_i = 0
for i in tab_com:
	j = i.split("?")

	adr_j            = j[0].encode("utf-8")
	nom_j            = j[1].encode("utf-8")
	site_j           = j[2].encode("utf-8")
	tel_j            = j[3].encode("utf-8")
	type_resto_com_j = j[4].encode("utf-8")

	geocode_result_com = gmaps.geocode(adr_j)
	if geocode_result_com != []:
		latitude  = str(geocode_result_com[0]["geometry"]["location"]["lat"])
		longitude = str(geocode_result_com[0]["geometry"]["location"]["lng"])

		virgule = "{\"geometry\": {\"type\": \"Point\", \"coordinates\": [" +longitude + "," + latitude+ "]}, \"properties\": {\"nom\":\" " + nom_j + "\", \"adresse\": \"" + adr_j + "\"}, \"other_information\": {\"siteweb\":\"" + site_j + "\", \"tel\":\"" + tel_j + "\", \"typeCom\": \"" + type_resto_com_j + "\"}},"

		if indice_i != len(tab_com) - 1:
			fichier.write(virgule + "\n")
		else:
			fichier.write(virgule[:-1] + "\n")
	indice_i += 1

fichier.write("]}")
fichier.close()



############### HEBERGEMENT COLLECTIF ##################
fichier = open("data_coll.js", "a")
fichier.write("{\"type\": \"collectif\",\n\"features\": [")

indice_i = 0
for i in tab_coll:
	j = i.split("?")

	adr_j      = j[0].encode("utf-8")
	nom_j      = j[1].encode("utf-8")
	etoile_j   = j[2].encode("utf-8")
	site_j     = j[3].encode("utf-8")
	tel_j      = j[4].encode("utf-8")
	prix_min_j = j[5].encode("utf-8")
	prix_max_j = j[6].encode("utf-8")

	geocode_result_coll = gmaps.geocode(adr_j)
	if geocode_result_coll != []:
		latitude  = str(geocode_result_coll[0]["geometry"]["location"]["lat"])
		longitude = str(geocode_result_coll[0]["geometry"]["location"]["lng"])

		virgule = "{\"geometry\": {\"type\": \"Point\", \"coordinates\": [" + longitude + "," + latitude + "]}, \"properties\": {\"nom\":\"" + nom_j + "\", \"adresse\": \"" + adr_j +"\"}, \"other_information\": {\"etoile\": \"" + etoile_j + "\", \"siteweb\": \"" + site_j + "\", \"tel\": \"" + tel_j + "\", \"prixMini\": \"" + prix_min_j + "\", \"prixMaxi\": \"" + prix_max_j + "\"}},"

		if indice_i != len(tab_coll) - 1:
			fichier.write(virgule + "\n")
		else:
			fichier.write(virgule[:-1] + "\n")
	indice_i += 1

fichier.write("]}")
fichier.close()



############### HEBERGEMENT LOCATIF ##################
fichier = open("data_loc.js", "a")
fichier.write("{\"type\": \"locatif\",\n\"features\": [")

indice_i = 0
for i in tab_loc:
	j = i.split("?")

	adr_j      = j[0].encode("utf-8")
	nom_j      = j[1].encode("utf-8")
	etoile_j   = j[2].encode("utf-8")
	site_j     = j[3].encode("utf-8")
	tel_j      = j[4].encode("utf-8")
	prix_min_j = j[5].encode("utf-8")
	prix_max_j = j[6].encode("utf-8")

	geocode_result_loc = gmaps.geocode(adr_j)
	if geocode_result_loc != []:
		latitude  = str(geocode_result_loc[0]["geometry"]["location"]["lat"])
		longitude = str(geocode_result_loc[0]["geometry"]["location"]["lng"])

		virgule = "{\"geometry\": {\"type\": \"Point\", \"coordinates\": [" + longitude + "," + latitude + "]}, \"properties\": {\"nom\":\"" + nom_j + "\", \"adresse\": \"" + adr_j +"\"}, \"other_information\": {\"etoile\": \"" + etoile_j + "\", \"siteweb\": \"" + site_j + "\", \"tel\": \"" + tel_j + "\", \"prixMini\": \"" + prix_min_j + "\", \"prixMaxi\": \"" + prix_max_j + "\"}},"

		if indice_i != len(tab_loc) - 1:
			fichier.write(virgule + "\n")
		else:
			fichier.write(virgule[:-1] + "\n")
	indice_i += 1

fichier.write("]}")
fichier.close()

print "FIN!"