# original source: https://www.tinfoilcipher.co.uk/2022/05/14/simulating-aws-terraform-builds-with-localstack/


provider "aws" {

    #--Standard Provider Configurations
    region     = "us-east-1"
    default_tags {
        tags = {
            Environment = "dev"
        }
    }

    #--Mocked Credentials
    access_key = "test"
    secret_key = "test"

    #--Forces proper S3 path validation. Hopefully this is in use throughout your code!
    # s3_force_path_style = true

    #--These settings allow for authentication and other validations which are enforced
    #--in the AWS provider to be bypassed by Localstack.
    skip_credentials_validation = true
    skip_metadata_api_check     = true
    skip_requesting_account_id  = true

    #--Redirect Service Endpoints to Localstack. Whilst we won't be any of these it's good
    #--to see how they work and one should be specified to avoid rogue creations.
    #--See the Localstack docs for a full list of suitable endpoints):
    #--https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/custom-service-endpoints#available-endpoint-customizations
    endpoints {
        apigateway     = "http://localhost:4566"
        cloudwatch     = "http://localhost:4566"
        ec2            = "http://localhost:4566"
        elasticache    = "http://localhost:4566"
        route53        = "http://localhost:4566"
        #s3             = "http://localhost:4566"
        s3             = "http://s3.localhost.localstack.cloud:4566" #--This format required for s3_force_path_style = true
    }
}

# test s3
resource "aws_s3_bucket" "test-bucket" {
    bucket = "test-bucket"
}
