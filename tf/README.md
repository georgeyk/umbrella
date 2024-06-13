Using terraform with localstack.

```bash
# create virtualenv, install pipenv, and then:
$ pipenv install localstack
$ localstack start -d
$ terraform init
$ terraform apply
# logs
$ localstack logs -f
```
