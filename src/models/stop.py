

class Stop:
  """
  A simplified model of a MBTA stop containing only the information needed to
  solve the challenges
  """

  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.routes = {}
