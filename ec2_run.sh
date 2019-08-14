cd ~
# install fundamentals (python & docker)
sudo apt-get update
sudo apt-get install \
	python3-venv \
	install npm \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

# download and verify docker depencies	
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88

# get docker image release for intial installation
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
# install docker   
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
docker-compose --version

# activate the python virtual environment
cd ~/testdriven-app/services/users
python3 -m venv venv
source venv/bin/activate

# set r/x permission so docker-compose can execute 
cd ~/testdriven-app/services/users
sudo chmod 755 entrypoint.sh
# start the docker project
cd ~/testdriven-app
sudo docker-compose up -d --build
echo Go to http://ec2-18-216-81-201.us-east-2.compute.amazonaws.com:5001/users/ping
