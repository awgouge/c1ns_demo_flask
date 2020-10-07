#if [ ! -d "env" ]; then
#    echo --------------------
#    echo Creating virtual environment
#    echo --------------------
#    python3 -m venv env
#fi
#source ./env/bin/activate

pip3 install -r requirements.txt
export FLASK_APP=app.py
python3 app.py &
