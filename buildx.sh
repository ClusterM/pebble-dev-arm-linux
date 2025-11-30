docker buildx create --name multi --use
docker buildx inspect --bootstrap

#docker login

docker buildx build --platform linux/arm64,linux/arm/v7 -t clustermeerkat/pebble-dev-arm-linux:1.0 -t clustermeerkat/pebble-dev-arm-linux:latest --push .
