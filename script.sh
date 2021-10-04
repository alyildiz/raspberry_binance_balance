source venv/bin/activate

var=$(cat .env | grep API_KEY)
export $var
var=$(cat .env | grep SECRET_API)
export $var

python3 run.py