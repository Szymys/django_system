from django.shortcuts import render
from . models import Category, Product
from django.shortcuts import get_object_or_404




def store(request):

    all_products = Product.objects.all()

    context = {'my_products': all_products}

    return render(request, 'store/store.html', context)





def categories(request):

    all_categories = Category.objects.all()

    return {'all_categories': all_categories}





def list_category(request, category_slug=None):

    category = get_object_or_404(Category, slug=category_slug)

    products = Product.objects.filter(category=category)

    return render(request, 'store/list-category.html', {'category':category, 'products':products})






def product_info(request, product_slug):

    product = get_object_or_404(Product, slug=product_slug)
    
    context = {'product': product}

    return render(request, 'store/product-info.html', context)



#******************** KALKULATORY




def bmi_calculator(request):
    bmi = None
    category = None

    if request.method == "POST":
        try:
            weight = float(request.POST.get("weight"))
            height_cm = float(request.POST.get("height"))

            height_m = height_cm / 100
            bmi = round(weight / (height_m ** 2), 2)


            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal weight"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Invalid data"


        except (TypeError, ValueError, ZeroDivisionError):
            bmi = None
            category = "Błędne dane"


    return render(request, "store/calculators/bmi.html", {
        "bmi": bmi,
        "category": category
    })




def calorie_calculator(request):
    calories = None

    if request.method == "POST":
        try:


            sex = request.POST.get("sex")
            age = int(request.POST.get("age"))
            weight = float(request.POST.get("weight"))
            height = float(request.POST.get("height"))
            activity = request.POST.get("activity")


            
            if sex == "male":
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age - 161

            activity_map = {
                "low": 1.2,
                "medium": 1.55,
                "high": 1.725,
            }

            calories = round(bmr * activity_map.get(activity, 1.2), 0)
        except (TypeError, ValueError):
            calories = None


    return render(request, "store/calculators/calories.html", {
        "calories": calories
    })
