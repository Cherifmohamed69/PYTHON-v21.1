players = [
    {
    	"name": "Kevin Durant",
    	"age":34,
    	"position": "small forward",
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum",
    	"age":24,
    	"position": "small forward",
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving",
    	"age":32,
        "position": "Point Guard",
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard",
    	"age":33,
        "position": "Point Guard",
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid",
    	"age":32,
        "position": "Power Foward",
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

class Player :
    def __init__(self,player_info):
        self.name = player_info["name"]
        self.age = player_info["age"]
        self.position = player_info["position"]
        self.team = player_info["team"]


