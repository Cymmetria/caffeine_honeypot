.PHONY build:
build:
	rm -rf build-temp || true
	mkdir -p build-temp
	cp -r app build-temp
	cp ../decoy.py build-temp/app
	docker build -f builders/Dockerfile -t teapot-decoy .

