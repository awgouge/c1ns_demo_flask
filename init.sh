#if [ ! -d "env" ]; then
#    echo --------------------
#    echo Creating virtual environment
#    echo --------------------
#    python3 -m venv env
#fi
#source ./env/bin/activate

if [ "$#" -ne 2 ]; then
    echo "$0 accepts two command line args: <victim_ip> <struts_port>"
fi

export VICTIM=$1
export STRUTS_PORT=$2
pip3 install -r requirements.txt
export FLASK_APP=app.py

echo $VICTIM > VICTIM_HOST.txt
echo $STRUTS_PORT > STRUTS_PORT.txt

cat <<EOT
[Unit]
Description=Demo Attack Site
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/cnp_demo_flask
ExecStart=/usr/bin/python3 /home/ubuntu/cnp_demo_flask/app.py
Restart=always

[Install]
WantedBy=multi-user.target
EOT

systemctl daemon-reload
systemctl enable flask_web.service
systemctl start flask_web.service
#python3 app.py &
