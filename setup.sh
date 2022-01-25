if docker run -dit --name web-ctn-dck -p 8080:80 web-ctn 2> ./log/err.log ; then
    docker rm web-ctn-dck
    docker run -dit --name web-ctn-dck -p 8080:80 web-ctn
fi

docker build --no-cache --quiet --pull -t web-ctn ./docker/web/
