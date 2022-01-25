cp -r ./src/flaskapp ./docker/api/

docker build --quiet --pull -f ./docker/web/Dockerfile -t web-img ./docker/web/
docker build --quiet --pull -f ./docker/api/Dockerfile -t flaskapp-img ./docker/api/

if docker run -dit --name web-ctn -p 8080:80 web-img 2> ./log/err.log ; then
    docker rm web-ctn
    docker run -dit --name web-ctn -p 8080:80 web-img
fi

if docker run -dit --name flaskapp-ctn -p 5050:5050 web-img 2> ./log/err.log ; then
    docker rm flaskapp-ctn
    docker run -dit --name flaskapp-ctn -p 5050:5050 web-img
fi
