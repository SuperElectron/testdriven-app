# download and verify docker depencies	
echo starting sequence
docker-compose --version

# activate the python virtual environment
cd services/users
python -m venv venv
source venv/scripts/activate

# set r/x permission so docker-compose can execute 
echo setting file permissions
chmod 755 entrypoint.sh
cd ../..
docker-compose up -d --build
echo Go to localhost:5001/users/ping
