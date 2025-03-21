docker build . -t myapp --build-arg "PORT=3000"
ocker run --rm -p 3000:3000 -t myapp