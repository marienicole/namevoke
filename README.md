# Simple Santa

[Simple Santa](http://www.simple-santa.com): A webapp to make your secret santa names more... secret, so everyone can participate!
![santa hat](https://raw.githubusercontent.com/wizmariefa/simple-santa/master/app/static/images/santahat_no_dec.gif)

## Getting Started

#### Clone the repository and start your own branch:

`git clone https://github.com/wizmariefa/simple-santa`

`git checkout -b my-dev-branch`

`cd simple-santa`


#### Install virtualenv and create a venv for development:

`pip3 install virtualenv` Then,

Create the venv: `virtualenv -p python3 .` then,

Activate/start the venv: `source bin/activate`.


#### Install dependencies inside the venv by running:
`pip install -r requirements.txt`


#### Deactivate when you're done:
This uses just the command `deactivate`.

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds
