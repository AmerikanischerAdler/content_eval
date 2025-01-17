# Content Evaluation

## Description

A way to turn content consumption into a productive exercise.

### Stack:

| Type  | Structure | Style | Elements   | Routes  | Database |
| :---: | :-------: | :---: | :--------: | :-----: | :------: |
| Flask | HTML5     | CSS3  | JavaScript | Python3 | MYSQL    |

## Installation

1) Open Terminal and Clone Repository:

```bash
git clone https://github.com/AmerikanischerAdler/content_eval
```

2) Install Python:

If python3 is not installed on your machine, run:

**MacOS:**

```bash
brew update 
brew install python3
``` 

**TIP**: For MacOS, be sure that homebrew is installed on your machine. If not, visit https://brew.sh to install.

**Ubuntu:**

```bash
sudo apt update 
sudo apt install python3
```

3) Set Up Virtual Environment:

```bash
pip3 install virtualenv
python3 -m venv env
source env/bin/activate
```

4) Install Dependencies:

```bash
pip install -r requirements.txt
```

5) Terminate Virtual Environment:

```bash 
deactivate
```

6) Set Up MYSQL Environment Variable:

Once you have created your MYSQL account, run this command in the terminal, substituting your own password for "my_password":

```bash
echo 'export MYSQLPW="my_password"' >> ~/.bashrc
```

Do the same to set up your own secret key, substituting its value for "my_secret_key":

```bash
echo 'export SECRET_KEY="my_secret_key"' >> ~/.bashrc
```

**TIP**: This implies that you are using bash as your current shell. If not, run
the command, substituting your own shell config file for ".bashrc"

7) Create MYSQL Database and Tables:

Once you are logged into your MYSQL environment, run the following commands:

**Substitute the name of your site for "ContentEval"**

*Create Database for ContentEval:*

```mysql
CREATE DATABASE ContentEval;
```

*Create Evals Table:*

```mysql
USE ContentEval;
CREATE TABLE evals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    isMovie BOOLEAN DEFAULT FALSE,
    isYT BOOLEAN DEFAULT FALSE,
    isBook BOOLEAN DEFAULT FALSE,
    isOther BOOLEAN DEFAULT FALSE,
    type VARCHAR(100),
    title VARCHAR(100),
    description VARCHAR(100),
    reflect VARCHAR(100),
    love VARCHAR(100),
    hate VARCHAR(100),
    lesson VARCHAR(100),
    insights VARCHAR(100),
    change VARCHAR(100),
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP
);
``` 

## Usage

1) Open Terminal

2) Navigate to content_eval Directory:

```bash
cd content_eval
```

3) Start Virtual Environment

```bash
python3 -m venv env
source env/bin/activate
```

**TIP**: To terminate your virtual environment, run:

```bash
deactivate
```

4) Start Flask App:

*This will spin up a local backend server*

```bash
python3 app.py
```

**TIP**: To terminate your local server, press CTRL-C

4) Open Web Browser to New Tab or Window

5) Enter Server Address in Search Bar:

You may be able to simply click this link: http://127.0.0.1:5000/

