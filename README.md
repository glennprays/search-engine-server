[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
# Search Engine
This program is a search engine that utilizes TF-IDF and Cosine Similarity methods for information retrieval.

## Prerequisites
1. Install [docker engine](https://docs.docker.com/engine/install/)
2. Move document files into `./flask/documents` directory
3. Generate TF-IDF model using [TF-IDF Vectorizer](https://github.com/glennprays/tf-idf-vectorizer), it will generate a few JSON files and put the generated JSON into `./flask/search-data` directory.
4. Copy the UI from [this repository](https://github.com/glennprays/search-engine-ui) into `./next` directory.

## Notes
### Run on server
If you want to run it on server don't forget to re-cofigure the `nginx.conf` for `server_name`, `ssl_certificate`, `ssl_certificate_key`.
### Run on local computer
To run it on local computer, remove the nginx `server {...]` block that listen to `port 443` and also remove `server_name` configuration.

## Get Started
### Docker
To start this project in docker:
1. Build the Docker Compose first
   ```
   docker compose build
   ```
2. Execute the Docker Compose useing 'up' command
   ```
   docker compose up
   ```
- Stopping Docker Compose
  ```
  docker compose down
  ```
