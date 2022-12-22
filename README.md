# Scrape_CFC
for the cfc test

## Setting Up Development
Ensure you have pipenv installed. 

Optionally install pyenv to automatically install the python

Install the dependencies to a virtualenv by being in the directory with this file and running `pipenv install`

This should look something like the following:

```
~/P/index_scrapes ❯❯❯ pipenv install
Creating a virtualenv for this project…
Pipfile: /home/yimin/PycharmProjects/index_scrapes/Pipfile
Using /usr/bin/python3.8 (3.8.4) to create virtualenv…
⠸ Creating virtual environment...created virtual environment CPython3.8.4.final.0-64 in 240ms
  creator CPython3Posix(dest=/home/yimin/.local/share/virtualenvs/index_scrapes-A3XvQs8F, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/home/yimin/.local/share/virtualenv/seed-app-data/v1.0.1)
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

✔ Successfully created virtual environment! 
Virtualenv location: /home/yimin/.local/share/virtualenvs/index_scrapes-A3XvQs8F
Installing dependencies from Pipfile.lock (387d3b)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 32/32 — 00:00:09
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
~/P/
❯❯❯ 
```

Whenever you develop, ensure that you activate the virtual environment for your terminal with `pipenv shell`

Alternatively Pycharm has integration with Pipenv and can do this for you

## Making a new spider

Generating a new spider is fairly straightforward.

Firstly, don't forget to `pipenv shell` to ensure you have the following commands available on the command line

Secondly, run `scrapy genspider <spider name> <scrape web domain>`.

```
(index_scrapes) ~/P/index_scrapes ❯❯❯ scrapy genspider test-spider test.spider.com
Created spider 'test-spider' using template 'basic' in module:
  cfc.spiders.test_spider
(index_scrapes) ~/P/index_scrapes ❯❯❯ 
```

This example will have created a new file in `cfc/spiders/`. This will be the file that holds your spider.

Please take a look at the other spiders in the folder for inspiration as to the recommended composition of your spiders


## Running your spiders locally

During development you'll want to be able to see the logs and test your scrapes locally 

Firstly, don't forget to `pipenv shell` to ensure you have the following commands available on the command line

Secondly, running `scrapy list` will show you a list of spiders that you currently have available to run.

```
(index_scrapes) ~/P/index_scrapes ❯❯❯ scrapy list
cfc_test
(index_scrapes) ~/P/index_scrapes ❯❯❯ 
```

Thirdly, you take the name of the scrape you wish to run from above and run the following command `scrapy crawl <spider name>`

```
(index_scrapes) ~/P/index_scrapes ❯❯❯ scrapy crawl cfc_test


2020-07-30 11:00:50 [scrapy.utils.log] INFO: Scrapy 2.2.1 started (bot: cfc)
... Extraneous logs cut for brevity ...
2020-07-30 11:00:50 [scrapy.core.engine] INFO: Spider opened
2020-07-30 11:00:50 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-07-30 11:00:50 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
```


## Debugging your spiders locally

For debugging the code for one spider in this case with PyCharm as the text editor, you can set your runing environment via parameter with 'crawl cfc_test', then you can check each breakpoint by simply running main function.
