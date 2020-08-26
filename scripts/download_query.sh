files=($(cat $1)) 

echo "Starting the download..."
echo "Process will run in background."
echo ${files[@]} | xargs -n 1 -P 8 wget -q -b
