
routes_data = [
  {
    'id': 'test1',
    'name': 'test1',
    'type': -1
  },
    {
    'id': 'test2',
    'name': 'test2',
    'type': -1
  },
    {
    'id': 'test3',
    'name': 'test3',
    'type': -1
  },
  {
    'id': 'Red',
    'name': 'Red Line',
    'type': 1
  },
  {
    'id': 'Mattapan',
    'name': 'Mattapan Trolley',
    'type': 0
  },
  {
    'id': 'Orange',
    'name': 'Orange Line',
    'type': 1
  },
  {
    'id': 'Green-B',
    'name': 'Green Line B',
    'type': 0
  },
  {
    'id': 'Green-C',
    'name': 'Green Line C',
    'type': 0
  },
  {
    'id': 'Green-D',
    'name': 'Green Line D',
    'type': 0
  },
  {
    'id': 'Green-E',
    'name': 'Green Line E',
    'type': 0
  },
  {
    'id': 'Blue',
    'name': 'Blue Line',
    'type': 1
  },
  {
    'id': 'CR-Fairmount',
    'name': 'Fairmount Line',
    'type': 2
  },
  {
    'id': 'CR-Fitchburg',
    'name': 'Fitchburg Line',
    'type': 2
  },
  {
    'id': 'CR-Worcester',
    'name': 'Framingham/Worcester Line',
    'type': 2
  },
  {
    'id': 'CR-Franklin',
    'name': 'Franklin/Foxboro Line',
    'type': 2
  },
  {
    'id': 'CR-Greenbush',
    'name': 'Greenbush Line',
    'type': 2
  },
  {
    'id': 'CR-Haverhill',
    'name': 'Haverhill Line',
    'type': 2
  },
  {
    'id': 'CR-Kingston',
    'name': 'Kingston Line',
    'type': 2
  },
  {
    'id': 'CR-Lowell',
    'name': 'Lowell Line',
    'type': 2
  },
  {
    'id': 'CR-Middleborough',
    'name': 'Middleborough/Lakeville Line',
    'type': 2
  },
  {
    'id': 'CR-Needham',
    'name': 'Needham Line',
    'type': 2
  },
  {
    'id': 'CR-Newburyport',
    'name': 'Newburyport/Rockport Line',
    'type': 2
  },
  {
    'id': 'CR-Providence',
    'name': 'Providence/Stoughton Line',
    'type': 2
  },
  {
    'id': 'CR-Foxboro',
    'name': 'Foxboro Event Service',
    'type': 2
  },
]

