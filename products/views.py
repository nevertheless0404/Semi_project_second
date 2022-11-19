from django.shortcuts import render, redirect, get_object_or_404
from .models import Products, Review
from dotenv import load_dotenv
import os
from .models import Products
from .forms import ReviewForm
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    products = Products.objects.all()

    products_high = Products.objects.all().order_by("가격")
    products_low = Products.objects.all().order_by("-가격")
    for product in products:
        product.ten_price = int(round((product.가격) * 1.1))
        product.save()
    # 가격 등급 나누기.
    for product in products:
        if product.가격 <= 500000:
            product.가격등급 = "1"
        elif product.가격 > 500000 and product.가격 <= 1000000:
            product.가격등급 = "2"
        elif product.가격 > 1000000 and product.가격 <= 1500000:
            product.가격등급 = "3"
        elif product.가격 > 1500000 and product.가격 <= 2000000:
            product.가격등급 = "4"
        elif product.가격 > 2000000:
            product.가격등급 = "5"
        product.save()
    # 저장 용량 등급 나누기.
    # for product in products:
    #     product.저장용량 = int(product.저장용량)
    #     if product.저장용량 <= 256:
    #         product.저장용량등급 = "1"
    #     elif product.저장용량 > 500 and product.저장용량 <= 516:
    #         product.저장용량등급 = "2"
    #     elif product.저장용량 > 999 and product.저장용량 <= 2000:
    #         product.저장용량등급 = "3"
    #     elif product.저장용량 > 2000:
    #         product.저장용량등급 = "4"
    #     product.save()
    # 그래픽카드 분류
    for product in products:
        if product.GPU종류 == "내장그래픽":
            product.GPU종류등급 = "1"
        elif product.GPU종류 > "외장그래픽":
            product.GPU종류등급 = "2"
        product.save()
    # 해상도 분류
    for product in products:
        if "FHD" in product.해상도:
            product.해상도등급 = "FHD"
        elif "QHD" in product.해상도:
            product.해상도등급 = "QHD"
        elif "UHD" in product.해상도:
            product.해상도등급 = "UHD"
        product.save()
    # 노트북 크기 분류
    for product in products:
        if (
            product.화면크기 == "35.5cm(14인치)"
            or product.화면크기 == "33.782cm(13.3인치)"
            or product.화면크기 == "34.5cm(13.6인치)"
            or product.화면크기 == "27.4cm(10.9인치)"
            or product.화면크기 == "33.7cm(13인치)"
            or product.화면크기 == "33.7cm(13.3인치)"
            or product.화면크기 == "34.03cm(13.4인치)"
            or product.화면크기 == "33.78cm(13.3인치)"
            or product.화면크기 == "35.6cm(14인치)"
            or product.화면크기 == "35.56cm(14인치)"
        ):
            product.화면크기등급 = "1"
        elif (
            product.화면크기 == "39.6cm(15.6인치)"
            or product.화면크기 == "36.8cm(14.5인치)"
            or product.화면크기 == "39.62cm(15.6인치)"
            or product.화면크기 == "40.8cm(16인치)"
            or product.화면크기 == "40.64cm(16인치)"
            or product.화면크기 == "35.97cm(14.2인치)"
            or product.화면크기 == "41.05cm(16.2인치)"
            or product.화면크기 == "38.1cm(15인치)"
            or product.화면크기 == "40.6cm(16인치)"
        ):
            product.화면크기등급 = "2"
        elif (
            product.화면크기 == "43.9cm(17.3인치)"
            or product.화면크기 == "43.1cm(17인치)"
            or product.화면크기 == "43.94cm(17.3인치"
            or product.화면크기 == "43.18cm(17인치)"
        ):
            product.화면크기등급 = "3"
        product.save()
    # 카테고리 분류
    category = request.GET.get("category")
    if category:
        products_category = Products.objects.filter(제조회사__contains=category)
    else:
        products_category = products
    # 가격 분류  1,2,3,4,5
    price = request.GET.get("price")
    if price:
        products_price = Products.objects.filter(가격등급__contains=price)
    else:
        products_price = products
    # 저장용량등급 분류  1,2,3,4
    storage = request.GET.get("storage")
    if storage:
        products_storage = Products.objects.filter(저장용량등급__contains=storage)
    else:
        products_storage = products
    # GPU종류등급 분류  1,2
    graphic = request.GET.get("graphic")
    if graphic:
        products_graphic = Products.objects.filter(GPU종류등급__contains=graphic)
    else:
        products_graphic = products
    # 해상도등급 분류  "FHD","QHD","UHD"
    resolution = request.GET.get("resolution")
    if resolution:
        products_resolution = Products.objects.filter(해상도등급__contains=resolution)
    else:
        products_resolution = products
    # 화면크기등급 분류  1,2,3,4,5
    size = request.GET.get("size")
    if size:
        products_size = Products.objects.filter(화면크기등급__contains=size)
    else:
        products_size = products

    # 합치는 작업
    a = set()
    for j in products_category:
        a.add(j.pk)
    b = set()
    for i in products_price:
        b.add(i.pk)
    # c = set()
    # for i in products_storage:
    #     c.add(i.pk)
    d = set()
    for i in products_graphic:
        d.add(i.pk)
    e = set()
    for i in products_resolution:
        e.add(i.pk)
    f = set()
    for i in products_size:
        f.add(i.pk)

    sum = a & b & d & e & f  # & c

    answer = []
    for p in products:
        if p.pk in sum:
            answer.append(p)
    print(answer)
    print(type(products_category))
    page = request.GET.get("page", "1")
    paginator = Paginator(answer, 6)
    page_obj = paginator.get_page(page)
    context = {
        "products": products,
        "category": category,
        "products_high": products_high,
        "products_low": products_low,
        "products_category": products_category,
        "page_obj": page_obj,
    }
    return render(request, "products/index.html", context)


