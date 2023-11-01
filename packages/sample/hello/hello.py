import os

def main(args):
      name = args.get("name", "stranger")
      greeting = "Hello " + name + "!"
      print(greeting)

      REAL_SPACES_ACCESS = os.getenv('REAL_SPACES_ACCESS')
      REAL_SPACES_KEY = os.getenv('REAL_SPACES_KEY')

      data = {'message': 'Hello, world!'}
      response = {
            'statusCode': 200,
            'headers': {
                  'Content-Type': 'application/html'
            },
            'body': '<html><h1>Hello, world!</h1></html>'
      }

      return response
  