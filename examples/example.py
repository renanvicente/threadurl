from threadurl import ThreadUrl

if __name__ == '__main__':
  url = ['http://renanvicente.com','http://renanvicente.com.br']
  trigger = ThreadUrl(5)
  trigger.load()
  trigger.method = "GET"
  trigger.verbose = True
  trigger.trigger(url)
  print(trigger.data_done)

