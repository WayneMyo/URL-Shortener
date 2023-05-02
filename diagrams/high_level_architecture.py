from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb, ElastiCache
from diagrams.aws.network import ELB, APIGateway, Route53
from diagrams.aws.management import Cloudwatch
from diagrams.aws.general import Users

output_dir = "diagrams/generated_diagrams/"

with Diagram("High Level Architecture", show=False, filename=output_dir + "high_level_architecture", outformat="png"):
    users = Users("External Users")

    with Cluster("AWS", graph_attr={"label": "AWS", "bgcolor": "lightgrey"}):
        lb = ELB("Elastic Load Balancer")
        api_gateway = APIGateway("API Management")
        route53 = Route53("Custom Domain")

        with Cluster("VPC"):
            with Cluster("Application Tier Private Subnet"):
                web = Lambda("API Backend")

            with Cluster("Database & Storage Tier Private Subnet"):
                dynamodb = Dynamodb("Application Data Store\n(Multi-AZ & Global Tables)")
                counter_cache = ElastiCache("Counter Cache\n(Multi-AZ)")

        cloudwatch = Cloudwatch("Monitoring & Logging")

    users >> lb
    lb >> api_gateway >> web
    web >> dynamodb
    web >> counter_cache
    route53 >> api_gateway
    cloudwatch >> web

"""
1. External Users: Represents the users who interact with the API endpoints through their web browsers, mobile apps, or other HTTP clients.
2. Elastic Load Balancer (ELB): Distributes incoming HTTP traffic to the API Gateway for request processing.
3. API Gateway: Routes requests to the AWS Lambda function, which is responsible for handling the logic of generating short URLs and redirecting users to the original URLs.
4. Route 53 (Custom Domain): Manages custom domain names for API backend, providing more control over API's domain and improving its availability through AWS Route 53's health checks and routing policies.
5. Lambda Function (API Backend): Stores and retrieves data from the Amazon DynamoDB database, which is used to persistently store the mappings between short URLs and their corresponding original URLs.
6. DynamoDB (Application Data Store): Stores the original URL, short URL, and other relevant data for each URL mapping. Enhanced with Multi-AZ deployment and Global Tables for increased durability and high availability.
7. ElastiCache (Counter Cache): Caches the counter values for generating unique short URLs to minimize latency and improve performance. Configured with Multi-AZ deployment for fault tolerance and high availability.
8. CloudWatch (Monitoring & Logging): Monitors application performance, tracks issues, and maintains high availability by collecting logs and providing alerts.
"""