stops_data = {
  'test1': ['stopA', 'stopB', 'stopC', 'stopD', 'stopK', 'stopL'],
  'test2': ['stopE', 'stopA', 'stopF', 'stopG'],
  'test3': ['stopB', 'stopH', 'stopI', 'stopF', 'stopM'],
  'Red': ['Alewife', 'Davis', 'Porter', 'Harvard', 'Central', 'Kendall/MIT', 'Charles/MGH', 'Park Street', 'Downtown Crossing', 'South Station', 'Broadway', 'Andrew', 'JFK/UMass', 'Savin Hill', 'Fields Corner', 'Shawmut', 'Ashmont', 'North Quincy', 'Wollaston', 'Quincy Center', 'Quincy Adams', 'Braintree'],
  'Mattapan': ['Ashmont', 'Cedar Grove', 'Butler', 'Milton', 'Central Avenue', 'Valley Road', 'Capen Street', 'Mattapan'],
  'Orange': ['Forest Hills', 'Green Street', 'Stony Brook', 'Jackson Square', 'Roxbury Crossing', 'Ruggles', 'Massachusetts Avenue', 'Back Bay', 'Tufts Medical Center', 'Chinatown', 'Downtown Crossing', 'State', 'Haymarket', 'North Station', 'Community College', 'Sullivan Square', 'Assembly', 'Wellington', 'Malden Center', 'Oak Grove'],
  'Green-B': ['Government Center', 'Park Street', 'Boylston', 'Arlington', 'Copley', 'Hynes Convention Center', 'Kenmore', 'Blandford Street', 'Boston University East', 'Boston University Central', 'Amory Street', 'Babcock Street', "Packard's Corner", 'Harvard Avenue', 'Griggs Street', 'Allston Street', 'Warren Street', 'Washington Street', 'Sutherland Road', 'Chiswick Road', 'Chestnut Hill Avenue', 'South Street', 'Boston College'],
  'Green-C': ['Cleveland Circle', 'Englewood Avenue', 'Dean Road', 'Tappan Street', 'Washington Square', 'Fairbanks Street', 'Brandon Hall', 'Summit Avenue', 'Coolidge Corner', 'Saint Paul Street', 'Kent Street', 'Hawes Street', "Saint Mary's Street", 'Kenmore', 'Hynes Convention Center', 'Copley', 'Arlington', 'Boylston', 'Park Street', 'Government Center'],
  'Green-D': ['Riverside', 'Woodland', 'Waban', 'Eliot', 'Newton Highlands', 'Newton Centre', 'Chestnut Hill', 'Reservoir', 'Beaconsfield', 'Brookline Hills', 'Brookline Village', 'Longwood', 'Fenway', 'Kenmore', 'Hynes Convention Center', 'Copley', 'Arlington', 'Boylston', 'Park Street', 'Government Center', 'Haymarket', 'North Station', 'Science Park/West End', 'Lechmere', 'Union Square'],
  'Green-E': ['Heath Street', 'Back of the Hill', 'Riverway', 'Mission Park', 'Fenwood Road', 'Brigham Circle', 'Longwood Medical Area', 'Museum of Fine Arts', 'Northeastern University', 'Symphony', 'Prudential', 'Copley', 'Arlington', 'Boylston', 'Park Street', 'Government Center', 'Haymarket', 'North Station', 'Science Park/West End', 'Lechmere'],
  'Blue': ['Bowdoin', 'Government Center', 'State', 'Aquarium', 'Maverick', 'Airport', 'Wood Island', 'Orient Heights', 'Suffolk Downs', 'Beachmont', 'Revere Beach', 'Wonderland'],
  'CR-Fairmount': ['Readville', 'Fairmount', 'Blue Hill Avenue', 'Morton Street', 'Talbot Avenue', 'Four Corners/Geneva', 'Uphams Corner', 'Newmarket', 'South Station'],
  'CR-Fitchburg': ['Wachusett', 'Fitchburg', 'North Leominster', 'Shirley', 'Ayer', 'Littleton/Route 495', 'South Acton', 'West Concord', 'Concord', 'Lincoln', 'Kendal Green', 'Brandeis/Roberts', 'Waltham', 'Waverley', 'Belmont', 'Porter', 'North Station'],
  'CR-Worcester': ['Worcester', 'Grafton', 'Westborough', 'Southborough', 'Ashland', 'Framingham', 'West Natick', 'Natick Center', 'Wellesley Square', 'Wellesley Hills', 'Wellesley Farms', 'Auburndale', 'West Newton', 'Newtonville', 'Boston Landing', 'Lansdowne', 'Back Bay', 'South Station'],
  'CR-Franklin': ['Forge Park/495', 'Franklin', 'Norfolk', 'Foxboro', 'Walpole', 'Windsor Gardens', 'Norwood Central', 'Norwood Depot', 'Islington', 'Dedham Corporate Center', 'Endicott', 'Readville', 'Forest Hills', 'Ruggles', 'Back Bay', 'South Station', 'Hyde Park'],
  'CR-Greenbush': ['Greenbush', 'North Scituate', 'Cohasset', 'Nantasket Junction', 'West Hingham', 'East Weymouth', 'Weymouth Landing/East Braintree', 'Quincy Center', 'JFK/UMass', 'South Station'],
  'CR-Haverhill': ['Haverhill', 'Bradford', 'Lawrence', 'Andover', 'Ballardvale', 'North Wilmington', 'Reading', 'Wakefield', 'Greenwood', 'Melrose Highlands', 'Melrose/Cedar Park', 'Wyoming Hill', 'Oak Grove', 'Malden Center', 'North Station'],
  'CR-Kingston': ['Kingston', 'Halifax', 'Hanson', 'Whitman', 'Abington', 'South Weymouth', 'Braintree', 'Quincy Center', 'JFK/UMass', 'South Station'],
  'CR-Lowell': ['Lowell', 'North Billerica', 'Wilmington', 'Anderson/Woburn', 'Wedgemere', 'West Medford', 'North Station'],
  'CR-Middleborough': ['Middleborough/Lakeville', 'Bridgewater', 'Campello', 'Brockton', 'Montello', 'Holbrook/Randolph', 'Braintree', 'Quincy Center', 'JFK/UMass', 'South Station'],
  'CR-Needham': ['Needham Heights', 'Needham Center', 'Needham Junction', 'Hersey', 'West Roxbury', 'Highland', 'Bellevue', 'Roslindale Village', 'Forest Hills', 'Ruggles', 'Back Bay', 'South Station'],
  'CR-Newburyport': ['Rockport', 'Gloucester', 'West Gloucester', 'Manchester', 'Beverly Farms', 'Montserrat', 'Newburyport', 'Rowley', 'Ipswich', 'Hamilton/Wenham', 'North Beverly', 'Beverly', 'Salem', 'Swampscott', 'Lynn', 'River Works', 'Chelsea', 'North Station'],
  'CR-Providence': ['Wickford Junction', 'TF Green Airport', 'Providence', 'Attleboro', 'Mansfield', 'Sharon', 'Stoughton', 'Canton Center', 'Canton Junction', 'Route 128', 'Hyde Park', 'Ruggles', 'Back Bay', 'South Station', 'Forest Hills'],
  'CR-Foxboro': ['South Station', 'Back Bay', 'Dedham Corporate Center', 'Providence', 'Attleboro', 'Mansfield', 'Foxboro']
}