def detail(request, pk):
    load_dotenv()
    KAKAO_KEY = os.getenv("KAKAOKEY")
    product = get_object_or_404(Products, pk=pk)
    reviews = product.review_set.all()
    review_form = ReviewForm()
    product_grade = 0
    lenReviews = len(reviews)
    for review in reviews:
        product_grade += review.grade
    if lenReviews != 0:
        product_grade = round((product_grade / lenReviews), 1)
    model_name = product.모델명
    special_price = product.가격
    price = int(round((product.가격) * 1.1, -4))
    thumbnail = product.썸네일
    image1 = product.이미지1
    image2 = product.이미지2
    image3 = product.이미지3

    context = {
        "review_form": review_form,
        "reviews": reviews,
        "product_grade": product_grade,
        "lenReviews": lenReviews,
        "KAKAO_KEY": KAKAO_KEY,
        "price": price,
        "special_price": special_price,
        "modelName": model_name,
        "product": product,
        "thumbnail": thumbnail,
        "image1": image1,
        "image2": image2,
        "image3": image3,
    }
    return render(request, "products/detail.html", context)


def like_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if product.like_product.filter(pk=request.user.pk).exists():
        product.like_product.remove(request.user)
        is_like = False
    else:
        product.like_product.add(request.user)
        is_like = True
    context = {
        "isLiked": is_like,
        "likeCount": product.like_product.count(),
    }
    return JsonResponse(context)


def like_reviews(request, product_pk, review_pk):
    product = get_object_or_404(Products, pk=product_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if review.like.filter(pk=request.user.pk).exists():
        review.like.remove(request.user)
        is_like = False
    else:
        review.like.add(request.user)
        is_like = True
    context = {
        "isLiked": is_like,
        "likeReviewCount": review.like.count(),
    }
    return JsonResponse(context)


def review_create(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.products = product
            review.save()
        return redirect("products:detail", product.pk)
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
        "product": product,
    }
    return render(request, "products/create.html", context)


def update(request, product_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("products:detail", product_pk)
    else:
        reviewContent = review.content
    context = {
        "reviewContent": reviewContent,
    }
    return JsonResponse(context)


def delete(request, product_pk, review_pk):
    get_object_or_404(Review, pk=review_pk).delete()
    context = {}
    return JsonResponse(context)
