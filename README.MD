Live Binance Futures Balance
==============================

Script en Python qui permet d'afficher la valeur de son compte Binance Futures sur un écran LCD monté sur un RaspberryPi 4

Le script affiche soit simplement la valeur du compte Binance Futures ou bien aussi les positions en cours

# Code

Pour lancer le script : 

- Créer /.env qui contient :

```
API_KEY=xxx
SECRET_API=xxx
```

- Créer un environnement virtuel et installer les librairies : 

```
python3 -m virtualenv venv
python3 -m pip install -r requirements.txt
```
- Lancer le script :

```
./script.sh
```

# Image

![alt text](https://github.com/alyildiz/raspberry_binance_balance/blob/master/img.jpg?raw=true)




