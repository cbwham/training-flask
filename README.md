# Flask

**Flask** is a Python [micro framework](https://flask.palletsprojects.com/en/3.0.x/) for building web applications.

# Demo Application

## Prerequisite

A working terminal running a shell is required.

To begin please install the [`Azure CLI`](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
) and succeed to logging in:

```shell
az login
```

## Deploy to Azure

Please read the according [documentation](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python) first!

```shell
az webapp up --location germanywestcentral --name cbwham-training-flask --runtime PYTHON:3.11 --sku B1 --generic-configurations '{"healthCheckPath": "/healthcheck"}' --only-show-errors
```

Note: `name` needs to be __unique__ Azure-wide!

### Example Output

```json
{
  "URL": "http://cbwham-training-flask.azurewebsites.net",
  "appserviceplan": "office_asp_3158",
  "location": "germanywestcentral",
  "name": "cbwham-training-flask",
  "os": "Linux",
  "resourcegroup": "office_rg_5180",
  "runtime_version": "PYTHON|3.11",
  "runtime_version_detected": "-",
  "sku": "BASIC",
  "src_path": "//Users//gretel//Sync//code//cbwham//training-flask"
}
```

### Connect

According to the output the web application should now be [reachable](https://learn.microsoft.com/de-de/azure/app-service/overview-tls) at:

https://cbwham-training-flask.azurewebsites.net/
