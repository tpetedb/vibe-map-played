# The rate is from the AWS EC2 On-Demand pricing page for t3.small in eu-west-1:
# https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html
RATE = 0.0228  # USD per instance-hour

print(f"2 hours: {RATE * 2:.2f} USD")
print(f"30 days: {RATE * 24 * 30:.2f} USD")
