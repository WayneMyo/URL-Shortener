from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb, ElastiCache
from diagrams.aws.network import ELB, APIGateway
from diagrams.aws.general import Users

output_dir = "diagrams/generated_diagrams/"

with Diagram("High Level Architecture", show=False, filename=output_dir + "high_level_architecture", outformat="png"):
    users = Users("External Users")

    with Cluster("AWS", graph_attr={"label": "AWS", "bgcolor": "lightgrey"}):
        lb = ELB("Elastic Load Balancer")
        api_gateway = APIGateway("API Management")

        with Cluster("VPC"):
            with Cluster("Application Tier Private Subnet"):
                web = Lambda("API Backend")
                
            with Cluster("Database & Storage Private Subnet"):
                dynamodb = Dynamodb("Application Data Store")
                counter_cache = ElastiCache("Counter Cache")

    users >> lb
    lb >> api_gateway >> web
    web >> dynamodb
    web >> counter_cache

'''
1. External Users: Represents the users who interact with the API endpoints through their web browsers, mobile apps, or other HTTP clients.
2. Elastic Load Balancer (ELB): Distributes incoming HTTP traffic to the API Gateway for request processing.
3. API Gateway: Routes requests to the AWS Lambda function, which is responsible for handling the logic of generating short URLs and redirecting users to the original URLs.
4. Lambda Function (API Backend): Stores and retrieves data from the Amazon DynamoDB database, which is used to persistently store the mappings between short URLs and their corresponding original URLs.
5. DynamoDB (Application Data Store): Stores the original URL, short URL, and other relevant data for each URL mapping.
6. ElastiCache (Counter Cache): Caches the counter values for generating unique short URLs to minimize latency and improve performance.
'''
