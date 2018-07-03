from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
		"my_list":[ 
{
	"restaurant_name":"KFC",
	"food_type":"Fried chicken",
},
{
	"restaurant_name":"pick",
	"food_type":"frozen yogurt",
},
		{
			"restaurant_name":"koko",
			"food_type":"fries",
			},
		],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object": 
{
	"restaurant_name":"KFC",
	"food_type":"Fried chicken",
},

    }
    return render(request, 'detail.html', context)
