cd ~/testdriven-app
echo shutting down project
sudo docker-compose down
echo 
echo
echo confirming shut-down with docker ps -a
sudo docker ps -a
echo 
echo
echo confirming shut-down with docker ps
sudo docker ps
echo

