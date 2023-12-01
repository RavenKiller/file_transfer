# A simple HTTP text and file transfer server
Use native python to start:
```
pip install tornado
python3 main.py
```

Use docker to start:
```
# Pull the latest image from hub
docker pull raven025/file-transfer
# or build a new image
docker build . -t <customized_tag>

# Then run
docker run -d -p 5555:5555 raven025/file-transfer
```

Then access `http://host:5555` in your browser.
