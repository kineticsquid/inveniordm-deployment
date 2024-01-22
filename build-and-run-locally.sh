#!/bin/bash
echo "Tagging and pushing docker image. Be sure to start docker.app first"
echo "To examine contents: 'docker run -it {image} sh'"

docker rmi kineticsquid/orcid:latest
docker build --rm --no-cache --pull -t kineticsquid/orcid:latest -f Dockerfile .
docker push kineticsquid/orcid:latest

# list the current images
echo "Docker Images..."
docker images

echo "Now running..."
./.vscode/run-image-locally.sh
