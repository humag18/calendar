#!/bin/bash
file1="/home/kitsensas/Desktop/Programming/python/calendar/portail.ical"
file2="/home/kitsensas/Desktop/Programming/python/calendar/nouveau_fichier.ical"
file3="/home/kitsensas/Desktop/Programming/python/calendar/informations_cours.ical"
if [ -e "$file1"]; then 
  rm "$file1"
fi 
if [-e "$file2"]; then
  rm "$file2"
fi
if [ -e "$file3"]; then
  rm "$file3"
fi
# URL du fichier iCal que vous souhaitez télécharger
url="https://portail.henallux.be/api/plannings/my/ical"

# Utilisation de curl pour télécharger le fichier iCal
curl -o portail.ical 'https://portail.henallux.be/api/plannings/my/ical' --compressed -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'X-Requested-With: XMLHttpRequest' -H 'X-CSRF-TOKEN: iK0goOdFAiyGoZ3otk32qotg8xlSwYVskKHjCWMZ' -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImM2MDEzMzQ2ZTY5ZGFmNzMwM2JmNmNhZTllZWUxZjgwZGY5MWMxYWQzNWU2NTU3ODY3MTU0NjM3MmExYzFkNDhmZWIzY2Q4NzdlYjYwM2M3In0.eyJhdWQiOiIxMCIsImp0aSI6ImM2MDEzMzQ2ZTY5ZGFmNzMwM2JmNmNhZTllZWUxZjgwZGY5MWMxYWQzNWU2NTU3ODY3MTU0NjM3MmExYzFkNDhmZWIzY2Q4NzdlYjYwM2M3IiwiaWF0IjoxNjk0NDM0MzgxLCJuYmYiOjE2OTQ0MzQzODEsImV4cCI6MTcyNjA1Njc4MSwic3ViIjoiMTI0NjgiLCJzY29wZXMiOltdfQ.nftahIKv6rWAGUYNzglrvXOCH62GTBYBGlbLmQ5oEHpg2NOmyg4LeBMjcw7aw4DK0fnEqplOv-_nWcq0-70lhYAw7T1cGEcvduYKbWYOH1DoJou46TLhItkB4hEktr0PJmgXPsO0R-t5e0nAMkO9E-m2xnZE9o5PkUnq1o3Ay0J8LbSUlAzYTK2WKJFAqsf3ElowJeM3eBfO0CET9nKuYc5s1wjudGqfD55RJBWaNnfElfuDWY_ZHDLZo2-p_R_pRPjYiustlCzonKJy38wY7jt3NOTALWKcq6WJUQSh05RtbGGkOojrcbUTJ11Z0IYDrvRCSWnhkPlU_8unf_RlsWuY8w4uzebwz1VB56bs1wLlpVsjAxAL5lLdeBVG4QoqCIv199oM1MsQqepWFgatvVxE3AgXqkqkxFjXUVq2qTJGVsd9ndwvAxbeF1MGaB1y4AQoUJE7ZAExBJBBrnMFO1mJVPU6Y7FGbdW-2RUbOgHQ-k-NHkxkMnUYPoo7_2_I2dlrGu-wEwQHKTqbfTteLxjwnbHn2pLeBoS2-k8t4_SmowG6-4zJU8biH35I6kvjRbPw4xs9PKZ5jBHvriilyI7HIaDqOJauIy673HKW4fmXTM7PeY7HVO-7N8fW9_7uEi7ohIYCLwi_ETNmv6iADR57zaDLpGkF3FmdTeLFCRU' -H 'Connection: keep-alive' -H 'Referer: https://portail.henallux.be/' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-origin'

# Vérification du statut de la requête
if [ $? -eq 0 ]; then
    echo "Téléchargement réussi. Le fichier iCal a été enregistré sous le nom 'my-calendar.ical'."
else
    echo "Erreur lors du téléchargement du fichier iCal."
fi

pythonscript1="/home/kitsensas/Desktop/Programming/python/calendar/ical.py"
pythonscript2="/home/kitsensas/Desktop/Programming/python/calendar/modif.py"
pythonscript3="/home/kitsensas/Desktop/Programming/python/calendar/import.py"
python3 "$pythonscript1"
python3 "$pythonscript2"
python3 "$pythonscript3"
