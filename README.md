# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Phyton - Locust application for stress test 
> * How many competitors a user request can sustain your application.
> * You can configure behaviour of any clients
> * After configuration you can watch client's behaviour in web UI.

### How do I get set up? ###

* $ sudo apt install python-pip
* $ pip install locustio
* $ locust --help (only for verifying that locust is installed)
* $ git clone git@bitbucket.org:Lubo13/locust.git
* $ cd locust
*   Edit urls in ./links.links.py with your urls for test
* $ locust -f ./locust_file.py --host=http://domain-for-stress-test.com
*   Type in browser -> http://localhost:8089

### Reference and docs ###

* https://locust.io/

### Who do I talk to? ###

* Bitbucket Repository -> https://bitbucket.org/Lubo13/docker
* Docker Hub -> 
* Email -> grozdanov.lubo@gmail.com
