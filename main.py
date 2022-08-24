import abc


class Parser(abc.ABC):
    def __init__(self, description):
        self.description = description
        self.parsed_description = None
        self.is_valid = None

    @abc.abstractmethod
    def parse(self):
        pass


class AwsParser(Parser):
    pass


class GcpParser(Parser):
    pass


if __name__ == '__main__':
    """
    aws_description spec:
    /w{12} - any 12 alphanumerical characters 
    "arn:aws:iam::*:" -> NOT OK
    "arn:aws:iam::\w{12}:role/*" -> NOT OK
    "arn:aws:iam::\w{12}:user/*" -> NOT OK
    "arn:aws:iam::\w{12}:federated-user/*" -> NOT OK
    "arn:aws:iam::\w{12}:oidc-provider/*" -> NOT OK
    "arn:aws:iam::1234567890ab:role/test" -> OK
    
    gcp_description spec:
    number{3} - dash number{3} - dash letter{3}
    "123-456-abc" -> OK
    "abc-def-123" -> NOT OK
    "123-456*-abc" -> NOT OK
    """

    gcp_description = "user: Joe\n" \
                      "email: joe.doe@example.com\n" \
                      "gcp_account: 123-456-abc\n"

    aws_description = "user: Karen\n" \
                      "email: karen.doe@example.com\n" \
                      "aws_arn: arn:aws:iam::1234567890ab:root\n"
