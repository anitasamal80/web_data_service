echo "Preparing to run the server"
cd mybaseproject
docker build . --tag wds:01
docker run -p 8000:8000 --name web_data_service wds:01