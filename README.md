# 🐵 Mailchimp Tests
Proof of concept of Mailchimp's Transactional API

Checkout [the intro video :D](https://youtu.be/yajrGRqOWXo)

This is meant for Grasshopperfund use, though this repository does not have code used in implementation. 
This can be referred to compare the purpose and functionality of the following Mailchimp APIs:

* [The Official Mailchimp Marketing Python API](https://github.com/mailchimp/mailchimp-marketing-python)
* [The Official Mailchimp Transactional Python API](https://github.com/mailchimp/mailchimp-transactional-python)
* [Third Party Vingt Cinq Mailchimp Marketing Python API](https://github.com/VingtCinq/python-mailchimp)


## Installation

**👩‍👧 Clone repository**


```console
git clone https://github.com/grasshopperfund/mailchimp-test
```


**Navigate into the repository** 

```console
$ cd mailchimp-test
```


**🐍 Create Python virtual environment**

There are a good amount of depencies for this project -- it will be good practice to use a virtual environment, albeit not necessary.

macOS/Linux:

```console
python3 -m venv env
```

Windows Command Line or Powershell:

```console
python -m venv env
```


The last argument is the location to create the virtual environment. Generally, you can just create this in your project and call it env.


**✅ Activate virtual environment**

macOS/Linux:

```
source env/bin/activate
```

Windows Command Line:

```
.\env\Scripts\activate.bat
```

Windows Powershell:

```
.\env\Scripts\activate.ps1
```


**📦 Install packages**


```console
python -m pip install -r requirements.txt
```

## Running tests

Just like any other python script:

```console
python ./<script_name>.py
```
