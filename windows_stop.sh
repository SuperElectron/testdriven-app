# run script in terminal  $: ./windows_stop.sh

echo shutting down project
docker-compose down
echo 
echo
echo confirming shut-down with docker ps -a
docker ps -a
echo 
echo
echo confirming shut-down with docker ps
docker ps
echo
