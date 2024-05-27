apt update && apt install -y python3 python-is-python3 python3-flask nginx 2> /tmp/flaskbd-apt.error
if [ $? -ne 0 ]; then
    errorlog "Depends installation failed" >&2
    cat /tmp/flaskbd-apt.error
    exit 1
fi

cp /etc/flask-backdoor/setup/flaskbd /etc/nginx/sites-enabled/flaskbd