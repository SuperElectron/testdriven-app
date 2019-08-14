# run script in terminal  $: ./ec2_run.sh

cd ~
echo
echo installing fundamentals - python - docker
sudo apt-get update
sudo apt-get install \
    python3-venv \
    npm \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common \
    nginx
echo ***********************
echo

echo download and verify docker depencies	
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
echo ***********************
echo verify fingerprints - docker
sudo apt-key fingerprint 0EBFCD88

echo get docker image release - intial installation
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
echo
echo ***********************
echo
echo install docker   
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
echo
echo ***********************
echo
docker-compose --version
echo ***********************
echo

echo activate the python virtual environment
cd ~/testdriven-app/services/users
python3 -m venv venv
source venv/bin/activate
echo give r/x permission so docker-compose can execute 
sudo chmod 755 entrypoint.sh
echo ***********************
echo

# install npm to create node_modules and package-lock.json
cd ~/testdriven-app/services/cleanui
echo ***********************
echo
echo running npm run build
npm run build 
echo ***********************
echo


# start the docker project
cd ~/testdriven-app
echo
echo checking status of nginx
# checking status of nginx
sudo systemctl status nginx

# point docker back to localhost
eval $(docker-machine env -u)
echo ***********************
echo

#sudo docker-compose up -d --build
sudo docker-compose -f docker-compose-prod.yml up -d --build
echo
echo ***********************
echo backend http://ec2-18-216-81-201.us-east-2.compute.amazonaws.com:5001/users/ping
echo
echo frontend
docker-machine ip testdriven-prod