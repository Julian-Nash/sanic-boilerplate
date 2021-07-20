# Sanic boilerplate

Sanic web application boilerplate with Jinja2 template rendering.

Starting the app:

```shell
python run.py
```

Options for starting the app:

```shell
$ python run.py --help
usage: Sanic application boilerplate [-h] [--host HOST] [--port PORT] [--debug DEBUG] [--access-log ACCESS_LOG] [--auto-reload AUTO_RELOAD] [--workers WORKERS]
                                     [--config {prod,dev,test}]

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           Application host (default: 0.0.0.0)
  --port PORT           Application port (default: 8000)
  --debug DEBUG         Enable debug mode (default: False)
  --access-log ACCESS_LOG
                        Enable debug mode (default: False)
  --auto-reload AUTO_RELOAD
                        Enable auto reload (default: False)
  --workers WORKERS     N. workers (default: 12)
  --config {prod,dev,test}
                        Configuration name (default: prod)

```

- Sanic docs - [Sanic](https://sanicframework.org/)
- Jinja2 docs - [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/)