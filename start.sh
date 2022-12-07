apt update && apt upgrade -y
apt install python3-pip -y
apt install ffmpeg -y
curl -sL https://deb.nodesource.com/setup_16.x | bash -
apt-get install -y nodejs
npm i -g npm
pip3 install --upgrade pip
pip3 install -U -r requirements.txt

gunicorn app:app

