apt install ffmpeg -y
curl -sL https://deb.nodesource.com/setup_16.x | bash -
apt-get install -y nodejs
gunicorn app:app
