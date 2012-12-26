from drinks.models import Drink
from django.shortcuts import render_to_response
import random
from datetime import *

class Pacific(tzinfo): 
	def utcoffset(self,dt): 
		return timedelta(hours=-7) 
	def tzname(self,dt): 
		return "GMT -7" 
	def dst(self,dt): 
		return timedelta(0)

pacific=Pacific()

curdate=datetime.now()
curdate=curdate.replace(tzinfo=pacific)

drinkcount=Drink.objects.all().count()




def index(request):
	random_number=random.randrange(0,drinkcount)
	if curdate.month==3 and curdate.day==17:
		drinknumber=19
		specialtext="It's fucking St. Patrick's Day!"
	else:
		drinknumber=random_number
		specialtext=""

	drink = Drink.objects.get(pk=drinknumber)
	name=drink.name
	alcohol=drink.alcohol
	url=drink.url
	return render_to_response('drinks/index.html',
		{
			'name': name,
			'url': url,
			'specialtext': specialtext,
		})
