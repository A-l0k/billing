import requests
from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, 'billing/home.html')

def products(request):
    return render(request, 'billing/products.html')

def billing_page(request):
    return render(request, 'billing/billing.html')

def invoice(request):
    return render(request, 'billing/invoice.html')

def stock(request):
    return render(request, 'billing/stock.html')

def reports(request):
    return render(request, 'billing/reports.html')


# 🔹 New API Integration
def lookup_product(request):
    barcode = request.GET.get("barcode")  # e.g. /lookup/?barcode=737628064502
    if not barcode:
        return JsonResponse({"error": "No barcode provided"}, status=400)

    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    data = response.json()

    if data.get("status") == 1:
        product = data["product"]
        return JsonResponse({
            "name": product.get("product_name", "Unknown"),
            "brand": product.get("brands", "Unknown"),
            "category": product.get("categories", "Unknown"),
            "quantity": product.get("quantity", "Unknown"),
        })
    else:
        return JsonResponse({"error": "Product not found"}, status=404)
