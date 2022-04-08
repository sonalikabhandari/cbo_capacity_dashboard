# Go to correct directory
cd staging && \

# Build the base python contianer and set the appropriate tag
docker build \
       --tag=git.netops.charter.com:5005/brianmask/cbo-portal/staging/intake \
       --no-cache . && \

# Push the container to the registry
docker push git.netops.charter.com:5005/brianmask/cbo-portal/staging/intake