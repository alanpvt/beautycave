import fire
from beetcave import app

class Bootstrap(object):

  def develop(self):
    app.config.from_mapping(
      ENV='development',
      SECRET_KEY=b'_9#er$323\\'
    )
    app.run()

  def run_prod(self):
    app.run()

def main():
  fire.Fire(Bootstrap)


if __name__ == '__main__':
  main()